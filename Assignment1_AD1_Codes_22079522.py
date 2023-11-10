# -*- coding: utf-8 -*-
"""""""""""""""""
Created on Thu Nov  9 23:01:44 2023

@author: 22079522 - S N Thomas
"""""""""""""""""

import pandas as pd  # Import pandas as pd
import matplotlib.pyplot as plt  # Import matplotlib.pyplot as plt
import numpy as np

# Specifying the link from which data is sourced
link = ("https://assets.publishing.service.gov.uk/media/6544c0fc9e05fd0014be7cad/fruitvegprices-6nov23.csv")

# Reading data from the source 'csv' file
Data = pd.read_csv(link, parse_dates=['date'])

print("Shape of the Data Set", np.shape(Data))  # Shape of the dataset
print("First 3 Values", Data.head(3))  # First 3 rows
print("Last 3 Values", Data.tail(3))  # Last three rows
print("Column Data Types", Data.dtypes)  # Data types of each column
print("Dataset Information")  # Information about the data set
Data.info()
Data.set_index('date', inplace=True)  # Set date column as index

"""""""""""""""""""""""
Data downloading/Reading/exploring ends
"""""""""""""""""""""""
""""""""""""""""""""""""""""""""""
Explore the data set- Displaying all columns and datatypes
"""""""""""""""""""""""""""""""""
# Creating the dataframe for the csv data
df = pd.DataFrame(Data)  # Create Data Frame

# Declaring datetime in index to extract year and month from date.

df.index  # Display index
df['Year'] = df.index.year  # Extract Year from date
df['Month'] = df.index.month  # Extract Month from date

"""""""""""
Filtering data
"""""""""
# Filtering 4 different type of Tomatoes and saving in another variable
# for plotting
Variety_Vegetables_Tomatoes1 = df[((df.category == 'vegetable') &
                                   (df.item == 'tomatoes') & (df.variety == 'cherry'))]
Variety_Vegetables_Tomatoes2 = df[((df.category == 'vegetable') &
                                   (df.item == 'tomatoes') & (df.variety == 'plum'))]
Variety_Vegetables_Tomatoes3 = df[((df.category == 'vegetable') &
                                   (df.item == 'tomatoes') & (df.variety == 'round'))]
Variety_Vegetables_Tomatoes4 = df[((df.category == 'vegetable') &
                                   (df.item == 'tomatoes') & (df.variety == 'vine'))]
Variety_Vegetables = df[((df.category == 'vegetable') &
                         (df.item == 'tomatoes'))]

V1 = Variety_Vegetables_Tomatoes1.price.resample('1M').mean()
V2 = Variety_Vegetables_Tomatoes2.price.resample('1M').mean()
V3 = Variety_Vegetables_Tomatoes3.price.resample('1M').mean()
V4 = Variety_Vegetables_Tomatoes4.price.resample('1M').mean()

V1.dropna().plot(label="Cherry", color='green',
                 linewidth=3, fontsize=10, figsize=(30, 16))
V2.dropna().plot(label="Plum", color='blue',
                 linewidth=3, fontsize=10, figsize=(30, 16))
V3.dropna().plot(label="Round", color='purple',
                 linewidth=3, fontsize=10, figsize=(30, 16))
V4.dropna().plot(label="Vine", color='red',
                 linewidth=3, fontsize=10, figsize=(30, 16))

plt.title("Tomatoes average price from 2018 -2023",
          fontsize=40, fontweight='bold')
plt.xlabel("Year", fontsize=12, fontweight='bold')
plt.ylabel("Average price of tomatoes/month", fontsize=12, fontweight='bold')
plt.legend(fontsize=12)
plt.savefig('Average price of Tomatoes per month.png', dpi=300)
plt.show()

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
BAR CHARTS - Showing mean price of category,variety,item.
This provides general idea of price distribution across the given dataset.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
S1 = df.groupby('category').price.mean()
S2 = df.groupby('item').price.mean()
S3 = df.groupby('variety').price.mean()


fig = plt.figure(figsize=(27, 12))
axis = fig.add_subplot(111)
width = 0.3
colour = ['blue', 'green', 'orange', 'purple']
S1.plot(kind='bar', color=colour, ax=axis, width=width, position=1)
axis.legend()
plt.title('Category,Item and Variety of year 2017-2023',
          fontsize=30, fontweight='bold')
plt.savefig('Barcharts Category,Item and Variety in the Dataset.png', dpi=300)
plt.show()


"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Data reduced to year 2023 to get a better view on the recent trends.
This is plotted across category, item and variety.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

df2023 = df.loc['2023']
T1 = df2023.groupby('category').price.mean()
T2 = df2023.groupby('item').price.mean()
T3 = df2023.groupby('variety').price.mean()

""""""""""""""""""""""""""""""""""
Plotting bar charts for data derived from 
2023 across category,item and variety. 
"""""""""""""""""""""""""""""""""
# Plot for T1

fig = plt.figure(figsize=(27, 12))
axis = fig.add_subplot(221)
width = 0.3
colour = ['blue', 'green', 'orange', 'purple']
T1.plot(kind='bar', color=colour, ax=axis, width=width, position=1)
plt.title('Average Price of Categories for the year 2023',
          fontsize=30, fontweight='bold')
plt.ylabel("Average Price", fontsize=12, fontweight='bold')
plt.xlabel("Categories", fontsize=12, fontweight='bold')
plt.savefig('Average Categories in the Dataset_2023.png', dpi=300)
axis.legend()
plt.show()


# Plot for T2

fig = plt.figure(figsize=(27, 12))
axis = fig.add_subplot(222)
width = 0.3
colour = ['blue', 'green', 'orange', 'purple']
T2.plot(kind='bar', color=colour, ax=axis, width=width, position=1)
plt.title('Average price of Items for the year2023',
          fontsize=30, fontweight='bold')
plt.ylabel("Average Price", fontsize=12, fontweight='bold')
plt.xlabel("Items", fontsize=12, fontweight='bold')
plt.savefig('Average price of Items in the Dataset_2023.png', dpi=300)
axis.legend()
plt.show()


# Plot for T3

fig = plt.figure(figsize=(27, 12))
axis = fig.add_subplot(223)
width = 0.3
colour = ['blue', 'green', 'orange', 'purple']
T3.plot(kind='bar', color=colour, ax=axis, width=width, position=1)
plt.title('Average price of Varieties for the year 2023',
          fontsize=30, fontweight='bold')
plt.ylabel("Average Price", fontsize=12, fontweight='bold')
plt.xlabel("Varieties", fontsize=12, fontweight='bold')
plt.savefig('Average Price of Varieties in the Dataset_2023.png', dpi=300)
plt.show()

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
PIE CHART - Mean price of Category of Products in Retail Data Set for 2023
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Catpie = df2023.groupby(['category']).price.mean()
Catpie.plot(kind='pie', figsize=(20, 12), subplots=True)
plt.title('Mean price of Category of Products in Retail Data Set for 2023',
          fontsize=30, fontweight='bold')
plt.savefig('Piechart.png', dpi=300)
