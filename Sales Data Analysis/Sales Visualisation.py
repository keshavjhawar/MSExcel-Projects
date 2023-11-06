
import pandas as pd
pd.set_option('display.max_columns',15)
import os
import matplotlib.pyplot as plt

# 1.Combining_sales_data
files = [file for file in os.listdir("/Users/macos/Downloads/Sales_Data")]

sales_df = pd.DataFrame()

for file in files:
    df = pd.read_csv("/Users/macos/Downloads/Sales_Data/"+file)
    sales_df = pd.concat([sales_df,df])

sales_df.to_csv('/Users/macos/Downloads/Sales_Data_1.csv', index = False)

sales_df = pd.read_csv('/Users/macos/Downloads/Sales_Data_1.csv')


# 2.Cleaning Up Data
sales_df = sales_df.dropna(how='all')
sales_df = sales_df[sales_df['Order Date'].str[0:2] != 'Or']
#
for data in sales_df['Quantity Ordered']:
    if data == '1Quantity Ordered':
      target_index = sales_df[sales_df['Quantity Ordered'] == data].index
      sales_df['Quantity Ordered'][target_index] = 1

# print(list(sales_df['Quantity Ordered']))
df_nan = sales_df[sales_df.isna().any(axis=1)]
# print(df_nan.head())

sales_df.to_csv('/Users/macos/Downloads/Sales_Data_2.csv',index='False')
sales_df = pd.read_csv('/Users/macos/Downloads/Sales_Data_2.csv')

# 3.Finding month with highest and lowest sale
# 3.1 Adding month column
sales_df['Month'] = sales_df['Order Date'].str[0:2].astype('int32')

# 3.2 Adding sales column
sales_df['Quantity Ordered'] = pd.to_numeric(sales_df['Quantity Ordered'])
sales_df['Price Each'] = pd.to_numeric(sales_df['Price Each'])
sales_df['Sales'] = sales_df['Quantity Ordered']*sales_df['Price Each']

# 3.3 Getting the Result
result_1 = sales_df.groupby('Month').sum()
print(result_1)

#3.4 Plotting bar-graph

months = range(1,13)
plt.bar(months,result_1['Sales'])
plt.xticks(months)
plt.ylabel("Sales in USD ($)")
plt.xlabel("Months")
plt.show()

# 4.Finding city with the highest number of sales
# 4.1 Adding City column
sales_df['City'] = sales_df['Purchase Address'].apply(
    lambda x: x.split(',')[1].replace(' ','',1) + ' '+ x.split(',')[2].split(' ')[1])
# # print(sales_df.head())

# 4.2 Getting the Result
result_2 = sales_df.groupby('City').sum()
# print(result_2)
cities = [city for city,df in sales_df.groupby('City')]

# 4.3 Plotting bar-graph
plt.bar(cities,result_2['Sales'])
plt.xticks(rotation = 90,size=5)
plt.ylabel('Sales in USD ($)')
plt.show()

# 5.Finding best time(hrs) to advertise
# 5.1 Adding Hour column
sales_df['Order Date'] = pd.to_datetime(sales_df['Order Date'])
sales_df['Purchase Hour'] = sales_df['Order Date'].dt.hour
# print(sales_df.head())

# 5.2 Getting the Result
result_3 = sales_df.groupby('Purchase Hour').sum()
purchase_hours = [hr for hr,df in sales_df.groupby('Purchase Hour')]

# 5.3 Plotting line-graph
plt.plot(purchase_hours,result_3['Sales'])
plt.xticks(purchase_hours)
plt.grid()
plt.show()

# 6.Which products get sold together the most
# 6.1 Creating DF of products sold together
duplicated = sales_df[sales_df['Order ID'].duplicated(keep=False)]
duplicated['Grouped'] = duplicated.groupby('Order ID')['Product'].transform(lambda x: ','.join(x))
duplicated = duplicated[['Order ID','Grouped']].drop_duplicates()
# print(duplicated.head(10))

# 6.2 Counting sets of 2 sold most together
from itertools import combinations
from collections import Counter

count = Counter()

for row in duplicated['Grouped']:
    row_list = row.split(',')
    count.update(Counter(combinations(row_list,2)))

# print(count.most_common(10))

for key,value in count.most_common(10):
    print(key,value)

# 7. Which product sold the most
product_group = sales_df.groupby('Product')

products = [product for product,df in product_group]
quantity_ordered = product_group.sum()['Quantity Ordered']

plt.bar(products, quantity_ordered)
plt.xticks(products, rotation = 'vertical')
# plt.show()

# 8. Comparison b/w average price and quantity sold
prices = sales_df.groupby('Product').mean()['Price Each']

fig, ax1 =plt.subplots()

ax2 = ax1.twinx()
ax1.bar(products,quantity_ordered,color='g')
ax2.plot(products,prices,'b-')

ax1.set_xlabel('Product Name')
ax1.set_ylabel('Quantity Ordered', color = 'g')
ax2.set_ylabel('Price in ($)',color = 'b')
ax1.set_xticklabels(products,rotation='vertical')

plt.show()
