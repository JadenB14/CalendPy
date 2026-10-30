import dearpygui.dearpygui as dpg


def timer_page():
    with dpg.child_window(tag="timer_page", height=-1):  # pyright: ignore[reportGeneralTypeIssues]
        dpg.add_text("Timer Page")
