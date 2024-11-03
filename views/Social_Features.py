import streamlit as st

# Initialize session state for user profiles and community features
if "users" not in st.session_state:
    st.session_state.users = {}
if "activity_feed" not in st.session_state:
    st.session_state.activity_feed = []
if "recipes" not in st.session_state:
    st.session_state.recipes = []

# Sidebar for navigation
st.sidebar.title("Navigation")
page = st.sidebar.selectbox("Choose a section:", ["User Profile", "Activity Feed", "Challenges", "Recipe Sharing"])

# 1. User Profile
if page == "User Profile":
    st.title("User Profile")
    username = st.text_input("Enter your username")
    if st.button("Create/Update Profile"):
        if username:
            st.session_state.users[username] = {"workouts": [], "achievements": []}
            st.success(f"Profile for {username} created/updated!")
        else:
            st.error("Please enter a username.")

# 2. Activity Feed
elif page == "Activity Feed":
    st.title("Activity Feed")
    username = st.text_input("Enter your username to post an update")
    activity_update = st.text_area("Share your workout or meal update")
    if st.button("Post Update"):
        if username in st.session_state.users and activity_update:
            st.session_state.activity_feed.append({"user": username, "update": activity_update})
            st.success("Update posted!")
        else:
            st.error("Please enter a valid username and an update.")

    # Display activity feed
    st.subheader("Updates:")
    for activity in st.session_state.activity_feed:
        st.write(f"{activity['user']}: {activity['update']}")

# 3. Challenges
elif page == "Challenges":
    st.title("Challenges")
    st.write("Join our monthly fitness challenges!")
    st.subheader("Current Challenges:")
    st.write("- 30-Day Plank Challenge")
    st.write("- 10,000 Steps a Day Challenge")
    st.write("- Weekly Yoga Challenge")

# 4. Recipe Sharing
elif page == "Recipe Sharing":
    st.title("Recipe Sharing")
    recipe_name = st.text_input("Recipe Name")
    recipe_details = st.text_area("Recipe Details")
    if st.button("Share Recipe"):
        if recipe_name and recipe_details:
            st.session_state.recipes.append({"name": recipe_name, "details": recipe_details})
            st.success("Recipe shared!")
        else:
            st.error("Please fill in both fields.")

    # Display shared recipes
    st.subheader("Shared Recipes:")
    for recipe in st.session_state.recipes:
        st.write(f"**{recipe['name']}**: {recipe['details']}")
