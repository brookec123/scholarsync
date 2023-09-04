class Event:
    def __init__(self, title, description, date, time, location):
        self.title = title
        self.description = description
        self.date = date
        self.time = time
        self.location = location

    def __str__(self):
        return f"{self.title} on {self.date} at {self.time}"


# Create an event instance
event1 = Event("Study Session", "Study for exams", "2023-09-15", "14:00", "Library")

# Access event attributes
print(event1.title)       # Output: Study Session
print(event1.date)        # Output: 2023-09-15
print(event1.description) # Output: Study for exams

# Print event details using the __str__ method
print(event1)             # Output: Study Session on 2023-09-15 at 14:00
