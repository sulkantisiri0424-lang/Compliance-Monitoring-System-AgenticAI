class CommunicationAgent:
    """
    Agent responsible for scanning communication messages
    for potential compliance red flags.
    """

    def __init__(self):
        self.risk_keywords = {
            "bypass compliance": "Possible attempt to bypass compliance controls.",
            "avoid reporting": "Possible attempt to avoid regulatory reporting.",
            "hide transaction": "Possible attempt to conceal a transaction.",
            "secret payment": "Potential undisclosed payment.",
            "ignore kyc": "Possible attempt to bypass KYC requirements.",
            "no records": "Possible attempt to avoid maintaining records."
        }

    def scan_message(self, message):
        message_lower = message.lower()
        findings = []

        for keyword, explanation in self.risk_keywords.items():
            if keyword in message_lower:
                findings.append({
                    "keyword": keyword,
                    "finding": explanation
                })

        if findings:
            risk_level = "HIGH"
        else:
            risk_level = "LOW"

        return {
            "message": message,
            "risk_level": risk_level,
            "findings": findings,
            "flagged": len(findings) > 0
        }