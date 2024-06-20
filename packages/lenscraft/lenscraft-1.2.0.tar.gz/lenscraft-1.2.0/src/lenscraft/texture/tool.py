import time
from typing import List, Optional
import dearpygui.dearpygui as dpg
import numpy as np
import shapely
from shapely.affinity import scale, translate
from keras.api.callbacks import Callback

from lenscraft.image import Image, ImageLibrary
from lenscraft.texture import TextureModelLibrary
from lenscraft.gabor import Gabor
from lenscraft.texture.model import ModelBuilder


def arr_to_data(arr):
    auxImg = np.asfarray(arr, dtype="f")
    auxImg = auxImg.ravel()
    auxImg = np.true_divide(auxImg, 255.0)
    return auxImg


def mask_to_data(mask):
    # Convert binary mask to an RGBA image where RGB channels follow the mask
    # and the alpha channel is set to 127 for 50% opacity
    rgba_image = np.zeros(
        (mask.shape[0], mask.shape[1], 4), dtype=np.float32
    )  # Create a 4-channel image
    rgba_image[:, :, :3] = mask[:, :, None] * 255  # Set RGB channels
    rgba_image[:, :, 3] = 128  # Set alpha channel to 50% opacity

    # Flatten the image and normalize to [0, 1]
    texture_data = rgba_image.ravel() / 255.0

    return texture_data


class ImageTab:
    def __init__(self, tab, image: Image, canvas):
        self.tab_id = tab
        self.image = image
        self.canvas_id = canvas
        self.mask_texture_id = None
        self.mask = None

    def canvas_origin(self):
        (x, y) = dpg.get_item_pos(self.canvas_id)
        return (x + 9, y + 32)

    def clear(self):
        if self.mask:
            dpg.delete_item(self.mask)
            self.mask = None

    def add_mask(self, mask):
        h, w = mask.shape[:2]
        if self.mask_texture_id is None:
            with dpg.texture_registry():
                self.mask_texture_id = dpg.add_dynamic_texture(
                    h, w, default_value=mask_to_data(mask)
                )
        else:
            dpg.set_value(self.mask_texture_id, mask_to_data(mask))

        w, h = dpg.get_item_rect_size(self.canvas_id)
        self.mask = dpg.draw_image(
            self.mask_texture_id, (0, 0), (w, h), parent=self.canvas_id
        )

    def polygon_to_image_space(self, screen_polygon):
        (width, height) = dpg.get_item_rect_size(self.canvas_id)
        offset_x, offset_y = self.canvas_origin()

        scale_x = self.image.width / width
        scale_y = self.image.height / height

        scaled_polygon = scale(
            screen_polygon, xfact=scale_x, yfact=scale_y, origin=(0, 0)
        )
        translated_polygon = translate(scaled_polygon, xoff=offset_x, yoff=offset_y)

        return translated_polygon


class TrainingProgressWindow(Callback):
    def __init__(self):
        self.id = "training_progress_popup"
        self.is_complete = False

    def on_epoch_end(self, epoch, logs=None):
        progress = epoch / 50.0
        dpg.set_value(self.progress_bar, progress)

    def on_train_end(self, logs=None):
        self.is_complete = True
        self.enable_close_button()

    def on_predict_end(self, logs=None):
        print("on_predict_end", logs)

    def on_test_end(self, logs=None):
        if self.is_complete:
            dpg.set_value(
                self.message, f"Training Complete. Test Accuracy: {logs['accuracy']}"
            )
            dpg.show_item(self.message)

    def show(self, parent="TextureToolWindow"):
        # Get the size of the parent window
        parent_width = dpg.get_item_width(parent)
        parent_height = dpg.get_item_height(parent)

        # Define the size of the popup window
        popup_width = 400
        popup_height = 150

        # Calculate the center position
        pos_x = (parent_width - popup_width) // 2
        pos_y = (parent_height - popup_height) // 2

        # Set the position and show the popup
        dpg.configure_item(
            self.id,
            pos=(pos_x, pos_y),
            width=popup_width,
            height=popup_height,
            show=True,
        )

    def hide(self):
        dpg.hide_item(self.id)

    def add_to_context(self):
        with dpg.window(
            label="Progress Popup", modal=True, show=False, tag=self.id, no_close=True
        ):
            dpg.add_text("Training a texture classifier. This may take a minute")
            self.progress_bar = dpg.add_progress_bar(
                label="Progress", default_value=0.0, width=-1, tag="progress_bar"
            )

            self.message = dpg.add_text("", show=False)
            self.ok_btn = dpg.add_button(
                label="OK", callback=self._on_ok_btn, show=False
            )

    def enable_close_button(self):
        dpg.show_item(self.ok_btn)

    def _on_ok_btn(self, sender):
        self.hide()


class TextureClassifierTool:
    def __init__(
        self, image_library: ImageLibrary, texture_library: TextureModelLibrary
    ):
        self.id = "TextureToolWindow"  # dpg.generate_uuid()
        self.image_library = image_library
        self.texture_library = texture_library
        self.image_library.on_update(self._on_image_added)
        self.borders: List[TextureBorder] = []
        self.current_model = None
        self.model_name = "my-texture"
        self.training_window = TrainingProgressWindow()

        self._current_tab_id = None
        self._tabs = {}
        self._masks = {}

    def load_image(self):
        pass

    def do_train_nn(self):
        model_builder = ModelBuilder()
        gabor = Gabor()
        feature_tab_map = {}
        self.training_window.show()

        # Gather training data
        for border in self.borders:
            if border.tab.tab_id in feature_tab_map:
                features = feature_tab_map[border.tab.tab_id]
            else:
                features = gabor.load_features(border.tab.image.path)
                feature_tab_map[border.tab.tab_id] = features

            inside, outside = border.extract_features(features)
            model_builder.add_blue(inside)
            model_builder.add_red(outside)

        # Train model
        model = model_builder.train(callback=self.training_window)

        # Run prediction on sample image
        features = feature_tab_map[border.tab.tab_id]
        fv = features.all()
        result = model.predict(fv).reshape(features.flat_shape())
        self.current_tab().add_mask(result)
        self.current_model = model_builder

        dpg.show_item("group_save_model")
        dpg.hide_item("group_create_model")

    def _on_tab_switch(self, sender, app_data):
        self._current_tab_id = app_data

    def _on_model_name_change(self, sender, app_data):
        self.model_name = app_data

    def _on_image_added(self):
        dpg.delete_item("tab_bar", children_only=True)
        self._current_tab_id = None
        self._tabs = {}
        for image in self.image_library.images:
            with dpg.tab(label=image.name, parent="tab_bar") as tab:
                if self._current_tab_id is None:
                    self._current_tab_id = tab

                (w, h) = image.fit(width=600)
                with dpg.drawlist(width=w, height=h) as canvas:
                    image.draw_image(width=w)
                self._tabs[tab] = ImageTab(tab, image, canvas)

    def _on_mouse_click(self):
        if not dpg.is_item_visible(self.id):
            return

        current_tab = self.current_tab()
        if not current_tab:
            return
        canvas = self._tabs[current_tab.tab_id].canvas_id
        if not dpg.is_item_hovered(canvas):
            return

        current_border = self.current_border()
        if current_border is None:
            self.start_new_border()
        else:
            pos = self.mouse_image_coordinates()
            current_border.mouse_click(pos)

    def _on_mouse_move(self):
        current_border = self.current_border()
        if current_border:
            pos = self.mouse_image_coordinates()
            current_border.mouse_move(pos)

    def mouse_image_coordinates(self):
        (ox, oy) = (9, 32)  # dpg.get_item_pos(self.current_canvas())
        (mx, my) = dpg.get_mouse_pos()
        return (mx - ox, my - oy)

    def current_border(self) -> Optional["TextureBorder"]:
        if len(self.borders) == 0:
            return None

        latest_border = self.borders[-1]
        if latest_border.done:
            return None

        return latest_border

    def clear(self):
        for border in self.borders:
            border.clear()
        for _, tab in self._tabs.items():
            tab.clear()
        self.borders = []
        self._update_border_list()

    def save_model(self):
        if self.current_model is None:
            print("No model to save")
            return

        new_path = self.current_model.save(self.model_name)
        self.texture_library.add_model(new_path)

        dpg.hide_item(self.id)

    def start_new_border(self):
        canvas = self.current_tab().canvas_id
        start = self.mouse_image_coordinates()
        print("Start:", start)
        new_line = TextureBorder(self.current_tab(), start)
        self.borders.append(new_line)
        self._update_border_list()

    def current_tab(self) -> Optional[ImageTab]:
        if self._current_tab_id is None:
            return None

        return self._tabs[self._current_tab_id]

    def current_canvas(self):
        return self.current_tab().canvas_id

    def _update_border_list(self):
        # Clear the list
        dpg.delete_item("border_list", children_only=True)

        # Re-Render the list
        for i, border in enumerate(self.borders):
            with dpg.child_window(height=70, autosize_x=True, parent="border_list"):
                with dpg.group(horizontal=True):
                    dpg.add_button(label="X", width=20, height=50)
                    dpg.add_text(f"Border {i}")

        if len(self.borders) > 0:
            dpg.show_item("group_create_model")
        else:
            dpg.hide_item("group_create_model")

    def add_to_context(self):
        # Create a window that fills the viewport and cannot be moved or closed
        with dpg.window(
            tag=self.id,
            label="TextureClassifierTool",
            no_collapse=True,
            show=False,
            height=600,
        ):
            dpg.add_text(
                "The texture tool allows you to separate the object you care about from the background based on texture pattern. Click on the image to draw a boundary",
                wrap=500,
            )
            with dpg.group(horizontal=True):
                # Child window for the image with a fixed size
                with dpg.group(horizontal=False):
                    with dpg.child_window(width=620, autosize_y=True):
                        with dpg.tab_bar(tag="tab_bar", callback=self._on_tab_switch):
                            pass

                # Child window for the toolbar, narrow and taking the full height
                with dpg.child_window(
                    tag="toolbar", width=250, autosize_y=True, border=True
                ):
                    with dpg.group(horizontal=True):
                        dpg.add_text("Texture Borders")
                        dpg.add_button(
                            label="?", width=20, height=20, tag="border_list_tip"
                        )
                        with dpg.tooltip("border_list_tip"):
                            dpg.add_text(
                                "Draw one or more texture boundaries on your images to train a texture classifier",
                                wrap=150,
                            )

                    with dpg.child_window(border=False, tag="border_list", height=-100):
                        pass

                    with dpg.group(tag="group_create_model", show=False):
                        dpg.add_button(
                            label="Train",
                            height=25,
                            width=-1,
                            callback=self.do_train_nn,
                        )
                    dpg.add_button(
                        label="Reset", height=25, width=-1, callback=self.clear
                    )
                    with dpg.group(tag="group_save_model", show=False):
                        dpg.add_input_text(
                            label="Name",
                            default_value=self.model_name,
                            callback=self._on_model_name_change,
                        )
                        dpg.add_button(
                            label="Save", height=25, width=-1, callback=self.save_model
                        )

        with dpg.handler_registry():
            dpg.add_mouse_release_handler(callback=self._on_mouse_click)
            dpg.add_mouse_move_handler(callback=self._on_mouse_move)

        self.training_window.add_to_context()


class TextureBorder:
    def __init__(self, tab: ImageTab, start=None, end=None, width=10):
        self.tab = tab
        self.start = np.array(start) if start else None
        self.end = np.array(end) if end else None
        self.done = False
        self.line_id = None
        self.outside_polygon_id = None
        self.inside_polygon_id = None
        self.width = width  # Width of the rectangles
        self._last_draw = 0

    def length(self):
        v = self.start - self.end
        return np.linalg.norm(v)

    def mouse_move(self, pos):
        # pos = np.array(dpg.get_mouse_pos(local=True))
        if not self.done:
            self.end = pos
            self.draw()

    def mouse_click(self, pos):
        # pos = np.array(dpg.get_mouse_pos(local=True))
        if self.start is None:
            print("Start", pos)
            self.start = pos
        elif not self.done:
            print("End", pos)
            self.end = pos
            self.done = True
            self.on_done()

    def on_done(self):
        pass

    def clear(self):
        if self.line_id:
            dpg.delete_item(self.line_id)
        if self.outside_polygon_id is not None:
            dpg.delete_item(self.outside_polygon_id)
        if self.inside_polygon_id is not None:
            dpg.delete_item(self.inside_polygon_id)

    def draw(self):
        dt = time.time() - self._last_draw
        if dt < 0.05:
            # Prevent drawing too fast
            return

        if np.array_equal(self.start, self.end):
            # Dont draw unless there is some distance between start and end
            return

        self.draw_line()
        self.draw_rectangles()
        self._last_draw = time.time()

    def draw_line(self):
        if self.line_id and dpg.does_item_exist(self.line_id):
            dpg.delete_item(self.line_id)

        if self.start is not None and self.end is not None:
            self.line_id = dpg.draw_line(
                self.start,
                self.end,
                color=(255, 0, 0, 255),
                thickness=3,
                parent=self.tab.canvas_id,
            )

    def draw_rectangles(self):
        if self.outside_polygon_id and dpg.does_item_exist(self.outside_polygon_id):
            dpg.delete_item(self.outside_polygon_id)
        if self.inside_polygon_id and dpg.does_item_exist(self.inside_polygon_id):
            dpg.delete_item(self.inside_polygon_id)

        width = max(self.length() / 3, self.width)
        x, y = self.outside_region(width).exterior.xy
        points_outside = list(zip(x, y))
        self.outside_polygon_id = dpg.draw_polygon(
            points=points_outside,
            color=(0, 255, 0, 255),
            thickness=1,
            parent=self.tab.canvas_id,
        )
        x, y = self.inside_region(width).exterior.xy
        points_inside = list(zip(x, y))
        self.inside_polygon_id = dpg.draw_polygon(
            points=points_inside,
            color=(0, 0, 255, 255),
            thickness=1,
            parent=self.tab.canvas_id,
        )

    def outside_region(self, width, buffer=3):
        # Create a LineString from the start and end points
        line = shapely.LineString([self.start, self.end])
        line = line.offset_curve(width + buffer)
        # Create a buffer polygon around the line
        buffer_polygon: shapely.Polygon = line.buffer(width, cap_style=2)
        return buffer_polygon

    def inside_region(self, width, buffer=3):
        # Create a LineString from the start and end points
        line = shapely.LineString([self.start, self.end])
        line = line.offset_curve(-width - buffer)
        # Create a buffer polygon around the line
        buffer_polygon: shapely.Polygon = line.buffer(width, cap_style=2)
        return buffer_polygon

    def inside_region_image_space(self, width, buffer=3):
        screen_polygon = self.inside_region(width, buffer)
        return self.tab.polygon_to_image_space(screen_polygon)

    def outside_region_image_space(self, width, buffer=3):
        screen_polygon = self.outside_region(width, buffer)
        return self.tab.polygon_to_image_space(screen_polygon)

    def extract_features(self, feature_map):
        width = max(self.length() / 3, self.width)
        # Determine the bounding box of the polygon to limit the search area
        outside_polygon = self.outside_region_image_space(width)
        outside_features = feature_map.get_polygon_area(outside_polygon, sample=200)

        inside_polygon = self.inside_region_image_space(width)
        inside_features = feature_map.get_polygon_area(inside_polygon, sample=200)

        return outside_features, inside_features
