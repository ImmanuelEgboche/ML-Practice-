import pandas as pd

#Reading the csv file 
df = pd.read_csv('State_zhvi_bdrmcnt_1_by_month_year.csv')


# what does melt do
# chaning so we have it in date order
df_long = df.melt(id_vars=df.columns[:5], var_name="Date", value_name="HousePrice")

df_long['Date'] = pd.to_datetime(df_long['Date'])

df_long['Year'] = df_long['Date'].dt.year

df_long['Month'] = df_long['Date'].dt.month

grouped = df_long.groupby(['RegionName','Year','Month'])['HousePrice'].mean()

# save to csv file and plot each state seperately

grouped.to_csv('every_state.csv')
print('done')