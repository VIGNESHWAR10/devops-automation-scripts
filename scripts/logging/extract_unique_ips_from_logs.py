#!/usr/bin/python3

import re # regular expressions module

def find_unique_ips(log_file):
    """
    Function to find unique IPs from a log file
    :param log_file: Path to the log file
    :return: List of unique IPs
    """

    unique_ips = set() # Set is used to store unique IPs
    ip_regex = re.compile(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}") # Regular expression object to match IP

    with open(log_file, "r") as file:
        for line in file:
            ip = ip_regex.findall(line)
            if ip:
                unique_ips.update(ip)

    return list(unique_ips)

if __name__ == "__main__":

    log_file = input("Enter log file path: ").strip() # Path to the log file
    
    unique_ips = find_unique_ips(log_file)

    print("Unique IPs:", unique_ips)

# Regular Expression explanation:
# r - raw string
# \d - matches any digit
# {1, 3} - between 1 and 3 digits
# \. - matches a period