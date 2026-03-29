# 🛰️ Sentinel: Enterprise RPA & Predictive Market Intelligence

**Sentinel** is an end-to-end Robotic Process Automation (RPA) framework designed to bridge the gap between volatile external market data and internal corporate decision-making systems. 

## 🎯 Project Aim
The primary objective of Sentinel is to demonstrate a **High-Availability Data Pipeline**. In a global pharmaceutical environment like Orion, manual data entry is a bottleneck. This project aims to:
1.  **Automate Extraction:** Eliminate manual monitoring of external web-based metrics.
2.  **Ensure Data Integrity:** Implement a "Decision Gate" to validate data before it touches internal ERP systems.
3.  **Visualize Volatility:** Transform raw, noisy data into actionable insights through advanced trend analysis.

## 🏗️ Technical Architecture
The system is built on a three-tier architecture:
1.  **The Scout (Playwright):** A resilient RPA engine that navigates web DOMs, handles cookie consent, and extracts localized currency/metric data.
2.  **The Warehouse (CSV/Pandas):** A persistent, audit-ready data store that maintains a historical record of every automation run.
3.  **The Command Center (Streamlit/Plotly):** A high-level analytics dashboard for executive stakeholders.



## 📊 Key Results & Features
* **Non-Linear Trend Analysis:** The system successfully visualizes complex market patterns, including **Exponential Growth** (supply shocks), **Sine Waves** (seasonal demand), and **Stochastic Spikes** (market anomalies).
* **Automated Anomaly Detection:** Implemented "Smart Metrics" that automatically flag **⚠️ VOLATILE** data points if the percentage change exceeds a 20% threshold between runs.
* **Cross-Application Transfer:** Demonstrated the ability to move captured web data into a secondary "Internal Portal," simulating a real-world ERP integration.
* **Zero-Loss Logging:** Engineered a robust logging system using `fsync` to ensure a permanent audit trail even in the event of hardware or network failure.

## 🚦 How to Execute the Pipeline
1.  **Environment Setup:** `source venv/bin/activate && pip install -r requirements.txt`
2.  **Data Generation:** Run `python3 bootstrap_data.py` to populate the warehouse with 10 days of historical volatile data.
3.  **Real-Time Scrape:** Run `python3 bot.py` to perform a live extraction and internal system update.
4.  **Launch Analytics:** Run `streamlit run app.py` to view the Intelligence Dashboard.

---
*Developed as a Technical Portfolio for Orion Information Management.*
