from datetime import datetime


class ReportAgent:
    """
    Agent responsible for generating compliance reports
    from the results produced by other agents.
    """

    def generate_report(
        self,
        transaction,
        violations,
        risk_score,
        risk_level,
        risk_factors=None
    ):
        if risk_factors is None:
            risk_factors = []

        if risk_level == "HIGH":
            recommendation = (
                "Escalate transaction for manual compliance review."
            )
        elif risk_level == "MEDIUM":
            recommendation = (
                "Continue enhanced monitoring of this transaction."
            )
        else:
            recommendation = (
                "Transaction appears compliant. Continue normal monitoring."
            )

        return {
            "report_id": f"COMP-{transaction.transaction_id}",
            "transaction_id": transaction.transaction_id,
            "customer_name": transaction.customer_name,
            "amount": transaction.amount,
            "country": transaction.country,
            "transaction_type": transaction.transaction_type,
            "risk_score": risk_score,
            "risk_level": risk_level,
            "risk_factors": risk_factors,
            "regulatory_violations": violations,
            "recommendation": recommendation,
            "generated_at": datetime.now().isoformat()
        }