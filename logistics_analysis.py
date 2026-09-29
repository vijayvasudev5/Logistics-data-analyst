import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "data" / "logistics_data.csv"
OUTPUT_DIR = BASE_DIR / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

# Load data
df = pd.read_csv(DATA_FILE)

# Convert dates
df["Order_Date"] = pd.to_datetime(df["Order_Date"])
df["Delivery_Date"] = pd.to_datetime(df["Delivery_Date"])
df["Promised_Date"] = pd.to_datetime(df["Promised_Date"])

# Calculate delivery time and delay
df["Delivery_Days"] = (df["Delivery_Date"] - df["Order_Date"]).dt.days
df["Delayed"] = df["Delivery_Date"] > df["Promised_Date"]

# KPI calculations
total_orders = len(df)
on_time_rate = (~df["Delayed"]).mean() * 100
delay_rate = df["Delayed"].mean() * 100
avg_delivery_days = df["Delivery_Days"].mean()
avg_cost = df["Transportation_Cost"].mean()
total_cost = df["Transportation_Cost"].sum()
avg_distance = df["Distance_KM"].mean()

print("\n===== LOGISTICS KPI SUMMARY =====")
print(f"Total Orders              : {total_orders}")
print(f"On-Time Delivery Rate     : {on_time_rate:.2f}%")
print(f"Delay Rate                : {delay_rate:.2f}%")
print(f"Average Delivery Time     : {avg_delivery_days:.2f} days")
print(f"Average Transportation Cost: ₹{avg_cost:.2f}")
print(f"Total Transportation Cost : ₹{total_cost:.2f}")
print(f"Average Distance          : {avg_distance:.2f} km")

# Route analysis
route_summary = df.groupby("Route").agg(
    Orders=("Order_ID", "count"),
    Avg_Cost=("Transportation_Cost", "mean"),
    Avg_Distance=("Distance_KM", "mean"),
    Delay_Rate=("Delayed", "mean")
).reset_index()

route_summary["Delay_Rate"] *= 100

print("\n===== ROUTE ANALYSIS =====")
print(route_summary.to_string(index=False))

# Save KPI summary
kpi = pd.DataFrame({
    "KPI": [
        "Total Orders", "On-Time Delivery Rate", "Delay Rate",
        "Average Delivery Time (days)", "Average Transportation Cost",
        "Total Transportation Cost", "Average Distance (km)"
    ],
    "Value": [
        total_orders, f"{on_time_rate:.2f}%", f"{delay_rate:.2f}%",
        f"{avg_delivery_days:.2f}", f"₹{avg_cost:.2f}",
        f"₹{total_cost:.2f}", f"{avg_distance:.2f}"
    ]
})
kpi.to_csv(OUTPUT_DIR / "kpi_summary.csv", index=False)

# Chart 1: Orders by route
df["Route"].value_counts().plot(kind="bar")
plt.title("Number of Orders by Route")
plt.xlabel("Route")
plt.ylabel("Orders")
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "orders_by_route.png")
plt.close()

# Chart 2: Transportation cost by route
df.groupby("Route")["Transportation_Cost"].mean().plot(kind="bar")
plt.title("Average Transportation Cost by Route")
plt.xlabel("Route")
plt.ylabel("Average Cost (₹)")
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "cost_by_route.png")
plt.close()

# Chart 3: Delay rate by route
route_summary.set_index("Route")["Delay_Rate"].plot(kind="bar")
plt.title("Delay Rate by Route")
plt.xlabel("Route")
plt.ylabel("Delay Rate (%)")
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "delay_rate_by_route.png")
plt.close()

print("\nAnalysis completed successfully.")
print(f"Charts and KPI summary saved in: {OUTPUT_DIR}")
