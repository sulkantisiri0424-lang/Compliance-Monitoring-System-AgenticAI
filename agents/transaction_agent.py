class TransactionAgent:
    """
    Agent responsible for analyzing transaction
    characteristics and calculating a risk score.
    """

    def analyze_transaction(self, transaction):
        risk_score = 0
        risk_factors = []

        # High-value transaction
        if transaction.amount > 100000:
            risk_score += 40
            risk_factors.append(
                "High transaction amount"
            )

        # Very high-value transaction
        if transaction.amount > 500000:
            risk_score += 30
            risk_factors.append(
                "Very high transaction amount"
            )

        # International transaction
        if transaction.transaction_type.lower() == "international":
            risk_score += 20
            risk_factors.append(
                "International transaction"
            )

        # Restricted country
        restricted_countries = [
            "North Korea",
            "Iran"
        ]

        if transaction.country in restricted_countries:
            risk_score += 30
            risk_factors.append(
                "Restricted country"
            )

        # Keep score between 0 and 100
        risk_score = min(risk_score, 100)

        return {
            "risk_score": risk_score,
            "risk_factors": risk_factors
        }