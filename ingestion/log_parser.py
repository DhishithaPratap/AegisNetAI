import pandas as pd

df = pd.read_json(
    "data/tcp_logs.json",
    lines=True
)

print(df.head())