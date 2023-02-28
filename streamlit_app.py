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
    
    # Set profile picture
    st.image("https://cdn.pixabay.com/photo/2016/08/08/09/17/avatar-1577909_960_720.png", width=250)
    
    # Set page title and subtitle
    st.title("My Portfolio Website")
    st.write("Welcome to my portfolio website!")
    
    # Add content
    st.header("My Projects")
    st.write("""
    - Project 1
    - Project 2
    - Project 3
    """)
    
    st.header("My Skills")
    st.write("""
    - Skill 1
    - Skill 2
    - Skill 3
    """)
    
    st.header("Contact Me")
    st.write("""
    - Email: me@example.com
    - Phone: 123-456-7890
    """)
    
if __name__ == "__main__":
    main()
