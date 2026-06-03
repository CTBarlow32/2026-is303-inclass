import pandas as pd
df = pd.read_csv("Repos/Module 6/world_development_data.csv")
df["region"] = df["region"].str.title().str.strip()
df["gdp_per_capita"] = pd.to_numeric(
    df["gdp_per_capita"].astype(str).str.replace(",", ""), errors = "coerce"
)

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



#Day 10
print(df.groupby("region")["population_thousands"].sum().sort_values(ascending = False))

print(df.groupby("region")["country"].count())

print(df.groupby("region")["life_expectancy"].max())
print(df.loc[df["life_expectancy"].idxmax()])

over_70 = (df.groupby("country")["gdp_per_capita"].sum())
print(f"{over_70}")


gtr_70 = df[df["life_expectancy"]> 70]
ls_60 = df[df["life_expectancy"] < 70]
print (gtr_70["gdp_per_capita"].mean())

#making new column!!!
df["total_gdp"] = df["gdp_per_capita"] * df["population_thousands"]
print(df.groupby("region")["total_gdp"].sum().max())
print(df.groupby("region")["total_gdp"].sum().idxmax())

