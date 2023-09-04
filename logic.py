from event import Event
from datetime import datetime, timedelta

calendar_events = []

def can_add_event_no_conflict(new_event):
   # Check for conflicts with existing events
    for event in calendar_events:
        if (
            event.date == new_event.date
            and event.time == new_event.time
        ):
            print("Conflict: An event already exists at the same date and time.")
            return False
    
    # If no conflicts, add the new event to the calendar
    calendar_events.append(new_event)
    print(f"Event '{new_event.title}' added to the calendar.")
    return True

def add_assignment(due_event, hours_needed):
    calendar_events.append(due_event)
    # Calculate the start time for working on the assignment
    start_time = due_event.date + " " + due_event.time
    start_datetime = datetime.strptime(start_time, "%Y-%m-%d %H:%M")
    work_start_datetime = start_datetime - timedelta(hours=hours_needed + 1)

    # Create a new event for working on the assignment
    assignment_event = Event(
        f"Work on {due_event.title}",
        f"Prepare and submit {due_event.title}",
        work_start_datetime.strftime("%Y-%m-%d"),
        work_start_datetime.strftime("%H:%M"),
        due_event.location
    )

    # Check if the assignment event can be added to the calendar
    if can_add_event_no_conflict(assignment_event):
        print(f"Assignment '{due_event.title}' scheduled to start {hours_needed} hours before the due time.")

def add_class(class_event, travel_times):
    # Calculate the start time for the class event
    start_time = class_event.date + " " + class_event.time
    start_datetime = datetime.strptime(start_time, "%Y-%m-%d %H:%M")

    # Calculate the travel time to class
    travel_duration_to_class = timedelta(minutes=travel_times.get(class_event.location, 0))

    # Calculate the end time of the class
    end_datetime = start_datetime + travel_duration_to_class

    # Create the class event
    class_event_start = Event(
        class_event.title,
        class_event.description,
        start_datetime.strftime("%Y-%m-%d"),
        start_datetime.strftime("%H:%M"),
        class_event.location
    )

    class_event_end = Event(
        class_event.title + " (End)",
        "End of class",
        end_datetime.strftime("%Y-%m-%d"),
        end_datetime.strftime("%H:%M"),
        class_event.location
    )

    # Check if both class events can be added to the calendar
    if can_add_event_no_conflict(class_event_start) and can_add_event_no_conflict(class_event_end):
        print(f"Class '{class_event.title}' scheduled with travel time.")
        print(f"Class starts at {class_event_start.time}, ends at {class_event_end.time}")

def add_appointment(appointment_event, travel_times):
    # Calculate the start time for the appointment event
    start_time = appointment_event.date + " " + appointment_event.time
    start_datetime = datetime.strptime(start_time, "%Y-%m-%d %H:%M")

    # Calculate the travel time to the appointment location
    travel_duration_to_appointment = timedelta(minutes=travel_times.get(appointment_event.location, 0))

    # Calculate the end time of the appointment
    end_datetime = start_datetime + travel_duration_to_appointment

    # Create the appointment event
    appointment_event_start = Event(
        appointment_event.title,
        appointment_event.description,
        start_datetime.strftime("%Y-%m-%d"),
        start_datetime.strftime("%H:%M"),
        appointment_event.location
    )

    appointment_event_end = Event(
        appointment_event.title + " (End)",
        "End of appointment",
        end_datetime.strftime("%Y-%m-%d"),
        end_datetime.strftime("%H:%M"),
        appointment_event.location
    )

    # Check if both appointment events can be added to the calendar
    if can_add_event_no_conflict(appointment_event_start) and can_add_event_no_conflict(appointment_event_end):
        print(f"Appointment '{appointment_event.title}' scheduled with travel time.")
        print(f"Appointment starts at {appointment_event_start.time}, ends at {appointment_event_end.time}")


# Create an event instance
event1 = Event("Study Session", "Study for exams", "2023-09-15", "14:00", "Library")
event2 = Event("Meeting", "Project meeting with team", "2023-09-16", "10:30", "Office")
event3 = Event("Assignment 1", "", "2023-09-16", "23:59", "Learn")

# Append Event objects to the calendar_events list

class_event = Event("Math Class", "Math lecture", "2023-09-15", "08:00", "School")
travel_times = {"School": 15, "Library": 20, "Office": 10}  # Travel time in minutes
add_class(class_event, travel_times)

appointment_event = Event("Dentist Appointment", "Dental checkup", "2023-09-16", "14:30", "Dental Clinic")
add_appointment(appointment_event, travel_times)

can_add_event_no_conflict(event1)
can_add_event_no_conflict(event2)
can_add_event_no_conflict(event1)
add_assignment(event3, 5)
for event in calendar_events:
    print(event)