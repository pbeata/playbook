
# Data Analysis Tutorial 
# Real-world example using bike sales data

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Read in the input data in .csv format into a DATA FRAME:
sales = pd.read_csv('./data/sales_data.csv',
	parse_dates=['Date'])

# Check the number of rows and columns with the SHAPE function:
print(sales.shape)

# To see information about our data set (column labels, non-null count, and data type per column)
print(sales.info())

# Get general statiscal properties of our data set
# (count, mean, std, min, 25%, 50%, 75%, max) --> quick statistical view of our data
print(sales.describe())
print("==========================================")

# Let's analyze the "unit_cost" column only
print(sales['Unit_Cost'].describe())

# Single out just the mean and median
print( "Mean Unit Cost:   " + str(sales['Unit_Cost'].mean()))
print( "Median Unit Cost: " + str(sales['Unit_Cost'].median()))

# Plot some data about the unit cost using the Pandas library:
sales['Unit_Cost'].plot(kind='box', vert=False, figsize=(12,5))
plt.show()

# Density plot example (SKIP PLOT)
# sales['Unit_Cost'].plot(kind='density', figsize=(12,5)) # kde
# plt.show()

# Now let's add in the mean and median to the density plot
ax = sales['Unit_Cost'].plot(kind='density', figsize=(12,5)) # kde
ax.axvline(sales['Unit_Cost'].mean(), color='red')
ax.axvline(sales['Unit_Cost'].median(), color='green')
plt.show()

# Finally, we can plot a histogram of the costs
ax = sales['Unit_Cost'].plot(kind='hist', figsize=(12,5))
ax.set_xlabel('Price (USD)')
ax.set_ylabel('Number of Sales')
plt.show()



# TESTING A PLOT WITH UBUNTU AND PYTHON 3
# df = pd.DataFrame({
#     'name':['john','mary','peter','jeff','bill','lisa','jose'],
#     'age':[23,78,22,19,45,33,20],
#     'gender':['M','F','M','M','M','F','M'],
#     'state':['california','dc','california','dc','california','texas','texas'],
#     'num_children':[2,0,0,3,2,1,4],
#     'num_pets':[5,1,0,5,2,2,3]
# })

# # a scatter plot comparing num_children and num_pets
# df.plot(kind='scatter',x='num_children',y='num_pets',color='red')
# plt.show()
