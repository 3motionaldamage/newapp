import streamlit
import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt

# Establish database connection
mydb = mysql.connector.connect(
    host="remote_host",
    user="username",
    password="password",
    database="database_name"
)

# Define function to retrieve data from MySQL server
def retrieve_data(start_date, end_date):
    # Query to retrieve data from database based on user input
    query = "SELECT * FROM table_name WHERE date BETWEEN '{}' AND '{}'".format(start_date, end_date)

    # Execute query and store results in a Pandas DataFrame
    df = pd.read_sql(query, con=mydb)

    return df

# Define function to plot comparison graph of two time periods
def plot_comparison_graph(df, start_date_1, end_date_1, start_date_2, end_date_2):
    # Create two subplots side by side
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 5))

    # Plot data for first time period
    df1 = df[(df['date'] >= start_date_1) & (df['date'] <= end_date_1)]
    ax1.plot(df1['date'], df1['data'], label='Time Period 1')

    # Plot data for second time period
    df2 = df[(df['date'] >= start_date_2) & (df['date'] <= end_date_2)]
    ax1.plot(df2['date'], df2['data'], label='Time Period 2')

    # Highlight major drops in data
    threshold = df['data'].quantile(0.10) # set threshold to 10th percentile of data
    ax2.axhline(y=threshold, linestyle='--', color='r')
    ax2.plot(df['date'], df['data'])
    ax2.fill_between(df['date'], threshold, df['data'], where=df['data'] <= threshold, color='red', alpha=0.5)

    # Set axis labels and legend
    ax1.set_xlabel('Date')
    ax1.set_ylabel('Data')
    ax1.legend()
    ax2.set_xlabel('Date')
    ax2.set_ylabel('Data')

    # Show plot
    plt.show()

# User input for date range
start_date_1 = '2022-01-01'
end_date_1 = '2022-01-31'
start_date_2 = '2022-02-01'
end_date_2 = '2022-02-28'

# Retrieve data from MySQL server
df = retrieve_data(start_date_1, end_date_2)

# Plot comparison graph of two time periods with major drops highlighted
plot_comparison_graph(df, start_date_1, end_date_1, start_date_2, end_date_2)
