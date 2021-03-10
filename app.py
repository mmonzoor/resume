import streamlit as st
import content

st.sidebar.title("Navigation")
selection = st.sidebar.radio("Go to", ["Resume", "About", "Experience", "Projects", "Skills", "Hobbies", "Contact"])


with st.spinner(f"Loading {selection} ..."):
    if selection == "Resume":
        content.about_content()
        content.experience()
        content.contact()
    elif selection == "About":
        content.about_content()
    elif selection == "Experience":
        content.experience()
    elif selection == "Projects":
        content.projects()
    elif selection == "Skills":
        content.skills()
    elif selection == "Hobbies":
        content.hobbies()
    elif selection == "Contact":
        content.contact()

st.sidebar.title("Connect with me!")
st.sidebar.info(
"""
If you are looking to get in touch, 
[email me](mailto:mmonzoor.wv@gmail.com) or reach out 
to me on [LinkedIn](https://www.linkedin.com/in/mmonzoor/)
""")

