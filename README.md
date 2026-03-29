# 🛰️ Sentinel: Enterprise RPA & Market Intelligence Pipeline

**Sentinel** is a modular Robotic Process Automation (RPA) and Data Visualization framework. It demonstrates an end-to-end pipeline: from automated web extraction to internal system integration and real-time anomaly detection.

## Key Features
* **Resilient Extraction:** Uses Playwright to navigate complex web environments with custom headers and cookie-consent handling.
* **Data Integrity Gate:** Implemented validation logic to prevent "dirty data" from entering internal systems.
* **Volatility Detection:** A custom analytics dashboard that identifies and flags non-linear market trends (Exponentials, Sine waves, and Spikes).
* **Cross-App Integration:** Automatically transfers captured metrics into a simulated ERP/Internal Portal.

##  Tech Stack
* **Engine:** Python 3.12, Playwright (RPA)
* **Analytics:** Pandas, NumPy (Data Processing)
* **Frontend:** Streamlit, Plotly (Visualization)
* **Infrastructure:** Git, GitHub Actions (CI/CD Ready)

##  Sample Visualization
The dashboard tracks multiple concurrent data streams, utilizing **Delta Metrics** and **⚠️ VOLATILE** flags to alert analysts of sudden market shifts.

##  Installation & Setup
1. Clone the repo: `git clone <your-repo-url>`
2. Setup environment: `source venv/bin/activate`
3. Install dependencies: `pip install -r requirements.txt`
4. Run the simulation: `python3 bootstrap_data.py`
5. Launch Dashboard: `streamlit run app.py`