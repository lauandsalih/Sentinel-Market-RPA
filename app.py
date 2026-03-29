import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Sentinel Market Intelligence", layout="wide")
st.title("🛰️ Sentinel: Comparative Performance Analytics")

try:
    df = pd.read_csv("warehouse_data.csv")
    df['Timestamp'] = pd.to_datetime(df['Timestamp'])
    df = df.sort_values('Timestamp')

    # --- KPI METRICS (The "Change" Visualizer) ---
    st.subheader("Current Market Pulse")
    cols = st.columns(5)
    
    unique_teams = df['Metric_Name'].unique()[:5]
    
    for i, team in enumerate(unique_teams):
        team_data = df[df['Metric_Name'] == team]
        if len(team_data) >= 2:
            current_val = team_data.iloc[-1]['Value']
            previous_val = team_data.iloc[-2]['Value']
            delta = current_val - previous_val
            # --- NONLINEAR ALERT LOGIC ---
            # If the change is more than 20% of the value, highlight it
            is_volatile = abs(delta) > (previous_val * 0.2)
            label_suffix = " ⚠️ VOLATILE" if is_volatile else ""
            
            cols[i].metric(
                label=f"{team.replace('Wins_', '').replace('_', ' ')}{label_suffix}", 
                value=f"{current_val:.1f}", 
                delta=f"{delta:.1f}"
            ) # <--- Check this one!
    # --- THE TREND CHART ---
    fig = px.line(df, x="Timestamp", y="Value", color="Metric_Name",
                  title="Performance Trends (Last 5 Days)",
                  template="plotly_dark", markers=True)
    
    st.plotly_chart(fig, use_container_width=True)

except Exception as e:
    st.info("Run the 'bootstrap_data.py' script to see the magic!")