PythonLogs - Log File Merger
This program reads and processes log files provided by the user and merges them into a single, structured output file.

Main Features:
Accepts multiple log file paths as input (space-separated)

Reads and extracts timestamps and log messages

Automatically handles:

Duplicate timestamps (in one file: messages are appended)

Missing data (empty cells left for missing timestamps)

Corrupted timestamps (invalid formats are skipped)

Merges all logs into a single file: mergedLogs.txt

Includes basic unit tests using Python’s unittest
