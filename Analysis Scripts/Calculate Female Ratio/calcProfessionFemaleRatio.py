import pandas as pd
import numpy as np

df = pd.read_csv("professionNames.csv")

names = pd.read_csv("name2Gender.csv")

df["Gender"] = np.nan

for index, row in df.iterrows():
  name = row["LLM-Generated Name"]
  df.at[index, "Gender"] = names[names["Name"] == name]["Gender"].values[0]

professions = list(df["Profession"].unique())

for profession in professions:
  professionData = df[df["Profession"] == profession]
  femaleRatio = len(professionData[professionData["Gender"] == "female"]) / len(professionData)
  print(profession, femaleRatio)