import qrcode
from datetime import datetime

event_summary = "Meeting with Team"
event_location = "Conference Room 1"
event_start = datetime(2024, 5, 30, 9, 0).strftime("%Y%m%dT%H%M%S")
event_end = datetime(2024, 5, 30, 10, 0).strftime("%Y%m%dT%H%M%S")
event_description = "Discuss project progress and next steps."

icalendar_data = f"""BEGIN:VEVENT
SUMMARY:{event_summary}
LOCATION:{event_location}
DTSTART:{event_start}
DTEND:{event_end}
DESCRIPTION:{event_description}
END:VEVENT"""

img = qrcode.make(icalendar_data)

img.save("calendar_event_qr.png")

print("QR code for calendar event generated and saved as 'calendar_event_qr.png'.")
