import time
from datetime import datetime

import dearpygui.dearpygui as dpg
from gcsa.event import Event

now = datetime.now()
date = datetime.date(now)

class Stopwatch():

    def __init__(self) -> None:
        self.running: bool = False
        self.start_time: float = 0.0
        self.elapsed: float = 0.0
        self.calendar_start_time = now
        self.calendar_end_time = now
        self.select_is_on = False

    def start_stopwatch(self):
        if not self.running:
            self.start_time = time.perf_counter()
            self.running = True
            self.calendar_start_time = datetime.now()
        print(self.calendar_start_time)

    def pause_stopwatch(self):
        combo_value = dpg.get_value("timer_input")

        if self.running:
            self.elapsed += time.perf_counter() - self.start_time
            self.running = False
            self.calendar_end_time = datetime.now()
            if combo_value == "Select an option:":
                raise Exception("Value needs to be selected.")
            else:
                self.timer_submit()

    def reset_stopwatch(self):
        self.running = False
        self.start_time = 0.0
        self.elapsed = 0.0
        self.calendar_start_time = now
        self.calendar_end_time= now

        dpg.set_value("stopwatch_display", "00:00:00.000")

    def update_stopwatch(self):
        if self.running:
            current_elapsed = self.elapsed + (
                time.perf_counter() - self.start_time
            )
        else:
            current_elapsed = self.elapsed

        hours = int(current_elapsed // 3600)
        minutes = int((current_elapsed % 3600) // 60)
        seconds = int(current_elapsed % 60)
        milliseconds = int((current_elapsed % 1) * 1000)

        display = f"{hours:02}:{minutes:02}:{seconds:02}.{milliseconds:03}"

        dpg.set_value("stopwatch_display", display)

    def font_init(self):
        with dpg.font_registry():  # pyright: ignore[reportGeneralTypeIssues]
                with dpg.font("./assets/ProggyClean.ttf", 48) as large_font:  # pyright: ignore[reportGeneralTypeIssues]
                    return large_font

    def timer_submit(self):
        event_check = dpg.get_value("timer_input")
        event_start_time = self.calendar_start_time
        event_end_time = self.calendar_end_time

        if event_check == "Custom":
            event_name = dpg.get_value("custom_input_timer")
        else:
            event_name = event_check

        event_data = Event(
            summary=event_name,
            start=event_start_time,
            end=event_end_time,
        )

        calendar.add_event(event_data)

    def dropdown_value(self, sender, app_data):
        if app_data == "Custom":
            dpg.show_item("custom_input_timer")
        elif app_data != "Custom":
            dpg.hide_item("custom_input_timer")
            dpg.set_value("custom_input_timer", "")

    def timer_page(self, gcalendar):
        global calendar
        calendar = gcalendar

        large_font = self.font_init()

        with dpg.child_window(tag="timer_page", height=-1):  # pyright: ignore[reportGeneralTypeIssues]
            dpg.add_text("Calendar Timer:")
            dpg.add_text("This timer will automaticlly track the time logged to your calendar.")

            dpg.add_separator()

            dpg.add_combo(
                default_value="Select an option:",
                items=["Workout", "Meditate","Study","Custom"],
                callback=self.dropdown_value,
                width=300,
                tag="timer_input",
                pos=[400, 100]
            )
            dpg.add_input_text(
                tag="custom_input_timer",
                width=400,
                hint="Custom Task:",
                pos=[350, 150]
            )
            dpg.hide_item("custom_input_timer")

            dpg.add_text(
                "00:00:00.000",
                tag="stopwatch_display",
                pos=[225, 200],

            )

            dpg.bind_item_font("stopwatch_display", large_font)

            dpg.add_spacer(height=15)

            with dpg.group(
                horizontal=True,
                pos=[300, 350],
                width=150,
                height=75
            ):  # pyright: ignore[reportGeneralTypeIssues]

                dpg.add_button(
                    label="Start",
                    width=100,
                    callback=self.start_stopwatch
                )

                dpg.add_button(
                    label="Pause",
                    width=100,
                    callback=self.pause_stopwatch
                )

                dpg.add_button(
                    label="Reset",
                    width=100,
                    callback=self.reset_stopwatch
                )
