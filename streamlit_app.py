import streamlit as st

def main():
    st.title("My Portfolio Website")
    st.write("Welcome to my portfolio website!")
    
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
