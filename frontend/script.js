const API_URL = "http://127.0.0.1:8000";


document
    .getElementById("transactionForm")
    .addEventListener("submit", async function (event) {

        event.preventDefault();

        const resultDiv = document.getElementById("result");
        const loadingDiv = document.getElementById("loading");

        loadingDiv.innerHTML = "🤖 AI agents are analyzing the transaction...";

        resultDiv.innerHTML = "";

        const transaction = {

            transaction_id:
                document.getElementById("transaction_id").value,

            customer_name:
                document.getElementById("customer_name").value,

            amount:
                Number(document.getElementById("amount").value),

            country:
                document.getElementById("country").value,

            transaction_type:
                document.getElementById("transaction_type").value
        };


        try {

            const response = await fetch(
                `${API_URL}/analyze`,
                {
                    method: "POST",

                    headers: {
                        "Content-Type": "application/json"
                    },

                    body: JSON.stringify(transaction)
                }
            );


            if (!response.ok) {
                throw new Error("Backend request failed");
            }


            const data = await response.json();

            const report = data.report;

            let riskClass = "risk-low";

            if (report.risk_level === "HIGH") {
                riskClass = "risk-high";
            }
            else if (report.risk_level === "MEDIUM") {
                riskClass = "risk-medium";
            }


            let violationsHTML = "";

            if (report.regulatory_violations.length > 0) {

                violationsHTML = `
                    <h3>⚠️ Regulatory Violations</h3>
                    <ul>
                        ${report.regulatory_violations
                            .map(
                                violation =>
                                    `<li>${violation}</li>`
                            )
                            .join("")}
                    </ul>
                `;

            }
            else {

                violationsHTML = `
                    <p>✅ No regulatory violations detected.</p>
                `;

            }


            let factorsHTML = "";

            if (report.risk_factors.length > 0) {

                factorsHTML = `
                    <h3>Risk Factors</h3>
                    <ul>
                        ${report.risk_factors
                            .map(
                                factor =>
                                    `<li>${factor}</li>`
                            )
                            .join("")}
                    </ul>
                `;

            }


            resultDiv.innerHTML = `

                <div class="result-box">

                    <h3>📄 Compliance Report</h3>

                    <p>
                        <strong>Report ID:</strong>
                        ${report.report_id}
                    </p>

                    <p>
                        <strong>Transaction:</strong>
                        ${report.transaction_id}
                    </p>

                    <p>
                        <strong>Customer:</strong>
                        ${report.customer_name}
                    </p>

                    <p>
                        <strong>Amount:</strong>
                        ₹${report.amount.toLocaleString()}
                    </p>

                    <p>
                        <strong>Risk Score:</strong>
                        ${report.risk_score}/100
                    </p>

                    <p>
                        <strong>Risk Level:</strong>
                        <span class="${riskClass}">
                            ${report.risk_level}
                        </span>
                    </p>

                    ${factorsHTML}

                    ${violationsHTML}

                    <h3>💡 Recommendation</h3>

                    <p>
                        ${report.recommendation}
                    </p>

                </div>
            `;


            loadingDiv.innerHTML =
                "✅ Analysis completed successfully.";

        }

        catch (error) {

            loadingDiv.innerHTML =
                "❌ Unable to connect to the backend.";

            resultDiv.innerHTML = `
                <div class="result-box">
                    <p>
                        Please make sure the FastAPI server
                        is running on port 8000.
                    </p>
                </div>
            `;

            console.error(error);
        }

    });