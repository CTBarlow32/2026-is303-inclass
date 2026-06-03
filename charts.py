import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Repos/Module 6/world_development_data.csv")


plt.scatter(df["literacy_rate"], df["life_expectancy"])
plt.title("Literacy Rate to Life Expectancy")
plt.xlabel("literacy_rate")
plt.ylabel("life_expectancy")
plt.tight_layout()
plt.savefig("literacy_rate_vs_life_expectancy.png")
plt.show()