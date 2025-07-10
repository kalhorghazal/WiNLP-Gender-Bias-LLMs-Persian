import pandas as pd
import numpy as np

df = pd.read_csv("sportNames.csv")

names = pd.read_csv("name2Gender.csv")

df["Gender"] = np.nan

for index, row in df.iterrows():
  name = row["LLM-Generated Name"]
  df.at[index, "Gender"] = names[names["Name"] == name]["Gender"].values[0]

sports = list(df["Sport"].unique())

for sport in sports:
  sportData = df[df["Sport"] == sport]
  femaleRatio = len(sportData[sportData["Gender"] == "female"]) / len(sportData)
  print(sport, femaleRatio)