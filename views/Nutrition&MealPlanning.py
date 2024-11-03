import streamlit as st

# Title for the app
st.title("Nutrition and Meal Tracker")

# Define food categories, their respective foods, calorie information, and YouTube links
food_categories = {
    "Vegan": {
        "foods": [
            {"name": "Quinoa", "calories": 222, "benefits": "High in protein and fiber, gluten-free.",
             "recipe_link": "https://www.youtube.com/watch?v=vfUDxET4yVY"},
            {"name": "Chickpeas", "calories": 164, "benefits": "Rich in protein and fiber; great for salads.",
             "recipe_link": "https://www.youtube.com/shorts/L4OXzlw4mps"},
            {"name": "Lentils", "calories": 230, "benefits": "Excellent source of protein, fiber, and iron.",
             "recipe_link": "https://www.youtube.com/watch?v=UaEogCDFV7c"},
            {"name": "Tofu", "calories": 144, "benefits": "High in protein, low in calories; versatile for many dishes.",
             "recipe_link": "https://www.youtube.com/watch?v=-zkj_8bOd58"},
            {"name": "Nuts (Almonds, Walnuts)", "calories": 576, "benefits": "Healthy fats, protein, and omega-3s.",
             "recipe_link": "https://www.youtube.com/watch?v=xcz2LIvpMwI"},
            {"name": "Green Peas", "calories": 62, "benefits": "Good source of protein, vitamins A, C, K.",
             "recipe_link": "https://www.youtube.com/watch?v=6J7nK7ul6UM"},
            {"name": "Brown Rice", "calories": 215, "benefits": "Whole grain, good source of magnesium and fiber.",
             "recipe_link": "https://www.youtube.com/watch?v=EDkTRENbQxs"},
            {"name": "Hemp Seeds", "calories": 170, "benefits": "High in protein and omega-3 fatty acids.",
             "recipe_link": "https://www.youtube.com/watch?v=AGaXInOghq0"},
            {"name": "Avocado", "calories": 160, "benefits": "Healthy fats, great for heart health.",
             "recipe_link": "https://www.youtube.com/watch?v=FMGArdg4-pY"},
            {"name": "Sweet Potatoes", "calories": 86, "benefits": "Rich in vitamins A and C, and fiber.",
             "recipe_link": "https://www.youtube.com/shorts/j3fJBXxRvGI"}
        ]
    },
    "Vegetarian": {
        "foods": [
            {"name": "Greek Yogurt", "calories": 100, "benefits": "High in protein and probiotics.",
             "recipe_link": "https://www.youtube.com/watch?v=g6BHi9chkbk"},
            {"name": "Eggs", "calories": 68, "benefits": "Complete protein source, high in vitamins.",
             "recipe_link": "https://www.youtube.com/watch?v=ZSGCk7Q1JcA"},
            {"name": "Cottage Cheese", "calories": 206, "benefits": "Rich in protein and calcium.",
             "recipe_link": "https://www.youtube.com/watch?v=JslwCzHnA_8"},
            {"name": "Spinach", "calories": 23, "benefits": "High in iron, calcium, and antioxidants.",
             "recipe_link": "https://www.youtube.com/watch?v=FvM5mcBa5Zc"},
            {"name": "Mushrooms", "calories": 22, "benefits": "Low calorie, rich in B vitamins.",
             "recipe_link": "https://www.youtube.com/watch?v=d_Pc_buMnjE"},
            {"name": "Bell Peppers", "calories": 31, "benefits": "High in vitamin C and antioxidants.",
             "recipe_link": "https://www.youtube.com/watch?v=77JHtM_OjI4"},
            {"name": "Broccoli", "calories": 55, "benefits": "Rich in vitamins K and C, fiber.",
             "recipe_link": "https://www.youtube.com/watch?v=LDFbvgzaE04"},
            {"name": "Cauliflower", "calories": 25, "benefits": "Low-calorie, high in fiber and vitamin C.",
             "recipe_link": "https://www.youtube.com/watch?v=LDFbvgzaE04"},
            {"name": "Chia Seeds", "calories": 138, "benefits": "High in fiber and omega-3 fatty acids.",
             "recipe_link": "https://www.youtube.com/watch?v=LDFbvgzaE04"},
            {"name": "Oats", "calories": 389, "benefits": "Good source of fiber and complex carbohydrates.",
             "recipe_link": "https://www.youtube.com/watch?v=LDFbvgzaE04"}
        ]
    },
    "Low Carb High Protein": {
        "foods": [
            {"name": "Chicken Breast", "calories": 165, "benefits": "Lean protein, low in fat.",
             "recipe_link": "https://www.youtube.com/watch?v=jrDjMhQRwDM",
             "recipe_link": "https://www.youtube.com/watch?v=jrDjMhQRwDM"},
            {"name": "Egg Whites", "calories": 17, "benefits": "High protein, low in calories and fat.",
             "recipe_link": "https://www.youtube.com/watch?v=5bAa1CwK5Tc"},
            {"name": "Greek Yogurt", "calories": 100, "benefits": "High in protein, low in carbs.",
             "recipe_link": "https://www.youtube.com/watch?v=3gG7tKD_KPk"},
            {"name": "Protein Powder", "calories": 120, "benefits": "Quick protein source for smoothies or shakes.",
             "recipe_link": "https://www.youtube.com/watch?v=jrDjMhQRwDM"},
            {"name": "Turkey Breast", "calories": 135, "benefits": "Low fat, high protein.",
             "recipe_link": "https://www.youtube.com/watch?v=jrDjMhQRwDM"},
            {"name": "Pork Tenderloin", "calories": 143, "benefits": "Lean cut, great source of protein.",
             "recipe_link": "https://www.youtube.com/watch?v=jrDjMhQRwDM"},
            {"name": "Beef Jerky", "calories": 116, "benefits": "High in protein, convenient snack.",
             "recipe_link": "https://www.youtube.com/watch?v=jrDjMhQRwDM"},
            {"name": "Seitan", "calories": 120, "benefits": "High protein meat substitute.",
             "recipe_link": "https://www.youtube.com/watch?v=jrDjMhQRwDM"},
            {"name": "Cottage Cheese", "calories": 206, "benefits": "Rich in protein and calcium.",
             "recipe_link": "https://www.youtube.com/watch?v=fVDmsTtZgWc"}
        ]
    }
}

# Initialize session state for meal tracking if it doesn't exist
if "meal_log" not in st.session_state:
    st.session_state.meal_log = []

# User selection for dietary preference
diet_choice = st.selectbox("Select Your Dietary Preference:", list(food_categories.keys()))

# Use an expander to hide/show the Nutrition-Rich Foods section
with st.expander(f"Nutrition-Rich Foods for {diet_choice} Diet", expanded=False):
    for item in food_categories[diet_choice]["foods"]:
        st.write(f"**{item['name']}**: {item['benefits']} (Calories: {item['calories']})")
        st.markdown(f"[Recipe Video]({item['recipe_link']})")

# Meal tracking section
st.subheader("Meal Tracking")
food_selected = st.multiselect("Select Food Items:", [item["name"] for item in food_categories[diet_choice]["foods"]])
quantities = {}

# Create a number input for each selected food item
for food in food_selected:
    quantity = st.number_input(f"Quantity of {food} (in servings):", min_value=1, value=1, key=food)
    quantities[food] = quantity

if st.button("Log Meals"):
    # Calculate total calories for the logged meals
    for food in food_selected:
        calories_per_serving = next(item["calories"] for item in food_categories[diet_choice]["foods"] if item["name"] == food)
        total_calories = calories_per_serving * quantities[food]
        st.session_state.meal_log.append
