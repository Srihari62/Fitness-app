import streamlit as st
from datetime import datetime, timedelta

# Initialize session state for user profiles, workouts, and exercises
if "users" not in st.session_state:
    st.session_state.users = {}
if "workouts" not in st.session_state:
    st.session_state.workouts = []
if "exercises" not in st.session_state:
    st.session_state.exercises = {
        "Strength": ["Squat", "Deadlift", "Bench Press", "Lunges"],
        "Cardio": ["Running", "Cycling", "Jump Rope", "Swimming"],
        "Flexibility": ["Yoga", "Pilates", "Stretching"]
    }

# Sidebar for navigation
st.sidebar.title("Navigation")
page = st.sidebar.selectbox("Choose a section:", ["User Profile", "Workout Logging", "Exercise Library", "Monthly Goal Setting", "Monthly Schedule"])

# 1. User Profile
if page == "User Profile":
    st.title("User Profile")
    username = st.text_input("Enter your username")
    if st.button("Create/Update Profile"):
        if username:
            if username not in st.session_state.users:
                st.session_state.users[username] = {"workouts": [], "goals": []}
            st.success(f"Profile for '{username}' created/updated!")
        else:
            st.error("Please enter a username.")

# 2. Workout Logging
elif page == "Workout Logging":
    st.title("Workout Logging")
    username = st.text_input("Enter your username to log workout")  # Prompt for username
    if username not in st.session_state.users:
        st.error("Please create a user profile first.")
    else:
        workout_name = st.selectbox("Select Workout Type", list(st.session_state.exercises.keys()))
        exercise = st.selectbox("Select Exercise", st.session_state.exercises[workout_name])
        sets = st.number_input("Sets", min_value=1, value=3)
        reps = st.number_input("Reps", min_value=1, value=10)
        weight = st.number_input("Weight (kg)", min_value=0.0, value=0.0, format="%.2f")
        
        if st.button("Log Workout"):
            workout_entry = {
                "user": username,
                "exercise": exercise,
                "sets": sets,
                "reps": reps,
                "weight": weight,
                "date": datetime.now().strftime("%Y-%m-%d")
            }
            st.session_state.workouts.append(workout_entry)
            st.session_state.users[username]["workouts"].append(workout_entry)
            st.success("Workout logged!")

        # Display logged workouts
        st.subheader("Logged Workouts:")
        if username in st.session_state.users:
            for workout in st.session_state.users[username]["workouts"]:
                st.write(f"{workout['user']} logged {workout['exercise']} on {workout['date']} - "
                         f"{workout['sets']} sets of {workout['reps']} reps at {workout['weight']} kg")

# 3. Exercise Library
elif page == "Exercise Library":
    st.title("Exercise Library")
    exercise_type = st.selectbox("Select Exercise Type", list(st.session_state.exercises.keys()))
    st.subheader(f"{exercise_type} Exercises")
    for exercise in st.session_state.exercises[exercise_type]:
        st.write(f"- {exercise}")

# 4. Monthly Goal Setting
elif page == "Monthly Goal Setting":
    st.title("Monthly Goal Setting")
    username = st.text_input("Enter your username to set goals")  # Prompt for username
    if username not in st.session_state.users:
        st.error("Please create a user profile first.")
    else:
        goal = st.text_input("Enter your monthly goal (e.g., 'Complete 10 workouts', 'Run 50 km')")
        if st.button("Save Goal"):
            if goal:
                st.session_state.users[username]["goals"].append(goal)
                st.success("Goal saved!")
            else:
                st.error("Please enter a goal.")

        # Display goals
        st.subheader("Your Monthly Goals:")
        if username in st.session_state.users and st.session_state.users[username]["goals"]:
            for goal in st.session_state.users[username]["goals"]:
                st.write(f"- {goal}")
        else:
            st.write("No goals set yet.")

# 5. Monthly Schedule
elif page == "Monthly Schedule":
    st.title("Monthly Workout Schedule")
    username = st.text_input("Enter your username to generate schedule")  # Prompt for username
    if username not in st.session_state.users:
        st.error("Please create a user profile first.")
    else:
        workout_frequency = st.number_input("Enter workout frequency (days per week):", min_value=1, max_value=7, value=3)
        
        # Generate a monthly schedule
        if st.button("Generate Schedule"):
            start_date = datetime.now()
            end_date = start_date + timedelta(days=30)
            current_date = start_date

            schedule = {}
            workout_count = 0
            
            while current_date < end_date:
                if current_date.weekday() < workout_frequency:  # Check if it's a workout day
                    if st.session_state.workouts:
                        workout = st.session_state.workouts[workout_count % len(st.session_state.workouts)]
                        schedule[current_date.strftime("%Y-%m-%d")] = workout
                        workout_count += 1
                current_date += timedelta(days=1)

            st.subheader("Your Monthly Schedule:")
            for date, workout in schedule.items():
                st.write(f"{date}: {workout['exercise']} - {workout['sets']} sets of {workout['reps']} reps at {workout['weight']} kg")
        else:
            st.write("Click 'Generate Schedule' to create your monthly workout plan.")

# Footer
st.sidebar.title("Profile Summary")
if 'users' in st.session_state:
    for user in st.session_state.users.keys():
        st.sidebar.write(f"**{user}**: {len(st.session_state.users[user]['workouts'])} workouts logged, "
                         f"{len(st.session_state.users[user]['goals'])} goals set.")
