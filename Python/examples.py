
# Real World Examples with matplotlib in Python

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


# LINE GRAPH
def run_ex1():
	print("Gas Price Example")

	# get data from GitHub
	gas = pd.read_csv('gas_prices.csv')

	# print(gas)
	print(gas.Year[::3])

	y = np.arange(0.0, 11.0, 1.0)

	# create a new figure and resize it
	plt.figure(figsize=(8,5))
	plt.title('Gas Prices over Time (USD)', fontdict={'fontweight': 'bold', 'fontsize': 18})

	# plot the countries we want to show
	plt.plot(gas.Year, gas.USA, 'b.-')
	# plt.plot(gas.Year, gas.Canada)
	plt.plot(gas['Year'], gas.Canada, 'r.-')
	plt.plot(gas['Year'], gas['South Korea'], 'g.-')
	plt.plot(gas.Year, gas.Australia, 'k.-')

	# plot all countries in the same graph
	# for country in gas:
	# 	if country != 'Year':
	# 		print(country)
	# 		plt.plot(gas.Year, gas[country], '.-')

	plt.yticks(y)
	plt.xticks(gas.Year[::3])
	# plt.xticks(gas.Year[::3].tolist() + [2011])

	plt.xlabel('Year')
	plt.ylabel('Gas Price (USD)')
	plt.legend(loc=2)

	plt.savefig('gas_price_graph.svg', format='svg')

	plt.show()


# HISTOGRAMS
def run_ex2():
	print("FIFA Example")

	fifa = pd.read_csv('fifa_data.csv')
	print(fifa.head(5))

	mybins = list(range(40, 101, 5))
	print(mybins)

	# plot overall skill level (how many players above 90? above 80?)
	# plt.hist(fifa.Overall, bins=mybins, color='red')

	# use a color picker to provide a hex code 
	# plt.hist(fifa.Overall, bins=mybins, color='#83f442')
	plt.hist(fifa.Overall, bins=mybins, color='#abcdef')

	plt.xticks(mybins)
	# plt.yticks()

	plt.ylabel('Number of Players')
	plt.xlabel('Skill Level')
	plt.title('Distribution of Player Skills in FIFA 2018')

	plt.show()


# PIE CHARTS
def run_ex3():
	print("FIFA Example with Pie Charts")

	# TEST
	# x = np.arange(0,17,1)
	# plt.figure(figsize=(4,3))
	# plt.plot(x, x**2, 'r.-')

	# wedge sizes are x 

	fifa = pd.read_csv('fifa_data.csv')

	# filter the data set for the left foot players
	left = fifa.loc[fifa['Preferred Foot'] == 'Left'].count()[0]
	right = fifa.loc[fifa['Preferred Foot'] == 'Right'].count()[0]
	print(left)
	print(right)

	my_labels = ['Left', 'Right']
	my_colors = ['#abcdef', '#83f442']

	plt.pie([left,right], labels=my_labels, colors=my_colors, autopct='%.2f %%')

	plt.title('Foot Preference of FIFA Players')

	plt.show()


def run_ex4():
	print("FIFA Example with Pie Charts - Part 2")

	fifa = pd.read_csv('fifa_data.csv')
	print(fifa.Weight)  # convert to kg later

	# remove the lbs text from the weight column
	# weight_values = [x.strip('lbs') if type(x)==str else x for x in fifa.Weight]
	# print(weight_values)  # (still a string)
	
	fifa.Weight = [int(x.strip('lbs')) if type(x)==str else x for x in fifa.Weight]
	print(fifa.Weight) 

	# plt.style.use('default')
	plt.style.use('ggplot')
	plt.title('Weight Distribution of FIFA Players (lbs)')
	
	light = fifa.loc[fifa.Weight < 125].count()[0]
	light_medium = fifa.loc[(fifa.Weight >= 125) & (fifa.Weight < 150)].count()[0]
	medium = fifa.loc[(fifa.Weight >= 150) & (fifa.Weight < 175)].count()[0]
	medium_heavy = fifa.loc[(fifa.Weight >= 175) & (fifa.Weight < 200)].count()[0]
	heavy = fifa.loc[fifa.Weight >= 200].count()[0]

	weights = [light, light_medium, medium, medium_heavy, heavy]
	labels = ['Under 125', '125 - 150', '150 - 175', '175 - 200', 'Over 200']

	explode = (.4, .1, 0, 0, .4)

	plt.pie(weights, labels=labels, autopct='%.2f %%', pctdistance=0.9, explode=explode)

	plt.show()


def run_ex5():
	print("Compare relative strengths of futbol clubs\n")

	fifa = pd.read_csv('fifa_data.csv')
	
	barca = fifa.loc[fifa.Club == 'FC Barcelona']['Overall']
	madrid = fifa.loc[fifa.Club == 'Real Madrid']['Overall']
	revs = fifa.loc[fifa.Club == 'New England Revolution']['Overall']
	print(barca)

	teams = ['FC Barcelona', 'Real Madrid', 'NE Revolution']

	y = np.arange(0,110,10, dtype='int32')

	plt.figure(figsize=(5,8))
	plt.title('Professional Club Comparison')

	bplot = plt.boxplot([barca, madrid, revs], labels=teams, patch_artist=True, medianprops={'linewidth':2})
	
	plt.ylabel('FIFA Overall Rating')
	plt.yticks(y)

	for box in bplot['boxes']:
		# set box edge color
		box.set(color='#4286f4', linewidth=2)
		# set box fill color
		box.set(facecolor='#e0e0e0')

	plt.show()



# MAIN
# run_ex1()
# run_ex2()
# run_ex3()
# run_ex4()
run_ex5()


