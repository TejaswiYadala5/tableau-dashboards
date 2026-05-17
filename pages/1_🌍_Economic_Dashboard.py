import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import pandas as pd
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from data.economic_data import (
    get_gdp_growth_df, get_unemployment_df, get_inflation_df,
    get_gdp_size_df, get_latest_snapshot, COUNTRIES, YEARS
)

st.set_page_config(page_title="Global Economic Dashboard", page_icon="🌍", layout="wide")

PALETTE = px.colors.qualitative.Bold
T = dict(paper_bgcolor="#ffffff", plot_bgcolor="#f8faff",
         font=dict(color="#1e293b", family="Arial", size=11),
         margin=dict(l=40, r=20, t=36, b=30))

st.markdown("""
<style>
  .kpi { background:#fff; border-radius:10px; padding:14px 18px;
         border-left:4px solid #1A1F71; box-shadow:0 1px 6px rgba(0,0,0,0.06); }
  .kpi.green  { border-left-color:#10b981; }
  .kpi.red    { border-left-color:#ef4444; }
  .kpi.amber  { border-left-color:#f59e0b; }
  .kpi-val { font-size:22pt; font-weight:800; color:#1A1F71; }
  .kpi-lbl { font-size:9pt; color:#64748b; text-transform:uppercase; letter-spacing:.5px; }
  .kpi-sub { font-size:9pt; color:#94a3b8; }
</style>
""", unsafe_allow_html=True)

# ── Sidebar ─────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("### 🌍 Economic Filters")
    sel_countries = st.multiselect("Countries", COUNTRIES, default=COUNTRIES)
    year_range = st.slider("Year Range", min_value=2015, max_value=2024, value=(2015, 2024))
    st.markdown("---")
    st.caption("Data: World Bank, IMF (public)")

if not sel_countries:
    sel_countries = COUNTRIES

yr_min, yr_max = year_range

df_gdp   = get_gdp_growth_df()
df_unemp = get_unemployment_df()
df_inf   = get_inflation_df()
df_size  = get_gdp_size_df()
df_snap  = get_latest_snapshot()

df_gdp   = df_gdp[df_gdp["Country"].isin(sel_countries) & df_gdp["Year"].between(yr_min, yr_max)]
df_unemp = df_unemp[df_unemp["Country"].isin(sel_countries) & df_unemp["Year"].between(yr_min, yr_max)]
df_inf   = df_inf[df_inf["Country"].isin(sel_countries) & df_inf["Year"].between(yr_min, yr_max)]
df_size  = df_size[df_size["Country"].isin(sel_countries) & df_size["Year"].between(yr_min, yr_max)]
df_snap  = df_snap[df_snap["Country"].isin(sel_countries)]

# ── Header ────────────────────────────────────────────────────────────────────
st.markdown("## 🌍 Global Economic Intelligence Dashboard")
st.caption(f"Macroeconomic trends · {yr_min}–{yr_max} · {len(sel_countries)} countries selected")
st.markdown("---")

# ── KPI Row ───────────────────────────────────────────────────────────────────
avg_gdp   = df_snap["GDP Growth (%)"].mean()
avg_unemp = df_snap["Unemployment (%)"].mean()
avg_inf   = df_snap["Inflation (%)"].mean()
total_gdp = df_snap["GDP (T USD)"].sum()
best      = df_snap.loc[df_snap["GDP Growth (%)"].idxmax(), "Country"]

c1,c2,c3,c4,c5 = st.columns(5)
with c1:
    st.markdown(f'<div class="kpi green"><div class="kpi-lbl">Avg GDP Growth</div>'
                f'<div class="kpi-val">{avg_gdp:.1f}%</div><div class="kpi-sub">2024 est.</div></div>', unsafe_allow_html=True)
with c2:
    st.markdown(f'<div class="kpi"><div class="kpi-lbl">Combined GDP</div>'
                f'<div class="kpi-val">${total_gdp:.1f}T</div><div class="kpi-sub">USD 2024</div></div>', unsafe_allow_html=True)
with c3:
    color = "red" if avg_unemp > 6 else "amber" if avg_unemp > 4 else "green"
    st.markdown(f'<div class="kpi {color}"><div class="kpi-lbl">Avg Unemployment</div>'
                f'<div class="kpi-val">{avg_unemp:.1f}%</div><div class="kpi-sub">2024 est.</div></div>', unsafe_allow_html=True)
with c4:
    color = "red" if avg_inf > 5 else "amber" if avg_inf > 3 else "green"
    st.markdown(f'<div class="kpi {color}"><div class="kpi-lbl">Avg Inflation</div>'
                f'<div class="kpi-val">{avg_inf:.1f}%</div><div class="kpi-sub">2024 est.</div></div>', unsafe_allow_html=True)
with c5:
    st.markdown(f'<div class="kpi green"><div class="kpi-lbl">Top Growth 2024</div>'
                f'<div class="kpi-val">{best}</div>'
                f'<div class="kpi-sub">{df_snap.loc[df_snap["Country"]==best,"GDP Growth (%)"].values[0]:.1f}%</div></div>', unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ── Row 1: GDP Growth Line + Bubble ──────────────────────────────────────────
col_a, col_b = st.columns([1.6, 1])

with col_a:
    fig = px.line(df_gdp, x="Year", y="GDP Growth (%)", color="Country",
                  title="GDP Growth Rate by Country (%)",
                  color_discrete_sequence=PALETTE, markers=True)
    fig.add_hline(y=0, line_dash="dash", line_color="#ef4444", opacity=0.4)
    fig.update_layout(**T)
    fig.update_xaxes(tickvals=list(range(yr_min, yr_max+1)), showgrid=False)
    fig.update_yaxes(showgrid=True, gridcolor="#e2e8f0", zeroline=False)
    st.plotly_chart(fig, use_container_width=True)

with col_b:
    fig2 = px.scatter(df_snap, x="Unemployment (%)", y="GDP Growth (%)",
                      size="GDP (T USD)", color="Continent", text="Country",
                      title="GDP Growth vs Unemployment (2024)",
                      color_discrete_sequence=PALETTE, size_max=55)
    fig2.update_traces(textposition="top center", textfont_size=9)
    fig2.add_hline(y=0, line_dash="dot", line_color="#ef4444", opacity=0.3)
    fig2.update_layout(**T)
    st.plotly_chart(fig2, use_container_width=True)

# ── Row 2: Inflation Heatmap + Unemployment Bar ───────────────────────────────
col_c, col_d = st.columns(2)

with col_c:
    pivot = df_inf.pivot(index="Country", columns="Year", values="Inflation (%)")
    fig3 = go.Figure(go.Heatmap(
        z=pivot.values, x=[str(y) for y in pivot.columns],
        y=pivot.index.tolist(),
        colorscale=[[0,"#dbeafe"],[0.4,"#93c5fd"],[0.7,"#f59e0b"],[1,"#ef4444"]],
        text=[[f"{v:.1f}%" for v in row] for row in pivot.values],
        texttemplate="%{text}", colorbar=dict(title="Inflation %"),
        zmin=0, zmax=12,
    ))
    fig3.update_layout(title="Inflation Rate Heatmap (% YoY)", **T)
    st.plotly_chart(fig3, use_container_width=True)

with col_d:
    latest_unemp = df_unemp[df_unemp["Year"] == yr_max].sort_values("Unemployment (%)")
    colors = ["#10b981" if v < 4 else ("#f59e0b" if v < 7 else "#ef4444")
              for v in latest_unemp["Unemployment (%)"]]
    fig4 = go.Figure(go.Bar(
        x=latest_unemp["Unemployment (%)"], y=latest_unemp["Country"],
        orientation="h", marker_color=colors,
        text=[f"{v:.1f}%" for v in latest_unemp["Unemployment (%)"]],
        textposition="outside",
    ))
    fig4.update_layout(title=f"Unemployment Rate by Country ({yr_max})",
                       xaxis_title="Rate (%)", **T)
    st.plotly_chart(fig4, use_container_width=True)

# ── Row 3: GDP Size Area + Summary Table ────────────────────────────────────
col_e, col_f = st.columns([1.4, 1])

with col_e:
    fig5 = px.area(df_size, x="Year", y="GDP (T USD)", color="Country",
                   title="GDP Size Over Time (Trillion USD)",
                   color_discrete_sequence=PALETTE)
    fig5.update_layout(**T)
    fig5.update_xaxes(tickvals=list(range(yr_min, yr_max+1)), showgrid=False)
    st.plotly_chart(fig5, use_container_width=True)

with col_f:
    st.markdown("##### 2024 Country Snapshot")
    show = df_snap[["Country","GDP Growth (%)","Unemployment (%)","Inflation (%)","GDP (T USD)"]].copy()
    show = show.sort_values("GDP Growth (%)", ascending=False).reset_index(drop=True)
    show.columns = ["Country","GDP Growth","Unemp.","Inflation","GDP ($T)"]
    show["GDP Growth"] = show["GDP Growth"].map("{:.1f}%".format)
    show["Unemp."]    = show["Unemp."].map("{:.1f}%".format)
    show["Inflation"] = show["Inflation"].map("{:.1f}%".format)
    show["GDP ($T)"]  = show["GDP ($T)"].map("${:.1f}T".format)
    st.dataframe(show, use_container_width=True, hide_index=True)

st.markdown("---")
st.caption("Sources: World Bank Open Data, IMF World Economic Outlook (public datasets) · Built by Tejaswi Yadala")
