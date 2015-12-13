# class OperationDay:
# 	def __init__(self, entry_string):
#       self.entry_string = entry_string

#       def get_days(self):
#       	for entry in self.entry_string:
#       		if bool(re.search('day-[SMTWF]', entry)):
#       			split_day_time = [x.strip() for x in entry.split(": ")] # ['Sunday-Thursday', '5:00 pm - 8:00 pm']
#       			day_range = split_day_time[0].split("-") # ['Sunday', 'Thursday']
#       			start = day_range.index(day_range[0])
