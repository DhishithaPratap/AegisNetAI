def build_incident(
    ip,
    incident_type,
    risk_score
):

    return {
        "src_ip": ip,
        "incident_type": incident_type,
        "risk_score": risk_score
    }