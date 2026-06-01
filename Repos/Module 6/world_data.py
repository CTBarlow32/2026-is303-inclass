import pandas as pd
df = pd.read_csv("Repos/Module 6/world_development_data.csv")
print(df.head())
print(df.describe())
print(df.shape)
print(df.info())

water_crisis = df[df["clean_water_pct"] < 80]
print(water_crisis[["country", "clean_water_pct"]])

#Life Expectency Below 60
life_expectancy = df[df["life_expectancy"] < 60]
print(life_expectancy[["country", "life_expectancy"]])

#Highest Life Expectency
life_expectancy_highest = df.loc[df["life_expectancy"].idxmax()]
print(life_expectancy_highest[["country", "life_expectancy"]])

#Unique Regions
df["region"] = df["region"].str.title().str.strip()
regions = df["region"].unique()
print(regions)

#Missing values in entire data
print(df.isnull().sum())

#sub Saharan Africa
ssa = df[df["region"]== "Sub-Saharan Africa"]
print(ssa[["country", "region"]])

#Fill in water
df["clean_water_pct"] = df["clean_water_pct"].fillna(0)
print(df[["clean_water_pct"]])

assert df["clean_water_pct"].notna().all(), "Missing clean water data!"

