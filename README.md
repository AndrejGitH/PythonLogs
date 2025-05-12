# PythonLogs - Log File Merger

This Python program reads and merges multiple log files provided by the user.  
It extracts timestamps and log messages, and outputs them into a clean, aligned table format.

---

## Features

- Accepts multiple file paths from user input (space-separated)
- Reads log files and extracts:
  - Timestamps (format: `HH:MM:SS.sss`)
  - Log messages
- Skips lines with corrupted or invalid timestamps
- Merges all logs based on unique timestamps
  - If the same timestamp appears more than once in a file, messages are appended
  - If a timestamp is missing in a file, the output column is left empty
- Outputs the merged log into a file called `mergedLogs.txt`
- Includes unit tests for key functions
