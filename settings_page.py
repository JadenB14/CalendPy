import dearpygui.dearpygui as dpg
from dotenv import set_key

def settings_page(save_callback):
    with dpg.child_window(tag="settings_page", height=-1):  # pyright: ignore[reportGeneralTypeIssues]
        dpg.add_text("Settings Page")

        dpg.add_separator()

        with dpg.group(horizontal=True):  # pyright: ignore[reportGeneralTypeIssues]

            dpg.add_text("Email: ")
            dpg.add_input_text(
                tag="email_input",
            )

        dpg.add_button(
            label="Save",
            callback=save_handler,
            user_data=save_callback
        )

        dpg.add_text("", tag="save_status")

def save_handler(sender, app_data, user_data):
    email = dpg.get_value("email_input").strip()

    if not email or "@" not in email:
        dpg.set_value(
            "save_status",
            "Please enter a valid email."
        )

    set_key("./.env", "EMAIL", email)

    user_data(email)

    dpg.set_value(
        "save_status",
        "Email saved!"
    )
