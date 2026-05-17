import streamlit as st

st.set_page_config(page_title="Analytics Portfolio", page_icon="📊", layout="wide")

st.markdown("""
<style>
  .hero { text-align:center; padding:40px 20px 20px; }
  .hero h1 { font-size:36pt; font-weight:800; color:#1A1F71; margin-bottom:8px; }
  .hero p  { font-size:13pt; color:#555; max-width:700px; margin:0 auto; }
  .card {
    background:#fff; border-radius:12px; padding:28px 24px;
    box-shadow:0 2px 12px rgba(0,0,0,0.08); border-top:4px solid #1A1F71;
    text-align:center; height:100%;
  }
  .card.gold { border-top-color:#F7B600; }
  .card h3   { font-size:15pt; font-weight:700; color:#1A1F71; margin-bottom:10px; }
  .card p    { font-size:10pt; color:#555; line-height:1.6; }
  .badge {
    display:inline-block; background:#eef2ff; color:#1A1F71;
    border-radius:20px; padding:4px 12px; font-size:9pt;
    font-weight:600; margin:3px;
  }
  .tag { background:#fff8e1; color:#b45309; }
  .metric-row { display:flex; gap:16px; justify-content:center; flex-wrap:wrap; margin:24px 0; }
  .metric-box { background:#f8faff; border-radius:10px; padding:16px 24px; text-align:center;
                border:1px solid #e0e7ff; min-width:140px; }
  .metric-box .val { font-size:20pt; font-weight:800; color:#1A1F71; }
  .metric-box .lbl { font-size:9pt; color:#6b7280; margin-top:2px; }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
  <h1>📊 Analytics Portfolio</h1>
  <p>Business Intelligence dashboards built with Python, Plotly & Streamlit — showcasing data
  analytics expertise across global economics and the payments industry.</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="metric-row">
  <div class="metric-box"><div class="val">10</div><div class="lbl">Countries Tracked</div></div>
  <div class="metric-box"><div class="val">10</div><div class="lbl">Years of Data</div></div>
  <div class="metric-box"><div class="val">$33T</div><div class="lbl">Payment Volume</div></div>
  <div class="metric-box"><div class="val">2</div><div class="lbl">Live Dashboards</div></div>
  <div class="metric-box"><div class="val">462B</div><div class="lbl">Transactions</div></div>
</div>
""", unsafe_allow_html=True)

st.markdown("---")
col1, col2 = st.columns(2, gap="large")

with col1:
    st.markdown("""
    <div class="card">
      <h3>🌍 Global Economic Dashboard</h3>
      <p>Explores macroeconomic trends across 10 major economies (2015–2024). Covers GDP growth,
      unemployment, inflation, and economic size — styled for executive-level reporting.</p>
      <br/>
      <span class="badge">GDP Trends</span>
      <span class="badge">Unemployment</span>
      <span class="badge">Inflation</span>
      <span class="badge">Country Comparison</span>
      <span class="badge">Heatmap</span>
      <span class="badge">Bubble Chart</span>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card gold">
      <h3>💳 Payments Industry Dashboard</h3>
      <p>Deep-dive into global payments data (2015–2024): payment volumes, digital adoption,
      contactless growth, fraud trends, regional breakdown, and network market share —
      aligned with how Visa's BI team tracks industry KPIs.</p>
      <br/>
      <span class="badge tag">Payment Volumes</span>
      <span class="badge tag">Contactless</span>
      <span class="badge tag">Fraud Rate</span>
      <span class="badge tag">Regional Data</span>
      <span class="badge tag">Network Share</span>
      <span class="badge tag">E-commerce</span>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
st.markdown("👈 **Use the sidebar to navigate between dashboards.**", unsafe_allow_html=False)
st.markdown("---")
st.markdown(
    "<p style='text-align:center;color:#9ca3af;font-size:10pt;'>"
    "Built by <a href='https://www.linkedin.com/in/tejaswi-y-82068b205/' style='color:#1A1F71;'>Tejaswi Yadala</a> · "
    "<a href='https://github.com/TejaswiYadala5' style='color:#1A1F71;'>GitHub</a> · "
    "Data sourced from World Bank, IMF, McKinsey Global Payments, Nilson Report (public summaries)"
    "</p>",
    unsafe_allow_html=True,
)
