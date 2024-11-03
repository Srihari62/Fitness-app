import streamlit as st 

# Page setup
st.set_page_config(page_title="Personal Fitness App", page_icon=":muscle:")

# Navigation setup
pages = {
    "Client Details":"views/Client_form.py", 
    "Nutrition & Meal Planning": "views/Nutrition&MealPlanning.py",
    "Social Features": "views/Social_Features.py",
    "Workout Planning": "views/workout.py",
    "Menstrual Cycle": "views/menstrual_cycle.py",
    "Contact Us":"forms/contact.py"
}

# Sidebar navigation
st.sidebar.title("Explore")  # Add title to the sidebar
selected_page = st.sidebar.selectbox("Select a Page", options=list(pages.keys()))


# Load the selected page
if selected_page:
    exec(open(pages[selected_page]).read())  # Dynamically load the selected page
