# Complete the droppedRequests function below.
def droppedRequests(requestTime):
    times_record = {}

    ten_sec_drops = {}
    minute_drops = {}

    for request in requestTime:
        if request in times_record:
            times_record[request] += 1
        else:
            times_record[request] = 1

    # seconds drop
    seconds_drop = 0
    for item in times_record:
        if times_record[item] > 3:
            seconds_drop += times_record[item] - 3

    times = sorted([item for item in times_record])

    # 10 seconds drop
    ten_seconds_drop = 0
    for item in times:
        cur_time = item
        count_past_10_sec = 0

        for time in range(cur_time - 9, cur_time + 1):
            if time in times_record:
                if not time in ten_sec_drops:
                    count_past_10_sec += times_record[time]
                    ten_sec_drops[time] = True
                else:
                    pass

        if count_past_10_sec > 20:
            ten_seconds_drop += count_past_10_sec - 20

            # minutes drop
    minute_drop = 0
    for item in times:

        cur_time = item
        count_past_min = 0

        for time in range(cur_time - 59, cur_time + 1):
            if time in times_record:
                if not time in minute_drops:
                    count_past_min += times_record[time]
                    minute_drops[time] = True
                else:
                    pass

        if count_past_min > 60:
            minute_drop += count_past_min - 60

    return seconds_drop + ten_seconds_drop + minute_drop

