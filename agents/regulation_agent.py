class RegulationAgent:
    """
    Agent responsible for checking transactions
    against compliance regulations.
    """

    def __init__(self):
        self.restricted_countries = [
            "North Korea",
            "Iran"
        ]

    def check_regulations(self, transaction):
        violations = []

        # High-value transaction rule
        if transaction.amount > 100000:
            violations.append(
                "High-value transaction requires additional compliance review."
            )

        # Restricted country rule
        if transaction.country in self.restricted_countries:
            violations.append(
                "Transaction involves a restricted country."
            )

        # International transaction rule
        if transaction.transaction_type.lower() == "international":
            if transaction.amount > 50000:
                violations.append(
                    "Large international transaction requires enhanced monitoring."
                )

        return violations

    def get_all_regulations(self):
        return {
            "high_value_threshold": 100000,
            "restricted_countries": self.restricted_countries,
            "international_monitoring_threshold": 50000
        }