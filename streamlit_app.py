import streamlit as st

def main():
    # Set page title
    st.set_page_config(page_title="My Portfolio Website", page_icon=":guardsman:", layout="wide")

    # Set background color and banner image
    page_bg_img = '''
    <style>
    .stApp {
      background-image: url("https://cdn.pixabay.com/photo/2016/11/29/03/20/background-1869755_960_720.png");
      background-size: cover;
    }
    </style>
    '''
    st.markdown(page_bg_img, unsafe_allow_html=True)

    # Set navigation bars
    st.sidebar.title("Navigation")
    pages = ["Home", "Skills and Experiences", "Look At My Work"]
    selection = st.sidebar.radio("Go to", pages)

    # Set profile picture
    st.image("https://cdn.pixabay.com/photo/2016/08/08/09/17/avatar-1577909_960_720.png", width=250, 
             caption="My Profile Picture", use_column_width=False,
             output_format="PNG", style="display: block; margin: auto;")

    # Show selected page content
    if selection == "Home":
        st.header("Home")

        # Add profile photo
        st.image("https://cdn.pixabay.com/photo/2016/08/08/09/17/avatar-1577909_960_720.png", width=200, 
             caption="My Profile Picture", use_column_width=False,
             output_format="PNG", style="display: block; margin: auto;")

        # Add introduction
        st.write("""
        Hi there! I'm Jane Doe, a software developer with 5 years of experience in Python and web development. I'm passionate about building software that solves real-world problems and makes people's lives easier. In my free time, I enjoy hiking, reading, and playing the guitar. Thanks for visiting my portfolio website!
        """)

    elif selection == "Skills and Experiences":
        st.header("Skills and Experiences")
        st.write("""
        This page is where you can share information about your skills and experiences.
        """)

    elif selection == "Look At My Work":
        st.header("Look At My Work")
        st.write("""
        This page is where you can showcase your work and projects.
        """)

    # Add contact information
    st.header("Contact Me")
    st.write("""
    - Email: me@example.com
    - Phone: 123-456-7890
    """)

if __name__ == "__main__":
    main()
