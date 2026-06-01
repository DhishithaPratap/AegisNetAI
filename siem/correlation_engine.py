import json

with open("data/alerts.json", "r") as file:
    alerts = json.load(file)

grouped_alerts = {}

for alert in alerts:

    ip = alert["src_ip"]

    if ip not in grouped_alerts:
        grouped_alerts[ip] = []

    grouped_alerts[ip].append(alert)

print(grouped_alerts)