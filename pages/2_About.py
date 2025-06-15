import streamlit as st

st.set_page_config(
    page_title="About",
    page_icon="📄",
)

# --- Page Title ---
st.markdown("<h1 style='font-size: 38px;'>📄 About This Project</h1>", unsafe_allow_html=True)

# --- Section 1: About the Website ---
st.markdown("<h2 style='font-size: 30px;'>🌐 PLAYSENSE:Best Price Checker</h2>", unsafe_allow_html=True)
st.markdown("""
<p style='font-size: 18px;'>
This website is a project made by a team of 4 students in their final year of Bachelor's Degree. It is a game price comparison and content-based video game recommendation system built using <strong>Python</strong> and <strong>Streamlit</strong>.<br>
It helps users search game info, compare it's prices amongst various platforms and discover new games based on their preferences by analyzing features like genre, rating, and keywords.<br>
Using <strong>cosine similarity</strong>, it suggests similar games based on user input, displaying detailed info and store links.<br>
Technologies used include: <strong>Pandas</strong>, <strong>Scikit-learn</strong>, <strong>Plotly</strong>, and <strong>Streamlit</strong>.
</p>
""", unsafe_allow_html=True)

# --- Section 2: Developer Info ---
st.markdown("<h2 style='font-size: 30px;'>👤 Developer Info</h2>", unsafe_allow_html=True)

developers = [
    {
        "name": "Avi Elasangi",
        "role": "API Developer and Database Manager",
        #"email": "john.doe@example.com",
        #"github": "https://github.com/johndoe",
        #"linkedin": "https://linkedin.com/in/johndoe"
    },
    {
        "name": "Eshan Painaik",
        "role": "API Developer and Database Manager",
        #"email": "jane.smith@example.com",
        #"github": "https://github.com/janesmith",
        #"linkedin": "https://linkedin.com/in/janesmith"
    },
    {
        "name": "Aaryan Sawant",
        "role": "Team Leader, Web Developer and ML Engineer",
        #"email": "alex.kim@example.com",
        #"github": "https://github.com/alexkim",
        #"linkedin": "https://linkedin.com/in/alexkim"
    },
    {
        "name": "Advait Sarang",
        "role": "Scheduling and Documentation",
        #"email": "priya.mehra@example.com",
        #"github": "https://github.com/priyamehra",
        #"linkedin": "https://linkedin.com/in/priyamehra"
    }
]

for dev in developers:
    st.markdown(f"""
    <div style='font-size: 18px; padding-bottom: 20px;'>
        <strong>Name:</strong> {dev['name']}<br>
        <strong>Role:</strong> {dev['role']}<br>
        </div>
    """, unsafe_allow_html=True)

        #<strong>Email:</strong> <a href="mailto:{dev['email']}">{dev['email']}</a><br>
        #<strong>GitHub:</strong> <a href="{dev['github']}" target="_blank">{dev['github']}</a><br>
        #<strong>LinkedIn:</strong> <a href="{dev['linkedin']}" target="_blank">{dev['linkedin']}</a>
