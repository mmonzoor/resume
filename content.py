import streamlit as st
def about_content():

    st.title("Mumtahin (Tahin) Monzoor | She/Her")

    st.markdown("""I am a Data Scientist with over 
    4 years of experience in fraud and data with the ability to lead projects 
    from both a technical and business capacity.  As a **Sr. Data 
    Scientist** at Interac, I have prevented over **$10 million**
    dollars in Fraud losses and saved hundreds of hours in operational time.
    Aside from working full time, I have also been pursuing a Masters degree 
    at the University of Pennsylvania.""") 
    
    st.write(""" *As I complete my 
    masters degree in Computer Science, I want to utilize the knowledge 
    I have gained in this program and take part in projects 
    more geared towards* **software enginnering.**""")

    st.markdown("""If you think you can help me in my journey, or have a 
    project I can help you with, please get in [touch](https://www.linkedin.com/in/mmonzoor/)! """)
def experience():
    st.title("Experience")
    st.subheader("Sr. Data Scientist | [Interac Corp.](https://newsroom.interac.ca/video-interac-up-close-mumtahin-monzoor/)| 2017/01 - Present")
    st.markdown("""
    - **Scam Detection**: Created a detection model targeting scammers exploiting Covid-19 
    relief funds and blocking $1,000,000 in scam attempts over 24 hours.
    - **Merchant Fraud Model**: Engineered a high-risk merchant classification tool that 
    created custom blocking rules and prevented **$150,000 in fraud losses/ month**.
    - **Trust Network**: Modelled trusted networks of legitimate users to reduce false positives and increase 
    alerting accuracy which removed **2000 false alerts/ month**, saving 120 hours of front-line Analyst time.
    - **Data Governance**: Vetted data sources from financial institutions, third-party vendors, and in-house applications 
    to ensure data integrity. Automated detections of re-occurring data quality issues.""")

    st.subheader("Data Scientist | University of Waterloo - [Netlabs](https://uwaterloo.ca/networks-lab/): 2017/09 - 2018/04")
    st.markdown("""
    - **Record Linkage Analysis**:  Using Python’s NLTK library, performed analysis of collaboration networks in 
    academia for biomedical research. The task was to resolve similar entities with overlapping names and 
    institutional origin by analyzing their writing styles.
    - **Survey Portal**: Using Django, created a portal for researchers to log into and fill out surveys in exchange for
    curated newsletters in their industry. 
    """)

    st.subheader("Computational Biology | University of Waterloo - [iGEM](http://2016.igem.org/Team:Waterloo) | 2015/09 - 2016/12")
    st.markdown("""
    - **Stop Codon Analysis**:  Using Python, created a software tool that performed analysis of the genome 
    of a heatshock protein (HSP104) found in Yeast for the purposes of researching chaperone behaviour 
    among prion proteins.Waterloo won gold in the iGEM (Synthetic Biology) competition where this software tool was a key component.
    - **Research Collaboration Network**: Modelled research networks within the iGEM community and modelled cross collaboration patterns
    amoung iGEM teams from the various countries and its impact on teams winning Gold, Silver, or Bronze. 
    """)
def projects():
    st.title("Projects")
    st.markdown("""
    - **Got an Edge?**: I wrote a Streamlit app (similar to this resume) that introduces 
    the concept of edge detection in Computer Vision. Feel free
    to check out the [app](https://share.streamlit.io/mmonzoor/edge_detection/app.py) 
    and scroll to the bottom if you want to upload your own image to find edges with!
    - **Avoid the Potholes!**: I wrote a tutorial introducing the steps of fetching, 
    parsing, and cleaning data with the objective of creating meaningful visualizations 
    for exploratory analysis. If you are interested, check out my [repo](
    https://github.com/mmonzoor/introductory_pot_hole_viz) and my [article](
    https://towardsdatascience.com/mapping-locations-of-reported-pot-holes-in-toronto-using-python-376402d8da53?sk=092fc3bf03d3d0cdae6d0751e82b04af).
    - **Fetch Data from API**: I created teaching content and workshop tutorials 
    for University of Waterloo's Big Data in Social Science course offered by 
    Dr. John McLevey. Curated content explaining API usage which can be found 
    in this [repo](https://github.com/mmonzoor/computational_social_science_course_notebooks/tree/master/APIs).
    - **Blockbuster Nostalgia**: I created a Virtual Movie Rental store as a throw back to 
    the ol' days of Blockbuster. The project was written in Java and I used the
    IMDB API to fetch movie records and mimicked the flow of an e-commerce store 
    for movie rentals. Detailed explanation for the project can be found [here](https://github.com/mmonzoor/CIT591_IMDB).
    """)

def contact():
    st.title("Let's Chat!")
    st.write("""I am a lifelong learner and always up for a new challenge. If you like the 
    work I have done in the past and want to chat more, please get in touch 
    through my **[LinkedIn](https://www.linkedin.com/in/mmonzoor/)**. If it is not a skillset you see that I currently have, but you are willing 
    to give me the opportunity to learn what I need to, let's also have a conversation!""")
def skills():
    st.title("Skills")
    st.text("Excellence is not a skill, it's an attitude. - Ralph Marston") 
    st.markdown("""
    - Python
    - SQL (Redshit, Oracle)
    - Java
    - Git
    - Linux
    - Model building
    - Policy Writing
    - Presentation
    - Data Governance 
    - Risk/ Fraud Management
    """) 
def hobbies():
    st.title("Hobbies")
    st.text("You never lose a dream, it just incubates as a hobby. - Larry Page")
    st.markdown("""
    - Video games
    - Painting
    - Reading
    - Gardening 
    """)