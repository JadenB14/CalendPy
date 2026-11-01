from datetime import datetime
import dearpygui.dearpygui as dpg
from gcsa.event import Event


now = datetime.now()

def tracker_page(get_calendar):

    date = now.date()
    time = now.time()

    with dpg.child_window(tag="tracker_page", height=-1):  # pyright: ignore[reportGeneralTypeIssues]
        dpg.add_text("Tracker:")

        dpg.add_text("Use this page to add a single event to your calendar.")

        dpg.add_separator()

        dpg.add_combo(
            default_value="Select an option:",
            items=["Workout", "Meditate","Study","Custom"],
            callback=dropdown_value,
            width=300,
            tag="tracker_input"
        )
        dpg.add_input_text(
            tag="custom_input",
            width=400,
            hint="Custom Task:"
        )
        dpg.hide_item("custom_input")


        dpg.add_text("Start Time:")
        dpg.add_time_picker(
            default_value={
                "hour": time.hour,
                "min": time.minute,
                "sec": time.second
            },
            tag="start_time"
        )

        dpg.add_separator()

        dpg.add_text("End Time:")
        dpg.add_time_picker(
            default_value= {
                "hour": time.hour + 1,
                "min": time.minute,
                "sec": time.second
            },
            tag="end_time",
        )

        dpg.add_separator()

        dpg.add_date_picker(
            default_value= {
                "month_day": date.day,
                "year": date.year - 1900,
                "month": date.month - 1
            },
            tag="tracker_date",
        )

        dpg.add_button(
            label="Submit",
            tag="submit",
            height=50,
            width=100,
            callback=tracker_submit,
            user_data=get_calendar
        )

def dropdown_value(sender, app_data):
    if app_data == "Custom":
        dpg.show_item("custom_input")
    elif app_data != "Custom":
        dpg.hide_item("custom_input")
        dpg.set_value("custom_input", "")
    else:
        return app_data

def tracker_submit(sender, app_data, user_data):

    calendar = user_data()

    if calendar is None:
        print("Please configure your Google Calendar Email in Settings.")
        return

    event_check = dpg.get_value("tracker_input")
    event_start_time = dpg.get_value("start_time")
    event_end_time = dpg.get_value("end_time")
    event_date = dpg.get_value("tracker_date")

    if event_check == "Custom":
        event_name = dpg.get_value("custom_input")
    else:
        event_name = event_check

    print(event_name,"Start: ",event_start_time,"End: ", event_end_time,"Date: ", event_date)

    event_data = Event(
        summary=event_name,
        start=datetime(year=event_date["year"] + 1900, month=event_date["month"] + 1, day=event_date["month_day"], hour=event_start_time['hour'], minute=event_start_time["min"]),
        end=datetime(year=event_date["year"] + 1900, month=event_date["month"] + 1, day=event_date["month_day"], hour=event_end_time['hour'], minute=event_end_time["min"]),
    )

    calendar.add_event(event_data)
