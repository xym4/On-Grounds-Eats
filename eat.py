from bs4 import BeautifulSoup
from urllib.request import urlopen
import re

# Getting urls of all food locations from food homepage
homepage_url = "http://virginia.campusdish.com/"
content = urlopen(homepage_url)
soup = BeautifulSoup(content, "html.parser")
navbar_links = soup.select(".mainnav .navItem ul li a")

location_links = []

for a in navbar_links:
	address = a['href']
	if address[1:9] == "Location":
		location_links.append(address)

# Parsing hours of operation from each food page
for link in location_links:
	food_url = "http://virginia.campusdish.com" + link
	food_content = urlopen(food_url)
	food_soup = BeautifulSoup(food_content, "html.parser")
	all_p = food_soup.select(".aside p")

	hours_index = 0

	# Look for p where first word is "Monday" as that's where hours of operation info begins
	for p in all_p:
		if(p.text.strip()[0:3] == "Mon"):
			hours_index = all_p.index(p)

	# Getting the name of the location
	name = food_soup.select("h1")
	name = name[0].text.strip()

	# First paragraph of page with , stripped of leading & trailing whitespaces, split into list by lines
	stripped_p_list = all_p[hours_index].text.strip().replace("<br>", "").replace("</br>", "").replace("Midnight", "12:00 am").replace("Noon", "12:00 pm").split("\n")

	# First line contains the hours of operation
	hours = stripped_p_list[0]
	
	# All hours of operations are on same line, like 'Monday-Friday: 7:30 am - 1:30 pmSaturday & Sunday: Closed', find indices of split with regex
	regex_indices = [m.span() for m in re.finditer("[amp]{2}[MTWFS]{1}", hours)]
	hours_list = []

	# Splitting will remove letters, so iterate through and collect times instead
	final_hours = [name]
	for i in range(0, len(regex_indices)):
		if i == 0:
			start = 0
			end = regex_indices[i][0]
			final_hours.append(hours[start:end+2].strip())
		else:
			start = regex_indices[i-1][1]-1
			end = regex_indices[i][0]+2
			final_hours.append(hours[start:end].strip())
		if i == len(regex_indices)-1:
			start = regex_indices[i][1]-1
			final_hours.append(hours[start:].strip())

	print(final_hours)




