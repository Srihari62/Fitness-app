import streamlit as st
from datetime import datetime, timedelta

# Initialize session state for menstrual cycle tracking
if "cycle_data" not in st.session_state:
    st.session_state.cycle_data = []

# 1. Menstrual Cycle Tracker
st.title("Menstrual Cycle Tracker")
st.subheader("Track Your Menstrual Cycle")

# Input for cycle start date and length
start_date = st.date_input("Start Date of Last Period", datetime.today() - timedelta(days=28))
cycle_length = st.number_input("Cycle Length (in days)", min_value=21, max_value=35, value=28)
symptoms = st.text_area("Symptoms (e.g., cramps, headaches)")
mood = st.selectbox("Mood", ["Happy", "Sad", "Irritable", "Anxious", "Neutral"])

if st.button("Save Cycle Data"):
    cycle_entry = {
        "start_date": start_date,
        "cycle_length": cycle_length,
        "symptoms": symptoms,
        "mood": mood,
        "next_period": start_date + timedelta(days=cycle_length)
    }
    st.session_state.cycle_data.append(cycle_entry)
    st.success("Cycle data saved!")

# 2. Cycle Summary
st.subheader("Cycle Summary")

if st.session_state.cycle_data:
    st.write("Previous Cycle Entries:")
    for entry in st.session_state.cycle_data:
        st.write(f"**Start Date:** {entry['start_date']}")
        st.write(f"**Cycle Length:** {entry['cycle_length']} days")
        st.write(f"**Next Expected Period:** {entry['next_period']}")
        st.write(f"**Symptoms:** {entry['symptoms']}")
        st.write(f"**Mood:** {entry['mood']}")
        st.write("---")
else:
    st.write("No cycle data available. Please add your cycle data.")

# 3. Dietary Recommendations
st.subheader("Dietary Recommendations for Menstrual Health")

phases = {
    "Menstrual Phase": {
        "duration": "Days 1-5",
        "foods": [
            "Leafy greens", 
            "Bananas", 
            "Dark chocolate", 
            "Nuts", 
            "Whole grains", 
            "Quinoa", 
            "Lentils", 
            "Pumpkin seeds", 
            "Fish (like salmon)", 
            "Chickpeas"
        ],
        "tips": "Focus on iron-rich foods to replenish what you lose. Stay hydrated and opt for light meals.",
        "explanation": "During menstruation, the body loses blood, leading to a drop in iron levels. Consuming iron-rich foods can help combat fatigue and maintain energy levels. Foods high in magnesium can also help reduce cramps.",
        "youtube_links": [
            "https://www.youtube.com/watch?v=E-8gvJlkY8c",
            "https://www.youtube.com/@theyogainstituteofficial"
        ]
    },
    "Follicular Phase": {
        "duration": "Days 6-14",
        "foods": [
            "Lean proteins", 
            "Fruits", 
            "Vegetables", 
            "Eggs", 
            "Seeds", 
            "Whole grains", 
            "Greek yogurt", 
            "Fish (like cod or tuna)", 
            "Berries", 
            "Avocados"
        ],
        "tips": "Increase protein intake and healthy fats to support muscle growth and energy levels. Focus on antioxidants from fruits and vegetables.",
        "explanation": "In this phase, estrogen levels rise, enhancing energy and mood. Eating nutrient-dense foods helps support your body during this revitalizing phase.",
        "youtube_links": [
            "https://www.youtube.com/watch?v=E-8gvJlkY8c",
            "https://www.youtube.com/@theyogainstituteofficial"
        ]
    },
    "Ovulation Phase": {
        "duration": "Days 15-17",
        "foods": [
            "Berries", 
            "Avocados", 
            "Cruciferous vegetables", 
            "Fish (like mackerel)", 
            "Legumes", 
            "Citrus fruits", 
            "Nuts", 
            "Sweet potatoes", 
            "Chia seeds", 
            "Pomegranate"
        ],
        "tips": "Focus on antioxidant-rich foods to support hormonal balance and boost mood. Healthy fats are important for hormone production.",
        "explanation": "Ovulation is when the body is at its peak fertility and energy. Consuming foods rich in vitamins and minerals can enhance overall well-being and mood.",
        "youtube_links": [
          "https://www.youtube.com/watch?v=E-8gvJlkY8c",
          "https://www.youtube.com/@theyogainstituteofficial"
        ]
    },
    "Luteal Phase": {
        "duration": "Days 18-28",
        "foods": [
            "Complex carbohydrates", 
            "Magnesium-rich foods", 
            "Fermented foods", 
            "Oily fish", 
            "Dark leafy greens", 
            "Chickpeas", 
            "Brown rice", 
            "Sweet potatoes", 
            "Nuts", 
            "Dark chocolate"
        ],
        "tips": "Manage cravings with balanced meals and ensure sufficient magnesium to reduce PMS symptoms. Incorporate fiber to help with digestion.",
        "explanation": "This phase often comes with PMS symptoms. Focus on balancing blood sugar and incorporating foods that soothe cramps and help stabilize mood.",
        "youtube_links": [
            "https://www.youtube.com/watch?v=E-8gvJlkY8c",
            "https://www.youtube.com/@theyogainstituteofficial"
        ]
    }
}

for phase, details in phases.items():
    with st.expander(phase, expanded=False):
        st.write(f"**Duration:** {details['duration']}")
        st.write("**Recommended Foods:**")
        for food in details['foods']:
            st.write(f"- {food}")
        st.write(f"**Tips:** {details['tips']}")
        st.write(f"**Explanation:** {details['explanation']}")
        st.write("**YouTube Links:**")
        for link in details['youtube_links']:
            st.write(f"- [Watch Here]({link})")
        st.write("---")



# Footer
st.write(f"Total Entries: {len(st.session_state.cycle_data)}")
