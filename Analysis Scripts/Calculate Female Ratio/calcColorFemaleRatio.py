import pandas as pd
import numpy as np

df = pd.read_csv("colorNames.csv")

names = pd.read_csv("name2Gender.csv")

df["Gender"] = np.nan

for index, row in df.iterrows():
  name = row["LLM-Generated Name"]
  df.at[index, "Gender"] = names[names["Name"] == name]["Gender"].values[0]

colors = list(df["Color"].unique())

for color in colors:
  colorData = df[df["Color"] == color]
  femaleRatio = len(colorData[colorData["Gender"] == "female"]) / len(colorData)
  print(color, femaleRatio)