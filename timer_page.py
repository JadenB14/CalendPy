import time
from datetime import datetime

import dearpygui.dearpygui as dpg
from gcsa.event import Event


class Stopwatch():

    def __init__(self) -> None:
        self.running: bool = False
        self.start_time: float = 0.0
        self.elapsed: float = 0.0
        self.total_elapsed: float = 0.0
        self.calendar_start_time = datetime.now()
        self.calendar_end_time = datetime.now()
        self.timer_lap = []

    def start_stopwatch(self):
        activity = dpg.get_value("timer_input")
        if activity == "Select an option:":
            activity = "None"

        if not self.running:
            self.start_time = time.perf_counter()
            self.running = True
            self.calendar_start_time = datetime.now()

            self.add_log_entry(
                f"{self.calendar_start_time.strftime('%I:%M:%S %p')} - Timer started ({activity})"
            )

        print(self.calendar_start_time)

    def pause_stopwatch(self, sender, app_data, user_data):
        if self.running:
            self.elapsed += time.perf_counter() - self.start_time
            self.running = False
            self.calendar_end_time = datetime.now()
            self.total_elapsed += self.elapsed

            self.add_log_entry(
                f"{self.calendar_end_time.strftime('%I:%M:%S %p')} - "
                f"Timer stopped ({self.elapsed:.2f} seconds)"
            )

            combo_value = dpg.get_value("timer_input")
            calendar = user_data()

            if combo_value == "Select an option:":
                print("Select an activity to add this session to your calendar")
            elif calendar is None:
                print("Please configure your Google Calendar first.")
            else:
                self.timer_submit(calendar)


    def reset_stopwatch(self):
        self.running = False
        self.start_time = 0.0
        self.elapsed = 0.0
        self.calendar_start_time = datetime.now()
        self.calendar_end_time = datetime.now()
        self.timer_lap = []

        dpg.set_value("log_text", "")
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

    def timer_submit(self, calendar):
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

    def add_log_entry(self, message):
        self.timer_lap.append(message)

        log_text = "\n".join(self.timer_lap)
        dpg.set_value("log_text", log_text)

    def timer_page(self, get_calendar):

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
                pos=[375, 90]
            )
            dpg.add_input_text(
                tag="custom_input_timer",
                width=400,
                hint="Custom Task:",
                pos=[325, 130]
            )
            dpg.hide_item("custom_input_timer")

            dpg.add_text(
                "00:00:00.000",
                tag="stopwatch_display",
                pos=[225, 160],

            )

            dpg.bind_item_font("stopwatch_display", large_font)

            dpg.add_spacer(height=15)

            with dpg.group(
                horizontal=True,
                pos=[300, 260],
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
                    callback=self.pause_stopwatch,
                    user_data=get_calendar
                )

                dpg.add_button(
                    label="Reset",
                    width=100,
                    callback=self.reset_stopwatch
                )

            with dpg.child_window(
                tag="log_display",
                height=300,
                width=660,
                pos=[200,350]
            ):  # pyright: ignore[reportGeneralTypeIssues]
                    dpg.add_text("", tag="log_text", wrap=0)
