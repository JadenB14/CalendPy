from datetime import datetime
import dearpygui.dearpygui as dpg
from tracker_page import tracker_page
from settings_page import settings_page
from timer_page import Stopwatch

now = datetime.now()
timer = Stopwatch()


class Gui():
    def __init__(self, calendar) -> None:
        self.calendar = calendar


    def context(self) -> None:
        dpg.create_context()

        dpg.set_global_font_scale(2)

        self.set_theme()

        with dpg.window(tag="prime"):  # pyright: ignore[reportGeneralTypeIssues]
            self.nav_bar()

            dpg.add_separator()

            tracker_page(self.calendar)
            timer.timer_page(self.calendar)
            settings_page()


        dpg.hide_item("timer_page")
        dpg.hide_item("settings_page")

        dpg.create_viewport(
            title="Calendpy",
            width=1080,
            height=720
        )

        dpg.setup_dearpygui()
        dpg.show_viewport()
        dpg.set_primary_window("prime", True)
        while dpg.is_dearpygui_running():
            timer.update_stopwatch()
            dpg.render_dearpygui_frame()
        dpg.destroy_context()

    def nav_bar(self):
        with dpg.group(horizontal=True):  # pyright: ignore[reportGeneralTypeIssues]
            dpg.add_button(
                label="Tracker",
                tag="tracker",
                callback=lambda: self.switch_page("tracker_page")
            )

            dpg.add_button(
                label="Timer",
                callback=lambda: self.switch_page("timer_page")
            )

            dpg.add_button(
                label="Settings",
                tag="settings",
                callback=lambda: self.switch_page("settings_page")
            )
            dpg.set_item_pos("settings", [950,10])

    def set_theme(self):

        with dpg.theme() as midnight_theme:  # pyright: ignore[reportGeneralTypeIssues]
            with dpg.theme_component(dpg.mvAll):  # pyright: ignore[reportGeneralTypeIssues]

                # Window background
                dpg.add_theme_color(
                    dpg.mvThemeCol_WindowBg,
                    (30, 30, 46),
                    category=dpg.mvThemeCat_Core
                )

                # Child window background
                dpg.add_theme_color(
                    dpg.mvThemeCol_ChildBg,
                    (49, 50, 68),
                    category=dpg.mvThemeCat_Core
                )

                # Button background
                dpg.add_theme_color(
                    dpg.mvThemeCol_Button,
                    (69, 71, 90),
                    category=dpg.mvThemeCat_Core
                )

                # Input field background
                dpg.add_theme_color(
                    dpg.mvThemeCol_FrameBg,
                    (69, 71, 90),
                    category=dpg.mvThemeCat_Core
                )

                # Input field when hovered
                dpg.add_theme_color(
                    dpg.mvThemeCol_FrameBgHovered,
                    (88, 91, 112),
                    category=dpg.mvThemeCat_Core
                )

                # Input field when selected
                dpg.add_theme_color(
                    dpg.mvThemeCol_FrameBgActive,
                    (100, 105, 135),
                    category=dpg.mvThemeCat_Core
                )

                # Border colour
                dpg.add_theme_color(
                    dpg.mvThemeCol_Border,
                    (137, 180, 250),
                    category=dpg.mvThemeCat_Core
                )

                # Border thickness
                dpg.add_theme_style(
                    dpg.mvStyleVar_FrameBorderSize,
                    1.5,
                    category=dpg.mvThemeCat_Core
                )

                # Rounded input corners
                dpg.add_theme_style(
                    dpg.mvStyleVar_FrameRounding,
                    5,
                    category=dpg.mvThemeCat_Core
                )

                # Button hover
                dpg.add_theme_color(
                    dpg.mvThemeCol_ButtonHovered,
                    (137, 180, 250),
                    category=dpg.mvThemeCat_Core
                )

                # Button clicked
                dpg.add_theme_color(
                    dpg.mvThemeCol_ButtonActive,
                    (116, 199, 236),
                    category=dpg.mvThemeCat_Core
                )

                # Text colour
                dpg.add_theme_color(
                    dpg.mvThemeCol_Text,
                    (205, 214, 244),
                    category=dpg.mvThemeCat_Core
                )

                # Input field background
                dpg.add_theme_color(
                    dpg.mvThemeCol_FrameBg,
                    (49, 50, 68),
                    category=dpg.mvThemeCat_Core
                )

                # Input field hover
                dpg.add_theme_color(
                    dpg.mvThemeCol_FrameBgHovered,
                    (69, 71, 90),
                    category=dpg.mvThemeCat_Core
                )

                # Input field active
                dpg.add_theme_color(
                    dpg.mvThemeCol_FrameBgActive,
                    (88, 91, 112),
                    category=dpg.mvThemeCat_Core
                )

        # Apply theme globally
        dpg.bind_theme(midnight_theme)

    def switch_page(self, page):
        dpg.hide_item("tracker_page")
        dpg.hide_item("timer_page")
        dpg.hide_item("settings_page")

        dpg.show_item(page)
