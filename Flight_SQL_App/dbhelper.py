import mysql.connector
from datetime import datetime

class DB:
    def __init__(self):
        #connect to the database
        try:
            self.conn = mysql.connector.connect(
                host = '127.0.0.1',
                user = 'root',
                password = '12345',
                database = 'store'
            )
            self.mycursor = self.conn.cursor()
            print('Connection established')
        except:
            print('Connection error')

    def fetch_city_names(self):
        city = []

        self.mycursor.execute("""
        select distinct(Destination_City) from store.flight
        union
        select distinct(Source_City) from store.flight
        """)

        data = self.mycursor.fetchall()

        for item in data:
            city.append(item[0])

        return city
    
    def fetch_all_flights(self, source, destination):
    # Query to fetch all flights

        if source == destination:
            return "No flights available.", []
        
        self.mycursor.execute("""
        SELECT Flight_Number, Airline, Departure_Time, Arrival_Time, Duration, USD
        FROM flight
        WHERE Source_City = %s AND Destination_City = %s
        """, (source, destination))

        flight_data = self.mycursor.fetchall()

        formatted_data = []
        for flight in flight_data:
            flight_number, airline, departure, arrival, duration, usd = flight
            
            # Convert time format from HH:MM:SS to HH:MM AM/PM
            departure_time = datetime.strptime(str(departure), "%H:%M:%S").strftime("%I:%M %p")
            arrival_time = datetime.strptime(str(arrival), "%H:%M:%S").strftime("%I:%M %p")

            formatted_data.append((flight_number, airline, departure_time, arrival_time, duration, usd))

        # Query to fetch average duration per airline
        self.mycursor.execute("""
        SELECT Airline, concat(ROUND(AVG(Duration),1),"h") AS Avg_Duration
        FROM flight
        WHERE Source_City = %s AND Destination_City = %s
        GROUP BY Airline
        ORDER BY Avg_Duration DESC;
        """, (source, destination))

        avg_duration_data = self.mycursor.fetchall()

        return formatted_data, avg_duration_data

    
    def fetch_airline_frequency(self):

        airline = []
        frequency = []
        
        self.mycursor.execute("""
        select airline,count(*) from flight
        group by airline
        """)

        data = self.mycursor.fetchall()

        for item in data:
            airline.append(item[0])
            frequency.append(item[1])

        return airline,frequency
    
    def fetch_busy_airport(self):
        city = []
        frequency = []
        self.mycursor.execute("""
        select Source_City,count(*) from (select Source_City from flight
                union all
                select Destination_City from flight) t
        group by t.Source_City
        order by count(*) desc
        """)
         
        data = self.mycursor.fetchall()

        for item in data:
            city.append(item[0])
            frequency.append(item[1])

        return city,frequency
    
    def fetch_daily_frequency(self):
        date = []
        frequency = []
        self.mycursor.execute("""
        select Date_of_Journey,count(*) from flight
        group by Date_of_Journey
        """)
         
        data = self.mycursor.fetchall()

        for item in data:
            date.append(item[0])
            frequency.append(item[1])

        return date,frequency
         

         
