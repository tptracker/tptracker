# This is the code for connecting excel to python
from typing import Dict, List
from time import sleep

# the interval after which we have to check the changes in the .csv file
CHECK_INTERVAL = 10


# dumper: a bathroom user
# dumpstation : a bathroom
#
# HIGHLIGHTS:
#
# 1. The program will be running continuously as it will have to read the
#    changing csv file.
#
# 2. We can check for data after every 10 minutes.
#    I thought of 10 minutes because I assumed that will be the average interval
#    between two dumpers will visiting a specific dumpstation. We may change
#    this value in future
#
# 3. After a check if False is detected in a room, we will want to email the
#    staff.
#

def data_extractor(file) -> Dict[str, bool]:
    """ Reads the data from the <file> and -+returns a dict with keys as the
    location and value as the current status of the toilet paper.

    --- Significance of Values ---
    True:
        Toilet paper is present
    False:
        Toilet paper is empty and needs a refill"""
    # TODO: Implement this function


def data_updater() -> None:
    """ Checks for data after every <CHECK_INTERVAL> minutes"""
    full = True
    # while every toilet paper is full
    while full:
        file = open('test_data.csv', 'r')
        data = data_extractor(file)
        # Checking if there is a toilet roll which is empty
        if False in data.values():
            # there is a toilet role which is empty
            full = False
            send_email()
        # Recheck for data after 10 minutes
        sleep(CHECK_INTERVAL * 60)


def data_scanner(info: Dict[str, bool]):  # return type to be assigned
    """ Scans through the <info> and detects if a False value exists triggers
    the email function"""
    # TODO: Implement this function


def send_email():
    # TODO: Create this function to send email as <data_scanner> triggers it to
    pass


if __name__ == '__main__':
    input('Press enter to start the searching')
    data_updater()
    # TODO: type 'exit' to stop the program
