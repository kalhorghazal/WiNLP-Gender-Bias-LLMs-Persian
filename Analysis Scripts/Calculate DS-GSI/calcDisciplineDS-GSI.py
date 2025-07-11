import pandas as pd
import numpy as np
import statistics

df = pd.read_csv("academicDisciplineNames.csv")

names = pd.read_csv("name2Gender.csv")

df["Gender"] = np.nan

for index, row in df.iterrows():
  name = row["LLM-Generated Name"]
  df.at[index, "Gender"] = names[names["Name"] == name]["Gender"].values[0]

disciplines = list(df["Academic Discipline"].unique())

absoluteVals = list()

for discipline in disciplines:
  disciplineData = df[df["Academic Discipline"] == discipline]
  femaleRatio = len(disciplineData[disciplineData["Gender"] == "female"]) / len(disciplineData)
  absVal = abs(femaleRatio * 2 - 1)
  absoluteVals.append(absVal)

metric = statistics.mean(absoluteVals)
print("DS-GSI:", metric)