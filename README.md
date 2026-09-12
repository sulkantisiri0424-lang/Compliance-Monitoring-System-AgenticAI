# 🤖 Compliance Monitoring System using Agentic AI

An Agentic AI-powered compliance monitoring system designed to analyze transactions, detect potential regulatory violations, assess risk, monitor communications, generate compliance reports, and maintain an audit trail.

## 🎯 Project Objective

The main objective of this project is to automate compliance monitoring using a multi-agent architecture.

The system uses specialized agents that independently perform different tasks and work together to produce a final compliance decision.

## 🤖 AI Agents

### 1. Regulation Agent
Checks transactions against predefined compliance regulations and identifies potential violations.

### 2. Transaction Monitoring Agent
Analyzes transaction amount, transaction type, and other transaction characteristics to calculate a risk score.

### 3. Risk Analysis Agent
Converts the calculated risk score into LOW, MEDIUM, or HIGH risk.

### 4. Communication Agent
Scans communication messages for potential compliance red flags.

### 5. Report Agent
Combines the results from different agents and generates a structured compliance report.

### 6. Audit Agent
Maintains an audit trail of compliance decisions for future review.

## 🔄 Agentic AI Workflow

```text
                    USER INPUT
                        │
                        ▼
                 ┌──────────────┐
                 │  FastAPI API │
                 └──────┬───────┘
                        │
              ┌─────────┴─────────┐
              ▼                   ▼
       Transaction Data     Communication
              │                   │
              ▼                   ▼
      Regulation Agent   Communication Agent
              │
              ▼
       Transaction Agent
              │
              ▼
          Risk Agent
              │
              ▼
         Report Agent
              │
              ▼
          Audit Agent
              │
              ▼
      COMPLIANCE DECISION