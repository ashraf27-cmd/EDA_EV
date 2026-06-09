import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns



# # General Idea Of  Dataset;

dat = pd.read_csv("Electric_Vehicle_Population_Data.csv")

print("A Peak into the dataset:\n ")
print(dat.head(7))

print("Information Regarding Dataset:\n")
print(dat.info())


# Clean Data

print("How Many Null Values do we have? ")
print(dat.isnull().sum())


print(dat.dtypes)


#Clearing The Null values;

for col in dat.columns:
    
    if dat[col].dtype == 'object':
        dat[col].fillna(dat[col].mode()[0], inplace=True)

    else:
        dat[col].fillna(dat[col].median(), inplace=True)

print("After Cleaning; ")
print(dat.isnull().sum())

print("Duplicate Values")
print(dat.duplicated().sum())

# 1. Manufacturer Market Share (Pie Chart)
marketshare = dat['Make'].value_counts().head(10)
plt.pie(marketshare,labels=marketshare.index,autopct='%1.1f%%')
plt.title("Top Manufacturer Market Share")
plt.show()


# 2. BEV Vs. PHEV - Donut Chart
top_makes = dat['Make'].value_counts().head(10)
ev_share = dat['Electric Vehicle Type'].value_counts()
plt.figure(figsize=(7,7))
plt.pie(ev_share,labels=ev_share.index,autopct='%1.1f%%',startangle=90)
centre_circle = plt.Circle((0,0),0.70,fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)
plt.title("BEV vs PHEV Market Share")
plt.show()


# 3. EV Manufacturer Trends By Year
top_makes = dat['Make'].value_counts().head(5).index
df_top = dat[dat['Make'].isin(top_makes)]
trend_make = (df_top.groupby(['Model Year', 'Make']).size().unstack(fill_value=0))

trend_make.plot(figsize=(10, 6),marker='o')
plt.title("Top EV Manufacturers Trend Over Time")
plt.xlabel("Model Year")
plt.ylabel("EV Registrations")
plt.grid(True, alpha=0.3)
plt.show()


# 4. Avg Electric Range (Bar Chart)
top_range = dat.groupby('Model')['Electric Range'].mean().sort_values(ascending=False).head(10)
top_range.plot(kind='barh')
plt.title("Top 10 EV Models by Average Electric Range")
plt.show()


# 5. CAFV Standards For Incentive Regain (Pie Chart)
cafv = dat['Clean Alternative Fuel Vehicle (CAFV) Eligibility'].value_counts()
cafv.plot(kind='pie', autopct='%1.1f%%')
plt.title("CAFV Eligibility Distribution")
plt.show()
