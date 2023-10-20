import pandas as pd

sdw2023_api = 'https://sdw-2023-prd.up.railway.app'

users = pd.read_csv("Projetos-DIO/Data Science/ETL-users.csv")
df = users['UserID'].tolist()
print(df)
