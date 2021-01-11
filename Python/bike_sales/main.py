
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
sales['Unit_Cost'].plot(kind='box', vert=False, figsize=(14,6))
plt.show()
