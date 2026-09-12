from datetime import datetime


class AuditAgent:
    """
    Agent responsible for maintaining an audit trail
    of compliance decisions.
    """

    def __init__(self):
        self.audit_logs = []

    def record_decision(
        self,
        transaction_id,
        risk_score,
        risk_level,
        decision
    ):
        audit_entry = {
            "transaction_id": transaction_id,
            "risk_score": risk_score,
            "risk_level": risk_level,
            "decision": decision,
            "timestamp": datetime.now().isoformat()
        }

        self.audit_logs.append(audit_entry)

        return audit_entry

    def get_audit_logs(self):
        return self.audit_logs

    def get_audit_count(self):
        return len(self.audit_logs)