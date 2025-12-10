# Display-Errors-logs

 Project Display Errors Logs

What the project does

This project is a small python script that makes it way easier to check Windows system errors. So instead of wasting your time this tool automates most of that work for you.

Basically:

  -Reads Windows Event Logs (only the error events)
  -Saves the errors in a JSON file (system_errors.json)
  -Shows them in a simple web page as a table with Event ID and Source

This makes it really easy for the user to see recent system errors quickly without digging through raw logs.


How the project is set up

The project has three main parts:

  1- Python script (backend)
  -Reads Windows Event Logs
  -Filters only error events
  -Saves the data to a JSON file
  -Prints the errors in the console for quick verification

  2- JSON file (storage)
  -Acts as a simple way to save the error data
  -Stores objects with EventID and SourceName
  -Keeps everything organized so the web page can easily load it

  3- Web page (frontend)
  -Simple HTML page with a table
  -Loads the JSON file using JavaScript
  -Displays the errors nicely in a table

Everything is separated cleanly: the Python script handles the data, the JSON file stores it, and the web page shows it to the user. This makes it easy to understand.

 How it works
  -Fetches up to 50 recent error events from the system
  -Prints errors in the console (for quick check)
  -Saves the errors in system_errors.json
  -Displays them in the web page table



Here’s a simple diagram of how everything connects:

                    Windows Event Logs  -->  Python script --> JSON file
                                                                   |
                                                                   v
                                                            Web page table



Good things about the project:

  -Code is simple and easy to read
  -Works without needing any extra software
  -JSON storage makes it easy to share

Conclusion

This project is a simple, useful script for quickly checking Windows errors. Right now, it does exactly what it’s supposed to do: show recent error events in a table. With some small improvements.


Conclusion

This project is a simple, useful script for quickly checking Windows errors. Right now, it does exactly what it’s supposed to do: show recent error events in a table. With some small improvement
