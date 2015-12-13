with open("LocationsAndTimes.txt") as f:
	everything = f.read().splitlines()

food_places = [item.split(",") for item in everything] 

for item in food_places:
	print(item)