from turtle import onclick, onrelease

import dearpygui.dearpygui as dpg

class Gui():
    def __init__(self) -> None:
        pass

    def context(self) -> None:
        dpg.create_context()

        self.window_def()

        dpg.create_viewport(title="Calendpy", width=720, height=480)
        dpg.setup_dearpygui()
        dpg.show_viewport()

        dpg.set_primary_window("Primary Window", True)

        dpg.start_dearpygui()
        dpg.destroy_context()

    def destroy(self):
        dpg.destroy_context()

    def window_def(self):
        with dpg.window(tag="Primary Window"):  # pyright: ignore[reportGeneralTypeIssues]
            dpg.add_button(label="Test", callback=self.destroy)



gui = Gui()

gui.context()
