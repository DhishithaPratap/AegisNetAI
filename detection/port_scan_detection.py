import pandas as pd

df = pd.read_json(
    "data/tcp_logs.json",
    lines=True
)

port_counts = (
    df.groupby("src_ip")["port"]
      .nunique()
)

print("Port Counts:")
print(port_counts)

for ip, count in port_counts.items():

    print(f"Checking {ip} -> {count} ports")

    if count >= 1:
        print(
            f"ALERT: Possible Port Scan Detected from {ip}"
        )