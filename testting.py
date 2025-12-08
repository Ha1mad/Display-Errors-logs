import win32evtlog

server = 'localhost'
log_type ='system'

handle = win32evtlog.OpenEventLog(server, log_type)

flags = win32evtlog.EVENTLOG_BACKWARDS_READ | win32evtlog.EVENTLOG_SEQUENTIAL_READ

print("System Errors:\n")

while True:
    events = win32evtlog.ReadEventLog(handle, flags, 0)
    if not events:
        break
    for event in events:
        if event.EventType == 1:  
            print(f"Error Event ID: {event.EventID}")
            print(f"Source: {event.SourceName}")
            print("-" * 40)