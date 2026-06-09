import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt 


# # General Idea Of  Dataset;

dat = pd.read_csv("Electric_Vehicle_Population_Data.csv")

# print("A Peak into the dataset:\n ")
# print(dat.head(7))

# print("Information Regarding Dataset:\n")
# print(dat.info())


# # Clean Data

# print("How Many Null Values do we have? ")
# print(dat.isnull().sum())


# print(dat.dtypes)


# #Clearing The Null values;

# for col in dat.columns:
    
#     if dat[col].dtype == 'object':
#         dat[col].fillna(dat[col].mode()[0], inplace=True)

#     else:
#         dat[col].fillna(dat[col].median(), inplace=True)

# print("After Cleaning; ")
# print(dat.isnull().sum())

# print("Duplicate Values")
# print(dat.duplicated().sum())






#

top_makes = dat['Make'].value_counts().head(10)

# plt.figure(figsize=(8,6))
# top_makes.sort_values().plot(kind='barh')
# plt.title("Top 10 EV Manufacturers by Registrations (BEV & PHEV incl.)")
# plt.xlabel("Number of EV Registrations")
# plt.ylabel("Manufacturer")
# plt.show()


# ev_share = dat['Electric Vehicle Type'].value_counts()

# plt.figure(figsize=(7,7))
# plt.pie(
#     ev_share,
#     labels=ev_share.index,
#     autopct='%1.1f%%',
#     startangle=90
# )

# centre_circle = plt.Circle((0,0),0.70,fc='white')
# fig = plt.gcf()
# fig.gca().add_artist(centre_circle)

# plt.title("BEV vs PHEV Market Share")
# plt.show()

# import seaborn as sns

# top_makes = dat['Make'].value_counts().head(5).index

# df_top = dat[dat['Make'].isin(top_makes)]

# trend_make = df_top.groupby(
#     ['Model Year', 'Make']
# ).size().unstack(fill_value=0)

# print(trend_make.shape)
# print(trend_make.head())

# plt.figure(figsize=(10,6))
# sns.heatmap(trend_make, cmap='YlGnBu')
# plt.title("EV Manufacturer Registrations by Year")
# plt.show()


# top_range = dat.groupby('Model')['Electric Range'].mean().sort_values(ascending=False).head(10)

# top_range.plot(kind='barh')
# plt.title("Top 10 EV Models by Average Electric Range")
# plt.show()


# cafv = dat['Clean Alternative Fuel Vehicle (CAFV) Eligibility'].value_counts()

# cafv.plot(kind='pie', autopct='%1.1f%%')
# plt.title("CAFV Eligibility Distribution")
# plt.show()

# market_share = dat['Make'].value_counts().head(10)

# plt.pie(
#     market_share,
#     labels=market_share.index,
#     autopct='%1.1f%%'
# )

# plt.title("Top Manufacturer Market Share")
# plt.show()
yearly = dat['Model Year'].value_counts().sort_index()

growth = yearly.pct_change()*100

growth.plot()
plt.axhline(0, linestyle='--')
plt.title("Year-over-Year EV Growth Rate (%)")
plt.show()