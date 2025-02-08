import streamlit as st
import pandas as pd
from dbhelper import DB
import plotly.graph_objects as go
import plotly.express as px

db = DB()

st.sidebar.title('Flight Analytics')

user_option = st.sidebar.selectbox('Menu',['Select One','Check Flights','Analytics'])

if user_option == 'Check Flights':
    st.title('Check Flights')

    col1, col2 = st.columns(2)

    city = db.fetch_city_names()

    with col1:
        source = st.selectbox('Source_City',sorted(city))

    with col2:
        destination = st.selectbox('Destination_City',sorted(city))

    if st.button('Search'):
        flights, avg_duration = db.fetch_all_flights(source, destination)

        if flights == "No flights available.":
            st.warning("No flights available.")
        else:
            df = pd.DataFrame(flights, columns=["Flight_Number", "Airline", "Departure_Time", "Arrival_Time", "Duration", "USD"])
            st.dataframe(df)
            st.subheader("Average Flight Duration Per Airline")
            avg_df = pd.DataFrame(avg_duration, columns=["Airline", "Avg_Duration"])
            st.dataframe(avg_df)

elif user_option == 'Analytics':
    airline, frequency = db.fetch_airline_frequency()
    fig = go.Figure(
        go.Pie(
            labels = airline,
            values = frequency,
            hoverinfo = "label+percent",
            textinfo = "value"
        ) 
    )
    st.header("Pie chart")
    st.plotly_chart(fig)

    city, frequency = db.fetch_busy_airport()
    fig = go.Figure(
        go.Bar(
            x = city,
            y = frequency,
            text = frequency,
            textposition = 'auto'
        ) 
    )
    st.header("Bar chart")
    st.plotly_chart(fig)

    date, frequency = db.fetch_daily_frequency()
    fig = go.Figure(
        go.Scatter(
            x = city,
            y = frequency,
            mode='lines+markers',
            line=dict(color='blue', width=2),
            marker=dict(size=6, color='red')
        ) 
    )
    st.header("Line chart")
    st.plotly_chart(fig)
     
     
else:
    st.title('Flight Search and Analytics System')
    st.text('''Welcome to the Flight Search and Analytics System, a streamlined platform designed to
            help users find flights between cities while providing insightful analytics. This application
            allows users to search for flights based on source and destination cities, view detailed flight information,
            and analyze average flight durations per airline.''')
    st.text('''
            **Key Features**
                Search for Flights: Enter the source and destination to retrieve available flights with details such as airline, flight number, departure time, arrival time, duration, and price.
                Real-time Data Display: Flights are presented in a structured table format for easy comparison.
                Accurate Time Formatting: Departure and arrival times are displayed in an intuitive AM/PM format.
                Average Flight Duration Analysis: Get insights into airline-wise average flight durations, formatted to two decimal places with 'h' for better readability.
                Error Handling: Ensures users don't search for flights between the same cities, displaying a "No flights available" message when applicable.
                Interactive & User-Friendly: Built using Streamlit, making it easy to use with a clean and responsive interface.
            ''')

