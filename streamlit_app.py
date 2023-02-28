import streamlit as st

def main():
    # Set page title
    st.set_page_config(page_title="Om Prakash Yadav", page_icon=":guardsman:", layout="wide")

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
    st.image("https://www.canva.com/design/DAFbRVgl8GI/kqeXUDAHFfSeZMmb1uaicg/view?utm_content=DAFbRVgl8GI&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton", width=250, 
             caption="My Profile Picture", use_column_width=False,
             output_format="PNG", style="display: block; margin: auto;")

    # Set page title and subtitle
    st.title("My Portfolio Website")
    st.write("Welcome to my portfolio website!")

    # Show selected page content
    if selection == "Home":
        st.header("Home")
        st.write("""
        This is the home page. Here, you can add any content you want to share with visitors to your website.
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
