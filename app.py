from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime
from typing import List


app = FastAPI(
    title="Compliance Monitoring System - Agentic AI",
    description="Multi-agent AI system for compliance monitoring and risk analysis.",
    version="1.0.0"
)


# -----------------------------
# Data Models
# -----------------------------

class Transaction(BaseModel):
    transaction_id: str
    customer_name: str
    amount: float
    country: str
    transaction_type: str


# -----------------------------
# Agent 1: Regulation Agent
# -----------------------------

class RegulationAgent:

    def check_regulations(self, transaction):
        violations = []

        if transaction.amount > 100000:
            violations.append(
                "High-value transaction requires additional compliance review."
            )

        restricted_countries = ["North Korea", "Iran"]

        if transaction.country in restricted_countries:
            violations.append(
                "Transaction involves a restricted country."
            )

        return violations


# -----------------------------
# Agent 2: Transaction Monitoring Agent
# -----------------------------

class TransactionAgent:

    def analyze_transaction(self, transaction):
        risk_score = 0

        if transaction.amount > 100000:
            risk_score += 50

        if transaction.amount > 500000:
            risk_score += 30

        if transaction.transaction_type.lower() == "international":
            risk_score += 20

        return min(risk_score, 100)


# -----------------------------
# Agent 3: Risk Analysis Agent
# -----------------------------

class RiskAgent:

    def classify_risk(self, risk_score):

        if risk_score >= 70:
            return "HIGH"

        elif risk_score >= 40:
            return "MEDIUM"

        return "LOW"


# -----------------------------
# Agent 4: Report Agent
# -----------------------------

class ReportAgent:

    def generate_report(
        self,
        transaction,
        violations,
        risk_score,
        risk_level
    ):

        return {
            "transaction_id": transaction.transaction_id,
            "customer": transaction.customer_name,
            "amount": transaction.amount,
            "country": transaction.country,
            "risk_score": risk_score,
            "risk_level": risk_level,
            "violations": violations,
            "timestamp": datetime.now().isoformat(),
            "recommendation": (
                "Escalate for manual compliance review."
                if risk_level == "HIGH"
                else "Continue monitoring."
            )
        }


# -----------------------------
# Initialize Agents
# -----------------------------

regulation_agent = RegulationAgent()
transaction_agent = TransactionAgent()
risk_agent = RiskAgent()
report_agent = ReportAgent()


# -----------------------------
# API Routes
# -----------------------------

@app.get("/")
def home():

    return {
        "message": "Compliance Monitoring System using Agentic AI",
        "status": "running",
        "agents": [
            "Regulation Agent",
            "Transaction Monitoring Agent",
            "Risk Analysis Agent",
            "Report Agent"
        ]
    }


@app.get("/health")
def health_check():

    return {
        "status": "healthy",
        "service": "Compliance Monitoring System"
    }


@app.post("/analyze")
def analyze_transaction(transaction: Transaction):

    # Regulation Agent
    violations = regulation_agent.check_regulations(transaction)

    # Transaction Monitoring Agent
    risk_score = transaction_agent.analyze_transaction(transaction)

    # Risk Analysis Agent
    risk_level = risk_agent.classify_risk(risk_score)

    # Report Agent
    report = report_agent.generate_report(
        transaction,
        violations,
        risk_score,
        risk_level
    )

    return {
        "success": True,
        "agent_decision": report
    }