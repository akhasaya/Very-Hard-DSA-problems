# We want to schedule a meeting, for two people.
# We are given inputs of working time of two people and we have a list of meetings for two people.
# meeting duration is another input.

# Now we need to compute a list of possible timings for this output

""" eg
{
  "calendar1": [
    ["9:00", "10:30"],
    ["12:00", "13:00"],
    ["16:00", "18:00"]
  ],
  "calendar2": [
    ["10:00", "11:30"],
    ["12:30", "14:30"],
    ["14:30", "15:00"],
    ["16:00", "17:00"]
  ],
  "dailyBounds1": ["9:00", "20:00"],
  "dailyBounds2": ["10:00", "18:30"],
  "meetingDuration": 30
}

"""
from datetime import time

def calendarMatching(calendar1, dailyBounds1, calendar2, dailyBounds2, meetingDuration):
    commonDailyBound = getCommonTime(dailyBounds1, dailyBounds2)
    if len(commonDailyBound) == 0:
        return [[]]
    allMeetings = getMeetingTimes(calendar1, calendar2)
    freeTime = subtract(commonDailyBound, allMeetings)
    possibleMeetingTimes = isGreaterThanOrEqualTo(freeTime, meetingDuration)
    answer = []
    for time in possibleMeetingTimes:
        answer.append([time[0].strftime('%-H:%M'), time[1].strftime('%-H:%M')])
    return answer

def toTime(str):
    hour, min = str.split(":")
    return time(int(hour), int(min))
    
def getCommonTime(dailyBounds1, dailyBounds2):
    startTime1 = toTime(dailyBounds1[0])
    startTime2 = toTime(dailyBounds2[0])
    endTime1 = toTime(dailyBounds1[1])
    endTime2 = toTime(dailyBounds2[1])

    if min(endTime1, endTime2) > max(startTime1, startTime2):
        return [max(startTime1, startTime2), min(endTime1, endTime2)]

    else:
        return []

def getMeetingTimes(calendar1, calendar2):
    calendar1.extend(calendar2)
    calendar1 = list(map(lambda x : [toTime(x[0]), toTime(x[1])], calendar1))
    calendar1.sort()
    stack = []

    for times in calendar1:
        if len(stack) == 0 or times[0] > stack[-1][1]:
            stack.append(times)
        else:
            stack[-1][1] = max(stack[-1][1], times[1])

    return stack

def subtract(bound, meetings):
    answer = []
    if len(meetings) == 0:
        return [bound]
    index = 0
    while index < len(meetings) and meetings[index][1] < bound[0]:
        index += 1
    index += 1
        
    if bound[0] < meetings[index-1][0]:
        answer.append([bound[0],meetings[index-1][0]])

    while index < len(meetings) and meetings[index][0] <= bound[1]:
        if meetings[index][0] > meetings[index-1][1]:
            answer.append([meetings[index-1][1], meetings[index][0]])
        index += 1

    if bound[1] > meetings[index-1][1]:
        answer.append([meetings[-1][1], bound[1]])

    return answer

def isGreaterThanOrEqualTo(freeTime, duration):
    return list(filter(lambda x: (x[1].hour * 60 + x[1].minute - x[0].hour * 60 - x[0].minute) >= duration, freeTime))
    
