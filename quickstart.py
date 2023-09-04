# from __future__ import print_function

# import datetime
# import os.path

# from google.auth.transport.requests import Request
# from google.oauth2.credentials import Credentials
# from google_auth_oauthlib.flow import InstalledAppFlow
# from googleapiclient.discovery import build
# from googleapiclient.errors import HttpError

# # If modifying these scopes, delete the file token.json.
# SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']


# def main():
#     """Shows basic usage of the Google Calendar API.
#     Prints the start and name of the next 10 events on the user's calendar.
#     """
#     creds = None
#     # The file token.json stores the user's access and refresh tokens, and is
#     # created automatically when the authorization flow completes for the first
#     # time.
#     if os.path.exists('token.json'):
#         creds = Credentials.from_authorized_user_file('token.json', SCOPES)
#     # If there are no (valid) credentials available, let the user log in.
#     if not creds or not creds.valid:
#         if creds and creds.expired and creds.refresh_token:
#             creds.refresh(Request())
#         else:
#             flow = InstalledAppFlow.from_client_secrets_file(
#                 'credentials.json', SCOPES)
#             creds = flow.run_local_server(port=0)
#         # Save the credentials for the next run
#         with open('token.json', 'w') as token:
#             token.write(creds.to_json())

#     try:
#         service = build('calendar', 'v3', credentials=creds)

#         # Call the Calendar API
#         now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
#         print('Getting the upcoming 10 events')
#         events_result = service.events().list(calendarId='primary', timeMin=now,
#                                               maxResults=10, singleEvents=True,
#                                               orderBy='startTime').execute()
#         events = events_result.get('items', [])

#         if not events:
#             print('No upcoming events found.')
#             return

#         # Prints the start and name of the next 10 events
#         for event in events:
#             start = event['start'].get('dateTime', event['start'].get('date'))
#             print(start, event['summary'])

#     except HttpError as error:
#         print('An error occurred: %s' % error)


# if __name__ == '__main__':
#     main()


from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials

# Load the credentials from a JSON file
creds = Credentials.from_authorized_user_file('C:\\Users\\Brooke\\OneDrive\\Documents\\GitHub\\scholarsync\\credentials.json')

# Build the Calendar API service
service = build('calendar', 'v3', credentials=creds)

# Event data
event_data = {
    'summary': 'Meeting with Client',
    'location': '123 Main St, City',
    'description': 'Discuss project details',
    'start': {
        'dateTime': '2023-09-15T14:00:00',
        'timeZone': 'YourTimeZone',
    },
    'end': {
        'dateTime': '2023-09-15T15:00:00',
        'timeZone': 'YourTimeZone',
    },
}

# Create the event
event = service.events().insert(calendarId='primary', body=event_data).execute()

# Print the event ID if successful
print('Event created: %s' % event.get('htmlLink'))
