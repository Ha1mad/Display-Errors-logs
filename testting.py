import win32evtlog
import json
import os

server = 'localhost'
log_type = 'system'
limit = 50
count = 0

handle = win32evtlog.OpenEventLog(server, log_type)

flags = win32evtlog.EVENTLOG_BACKWARDS_READ | win32evtlog.EVENTLOG_SEQUENTIAL_READ

print("Looking for system errors...\n")
data = []

while True:
    events = win32evtlog.ReadEventLog(handle, flags, 0)
    if not events or count >= limit:
        break

    for event in events:
        if event.EventType == 1:
            
            time_str = "N/A"
            if event.TimeGenerated:
                try:
                    time_str = event.TimeGenerated.strftime('%Y-%m-%d %H:%M:%S')
                except:
                    time_str = str(event.TimeGenerated)
            
            
            desc = "No description"
            if event.StringInserts:
                try:
                    
                    parts = []
                    for item in event.StringInserts:
                        if item:
                            parts.append(str(item))
                    if parts:
                        desc = ' '.join(parts)
                except:
                    pass
            
            print(f"ID: {event.EventID} | Source: {event.SourceName} | Time: {time_str}")
            
            data.append({
                'EventID': event.EventID,
                'SourceName': event.SourceName,
                'TimeGenerated': time_str,
                'Description': desc
            })

            count += 1
            if count >= limit:
                break


win32evtlog.CloseEventLog(handle)

with open('system_errors.json', 'w') as f:
    json.dump(data, f, indent=4)

print(f"\nFound {count} errors")
print(f"Saved to: {os.path.join(os.getcwd(), 'system_errors.json')}")
