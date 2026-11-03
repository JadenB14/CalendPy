import os
import time
import dearpygui.dearpygui as dpg
from dotenv import set_key, load_dotenv

load_dotenv()

EMAIL = os.getenv("EMAIL")

class Settings():
    def __init__(self) -> None:
        pass

    def settings_page(self, save_callback):
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
                callback=self.save_handler,
                user_data=save_callback
            )

            dpg.add_text(
                f"Current Email: {EMAIL}",
                tag="email_config"
            )

            dpg.add_text("", tag="save_status")


    def save_handler(self, sender, app_data, user_data):
        email = dpg.get_value("email_input").strip()

        def status_time():
            dpg.show_item("save_status")
            for i in range(1, 6):
                time.sleep(1)
            dpg.hide_item("save_status")

        if not email or "@" not in email:
            dpg.set_value(
                "save_status",
                "Please enter a valid email."
            )
            status_time()
        else:
            set_key("./.env", "EMAIL", email)
            user_data(email)

            dpg.set_value(
                "save_status",
                "Email saved!"
            )
            status_time()

        dpg.set_value(
            "email_config",
            f"Current Email: {email}"
        )
