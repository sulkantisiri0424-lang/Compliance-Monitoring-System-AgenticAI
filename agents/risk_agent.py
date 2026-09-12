class RiskAgent:
    """
    Agent responsible for classifying compliance risk
    based on the calculated risk score.
    """

    def classify_risk(self, risk_score):
        if risk_score >= 70:
            return "HIGH"

        elif risk_score >= 40:
            return "MEDIUM"

        else:
            return "LOW"

    def recommend_action(self, risk_level):
        if risk_level == "HIGH":
            return "Escalate transaction for manual compliance review."

        elif risk_level == "MEDIUM":
            return "Continue enhanced monitoring."

        else:
            return "Transaction appears compliant. Continue normal monitoring."