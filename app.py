from fastapi import FastAPI
from pydantic import BaseModel

from agents.regulation_agent import RegulationAgent
from agents.transaction_agent import TransactionAgent
from agents.risk_agent import RiskAgent
from agents.report_agent import ReportAgent
from agents.audit_agent import AuditAgent
from agents.communication_agent import CommunicationAgent


app = FastAPI(
    title="Compliance Monitoring System - Agentic AI",
    description="Multi-agent AI system for compliance monitoring, risk analysis and reporting.",
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


class Communication(BaseModel):
    message: str


# -----------------------------
# Initialize Agents
# -----------------------------

regulation_agent = RegulationAgent()
transaction_agent = TransactionAgent()
risk_agent = RiskAgent()
report_agent = ReportAgent()
audit_agent = AuditAgent()
communication_agent = CommunicationAgent()


# -----------------------------
# Home
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
            "Report Agent",
            "Audit Agent",
            "Communication Agent"
        ]
    }


# -----------------------------
# Health Check
# -----------------------------

@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "Compliance Monitoring System"
    }


# -----------------------------
# Transaction Analysis
# -----------------------------

@app.post("/analyze")
def analyze_transaction(transaction: Transaction):

    # Agent 1: Regulation Analysis
    violations = regulation_agent.check_regulations(transaction)

    # Agent 2: Transaction Analysis
    transaction_result = transaction_agent.analyze_transaction(
        transaction
    )

    risk_score = transaction_result["risk_score"]
    risk_factors = transaction_result["risk_factors"]

    # Agent 3: Risk Classification
    risk_level = risk_agent.classify_risk(risk_score)

    recommendation = risk_agent.recommend_action(
        risk_level
    )

    # Agent 4: Report Generation
    report = report_agent.generate_report(
        transaction=transaction,
        violations=violations,
        risk_score=risk_score,
        risk_level=risk_level,
        risk_factors=risk_factors
    )

    report["recommendation"] = recommendation

    # Agent 5: Audit
    audit_entry = audit_agent.record_decision(
        transaction_id=transaction.transaction_id,
        risk_score=risk_score,
        risk_level=risk_level,
        decision=recommendation
    )

    return {
        "success": True,
        "workflow": [
            "Regulation Agent",
            "Transaction Agent",
            "Risk Agent",
            "Report Agent",
            "Audit Agent"
        ],
        "report": report,
        "audit": audit_entry
    }


# -----------------------------
# Communication Analysis
# -----------------------------

@app.post("/scan-communication")
def scan_communication(communication: Communication):

    result = communication_agent.scan_message(
        communication.message
    )

    return {
        "success": True,
        "agent": "Communication Agent",
        "analysis": result
    }


# -----------------------------
# Regulations
# -----------------------------

@app.get("/regulations")
def get_regulations():

    return {
        "success": True,
        "regulations": regulation_agent.get_all_regulations()
    }


# -----------------------------
# Audit Logs
# -----------------------------

@app.get("/audit-logs")
def get_audit_logs():

    return {
        "success": True,
        "total_logs": audit_agent.get_audit_count(),
        "logs": audit_agent.get_audit_logs()
    }