# Flight Search and Analytics System 

## Overview
The **Flight Search and Analytics System** is a user-friendly dashboard that allows users to search for flights between different cities while providing insightful analytics. The platform helps users find available flights, view key details such as departure and arrival times, and analyze airline-wise average flight durations.

---

## 📷 Dashboard Preview

![Screenshot (10)](https://github.com/user-attachments/assets/36441887-fd88-4c45-bc6f-39754a013a01)

![Screenshot (11)](https://github.com/user-attachments/assets/a430dd5f-0657-48ee-95e1-972dbcee59e5)

![Screenshot (12)](https://github.com/user-attachments/assets/2997be31-140e-4c1c-9138-21546d776c4b)

![Screenshot (13)](https://github.com/user-attachments/assets/a980684f-ba15-45ff-a1fc-5a6dea268e2e)

---

## Features
**Flight Search:** Enter source and destination cities to view available flights with details like airline, flight number, departure time, arrival time, duration, and price.

**Real-time Data Display:** Flights are shown in a structured table for easy comparison.

**Accurate Time Formatting:** Departure and arrival times are displayed in an intuitive **AM/PM** format.

**Average Flight Duration Analysis:** Displays **airline-wise average flight durations**, formatted to two decimal places with 'h' appended.

**Error Handling:** Prevents searching for flights between the same city, displaying a **"No flights available"** message when applicable.

**Interactive UI:** Built using **Streamlit**, offering a responsive and user-friendly interface.

---

## Technologies Used
- **Python** – Backend logic and data processing
- **MySQL** – Database management for flight records
- **Streamlit** – Web application framework for interactive UI



**Run the Streamlit App**
``
streamlit run app.py
``


## Data Flow
1. User enters **source** and **destination** cities.
2. The system queries the **MySQL database** to fetch matching flights.
3. Flight details are displayed in a structured table.
4. The system computes **average flight duration per airline** and presents insights.

---

## Future Enhancements
- Add **filter options** (e.g., price range, airline selection).
- Include **real-time flight updates**.
- Implement **flight booking integration**.



