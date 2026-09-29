# Logistics Strategic Planning and Data Exploration

## Week 1 Internship Project

This project demonstrates the strategic planning and data exploration phase of a logistics data analysis project. The goal is to understand delivery performance, transportation cost, delays, order volume, and resource utilization using Python.

## Objectives
- Define a practical logistics scenario.
- Explore logistics order and delivery data.
- Calculate important KPIs.
- Identify delivery delays and high-cost areas.
- Use Python and pandas for data analysis.
- Generate simple visualizations to support strategic decisions.

## Key KPIs
1. On-Time Delivery Rate
2. Average Delivery Time
3. Average Transportation Cost
4. Total Orders
5. Total Logistics Cost
6. Average Distance
7. Delay Rate

## Project Structure

```text
Logistics_Strategic_Planning/
│
├── data/
│   └── logistics_data.csv
│
├── outputs/
│   └── (generated charts and KPI summary)
│
├── logistics_analysis.py
├── strategic_planning.md
├── requirements.txt
├── .gitignore
└── README.md
```

## Technologies
- Python
- Pandas
- Matplotlib

## How to Run

### 1. Install Python
Make sure Python is installed and available in the terminal.

### 2. Install libraries
```bash
pip install -r requirements.txt
```

### 3. Run the project
```bash
python logistics_analysis.py
```

If `python` is not recognized on Windows, try:
```bash
py logistics_analysis.py
```

The program reads the CSV file, calculates KPIs, prints the results, and saves charts in the `outputs` folder.

## Expected Outcome
The analysis helps identify delivery delays, cost patterns, and operational areas that may require better route planning, resource allocation, or monitoring.

## Author
Vijay Vasudev
