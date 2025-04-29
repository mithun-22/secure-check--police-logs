
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import sqlite3

# Load data
@st.cache_data
def load_data():
    return pd.read_csv("traffic.csv")

df = load_data()

# Sidebar menu
menu = ["Home", "View Data", "Statistics", "Visualization", "SQL Queries"]
choice = st.sidebar.selectbox("Navigation", menu)

# Home
if choice == "Home":
    st.title("🚓 Police Traffic Stops App")
    st.markdown("Welcome to the Police Traffic Stop Dashboard. Navigate using the sidebar.")

# View Data
elif choice == "View Data":
    st.title("🔍 View Data")
    st.write(df)
    st.download_button("Download CSV", df.to_csv(index=False), "traffic.csv")

# Statistics
elif choice == "Statistics":
    st.title("📊 Basic Statistics")
    st.write(df.describe(include='all'))
    st.write("Null values per column:")
    st.write(df.isnull().sum())

# Visualization
elif choice == "Visualization":
    st.title("📈 Data Visualizations")
    numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns.tolist()
    if numeric_cols:
        col = st.selectbox("Choose a numeric column to visualize", numeric_cols)
        fig, ax = plt.subplots()
        sns.histplot(df[col], kde=True, ax=ax)
        st.pyplot(fig)
    else:
        st.warning("No numeric columns available for visualization.")

# SQL Queries
elif choice == "SQL Queries":
    st.title("🧮 SQL Queries")
    conn = sqlite3.connect(":memory:")
    df.to_sql("traffic", conn, index=False)

    queries = {
        "1. First 5 rows": "SELECT * FROM traffic LIMIT 5",
        "2. Total number of stops": "SELECT COUNT(*) AS total_stops FROM traffic",
        "3. Unique violations": "SELECT DISTINCT violation FROM traffic",
        "4. Stops by violation": "SELECT violation, COUNT(*) AS count FROM traffic GROUP BY violation ORDER BY count DESC",
        "5. Stops by gender": "SELECT driver_gender, COUNT(*) AS count FROM traffic GROUP BY driver_gender",
        "6. Search conducted rate": "SELECT search_conducted, COUNT(*) AS count FROM traffic GROUP BY search_conducted",
        "7. Most common stop time": "SELECT stop_time, COUNT(*) AS count FROM traffic GROUP BY stop_time ORDER BY count DESC LIMIT 10",
        "8. Average stop duration": "SELECT AVG(stop_duration) AS avg_duration FROM traffic",
        "9. Most frequent stop duration": "SELECT stop_duration, COUNT(*) FROM traffic GROUP BY stop_duration ORDER BY COUNT(*) DESC LIMIT 1",
        "10. Violations by gender": "SELECT driver_gender, violation, COUNT(*) AS count FROM traffic GROUP BY driver_gender, violation ORDER BY count DESC",
        "11. Search rate by gender": "SELECT driver_gender, AVG(CASE WHEN search_conducted = 'True' THEN 1 ELSE 0 END) AS search_rate FROM traffic GROUP BY driver_gender",
        "12. Stops per day": "SELECT stop_date, COUNT(*) AS count FROM traffic GROUP BY stop_date ORDER BY stop_date",
        "13. Most stopped drivers by age (if age column exists)": "SELECT driver_age, COUNT(*) AS count FROM traffic GROUP BY driver_age ORDER BY count DESC LIMIT 10",
        "14. Percentage of searches": "SELECT (SUM(CASE WHEN search_conducted = 'True' THEN 1 ELSE 0 END)*100.0/COUNT(*)) AS search_percentage FROM traffic",
        "15. Violations and stop duration": "SELECT violation, stop_duration, COUNT(*) AS count FROM traffic GROUP BY violation, stop_duration ORDER BY count DESC",
        "16. Time of day distribution (hourly if available)": "SELECT SUBSTR(stop_time, 1, 2) AS hour, COUNT(*) AS count FROM traffic GROUP BY hour ORDER BY hour",
        "17. Gender and search conducted": "SELECT driver_gender, search_conducted, COUNT(*) FROM traffic GROUP BY driver_gender, search_conducted",
        "18. Top 5 common violation & gender pairs": "SELECT violation, driver_gender, COUNT(*) AS count FROM traffic GROUP BY violation, driver_gender ORDER BY count DESC LIMIT 5",
        "19. Total searches per violation": "SELECT violation, SUM(CASE WHEN search_conducted = 'True' THEN 1 ELSE 0 END) AS searches FROM traffic GROUP BY violation ORDER BY searches DESC",
        "20. Longest stop durations per violation": "SELECT violation, MAX(stop_duration) AS max_duration FROM traffic GROUP BY violation",
        "21. Total stops by stop duration": "SELECT stop_duration, COUNT(*) AS count FROM traffic GROUP BY stop_duration ORDER BY count DESC",
        "22. Daily stops trend": "SELECT stop_date, COUNT(*) FROM traffic GROUP BY stop_date ORDER BY stop_date"
    }

    query_choice = st.selectbox("Choose a query", list(queries.keys()))
    query = queries[query_choice]
    result = pd.read_sql_query(query, conn)
    st.dataframe(result)
    conn.close()
