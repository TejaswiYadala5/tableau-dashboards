import pandas as pd
import numpy as np

YEARS = list(range(2015, 2025))
COUNTRIES = ["USA", "China", "Germany", "Japan", "UK", "India", "Brazil", "France", "Canada", "Australia"]

GDP_GROWTH = {
    "USA":       [3.1, 1.7, 2.3, 2.9, 2.3, -2.8, 5.9, 2.1, 2.5, 2.8],
    "China":     [7.0, 6.7, 6.9, 6.7, 6.0,  2.2, 8.1, 3.0, 5.2, 4.9],
    "Germany":   [1.5, 2.2, 2.6, 1.5, 0.6, -4.6, 2.6, 1.8,-0.3, 0.2],
    "Japan":     [1.6, 0.8, 1.7, 0.6,-0.4, -4.1, 2.1, 1.0, 1.9, 0.3],
    "UK":        [2.4, 1.8, 1.7, 1.3, 1.6,-11.0, 7.5, 4.1, 0.1, 0.4],
    "India":     [8.0, 8.3, 6.8, 6.5, 5.0, -5.8, 9.1, 7.2, 8.2, 7.8],
    "Brazil":    [-3.5,-3.3, 1.3, 1.8, 1.2, -3.3, 5.0, 2.9, 2.9, 3.2],
    "France":    [1.1, 1.1, 2.3, 1.8, 1.8, -7.9, 6.8, 2.5, 0.9, 1.1],
    "Canada":    [0.7, 1.4, 3.0, 2.0, 1.9, -5.1, 5.0, 3.4, 1.2, 1.5],
    "Australia": [2.5, 2.8, 2.2, 2.8, 1.9, -2.1, 4.9, 3.7, 2.0, 1.5],
}

UNEMPLOYMENT = {
    "USA":       [5.3, 4.9, 4.4, 3.9, 3.7, 8.1, 5.4, 3.6, 3.4, 3.7],
    "China":     [4.1, 4.0, 3.9, 4.0, 5.2, 5.6, 5.1, 5.5, 5.2, 5.0],
    "Germany":   [4.6, 4.2, 3.8, 3.4, 3.2, 4.2, 3.6, 3.0, 2.9, 3.4],
    "Japan":     [3.4, 3.1, 2.8, 2.4, 2.4, 2.8, 2.8, 2.6, 2.5, 2.5],
    "UK":        [5.4, 4.9, 4.4, 4.1, 3.8, 4.9, 4.5, 3.7, 4.2, 4.4],
    "India":     [5.5, 5.4, 5.3, 5.3, 5.4, 7.1, 6.1, 7.3, 7.2, 7.0],
    "Brazil":    [8.5,11.5,12.7,12.3,11.9,13.5,13.2, 9.3, 7.8, 6.9],
    "France":    [10.4,10.1,9.4, 9.0, 8.5,7.9, 8.1, 7.4, 7.3, 7.5],
    "Canada":    [6.9, 7.0, 6.4, 5.8, 5.7, 9.6, 7.5, 5.2, 5.4, 6.2],
    "Australia": [6.1, 5.7, 5.6, 5.3, 5.2, 6.5, 5.1, 3.5, 3.6, 4.0],
}

INFLATION = {
    "USA":       [0.1, 1.3, 2.1, 2.4, 1.8, 1.2, 4.7, 8.0, 4.1, 2.9],
    "China":     [1.4, 2.0, 1.6, 2.1, 2.9, 2.5, 0.9, 2.0, 0.2, 0.5],
    "Germany":   [0.1, 0.4, 1.7, 1.9, 1.4, 0.4, 3.2, 8.7, 5.9, 2.5],
    "Japan":     [0.8, -0.1,0.5, 1.0, 0.5, 0.0, -0.2,2.5, 3.3, 2.7],
    "UK":        [0.0, 0.7, 2.7, 2.5, 1.8, 0.9, 2.6, 9.1, 7.3, 2.5],
    "India":     [4.9, 4.5, 3.6, 3.4, 4.8, 6.2, 5.5, 6.7, 5.4, 4.5],
    "Brazil":    [9.0, 8.7, 3.4, 3.7, 3.7, 3.2, 8.3,11.9, 4.6, 4.2],
    "France":    [0.1, 0.3, 1.2, 2.1, 1.3, 0.5, 2.1, 5.9, 5.7, 2.3],
    "Canada":    [1.1, 1.4, 1.6, 2.3, 2.0, 0.7, 3.4, 6.8, 3.9, 2.5],
    "Australia": [1.5, 1.3, 2.0, 1.9, 1.6, 0.9, 2.8, 6.6, 5.6, 3.5],
}

GDP_TRILLION = {
    "USA":       [18.2,18.7,19.5,20.6,21.4,20.9,23.3,25.5,27.4,29.2],
    "China":     [11.1,11.2,12.3,13.9,14.3,14.7,17.7,17.9,17.7,18.5],
    "Germany":   [3.4, 3.5, 3.7, 4.0, 3.9, 3.8, 4.3, 4.1, 4.4, 4.5],
    "Japan":     [4.4, 4.9, 4.9, 5.0, 5.1, 5.0, 5.0, 4.2, 4.2, 4.1],
    "UK":        [2.9, 2.7, 2.7, 2.9, 2.8, 2.7, 3.1, 3.1, 3.1, 3.3],
    "India":     [2.1, 2.3, 2.7, 2.7, 2.9, 2.7, 3.2, 3.4, 3.6, 4.0],
    "Brazil":    [1.8, 1.8, 2.1, 1.9, 1.9, 1.4, 1.6, 1.9, 2.1, 2.3],
    "France":    [2.4, 2.5, 2.6, 2.8, 2.7, 2.6, 2.9, 2.8, 3.0, 3.1],
    "Canada":    [1.6, 1.5, 1.6, 1.7, 1.7, 1.6, 1.9, 2.1, 2.1, 2.2],
    "Australia": [1.3, 1.2, 1.3, 1.4, 1.4, 1.3, 1.6, 1.7, 1.7, 1.8],
}

CONTINENT = {
    "USA": "North America", "Canada": "North America", "Brazil": "South America",
    "UK": "Europe", "Germany": "Europe", "France": "Europe",
    "China": "Asia", "Japan": "Asia", "India": "Asia", "Australia": "Oceania",
}

def get_gdp_growth_df():
    rows = []
    for country, values in GDP_GROWTH.items():
        for year, val in zip(YEARS, values):
            rows.append({"Country": country, "Year": year, "GDP Growth (%)": val,
                         "Continent": CONTINENT[country]})
    return pd.DataFrame(rows)

def get_unemployment_df():
    rows = []
    for country, values in UNEMPLOYMENT.items():
        for year, val in zip(YEARS, values):
            rows.append({"Country": country, "Year": year, "Unemployment (%)": val})
    return pd.DataFrame(rows)

def get_inflation_df():
    rows = []
    for country, values in INFLATION.items():
        for year, val in zip(YEARS, values):
            rows.append({"Country": country, "Year": year, "Inflation (%)": val})
    return pd.DataFrame(rows)

def get_gdp_size_df():
    rows = []
    for country, values in GDP_TRILLION.items():
        for year, val in zip(YEARS, values):
            rows.append({"Country": country, "Year": year, "GDP (T USD)": val,
                         "Continent": CONTINENT[country]})
    return pd.DataFrame(rows)

def get_latest_snapshot():
    latest_year = max(YEARS)
    rows = []
    for country in COUNTRIES:
        rows.append({
            "Country": country,
            "Continent": CONTINENT[country],
            "GDP Growth (%)": GDP_GROWTH[country][-1],
            "Unemployment (%)": UNEMPLOYMENT[country][-1],
            "Inflation (%)": INFLATION[country][-1],
            "GDP (T USD)": GDP_TRILLION[country][-1],
        })
    return pd.DataFrame(rows)
