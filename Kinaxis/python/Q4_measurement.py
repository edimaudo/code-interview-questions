# WMAPE, OC and UC calculations
# Using python 2.7

import pandas as pd
df = pd.read_csv("measurement.csv")

# WMAPE, OC and UC for Item Week level
df_item_week = df.groupby(['item','week']).aggregate({'units': 'sum',
                             'forecast': 'sum'}).reset_index()
df_item_week = df.groupby(['item','week']).aggregate({'units': 'sum',
                             'forecast': 'sum'}).reset_index()
df_item_week ['WMAPE'] = df_item_week ['units'] - df_item_week ['forecast']
df_item_week ['WMAPE'] = df_item_week ['WMAPE'].abs()
df_item_week ['WMAPE'] = df_item_week ['WMAPE'] / df_item_week ['units']*df_item_week ['units']
WMAPE = df_item_week['WMAPE'].sum()/df_item_week ['units'].sum()                   
ITEM_WEEK = [WMAPE, 0.8*WMAPE, 0.2*WMAPE]

# WMAPE FOR STORE CATEGORY WEEK LEVEL
df_store_category_week = df.groupby(['store','category','week']).aggregate({'units': 'sum',
                             'forecast': 'sum'}).reset_index()
df_store_category_week ['WMAPE'] = df_store_category_week ['units'] - df_store_category_week ['forecast']
df_store_category_week ['WMAPE'] = df_store_category_week ['WMAPE'].abs()
df_store_category_week ['WMAPE'] = df_store_category_week ['WMAPE'] / df_store_category_week ['units']*df_store_category_week ['units']
WMAPE = df_store_category_week['WMAPE'].sum()/df_store_category_week ['units'].sum()
STORE_CATEGORY_WEEK = [WMAPE, 0.8*WMAPE, 0.2*WMAPE]

df_week_info = [ITEM_WEEK,STORE_CATEGORY_WEEK]
df_final = pd.DataFrame(df_week_info, index = ['Item week','Store Category Week'], columns =['WMAPE','OC','UC'])
print(df_final)