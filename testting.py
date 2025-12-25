import win32evtlog
import json
import time
from datetime import datetime

logs_to_check = ['System', 'Application']
json_file = 'system_errors.json'

def get_events():
   
    
    all_events = []
    
    for log_type in logs_to_check:
        try:
            print(f"  Reading {log_type}...")
            handle = win32evtlog.OpenEventLog('localhost', log_type)
            
            
            flags = win32evtlog.EVENTLOG_SEQUENTIAL_READ | win32evtlog.EVENTLOG_BACKWARDS_READ
            
            
            events = win32evtlog.ReadEventLog(handle, flags, 4096)
            
            if events:
                print(f"    Got {len(events)} events")
                
                
                for event in events[:10]:
                    
                    time_str = "No time"
                    if event.TimeGenerated:
                        try:
                            
                            hour = event.TimeGenerated.hour + 3
                            if hour >= 24:
                                hour -= 24
                            time_str = f"{event.TimeGenerated.year}-{event.TimeGenerated.month:02d}-{event.TimeGenerated.day:02d} {hour:02d}:{event.TimeGenerated.minute:02d}:{event.TimeGenerated.second:02d} KSA"
                        except:
                            time_str = str(event.TimeGenerated)
                    
                    
                    if event.EventType == 1:
                        etype = "ERROR"
                    elif event.EventType == 2:
                        etype = "WARNING"
                    else:
                        etype = "INFO"
                    
                    all_events.append({
                        'EventID': event.EventID,
                        'SourceName': event.SourceName,
                        'TimeGenerated': time_str,
                        'EventType': etype,
                        'Log': log_type, 
                        'Description': str(event.StringInserts)[:150] if event.StringInserts else   'no details'
                    })
            
            win32evtlog.CloseEventLog(handle)
            
        except Exception as e:
            print(f"    Error: {e}")
    
    return all_events

def main():
    print("Windows Event Monitor")
    print("=" * 50)
    
    try:
        check_count = 0
        while True:
            check_count += 1
            now = datetime.now().strftime('%H:%M:%S')
            
            print(f"\n[{now}] Check #{check_count}")
            
            events = get_events()
            
            if events:
            
                events = events[:10]
                
                
                with open(json_file, 'w') as f:
                    json.dump(events, f, indent=2)
                
                print(f"Saved {len(events)} events to {json_file}")
                
                
                for i, evt in enumerate(events[:3]):
                    print(f"  {i+1}. {evt['SourceName']} - {evt['EventType']}")
                
            else:
                print("No events found")
                
                with open(json_file, 'w') as f:
                    json.dump([], f, indent=2)
            
            print(f"\nWaiting 10 seconds...")
            time.sleep(10)
            
    except KeyboardInterrupt:
        print("\n\nStopped!")

if __name__ == "__main__":
    main()
