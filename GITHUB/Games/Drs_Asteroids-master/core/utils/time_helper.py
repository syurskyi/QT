from datetime import datetime


def get_current_time_in_microseconds():
    curr_time = datetime.now()
    return curr_time.hour * 3600000000 + curr_time.minute * 60000000 + curr_time.second * 1000000 \
        + curr_time.microsecond


def convert_timestamp_to_microseconds(timestamp: datetime):
    return timestamp.hour * 3600000000 + timestamp.minute * 60000000 + timestamp.second * 1000000 \
        + timestamp.microsecond
