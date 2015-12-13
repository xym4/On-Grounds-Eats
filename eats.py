import re

with open("LocationsAndTimes.txt") as f:
	everything = f.read().splitlines()

food_places = [item.split(",") for item in everything] 

days_of_week = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

food_dict = {}

for location in food_places:
	new_entry = {}
	for entry in (location[1:]):
		split_day_time = [x.strip() for x in entry.split(": ")] # ['Sunday-Thursday', '5:00 pm - 8:00 pm']
		time_range = split_day_time[1].split(" - ")
		if bool(re.search('day-[SMTWF]', entry)):
			day_range = split_day_time[0].split("-") # ['Sunday', 'Thursday']
			start = days_of_week.index(day_range[0])
			end = days_of_week.index(day_range[1])
			new_entry[day_range[0]] = time_range

			while(start != end):
				start+=1
				if start == 7:
					start = 0
				new_entry[days_of_week[start]]=time_range

		else:
			new_entry[split_day_time[0]] = time_range

	food_dict[location[0]] = new_entry

# for entry in food_dict:
# 	print(entry, food_dict[entry])

# print(food_dict.get("Argo Tea").get("Monday"))

			


