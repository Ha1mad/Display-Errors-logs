import win32evtlog
import json
import os

server = 'localhost'
log_type ='system'
limit = 50
count = 0

handle = win32evtlog.OpenEventLog(server, log_type)

flags = win32evtlog.EVENTLOG_BACKWARDS_READ | win32evtlog.EVENTLOG_SEQUENTIAL_READ

print("System Errors:\n")
data = []

while True:
    events = win32evtlog.ReadEventLog(handle, flags, 0)
    if not events or count >= limit:
        break

    for event in events:
        if event.EventType == 1:
            print(f"Error Event ID: {event.EventID}")
            print(f"Source: {event.SourceName}")
            print("-" * 70)

            data.append({
                'EventID': event.EventID,
                'SourceName': event.SourceName
            })

            count += 1
            if count >= limit:
                break

# Save JSON ONCE after collecting logs
with open('system_errors.json', 'w') as f:
    json.dump(data, f, indent=4)

# Show exactly where the file is
print("JSON saved to:", os.path.join(os.getcwd(), "system_errors.json"))
