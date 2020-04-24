
# AGGREGATE STATS (GROUPBY FUNCTION)
import pandas as pd


# load our initial data set
df = pd.read_csv('new_pokemon_data.csv')
print(df.head(5))

print( df.groupby(['Type 1']).mean().sort_values('Defense', ascending=False) )
print( df.groupby(['Type 1']).mean().sort_values('Attack', ascending=False) )
print( df.groupby(['Type 1']).mean().sort_values('HP', ascending=False) )

print( df.groupby(['Type 1']).mean().sort_values('Total', ascending=False) )
print( df.groupby(['Type 1']).sum().sort_values('Total', ascending=False) )
print( df.groupby(['Type 1']).count() )

# add a new column to get an accurate count!
df['count'] = 1
print( df.groupby(['Type 1']).count()['count'] )

# sub-category counts
print( df.groupby(['Type 1', 'Type 2']).count()['count'] )


# WORKING WITH LARGE AMOUNTS OF DATA

# Load in chunks of data at a time
new_df = pd.DataFrame(columns=df.columns)

for df in pd.read_csv('pokemon_data.csv', chunksize=5):   # 5 rows passed in 
	# print(df)
	results = df.groupby(['Type 1']).count()
	new_df = pd.concat([new_df, results])
	# incrementally build new data frame with aggregated stats that you really want






