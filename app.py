import streamlit as st
from PIL import Image

# ---------- CONFIG ----------
st.set_page_config(page_title="Portofolio | Dzakiyuddin", layout="wide")

# ---------- CUSTOM CSS ----------
st.markdown("""
    <style>
    body {
        color: #fff;
        background-color: #0e1117;
    }
    .stButton>button {
        background-color: #262730;
        color: white;
        border: none;
        border-radius: 8px;
        width: 100%;
        margin-bottom: 10px;
        text-align: left;
        font-size: 16px;
        white-space: nowrap;
        overflow: hidden;
        text-overflow: ellipsis;
    }
    .stButton>button:hover {
        background-color: #444;
    }
    [data-testid="stSidebar"] {
        min-width: 200px;
        max-width: 200px;
    }
    </style>
""", unsafe_allow_html=True)

# ---------- SIDEBAR NAVIGATION STATE ----------
if "page" not in st.session_state:
    st.session_state.page = "profil"
if st.sidebar.button("👤 Profile"):
    st.session_state.page = "profil"
if st.sidebar.button("🎓 Education"):
    st.session_state.page = "pendidikan"
if st.sidebar.button("💼 Work Experiences"):
    st.session_state.page = "pengalaman"
if st.sidebar.button("🧠 Project"):
    st.session_state.page = "proyek"
if st.sidebar.button("📚 Publication"):
    st.session_state.page = "publikasi"

nav_option = st.session_state.page

# ---------- CONTENT FUNCTIONS ----------
def show_profile():
    image = Image.open("assets/profile.jpeg")
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image(image, width=120)
    with col2:
        st.title("Muhammad Dzakiyuddin Haidar")
        st.write("📍 Ciamis - West Java | ✉️ dzakiyuddinhaidar@gmail.com | 📞 +6282127289858")
        st.write("I am a fresh graduate in 2025 from Telkom University with a GPA of 3.56 in Informatics. I have a strong enthusiasm and commitment to developing analytical skills, especially in understanding and analyzing behavior and trends on social media. Since the beginning of my studies, I have had a deep interest in how information spreads and interacts on digital platforms.")
    st.markdown("---")
    st.subheader("📱 Social Media")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.link_button("LinkedIn", "https://www.linkedin.com/in/muhammad-dzakiyuddin-haidar/")
    with col2:
        st.link_button("GitHub", "https://github.com/haidarzaki")
    with col3:
        st.link_button("Instagram", "https://www.instagram.com/haidarzakii/")

def show_education():
    st.title("🎓 Education")
    st.markdown("""
**Telkom University**  
Jl. Telekomunikasi. 1, Terusan Buahbatu - Bojongsoang, Telkom University, Sukapura, Kec. Dayeuhkolot, Kabupaten Bandung, Jawa Barat 40257  
**Sep 2021 - Feb 2025**  
**Bachelor of Informatics, GPA: 3.56 / 4.00**  

- Focused coursework in data visualization, dashboard development, and data analysis.  
- Hands-on experience with Power BI, Tableau, Looker Studio, SQL, and Python.  
- Training in Human-Computer Interaction, Software Engineering, Database Systems, and Social Network Analysis.  
- Application of analytical and visualization techniques to support insight-driven decision making.
""")

def show_experience():
    st.title("💼 Work Experiences")
    st.markdown("""
**Informatics Lab - Bandung**  
*Sep 2023 - Jan 2024*  
**Data Structure Lab Assistant**  
- Provided guidance and support to undergraduate students during data structures lab sessions using C++, ensuring clear understanding of key programming concepts.  
- Assisted 10+ undergraduate students in weekly C++ data structures lab sessions.  
- Evaluated student submissions, provided constructive feedback, and maintained accurate assessment records.  
- Improving comprehension of key programming concepts by 30% based on feedback surveys.  

**Telkom Indonesia - Bandung**  
*Jul 2024 - Aug 2024*  
**UI/UX Designer & Frontend Developer - Intern**  
- Collaborated cross-functionally with product managers, designers, and engineers in an agile team of 6 to develop Telpass, a digital leave management platform.  
- Conducted user interviews and usability testing with 20+ internal stakeholders.  
- Translated research insights into wireframes and interactive prototypes, increasing user satisfaction by 25%.  
- Contributed to frontend development using Tailwind CSS, JavaScript, and HTML.  

**Badan Riset dan Inovasi Nasional (BRIN)**  
*Mar 2024 - Jul 2024*  
**Journal Data Analyst - Intern**  
- Collected, cleaned, and pre-processed survey data from 120+ SMEs to assess digital technology readiness.  
- Conducted exploratory data analysis (EDA) and categorized SMEs into three maturity levels.  
- Modeled social network analysis using text modeling.  
- Contributed as a journal author on Social Network Analysis (SNA)-related research.
""")

def show_projects():
    st.title("🧠 Project")
    with st.expander("🔧 Telpass – Digital Leave Management Platform"):
        st.markdown("""
**Overview:**  
Telpass is a digital leave management platform designed to streamline employee leave request processes across multiple departments within an organization. This project was developed as part of a university internship program (_Kerja Praktik_), with a focus on frontend development and UI/UX design.

**Role & Contribution:**  
- Developed the **frontend interface** using **HTML**, **CSS**, and **JavaScript**, ensuring responsive and accessible user experiences across devices.  
- Designed and prototyped the **user interface** using **Figma**, focusing on clean layout, intuitive navigation, and minimal interaction friction.  
- Collaborated closely with a cross-functional team to translate functional requirements into visual and interactive elements.  

**Key Features:**  
- Streamlined leave request form with real-time validation  
- Department-specific approval workflow display  
- User-friendly dashboard for both employees and administrators

**Tools & Tech Stack:**  
`HTML`, `CSS`, `JavaScript`, `Figma`

**Outcome:**  
Improved the usability and clarity of the leave management process, contributing to faster onboarding and increased user satisfaction during internal usability testing.
""")
        st.link_button("GitHub Repo", "https://github.com/haidarzaki/Telpass")
    with st.expander("🌐 Journal Data Analysis – BRIN Internship"):
        st.markdown("""
**Overview:**  
This project was conducted as part of an internship program at BRIN (National Research and Innovation Agency), where I worked as a **Journal Data Analyst**. The objective was to analyze survey data from small and medium enterprises (SMEs) to assess their readiness in adopting digital technologies.

**Key Contributions:**  
- Collected, cleaned, and pre-processed survey data from 120+ SMEs to assess digital technology readiness.  
- Conducted exploratory data analysis (EDA) and categorized SMEs into three maturity levels (Learning, Implementation, Development). 

**Tools & Techniques:**  
`Python`, `Google Spreadsheet`

**Outcome:**  
The analysis supported policy recommendations for accelerating digital transformation among SMEs and resulted in a journal publication:
""")
        st.markdown("- [**Measuring Digital Technology Readiness in Manufacturing Small and Medium Enterprises (SMEs) in Indonesia**](https://doi.org/10.1109/ASIANComNet63184.2024.10811067)")

def show_publications():
    st.title("📚 Publications")
    st.markdown("""
- ["Measuring Digital Technology Readiness in Manufacturing Small and Medium Enterprises (SMEs) in Indonesia", *IEEE*, 2024](https://doi.org/10.1109/ASIANComNet63184.2024.10811067)
""")

# ---------- RENDER SELECTED PAGE ----------
if nav_option == "profil":
    show_profile()
elif nav_option == "pendidikan":
    show_education()
elif nav_option == "pengalaman":
    show_experience()
elif nav_option == "proyek":
    show_projects()
elif nav_option == "publikasi":
    show_publications()
