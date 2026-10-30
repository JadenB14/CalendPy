import dearpygui.dearpygui as dpg


def settings_page():
    with dpg.child_window(tag="settings_page", height=-1):  # pyright: ignore[reportGeneralTypeIssues]
        dpg.add_text("Settings Page")
