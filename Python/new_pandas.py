
import numpy as np
import pandas as pd

# read in your data in CSV format (very common)
dataFrame = pd.read_csv('./pokemon_data.csv')
# print(dataFrame.head(3))
# print(dataFrame.tail(3))

# we can also load in txt and xlsx formats
# df_excel = pd.read_excel('./pokemon_data.xlsx')
# df_txt = pd.read_csv('./pokemon_data.txt', delimiter='\t')   # TAB separated

# specify the delimiter based on whatever separates the columns in your file type

# Read Headers
print(dataFrame.columns)

# Read Each Column
print(dataFrame['Name'])	 	# index by column header string
print(dataFrame['Name'][0:5])   # index to only give the first 5 names

# index by a LIST of column names
print(dataFrame[['Name', 'Type 1', 'HP']][0:4])

# Read Each Row
print(dataFrame.iloc[1])  # iloc = integer locations
print(dataFrame.iloc[1:4])

# Read a Specific Entry in the Table
print(dataFrame.iloc[2,1])

# Iterate through the rows
for index, row in dataFrame.iterrows():
	# print(index, row)
	print(index, row['Name'])

# locate something that is not just based in integer info
print(dataFrame.loc[dataFrame['Type 1'] == 'Grass'])
print(dataFrame.loc[dataFrame['Type 1'] == 'Fire'])

# high-level stats
print(dataFrame.describe())

# sorting values
# print(dataFrame.sort_values('Name'))
# print(dataFrame.sort_values('Name', ascending=False))
# print(dataFrame.sort_values(['Type 1', 'HP'], ascending=[1,0]))


# Add All the Stat Categories to Get a TOTAL SCORE for each Pokemon
dataFrame['Total'] = dataFrame['HP'] + dataFrame['Attack'] + dataFrame['Defense'] + dataFrame['Sp. Atk'] + dataFrame['Sp. Def'] + dataFrame['Speed']
print(dataFrame.head(5))
# Question: how does it know the data type we are adding together in each column?

# drop a column
dataFrame = dataFrame.drop(columns=['Total'])
print(dataFrame.head(5))

# add a column in a more concise way
# make a new column for the result?
dataFrame['Total'] = dataFrame.iloc[:, 4:10].sum(axis=1)  # axis = 0 means the vertical direction, 1 = horizontal
print(dataFrame.head(5))

# reorder the columns so it makes sense
columns = list(dataFrame.columns.values)
dataFrame = dataFrame[columns[0:4] + [columns[-1]] + columns[4:12]]
print(dataFrame.head(5))

# be careful using index numbers like this because data and columns can change in the future (i.e. avoid magic numbers)

df = dataFrame
# df.to_csv('new_pokemon_data.csv')
df.to_csv('new_pokemon_data.csv', index=False)   # remove the first column showing the index number
# df.to_excel('new_pokemon_data.xlsx', index=False)
# df.to_csv('new_pokemon_data.txt', index=False, sep='\t') # specify that you want tab separated values file



# Filtering Data
print( df.loc[df['Type 1'] == 'Grass'] )
print( df.loc[(df['Type 1'] == 'Grass') & (df['Type 2'] == 'Poison')] )	 # AND  &
print( df.loc[(df['Type 1'] == 'Grass') | (df['Type 2'] == 'Poison')] )  # OR   |


print( df.columns )
print( df.loc[df['HP'] > 70] )  # conditions based on values in the columns
print( df.loc[(df['Type 1'] == 'Grass') & (df['Type 2'] == 'Poison') & (df['HP'] > 70)] )	

new_df = df.loc[(df['Type 1'] == 'Grass') & (df['Type 2'] == 'Poison') & (df['HP'] > 70)]
new_df.to_csv('filtered_pokemon_data.csv')

# NOTE: the old index stays there in the new data frame
# so we can reset the index if we need 

new_df = new_df.reset_index()  # old index is saved as a new column!
new_df = new_df.reset_index(drop=True)   # drop old index column
# new_df = new_df.reset_index(drop=True, inplace=True)   # better for memory management
print(new_df)

# CHECK THE RESET INDEX (I DON'T THINK IT'S WORKING)

# Filter out all the MEGA Pokemon

print(df.loc[df['Name'].str.contains('Mega')])
print(df.loc[~df['Name'].str.contains('Mega')])  # do not show Name if it contains Mega


# regular expressions (regex)
import re

print( df.loc[df['Type 1'].str.contains('Fire|Grass', regex=True)] )
print( df.loc[df['Type 1'].str.contains('fire|grass', flags=re.I, regex=True)] )

# All Pokemon that begin with "pi"
print( df.loc[df['Name'].str.contains('pi[a-z]*', flags=re.I, regex=True)] )
print( df.loc[df['Name'].str.contains('^pi[a-z]*', flags=re.I, regex=True)] )

# Conditional Changes
df.loc[df['Type 1'] == 'Fire', 'Type 1'] = 'Flamer'
print(df.head(10))

df.loc[df['Type 1'] == 'Flamer', 'Legendary'] = True
print(df.head(10))

# df.loc[df['Total'] > 500, ['Generation', 'Legendary']] = 'CHECK'
df.loc[df['Total'] > 500, ['Generation', 'Legendary']] = ['Test1', 'Test2']
print(df)






