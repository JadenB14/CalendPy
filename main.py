from beautiful_date import Jan, Apr, Oct
from dotenv import load_dotenv
from gcsa.event import Event
from gcsa.google_calendar import GoogleCalendar
from gcsa.recurrence import Recurrence, DAILY, SU, SA
import os

load_dotenv()

EMAIL: str = os.environ["EMAIL"]
CLIENT_SECRET = "~/.credentials/credentials.json"

calendar = GoogleCalendar(EMAIL, authentication_flow_port=8100)
event = Event(
    'Breakfast',
    start=(29 / Oct / 2026)[9:00],
#     recurrence=[
#        Recurrence.rule(freq=DAILY),
#        Recurrence.exclude_rule(by_week_day=[SU, SA]),
#        Recurrence.exclude_times([
#            (19 / Apr / 2019)[9:00],
#            (22 / Apr / 2019)[9:00]
#        ])
#    ],
#    minutes_before_email_reminder=50
)
def main():

    calendar.add_event(event)


if __name__ == "__main__":
    main()
