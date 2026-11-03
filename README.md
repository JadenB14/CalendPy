# Calendpy

Calendpy is a Python desktop application built with Dear PyGui that helps you track activities and manage your time using Google Calendar.

## Getting Started

Follow these instructions to get Calendpy running on your machine.

### 1. Clone the Repository

Clone the project and navigate into its directory:

```bash
git clone <repository-url>
cd Calendpy
```

### 2. Install Dependencies

Calendpy uses [uv](https://docs.astral.sh/uv/) for Python package and environment management.

If you don't already have uv installed, follow the [official installation instructions](https://docs.astral.sh/uv/getting-started/installation/).

Once installed, run:

```bash
uv sync
```

This will create a virtual environment and install the project's dependencies.

### 3. Configure Google Calendar API

Calendpy uses Google Calendar to create and manage calendar events. Before using this feature, you must configure a Google Cloud project and enable API access.

#### Create a Google Cloud Project

1. Visit the [Google Cloud Console](https://console.cloud.google.com/).
2. Create a new project or select an existing project.
3. Navigate to **APIs & Services → Library**.
4. Search for **Google Calendar API**.
5. Open it and click **Enable**.

#### Configure Google Authentication

1. Navigate to the [Google Auth Platform](https://console.cloud.google.com/auth/).
2. Open **Branding** and configure your application information as needed.
3. Open **Audience**.
4. Set the application audience to **External** if you want to authorize personal Google accounts outside your own organization.
5. Under **Test users**, click **Add users**.
6. Add the Google email address you intend to use with Calendpy.

**Important:** While your OAuth application is in testing mode, only accounts added as test users can authorize it.

#### Create OAuth Credentials

1. In Google Cloud Console, navigate to **Google Auth Platform → Clients**.
2. Create an OAuth client.
3. Select the appropriate application type for your OAuth implementation.
4. Download the OAuth client credentials.
5. Place the downloaded credentials file in the location expected by Calendpy.

You may need to authorize Calendpy through your browser the first time you connect your Google account.

### 4. Configure Calendpy

Launch Calendpy and navigate to the **Settings** page.

Enter the Google email address you added as a test user in the Google Auth Platform and save your settings.

Make sure the Google account you authorize through OAuth matches the email configured in Calendpy.

### 5. Launch Calendpy

Run the application using uv:

```bash
uv run main.py
```

## Features

- **Activity Tracker:** Manually create calendar events for activities.
- **Stopwatch:** Track the duration of activities in real time.
- **Activity Logging:** View a history of timer start and stop events.
- **Google Calendar Integration:** Automatically add tracked activities to Google Calendar.
- **Settings:** Configure your Google Calendar email.

## Troubleshooting

- **Missing dependencies:** Run `uv sync` to install the project's dependencies.
- **Google Calendar authorization errors:** Verify that the Google Calendar API is enabled and your OAuth credentials are configured correctly.
- **Access blocked during authorization:** Make sure the Google account you're using has been added under Google Auth Platform → Audience → Test users.
- **Calendar connection issues:** Verify that the Google account authorized through OAuth matches the email entered in Calendpy.

## Technologies

- Python
- [uv](https://docs.astral.sh/uv/)
- [Dear PyGui](https://dearpygui.readthedocs.io/)
- [GCSA](https://github.com/kuzmoyev/google-calendar-simple-api)
- Google Calendar API
