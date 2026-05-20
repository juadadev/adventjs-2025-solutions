from datetime import datetime

from_time = "2025*12*24@23|59|30 NP"
takeoff = "2025*12*25@00|00|00 NP"


def time_until_take_off(from_time: str, take_off_time: str) -> int:
    return 0


print(datetime.today())


list_from_time = [char for char in from_time if char.isnumeric()]
str_date = "".join(list_from_time)
print(str_date)
list_takeoff = [char for char in takeoff if char.isnumeric()]
str_date2 = "".join(list_takeoff)
print(str_date2)

convert_date = datetime.strptime(str_date, "%Y%m%d%H%M%S")
convert_date2 = datetime.strptime(str_date2, "%Y%m%d%H%M%S")
print(convert_date)
print(convert_date2)
seconds = (convert_date2 - convert_date).total_seconds()
print(int(seconds))
