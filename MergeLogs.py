#Get N files - from user input
#Store files - each file will be in dictonary - timestamp: key, log detail: value
#Each dictionary(file) will be stored in the list
#Extract unique timestamps - hashset
#Sort unique timestamps - or use sortedset
#Write a unique timestamp first, then search in dictionary if there is such key, if yes, write log detail in same row, if not, leavte the space empty

import os
import sys


def get_paths():
    """Get path from user as paramter"""

    file_paths = input("Enter file paths (separated by spaces): ").split()

    #Remove duplicates and whitespaces
    file_paths = list(set([p.strip() for p in file_paths if p.strip()]))

    if not file_paths:
        print("No file path entered!")
        sys.exit()
    return file_paths


def check_valid_format(timestamp):
    """Check if the timestamp is in the correct format"""

    parts = timestamp.split(':')
    if len(parts) != 3:
        return False
    try:
        hours = int(parts[0])
        minutes = int(parts[1])
        seconds_part = parts[2].split('.')
        if len(seconds_part) != 2:
            return False
        seconds = int(seconds_part[0])
        milliseconds = int(seconds_part[1])
        return True
      
    except ValueError:
        return False


def get_log_files(file_paths):
    """Reading the files and storing content in a list of dictionaries"""

    #List to hold all dictionaries which contain file data
    logs_list = []

    #Algo for getting data into the list
    for path in file_paths:
        file_dictionary = {}

        try:
            with open(path, 'r', encoding="utf-8") as file:
                for line in file:
                    line = line.strip()
                    if not line:
                        continue
                    space_index = line.find(' ')
                    if space_index != -1:
                        timestamp = line[:space_index]
                        message = line[space_index+1:]
                        #If timestampt is corrupted - skip the line
                        if not check_valid_format(timestamp):
                            continue
                        #If multiple logs at the same time, append them together
                        if timestamp in file_dictionary:
                            file_dictionary[timestamp].append(message)
                        else:
                            file_dictionary[timestamp] = [message]

            logs_list.append(file_dictionary)
        except FileNotFoundError:
            print(f"File not found: {path}")
        except Exception as ex:
            print("Error occured! Details: ", ex)

    if not logs_list:
        print("No valid logs to process! Exiting the program.")
        sys.exit()

    return logs_list


def get_timestamps(logs_list):
    """Sorted set of all unique timestamps"""

    #Store all unique timestamps
    all_timestamps = set()
    for file in logs_list:
        for timestamp in file.keys():
            all_timestamps.add(timestamp)
    #Sorting unique timestamps
    sorted_timestamps = sorted(all_timestamps)
    return sorted_timestamps


def get_longest_message(logs_list):
    """Get the longest message in the logs"""

    max_length = 0
    for log in logs_list:
        for message in log.values():
            appended = ";".join(message)
            max_length = max(max_length, len(appended)) 

    return max(max_length + 5,5)


def get_merged_logs(file_paths, logs_list, sorted_timestamps):
    """Merging logs into a single file"""

    #Set column width
    timestamp_width = 13
    text_width = get_longest_message(logs_list)

    #Write header to the output file
    with open("mergedLogs.txt", "w", encoding="utf-8") as output:
        output.write("Timestamp".ljust(timestamp_width))
        for path in file_paths:
            output.write("| " + os.path.basename(path).ljust(text_width))
        output.write("\n")

    #Check if the list contains particular timestamp, if not, leave it blank
        for time in sorted_timestamps:
            output.write(time.ljust(timestamp_width))
            for file in logs_list:
                if time in file:
                    messages = ";".join(file[time])
                    output.write("| " + messages.ljust(text_width))
                else:
                    output.write("| " + "".ljust(text_width))

            output.write("\n")

    print("Merging successfull!")


def main():
    paths = get_paths()
    logs = get_log_files(paths)
    sorted_timestamps = get_timestamps(logs)
    get_merged_logs(paths,logs,sorted_timestamps)

if __name__ == "__main__":
   main()