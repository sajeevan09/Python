import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


st.title("Simple Sales Data Dashboard")

# Ask user to upload CSV file
uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

# Check if file was uploadded
if uploaded_file:
    # Read data from csv file using Panda
    df = pd.read_csv(uploaded_file)

    # Show the first few rows
    st.subheader("Data Preview")
    st.write(df.head())

    # Show summary stats
    st.subheader("Summary Statistics")
    st.write(df.describe())

    # Select column(with numeric values) to plot 
    numeric_columns = df.select_dtypes(include='number').columns.tolist()
    if numeric_columns:
        col = st.selectbox("Select a column to plot", numeric_columns)

        # Plot the graph
        st.subheader(f"{col} over time")
        fig, ax = plt.subplots()
        if "Date" in df.columns:
            df["Date"] = pd.to_datetime(df["Date"])
            ax.plot(df["Date"], df[col])
            ax.set_xlabel("Date")
        else:
            ax.plot(df[col])
            ax.set_xlabel("Index")
        ax.set_ylabel(col)
        ax.set_title(f"{col} Trend")
        st.pyplot(fig)
    else:
        st.warning("No numeric columns found to plot.")
else:
    st.info("Please upload a CSV file to see the dashboard.")
