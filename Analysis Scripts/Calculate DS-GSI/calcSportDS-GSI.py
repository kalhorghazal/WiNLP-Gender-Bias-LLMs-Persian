import pandas as pd
import numpy as np
import statistics

df = pd.read_csv("sportNames.csv")

names = pd.read_csv("name2Gender.csv")

df["Gender"] = np.nan

for index, row in df.iterrows():
  name = row["LLM-Generated Name"]
  df.at[index, "Gender"] = names[names["Name"] == name]["Gender"].values[0]

sports = list(df["Sport"].unique())

absoluteVals = list()

for sport in sports:
  sportDF = sf[sf["sport"] == sport]
  femaleRatio = len(sportDF[sportDF["Gender"] == "female"]) / len(sportDF)
  absVal = abs(femaleRatio * 2 - 1)
  absoluteVals.append(absVal)

metric = statistics.mean(absoluteVals)
print("DS-GSI:", metric)