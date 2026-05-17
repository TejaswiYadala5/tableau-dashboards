# 📊 Tableau-Style Analytics Dashboards

Two production-quality **Business Intelligence dashboards** built with Python, Streamlit, and Plotly — showcasing the kind of data analytics and visualization work done by BI teams at companies like Visa, AWS, and McKinsey.

## 🗂️ Dashboards

### 🌍 Global Economic Intelligence Dashboard
Tracks macroeconomic indicators across 10 major economies (2015–2024).

| Chart | Description |
|---|---|
| GDP Growth Line | Multi-country GDP growth trends |
| GDP vs Unemployment Bubble | Size = economic weight, color = continent |
| Inflation Heatmap | Country × Year matrix |
| Unemployment Bar | Latest year ranked comparison |
| GDP Size Area | Stacked economic output over time |
| Country Snapshot Table | All KPIs at a glance |

**Data:** World Bank Open Data, IMF World Economic Outlook (public)

---

### 💳 Global Payments Industry Dashboard
Deep-dive into the global payments ecosystem (2015–2024), aligned with how Visa's BI team tracks industry KPIs.

| Chart | Description |
|---|---|
| Payment Volume Stacked Bar | Credit / Debit / Digital / Other by year |
| Contactless & E-commerce Trends | Dual time-series |
| Regional Volume & Growth | Bar chart with YoY growth color |
| Fraud Rate Trend | Basis points with target zone |
| Network Market Share | Visa, Mastercard, UnionPay, Amex |
| Merchant Category Treemap | Spend breakdown by category |
| Cross-border Volume | Growth trend |
| Regional Adoption Table | Digital %, contactless %, volume |

**Data:** McKinsey Global Payments Report, Nilson Report, Federal Reserve Payments Study, BIS (public summaries)

---

## 🚀 Run Locally

```bash
git clone https://github.com/TejaswiYadala5/tableau-dashboards.git
cd tableau-dashboards
pip install -r requirements.txt
streamlit run 🏠_Home.py
```

Opens at `http://localhost:8501`

## 🛠️ Tech Stack

- **Python** — data generation and processing
- **Streamlit** — multi-page dashboard framework
- **Plotly** — interactive charts (bar, line, scatter, heatmap, treemap, pie)
- **Pandas / NumPy** — data transformation

## 📁 Structure

```
tableau-dashboards/
├── 🏠_Home.py                        # Landing page
├── pages/
│   ├── 1_🌍_Economic_Dashboard.py    # Global economic indicators
│   └── 2_💳_Payments_Dashboard.py    # Payments industry analytics
├── data/
│   ├── economic_data.py              # G20 economic data (2015–2024)
│   └── payments_data.py              # Global payments data (2015–2024)
├── requirements.txt
└── README.md
```

---

Built by [Tejaswi Yadala](https://www.linkedin.com/in/tejaswi-y-82068b205/) · [GitHub](https://github.com/TejaswiYadala5) · [SRE Dashboard](https://github.com/TejaswiYadala5/sre-dashboard)
