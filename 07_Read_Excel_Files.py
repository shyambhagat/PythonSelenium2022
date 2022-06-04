import pandas as pd

countriesDF = pd.read_excel("Data/Countries.xlsx")

print(countriesDF)

for index, row in countriesDF.iterrows():
    print(row["Contry"],  row["Continent"])