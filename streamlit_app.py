import streamlit as st

# Set up the sidebar options
st.sidebar.title("Gym App")
options = ["Home", "Equipment", "Classes", "Membership"]
choice = st.sidebar.selectbox("Select an option", options)

# Set up the pages
if choice == "Home":
    st.title("Welcome to our gym!")
    st.write("We offer a wide range of equipment and classes to help you reach your fitness goals.")

elif choice == "Equipment":
    st.title("Equipment")
    equipment_list = ["Treadmill", "Elliptical", "Weight Machines", "Free Weights"]
    equipment = st.selectbox("Select an equipment", equipment_list)
    if equipment == "Treadmill":
        st.write("Our treadmills are state-of-the-art and perfect for cardio workouts.")
    elif equipment == "Elliptical":
        st.write("Our ellipticals provide a low-impact workout that's easy on your joints.")
    elif equipment == "Weight Machines":
        st.write("Our weight machines target specific muscle groups for a comprehensive strength training workout.")
    elif equipment == "Free Weights":
        st.write("Our free weights area has a wide range of dumbbells and barbells for your strength training needs.")

elif choice == "Classes":
    st.title("Classes")
    class_list = ["Yoga", "Pilates", "Spin", "Zumba"]
    gym_class = st.selectbox("Select a class", class_list)
    if gym_class == "Yoga":
        st.write("Our yoga classes focus on flexibility, strength, and balance.")
    elif gym_class == "Pilates":
        st.write("Our Pilates classes are designed to strengthen your core and improve your posture.")
    elif gym_class == "Spin":
        st.write("Our spin classes provide an intense cardiovascular workout on stationary bikes.")
    elif gym_class == "Zumba":
        st.write("Our Zumba classes combine dance and fitness for a fun, full-body workout.")

elif choice == "Membership":
    st.title("Membership")
    st.write("To become a member of our gym, please visit our website or stop by our location to sign up.")


