import streamlit as st
import pandas as pd
from datetime import datetime

# Function to save appointment data
def save_appointment(data):
    # Here you can implement saving to a database or CSV file
    # For example, appending to a CSV file
    df = pd.DataFrame([data])
    df.to_csv('appointments.csv', mode='a', header=False, index=False)

# Streamlit app
st.title("Contact Us")

# Appointment form
with st.form(key='appointment_form'):
    st.header("Request an Appointment with a Nutritionist")

    name = st.text_input("Your Name", "")
    email = st.text_input("Your Email", "")
    appointment_date = st.date_input("Preferred Appointment Date", datetime.today())
    appointment_time = st.time_input("Preferred Appointment Time", datetime.now().time())

    submit_button = st.form_submit_button(label='Submit')

    if submit_button:
        if name and email:
            appointment_data = {
                'Name': name,
                'Email': email,
                'Date': appointment_date,
                'Time': appointment_time
            }
            save_appointment(appointment_data)
            st.success("Your appointment request has been submitted successfully!")
        else:
            st.error("Please fill in all fields.")

# Display previous appointments (optional)
if st.checkbox("Show Previous Appointments"):
    try:
        appointments = pd.read_csv('appointments.csv', names=['Name', 'Email', 'Date', 'Time'])
        st.dataframe(appointments)
    except FileNotFoundError:
        st.error("No previous appointments found.")
