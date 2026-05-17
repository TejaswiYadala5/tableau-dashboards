import pandas as pd
import numpy as np

YEARS = list(range(2015, 2025))

# Global card payment volumes (trillions USD) - inspired by Nilson Report & McKinsey Global Payments
TOTAL_VOLUME = [12.5, 13.8, 15.4, 17.5, 19.8, 19.2, 22.5, 26.4, 29.3, 33.1]
CREDIT_VOL   = [5.2,  5.7,  6.3,  7.1,  7.9,  7.5,  8.8, 10.1, 11.1, 12.4]
DEBIT_VOL    = [4.8,  5.3,  5.9,  6.7,  7.6,  7.4,  8.6,  9.8, 10.7, 11.9]
DIGITAL_VOL  = [1.2,  1.6,  2.1,  2.6,  3.2,  3.4,  4.2,  5.4,  6.4,  7.5]
OTHER_VOL    = [1.3,  1.2,  1.1,  1.1,  1.1,  0.9,  0.9,  1.1,  1.1,  1.3]

# Contactless payment adoption %
CONTACTLESS  = [5, 8, 12, 18, 25, 40, 52, 61, 68, 74]

# E-commerce share of total payments %
ECOMMERCE    = [14, 15, 17, 19, 22, 30, 35, 33, 34, 36]

# Cross-border payment volume (trillions)
CROSS_BORDER = [1.8, 2.0, 2.3, 2.7, 3.0, 2.4, 3.0, 3.8, 4.4, 5.1]

# Fraud rate in basis points (cents per $100)
FRAUD_RATE   = [8.5, 8.8, 9.2, 8.9, 8.6, 9.1, 8.4, 7.9, 7.5, 7.2]

# Transaction counts (billions)
TXN_COUNT    = [165, 185, 207, 235, 263, 255, 304, 363, 407, 462]

# Regional breakdown 2024 (%)
REGIONS = {
    "North America": {"share": 38, "growth": 8.2, "digital_pct": 72, "contactless": 68},
    "Europe":        {"share": 22, "growth": 7.5, "digital_pct": 65, "contactless": 78},
    "Asia Pacific":  {"share": 28, "growth": 14.1,"digital_pct": 82, "contactless": 81},
    "Latin America": {"share": 7,  "growth": 11.3,"digital_pct": 48, "contactless": 42},
    "MEA":           {"share": 5,  "growth": 12.8,"digital_pct": 44, "contactless": 51},
}

# Payment network market share 2024 (%)
NETWORKS = {"Visa": 38, "Mastercard": 24, "UnionPay": 27, "Amex": 5, "Others": 6}

# Merchant category breakdown (% of spend)
MERCHANT_CATS = {
    "Retail": 28, "Food & Dining": 18, "Travel": 14, "E-commerce": 16,
    "Healthcare": 9, "Entertainment": 7, "Utilities": 5, "Other": 3,
}

def get_volume_df():
    rows = []
    for i, yr in enumerate(YEARS):
        rows += [
            {"Year": yr, "Type": "Credit Cards",    "Volume": CREDIT_VOL[i]},
            {"Year": yr, "Type": "Debit Cards",     "Volume": DEBIT_VOL[i]},
            {"Year": yr, "Type": "Digital Wallets", "Volume": DIGITAL_VOL[i]},
            {"Year": yr, "Type": "Other",            "Volume": OTHER_VOL[i]},
        ]
    return pd.DataFrame(rows)

def get_trends_df():
    return pd.DataFrame({
        "Year": YEARS,
        "Total Volume (T$)": TOTAL_VOLUME,
        "Contactless (%)": CONTACTLESS,
        "E-commerce (%)": ECOMMERCE,
        "Cross-border (T$)": CROSS_BORDER,
        "Fraud Rate (bps)": FRAUD_RATE,
        "Transactions (B)": TXN_COUNT,
    })

def get_regional_df():
    rows = []
    for region, vals in REGIONS.items():
        rows.append({
            "Region": region,
            "Market Share (%)": vals["share"],
            "YoY Growth (%)": vals["growth"],
            "Digital Adoption (%)": vals["digital_pct"],
            "Contactless (%)": vals["contactless"],
            "Volume (T$)": round(TOTAL_VOLUME[-1] * vals["share"] / 100, 2),
        })
    return pd.DataFrame(rows)

def get_network_df():
    return pd.DataFrame([
        {"Network": k, "Share (%)": v} for k, v in NETWORKS.items()
    ])

def get_merchant_df():
    return pd.DataFrame([
        {"Category": k, "Spend Share (%)": v} for k, v in MERCHANT_CATS.items()
    ])
