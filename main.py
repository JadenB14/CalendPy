from gcsa.google_calendar import GoogleCalendar
from dotenv import load_dotenv
import os
import gui


load_dotenv()
EMAIL: str = os.environ["EMAIL"]


# Define Objects
calendar = GoogleCalendar(EMAIL, authentication_flow_port=8100)
gui_obj = gui.Gui(calendar)


def main():
    gui_obj.context()


if __name__ == "__main__":
    main()
