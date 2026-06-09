# EDA_EV

## EV Market Analysis using Python

Analyzed **250,000+ electric vehicle registration records** from Washington State, USA to identify manufacturer dominance, model popularity, EV adoption trends, and the market's transition toward fully electric vehicles using Exploratory Data Analysis (EDA).

---

## Project Overview

The adoption of electric vehicles (EVs) has accelerated significantly due to technological advancements, government incentives, and increasing demand for sustainable transportation.

This project analyzes large-scale electric vehicle registration data from Washington State to understand market behavior, identify leading manufacturers and models, examine EV adoption trends over time, and evaluate whether the market is shifting toward fully electric vehicles.

---

## Problem Statement

**Electric Vehicle Market Analysis Based on Manufacturer and Model Trends in Washington State**

The objectives of this project are to:

* Identify leading EV manufacturers and popular vehicle models
* Analyze EV adoption trends over time
* Examine the shift from Plug-in Hybrid Electric Vehicles (PHEVs) to Battery Electric Vehicles (BEVs)
* Explore improvements in EV technology using electric range data
* Understand market concentration and consumer preferences

---

## Dataset

**Source:** U.S. Open Data – Electric Vehicle Population Data

**Dataset Size:** ~250,000 vehicle records

### Key Features Used

* Make
* Model
* Model Year
* Electric Vehicle Type (BEV / PHEV)
* Electric Range
* State

Each record represents a registered electric vehicle.

---

## Tools & Technologies

### Languages

* Python

### Libraries

* Pandas
* Matplotlib

### Data Processing

* Data Cleaning
* Missing Value Handling
* Exploratory Data Analysis (EDA)
* Trend Analysis
* Data Visualization

> SQL was intentionally not used in this project because spreadsheet-based aggregation and Python analysis were sufficient for the project's objectives.

---

## Project Structure

```text
EDA_EV/
│
├── data/
│   └── Electric_Vehicle_Population_Data.csv
│
├── visualizations/
│   ├── manufacturer_market_share.png
│   ├── bev_vs_phev_market_share.png
│   ├── manufacturer_year_heatmap.png
│   ├── electric_range_analysis.png
│   └── cafv_eligibility_distribution.png
│
├── EDA_EV.py
├── README.md
└── LICENSE
```

---

## Analysis Performed

### 1. Manufacturer Market Share

* Market concentration analysis
* Leading EV manufacturer identification

### 2. BEV vs PHEV Distribution

* Comparison of fully electric and plug-in hybrid vehicles
* Analysis of the shift toward fully electric mobility

### 3. EV Manufacturer Trends by Year

* Manufacturer registration patterns over time
* Growth analysis across major EV brands

### 4. Electric Range Analysis

* Top EV models by average electric range
* Evaluation of technological advancements in battery performance

### 5. CAFV Eligibility Analysis

* Distribution of Clean Alternative Fuel Vehicle (CAFV) eligible vehicles
* Assessment of government incentive participation

---

## Key Insights

* The EV market is highly concentrated, with a small number of manufacturers accounting for a significant share of total registrations.
* Battery Electric Vehicles (BEVs) represent the majority of EV registrations, indicating growing consumer preference for fully electric transportation.
* EV registrations have increased substantially over recent model years, reflecting rapid market growth and wider adoption.
* Modern EV models offer significantly improved electric driving range, demonstrating advancements in battery technology and efficiency.
* Government incentive programs continue to play an important role, with a substantial portion of registered EVs qualifying for CAFV benefits.

---

## Conclusion

This project demonstrates how large-scale vehicle registration data can be leveraged to understand market behavior, consumer preferences, and technological progress within the electric vehicle industry.

Through data cleaning, exploratory analysis, and visualization, the study provides insights into EV adoption patterns, manufacturer dominance, electric range improvements, and the ongoing transition toward fully electric transportation.

The findings indicate strong growth in EV adoption and suggest that Battery Electric Vehicles are becoming the dominant technology within the evolving automotive market.

---

## Requirements

```text
pandas
matplotlib
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## License

This project is licensed under the MIT License.
