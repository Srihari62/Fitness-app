import streamlit as st

# Mock functions to replace Langflow-based functionality for illustration
def ask_ai(profile, question):
    # Extract relevant information from the profile
    name = profile["general"]["name"]
    weight = profile["general"]["weight"]
    height = profile["general"]["height"]
    gender = profile["general"]["gender"]
    activity_level = profile["general"]["activity_level"]
    goals = profile["goals"]

    # Basic logic to provide a more useful response based on the question
    if "what should I eat" in question.lower() and "muscle gain" in question.lower():
        # Example advice for muscle gain
        response = (
            f"{name}, to support muscle gain, you should focus on high-protein foods. "
            f"Here are some recommendations:\n"
            f"- **Protein Sources:** Include chicken breast, lean beef, fish, eggs, dairy products, and legumes.\n"
            f"- **Carbohydrates:** Don't skip on complex carbs such as whole grains (brown rice, oats) and plenty of vegetables.\n"
            f"- **Healthy Fats:** Avocados, nuts, seeds, and olive oil are great sources of healthy fats.\n"
            f"- **Hydration:** Drink plenty of water throughout the day.\n"
            f"- **Meal Frequency:** Consider eating 5-6 smaller meals throughout the day to fuel your muscles consistently."
        )
        return response

    # Placeholder for other types of questions
    elif "how can I lose weight" in question.lower():
        response = (
            f"{name}, to lose weight, focus on a caloric deficit, combining regular exercise with a balanced diet. "
            f"Prioritize whole foods, limit processed sugars, and consider portion control."
        )
        return response

    return "I'm not sure how to answer that. Could you ask something else?"

def get_macros(general_info, goals):
    return {"calories": 2000, "protein": 150, "fat": 70, "carbs": 250}

def create_profile(profile_id):
    profile = {
        "general": {"name": "", "age": 0, "weight": 0.0, "height": 0.0, "gender": "", "activity_level": ""},
        "goals": [],
        "nutrition": {}
    }
    return profile_id, profile

def get_notes(profile_id):
    return []

def get_profile(profile_id):
    return {
        "general": {"name": "John", "age": 25, "weight": 70.0, "height": 175.0, "gender": "Male", "activity_level": "Moderately Active"},
        "goals": ["Muscle Gain"],
        "nutrition": {"calories": 2500, "protein": 180, "fat": 80, "carbs": 300}
    }

def update_personal_info(profile, section, **kwargs):
    profile[section].update(kwargs)
    return profile

def add_note(note_text, profile_id):
    return {"_id": len(st.session_state.notes) + 1, "text": note_text}

def delete_note(note_id):
    pass

st.title("Personal Fitness App")

def personal_data_form():
    with st.form("personal_data"):
        st.header("Personal Data")
        profile = st.session_state.profile

        name = st.text_input("Name", value=profile["general"]["name"])
        age = st.number_input("Age", min_value=1, max_value=120, step=1, value=profile["general"]["age"])
        weight = st.number_input("Weight (kg)", min_value=0.0, max_value=300.0, step=0.1, value=float(profile["general"]["weight"]))
        height = st.number_input("Height (cm)", min_value=0.0, max_value=250.0, step=0.1, value=float(profile["general"]["height"]))
        genders = ["Male", "Female", "Other"]
        gender = st.radio("Gender", genders, index=genders.index(profile["general"].get("gender", "Male")))
        activities = ["Sedentary", "Lightly Active", "Moderately Active", "Very Active", "Super Active"]
        activity_level = st.selectbox("Activity Level", activities, index=activities.index(profile["general"].get("activity_level", "Sedentary")))

        if st.form_submit_button("Save"):
            if all([name, age, weight, height, gender, activity_level]):
                with st.spinner("Saving information..."):
                    st.session_state.profile = update_personal_info(
                        profile, "general", name=name, age=age, weight=weight, height=height, gender=gender, activity_level=activity_level
                    )
                    st.success("Information saved.")
            else:
                st.warning("Please fill in all of the data!")


def macros():
    profile = st.session_state.profile
    st.header("Macros")
    if st.button("Generate Macros with AI"):
        result = get_macros(profile.get("general"), profile.get("goals"))
        profile["nutrition"] = result
        st.success("AI-generated macros")

    with st.form("nutrition_form"):
        calories = st.number_input("Calories", min_value=0, step=1, value=profile["nutrition"].get("calories", 0))
        protein = st.number_input("Protein", min_value=0, step=1, value=profile["nutrition"].get("protein", 0))
        fat = st.number_input("Fat", min_value=0, step=1, value=profile["nutrition"].get("fat", 0))
        carbs = st.number_input("Carbs", min_value=0, step=1, value=profile["nutrition"].get("carbs", 0))

        if st.form_submit_button("Save"):
            with st.spinner("Saving nutrition information..."):
                st.session_state.profile = update_personal_info(profile, "nutrition", calories=calories, protein=protein, fat=fat, carbs=carbs)
                st.success("Nutrition information saved")

def notes():
    st.subheader("Notes")
    for i, note in enumerate(st.session_state.notes):
        cols = st.columns([5, 1])
        with cols[0]:
            st.text(note.get("text"))
        with cols[1]:
            if st.button("Delete", key=i):
                delete_note(note.get("_id"))
                st.session_state.notes.pop(i)
                st.rerun()
    
    new_note = st.text_input("Add a new note")
    if st.button("Add Note"):
        if new_note:
            note = add_note(new_note, st.session_state.profile_id)
            st.session_state.notes.append(note)
            st.rerun()



def forms():
    if "profile" not in st.session_state:
        profile_id = 1
        profile = get_profile(profile_id)
        if not profile:
            profile_id, profile = create_profile(profile_id)

        st.session_state.profile = profile
        st.session_state.profile_id = profile_id

    if "notes" not in st.session_state:
        st.session_state.notes = get_notes(st.session_state.profile_id)

    personal_data_form()
    macros()
    notes()
    

if __name__ == "__main__":
    forms()
