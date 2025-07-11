import pandas as pd
import numpy as np
import statistics

df = pd.read_csv("professionNames.csv")

names = pd.read_csv("name2Gender.csv")

df["Gender"] = np.nan

for index, row in df.iterrows():
  name = row["LLM-Generated Name"]
  df.at[index, "Gender"] = names[names["Name"] == name]["Gender"].values[0]

professions = list(df["Profession"].unique())

absoluteVals = list()

for profession in professions:
  professionData = df[df["Profession"] == profession]
  femaleRatio = len(professionData[professionData["Gender"] == "female"]) / len(professionData)
  absVal = abs(femaleRatio * 2 - 1)
  absoluteVals.append(absVal)

metric = statistics.mean(absoluteVals)
print("DS-GSI:", metric)