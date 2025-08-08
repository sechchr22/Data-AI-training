import requests
import pandas as pd
import io

response = requests.get("https://coderbyte.com/api/challenges/logs/user-info-csv")

# write your solution here
df = pd.read_csv(io.StringIO(response.text))
df.columns = df.columns.str.lower()
df = df.sort_values(by='email')

print(df.to_json(orient='records'))
