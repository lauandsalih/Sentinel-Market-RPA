# 🛰️ Sentinel: Enterprise RPA & Predictive Market Intelligence

**Sentinel** is an end-to-end Robotic Process Automation (RPA) and Data Visualization framework. It is designed to solve the critical business bottleneck of manual data synchronization between fragmented external markets and internal corporate ERP systems.

## 🎯 The Business Challenge: The "Manual Bottleneck"
In modern Information Management, relying on human operators to monitor, verify, and input market data creates three primary risks:
1.  **Latency:** Manual entry is slow, meaning decision-makers work with "stale" data.
2.  **Scalability:** As the number of monitored metrics grows, human labor costs scale linearly. 
3.  **Accuracy (The Fat Finger Risk):** Manual transcription leads to costly data-entry errors, especially with complex decimals and currency conversions.

**Sentinel eliminates this bottleneck by acting as a "Digital Bridge"—executing extraction, validation, and entry in seconds with 100% precision.**

## 🏗️ Technical Architecture
The system is built on a three-tier "Extraction-to-Insight" architecture:
1.  **The Scout (Playwright):** A resilient RPA engine that navigates web DOMs, handles regional GDPR overlays, and extracts localized metrics.
2.  **The Warehouse (CSV/Pandas):** An audit-ready data store that maintains a historical "Source of Truth" for every automation run.
3.  **The Command Center (Streamlit/Plotly):** An analytics dashboard for executive stakeholders to visualize volatility and trends.

## 📊 Key Results & Strategic Features
* **Automated Data Entry:** Demonstrated via a cross-application transfer where captured web metrics are automatically "typed" into a secondary internal portal, simulating a live ERP integration.
* **Non-Linear Trend Analysis:** The system visualizes complex market patterns, including **Exponential Growth** (demand shocks), **Sine Waves** (cyclical trends), and **Stochastic Spikes** (market anomalies).
* **Anomaly Detection:** Integrated "Smart Metrics" that flag **⚠️ VOLATILE** data points if the percentage change exceeds a 20% threshold, allowing analysts to focus only on high-risk shifts.
* **Zero-Loss Logging:** Engineered with `fsync` persistence to ensure a permanent audit trail for compliance and regulatory standards.

## 🚦 How to Execute the Pipeline
1.  **Environment Setup:** `source venv/bin/activate && pip install -r requirements.txt`
2.  **Generate History:** Run `python3 bootstrap_data.py` (Populates the warehouse with 10 days of volatile data).
3.  **Execute RPA Loop:** Run `python3 bot.py` (Performs live extraction and automated internal system update).
4.  **Launch Analytics:** Run `streamlit run app.py` (Launches the Intelligence Dashboard).

---
*Developed as a high-performance portfolio piece for Robotic Process Automation and Information Management roles.*
