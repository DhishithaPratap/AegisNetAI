import json
from risk_scoring import RISK_SCORES
from incident_builder import build_incident

# Load alerts
with open("data/alerts.json", "r") as file:
    alerts = json.load(file)

# Group alerts by source IP
grouped_alerts = {}

for alert in alerts:

    ip = alert["src_ip"]

    if ip not in grouped_alerts:
        grouped_alerts[ip] = []

    grouped_alerts[ip].append(alert)

# Store incidents
incidents = []

# Correlation logic
for ip, ip_alerts in grouped_alerts.items():

    alert_types = []

    for alert in ip_alerts:
        alert_types.append(alert["alert_type"])

    risk_score = 0

    for alert in ip_alerts:
        risk_score += RISK_SCORES.get(
            alert["alert_type"],
            0
        )

    if (
        "PORT_SCAN" in alert_types
        and
        "SUSPICIOUS_DOMAIN" in alert_types
    ):

        incident = build_incident(
            ip,
            "RECON_ACTIVITY",
            risk_score
        )

        incidents.append(incident)

        print(
            f"INCIDENT: Recon Activity Detected from {ip}"
        )

        print(
            f"Risk Score: {risk_score}"
        )

# Save incidents
with open("siem/incidents.json", "w") as file:
    json.dump(
        incidents,
        file,
        indent=4
    )