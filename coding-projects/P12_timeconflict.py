# POTD 12 skel
# Author: Mackenzie Gallovitch
# Date: 6 February 2026
# Description: Time Conflict with Event

import sys


 
def to_seconds(hms_tuple):
    """ Returns the total number of seconds represented by a duration given as
    a 3-tuple containing (hours, minutes, and seconds). """
    
    (hours, minutes, seconds) = hms_tuple
    
    hours_sec = (hours * (60**2))
    minutes_sec = (minutes * 60)
    total_seconds = hours_sec + minutes_sec + seconds
    
    return(total_seconds)


def to_hms(seconds):
    """ Returns a tuple of (hours, minutes, seconds) for the given
    raw number of seconds. Precondition: seconds >= 0. """
    
    if seconds >= 0:
        sec_hours = (seconds // (60**2))
        sec_min = ((seconds % (60**2)) // 60)
        seconds = (seconds % 60)
        
    return (sec_hours, sec_min, seconds)

    
def conflicts(start_time, end_time, query_time):
    """ Returns whether query_time is inside the interval from start_time to
    end_time, including the endpoints. Preconditions: Input times are given
    as 3-tuples of (hour, minute, second) in 24h format, and start_time is
    before end_time (on the same day). """
    
    start_seconds = to_seconds(start_time)
    end_seconds = to_seconds(end_time)
    query_seconds = to_seconds(query_time)
    
    if start_seconds < end_seconds and (query_seconds < start_seconds or query_seconds > end_seconds):
        status = False
        
    else:
        status = True

    
    
    return (status)


if __name__ == "__main__":
    start_t = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
    end_t   = int(sys.argv[4]), int(sys.argv[5]), int(sys.argv[6])
    query_t = int(sys.argv[7]), int(sys.argv[8]), int(sys.argv[9])
    
    if conflicts(start_t, end_t, query_t) == True:
        print(query_t, "conflicts with the interval from", start_t, "to", end_t)
        
    else:
        print(query_t, "does not conflict with the interval from", start_t, "to", end_t)
