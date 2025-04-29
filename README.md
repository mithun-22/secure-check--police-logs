# secure-check--police-logs

# 🚓 Secure-Check — Police Logs Dashboard

This project provides an interactive dashboard to explore and analyze police traffic stop data. Using the power of **Pandas**, **SQL**, and **Streamlit**, the app lets users view raw data, generate descriptive statistics, run custom SQL queries, and visualize key insights—all from an intuitive web interface.

---

## 📌 Features

### 🔍 View Data
- Explore the full dataset in a searchable, scrollable table.
- Download the dataset as a CSV for offline analysis.

### 📊 Statistics
- Get summary statistics of all numerical and categorical fields.
- See missing values and understand the distribution of your data at a glance.

### 📈 Visualization
- Generate histograms with KDE (Kernel Density Estimation) for any numeric column.
- Instantly visualize traffic stop patterns and trends.

### 🧮 SQL Queries
- Run **22 built-in SQL queries** on the dataset using an in-memory SQLite engine.
- Queries cover common insights like stop counts by gender, violation types, search rates, time-based patterns, and more.

---

##TOOLS USED :

- **Streamlit** – For building the interactive web dashboard.
- **Pandas** – For data manipulation and preprocessing.
- **SQLite (via Pandas/SQLAlchemy)** – To enable flexible querying using SQL.
- **Seaborn & Matplotlib** – For creating clean and informative plots.


