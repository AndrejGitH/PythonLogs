#Get N files - from user input
#Store files - each file will be in dictonary - timestamp: key, log detail: value
#Each dictionary(file) will be stored in the list
#Extract unique timestamps - hashset
#Sort unique timestamps - or use sortedset
#Write a unique timestamp first, then search in dictionary if there is such key, if yes, write log detail in same row, if not, wriet N/A

import os

#User provided path
file_paths = input("Enter file paths (separated by spaces): ").split()
#List to hold all dictionaries which contain file data
all_logs = []

#Algo for getting data into the list
for path in file_paths:
    file_dictionary = {}

    try:
        with open(path, 'r') as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                space_index = line.find(' ')
                if space_index != -1:
                    timestamp = line[:space_index]
                    message = line[space_index+1:]
                    #If multiple logs at the same time, append them together
                    if timestamp in file_dictionary:
                        file_dictionary[timestamp].append(message)
                    else:
                        file_dictionary[timestamp] = [message]

        all_logs.append(file_dictionary)
    
    except FileNotFoundError:
        print(f"File not found: {path}")

#Store all unique timestamps
all_timestamps = set()
for file in all_logs:
    for timestamp in file.keys():
        all_timestamps.add(timestamp)

#Sorting unique timestamps
sorted_timestamps = sorted(all_timestamps)

#Set column width
timestamp_width = 13
max_length = 0

#Find the longest message
for log in all_logs:
    for message in log.values():
        appended = ";".join(message)
        max_length = max(max_length, len(appended)) 

text_width = max(max_length + 5,5)

#Write header to the output file
with open("mergedLogs.txt", "w") as output:
    output.write("Timestamp".ljust(timestamp_width))
    for path in file_paths:
        output.write("| " + os.path.basename(path).ljust(text_width))
    output.write("\n")

#Check if the list contain particular timestamp, if not, write N/A
    for time in sorted_timestamps:
        output.write(time.ljust(timestamp_width))
        for file in all_logs:
            if time in file:
                messages = ";".join(file[time])
                output.write("| " + messages.ljust(text_width))
            else:
                output.write("| "+ "N/A".ljust(text_width))

        output.write("\n")

print("Merging successfull!")