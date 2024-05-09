import requests
import time
import pandas as pd
pd.set_option('display.max_rows', None)
df = pd.DataFrame()
for i in range(0, 60):
    pi_time = requests.get("https://4feaquhyai.execute-api.us-east-1.amazonaws.com/api/pi")
    df = df._append(pi_time.json(), ignore_index=True)
    time.sleep(60)
print(df)
