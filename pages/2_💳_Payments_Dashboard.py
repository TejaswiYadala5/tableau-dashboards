import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import pandas as pd
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from data.payments_data import (
    get_volume_df, get_trends_df, get_regional_df,
    get_network_df, get_merchant_df, YEARS
)

st.set_page_config(page_title="Payments Industry Dashboard", page_icon="💳", layout="wide")

VISA_BLUE = "#1A1F71"
VISA_GOLD = "#F7B600"
PAY_PAL   = [VISA_BLUE, VISA_GOLD, "#10b981", "#ef4444", "#8b5cf6", "#06b6d4", "#f97316"]
T = dict(paper_bgcolor="#ffffff", plot_bgcolor="#f8f9ff",
         font=dict(color="#1e293b", family="Arial", size=11),
         margin=dict(l=40, r=20, t=36, b=30))

st.markdown(f"""
<style>
  .kpi {{ background:#fff; border-radius:10px; padding:14px 18px;
          border-left:4px solid {VISA_BLUE}; box-shadow:0 1px 6px rgba(0,0,0,0.06); }}
  .kpi.gold  {{ border-left-color:{VISA_GOLD}; }}
  .kpi.green {{ border-left-color:#10b981; }}
  .kpi.red   {{ border-left-color:#ef4444; }}
  .kpi-val {{ font-size:22pt; font-weight:800; color:{VISA_BLUE}; }}
  .kpi-lbl {{ font-size:9pt; color:#64748b; text-transform:uppercase; letter-spacing:.5px; }}
  .kpi-sub {{ font-size:9pt; color:#94a3b8; }}
  .section {{ font-size:14pt; font-weight:700; color:{VISA_BLUE}; margin:8px 0 4px; }}
</style>
""", unsafe_allow_html=True)

# ── Sidebar ─────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("### 💳 Payments Filters")
    year_range = st.slider("Year Range", 2015, 2024, (2015, 2024))
    show_types = st.multiselect("Payment Types",
                                ["Credit Cards","Debit Cards","Digital Wallets","Other"],
                                default=["Credit Cards","Debit Cards","Digital Wallets","Other"])
    st.markdown("---")
    st.caption("Data: McKinsey Global Payments, Nilson Report, Fed Reserve (public summaries)")

yr_min, yr_max = year_range
df_trends = get_trends_df()
df_vol    = get_volume_df()
df_region = get_regional_df()
df_net    = get_network_df()
df_merch  = get_merchant_df()

df_trends = df_trends[df_trends["Year"].between(yr_min, yr_max)]
df_vol    = df_vol[df_vol["Year"].between(yr_min, yr_max) & df_vol["Type"].isin(show_types)]

# ── Header ─────────────────────────────────────────────────────────────────
st.markdown(f"## 💳 Global Payments Industry Dashboard")
st.caption(f"Payments analytics · {yr_min}–{yr_max} · Aligned with Visa BI reporting standards")
st.markdown("---")

# ── KPI Row ────────────────────────────────────────────────────────────────
latest = df_trends[df_trends["Year"] == yr_max].iloc[0]
prev   = df_trends[df_trends["Year"] == yr_max - 1].iloc[0]
vol_chg = (latest["Total Volume (T$)"] - prev["Total Volume (T$)"]) / prev["Total Volume (T$)"] * 100

c1,c2,c3,c4,c5 = st.columns(5)
with c1:
    st.markdown(f'<div class="kpi"><div class="kpi-lbl">Total Payment Volume</div>'
                f'<div class="kpi-val">${latest["Total Volume (T$)"]:.1f}T</div>'
                f'<div class="kpi-sub">▲ {vol_chg:.1f}% YoY</div></div>', unsafe_allow_html=True)
with c2:
    st.markdown(f'<div class="kpi gold"><div class="kpi-lbl">Transactions</div>'
                f'<div class="kpi-val">{latest["Transactions (B)"]:.0f}B</div>'
                f'<div class="kpi-sub">Global card txns</div></div>', unsafe_allow_html=True)
with c3:
    st.markdown(f'<div class="kpi green"><div class="kpi-lbl">Contactless Share</div>'
                f'<div class="kpi-val">{latest["Contactless (%)"]:.0f}%</div>'
                f'<div class="kpi-sub">of all transactions</div></div>', unsafe_allow_html=True)
with c4:
    st.markdown(f'<div class="kpi gold"><div class="kpi-lbl">E-commerce Share</div>'
                f'<div class="kpi-val">{latest["E-commerce (%)"]:.0f}%</div>'
                f'<div class="kpi-sub">of total spend</div></div>', unsafe_allow_html=True)
with c5:
    st.markdown(f'<div class="kpi green"><div class="kpi-lbl">Fraud Rate</div>'
                f'<div class="kpi-val">{latest["Fraud Rate (bps)"]:.1f} bps</div>'
                f'<div class="kpi-sub">↓ from {prev["Fraud Rate (bps)"]:.1f} bps</div></div>', unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ── Row 1: Payment Volume Stacked + Trends ──────────────────────────────────
col_a, col_b = st.columns([1.5, 1])

with col_a:
    fig1 = px.bar(df_vol, x="Year", y="Volume", color="Type",
                  title="Global Payment Volume by Type (Trillion USD)",
                  color_discrete_sequence=PAY_PAL, barmode="stack")
    fig1.update_layout(**T)
    fig1.update_xaxes(tickvals=list(range(yr_min, yr_max+1)), showgrid=False)
    fig1.update_yaxes(showgrid=True, gridcolor="#e2e8f0", title="Volume ($T)")
    st.plotly_chart(fig1, use_container_width=True)

with col_b:
    fig2 = make_subplots(rows=2, cols=1, shared_xaxes=True, vertical_spacing=0.12,
                         subplot_titles=("Contactless Adoption (%)", "E-commerce Share (%)"))
    fig2.add_trace(go.Scatter(x=df_trends["Year"], y=df_trends["Contactless (%)"],
                               fill="tozeroy", line=dict(color=VISA_BLUE, width=2),
                               fillcolor="rgba(26,31,113,0.12)", name="Contactless"), row=1, col=1)
    fig2.add_trace(go.Scatter(x=df_trends["Year"], y=df_trends["E-commerce (%)"],
                               fill="tozeroy", line=dict(color=VISA_GOLD, width=2),
                               fillcolor="rgba(247,182,0,0.15)", name="E-commerce"), row=2, col=1)
    fig2.update_layout(showlegend=False, title="Digital Payment Trends", **T)
    fig2.update_xaxes(tickvals=list(range(yr_min, yr_max+1)), showgrid=False)
    st.plotly_chart(fig2, use_container_width=True)

# ── Row 2: Regional + Fraud ──────────────────────────────────────────────────
col_c, col_d = st.columns(2)

with col_c:
    fig3 = px.bar(df_region.sort_values("Volume (T$)"), x="Volume (T$)", y="Region",
                  orientation="h", color="YoY Growth (%)",
                  color_continuous_scale=[[0,"#dbeafe"],[0.5,VISA_BLUE],[1,"#1e3a8a"]],
                  title="Payment Volume & Growth by Region (2024)",
                  text=df_region.sort_values("Volume (T$)")["Volume (T$)"].map("${:.1f}T".format))
    fig3.update_traces(textposition="outside")
    fig3.update_layout(**T, coloraxis_colorbar=dict(title="YoY Growth %"))
    st.plotly_chart(fig3, use_container_width=True)

with col_d:
    fig4 = go.Figure()
    fig4.add_trace(go.Scatter(
        x=df_trends["Year"], y=df_trends["Fraud Rate (bps)"],
        mode="lines+markers+text",
        line=dict(color="#ef4444", width=2.5),
        marker=dict(size=8, color="#ef4444"),
        text=[f"{v}" for v in df_trends["Fraud Rate (bps)"]],
        textposition="top center", textfont_size=9, name="Fraud Rate",
    ))
    fig4.add_hrect(y0=0, y1=7.5, fillcolor="rgba(16,185,129,0.07)", line_width=0,
                   annotation_text="Target Zone", annotation_position="bottom right")
    fig4.update_layout(title="Fraud Rate (basis points per $100)", yaxis_title="bps",
                       showlegend=False, **T)
    fig4.update_xaxes(tickvals=list(range(yr_min, yr_max+1)), showgrid=False)
    st.plotly_chart(fig4, use_container_width=True)

# ── Row 3: Network Share + Merchant Categories + Cross-border ───────────────
col_e, col_f, col_g = st.columns(3)

with col_e:
    fig5 = go.Figure(go.Pie(
        labels=df_net["Network"], values=df_net["Share (%)"],
        hole=0.5, marker_colors=[VISA_BLUE,"#eb5757","#f59e0b","#10b981","#94a3b8"],
        textinfo="label+percent",
    ))
    fig5.update_layout(title="Payment Network Market Share (2024)",
                       showlegend=False, **T)
    st.plotly_chart(fig5, use_container_width=True)

with col_f:
    fig6 = px.treemap(df_merch, path=["Category"], values="Spend Share (%)",
                      title="Spend by Merchant Category (2024)",
                      color="Spend Share (%)",
                      color_continuous_scale=[[0,"#dbeafe"],[1,VISA_BLUE]])
    fig6.update_layout(**T)
    st.plotly_chart(fig6, use_container_width=True)

with col_g:
    fig7 = go.Figure()
    fig7.add_trace(go.Scatter(
        x=df_trends["Year"], y=df_trends["Cross-border (T$)"],
        fill="tozeroy", line=dict(color=VISA_GOLD, width=2.5),
        fillcolor="rgba(247,182,0,0.15)", name="Cross-border",
        mode="lines+markers",
        text=[f"${v}T" for v in df_trends["Cross-border (T$)"]],
        textposition="top center", textfont_size=8,
    ))
    fig7.update_layout(title="Cross-Border Payment Volume ($T)",
                       yaxis_title="$T", showlegend=False, **T)
    fig7.update_xaxes(tickvals=list(range(yr_min, yr_max+1)), showgrid=False)
    st.plotly_chart(fig7, use_container_width=True)

# ── Regional Digital Adoption Table ─────────────────────────────────────────
st.markdown("---")
st.markdown('<div class="section">Regional Digital Adoption Summary</div>', unsafe_allow_html=True)
disp = df_region[["Region","Market Share (%)","YoY Growth (%)","Digital Adoption (%)","Contactless (%)","Volume (T$)"]].copy()
disp["Volume (T$)"] = disp["Volume (T$)"].map("${:.2f}T".format)
disp["Market Share (%)"] = disp["Market Share (%)"].map("{:.0f}%".format)
disp["YoY Growth (%)"] = disp["YoY Growth (%)"].map("{:.1f}%".format)
disp["Digital Adoption (%)"] = disp["Digital Adoption (%)"].map("{:.0f}%".format)
disp["Contactless (%)"] = disp["Contactless (%)"].map("{:.0f}%".format)
st.dataframe(disp, use_container_width=True, hide_index=True)

st.markdown("---")
st.caption("Sources: McKinsey Global Payments Report, Nilson Report, Federal Reserve Payments Study, BIS Statistics (public summaries) · Built by Tejaswi Yadala")
