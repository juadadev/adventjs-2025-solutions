from datetime import datetime

from_time = "2025*12*24@23|59|30 NP"
takeoff = "2025*12*25@00|00|00 NP"


def time_until_take_off(from_time: str, take_off_time: str) -> int:
    def clear_time(time: str) -> datetime:
        for delim in ["*", "@", "|"]:
            time = time.replace(delim, " ")
        time = time.replace("NP", "")

        return datetime.strptime(time.replace(" ", ""), "%Y%m%d%H%M%S")

    list_from_time = clear_time(from_time)
    take_off_time_converted = clear_time(take_off_time)
    diff_seconds = (take_off_time_converted - list_from_time).total_seconds()
    return int(diff_seconds)


print(time_until_take_off(from_time, takeoff))
