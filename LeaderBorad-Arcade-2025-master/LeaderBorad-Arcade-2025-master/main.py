import streamlit as st
from utils import inject_heading, set_custom_style
import Leaderboard
import CheckYourStatus
import FAQ
import YourFacilitator
import WeeklyChallenge
import LabFreeCourse
import RegistrationGuide

# Set page configuration
st.set_page_config(page_title="Google Cloud Arcade Facilitator", layout="wide")

# Display the sidebar logo
# display_sidebar_logo()..

# Display the common heading on all tabs
inject_heading()

set_custom_style()

# Create tabs for each section
tabs = st.tabs(
    [
        "Registration Guide",
        "Leaderboard",
        "Check Your Status",
        "Weekly Challenge",
        "Lab Free Courses",
        "FAQ",
        "Your Facilitator",
    ]
)

st.markdown(
    """
            <style>
                .stTabs [data-baseweb="tab-list"] {
                    display: flex;
                    justify-content: center;
                }
                .stTabs [data-baseweb="tab"] {
                    height: 40px;
                    white-space: pre-wrap;
                    width: 300px;
                }
                
            </style>
            """,
    unsafe_allow_html=True,
)


with tabs[0]:
    RegistrationGuide.app()

with tabs[1]:
    Leaderboard.app()

with tabs[2]:
    CheckYourStatus.app()

with tabs[3]:
    WeeklyChallenge.app()

with tabs[4]:
    LabFreeCourse.app()

with tabs[5]:
    FAQ.app()

with tabs[6]:
    YourFacilitator.app()
