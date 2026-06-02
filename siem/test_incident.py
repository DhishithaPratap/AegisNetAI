from incident_builder import build_incident

incident = build_incident(
    "10.0.0.5",
    "RECON_ACTIVITY",
    55
)

print(incident)