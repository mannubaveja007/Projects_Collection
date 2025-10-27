import streamlit as st
from week1 import week1
from week2 import week2
from week3 import week3
from week5 import week5
from week6 import week6

# from week4 import week4
from May import may


def app():
    # Weekly Challenges Heading
    st.markdown(
        """
        ### 📌 **Important Notes**  
        - ✅ **Complete all the Badges, Trivia, and Games Before the deadline.**  
        - 🎯 *Plan your daily lab completions efficiently. You can perform 15 labs per day.*  
        - 📅 **Deadlines are strict!** Complete your tasks on time! I am not responsible for any failure.  
        - 🏆 **To find the lab solutions, copy the lab name or lab code (below the lab name) and paste it on YouTube. (Suggested Channels: Quick Lab, Cloud Hustlers, Btechy)**
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <style>
            @font-face {
                font-family: 'Poppins';
                src: url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap');
            }
        </style>
        <h2 style='text-align: center; font-family: Poppins, sans-serif; color: #E74C3C; font-weight:600; padding: 10px;'>
            ⚡ Weekly Challenges
        </h2>
        """,
        unsafe_allow_html=True,
    )

    # 👇 Use Streamlit Tabs to organize Weeks
    tabs = st.tabs(
        [
            "📅 Task 1: August 6  - August 13",
            "📅 Task 2: August 14 - August 20",
            "📅 Task 3: August 21 - August 31",
            "📅 Task 4: September 1 - September 7",
            "📅 October Challenges",
        ]
    )

    with tabs[0]:
        week1()
    with tabs[1]:
        week2()
    with tabs[2]:
        week3()
    with tabs[3]:
        week5()
    with tabs[4]:
        week6()
    # with tabs[4]:
    #     may()


# Important Notes Section


if __name__ == "__main__":
    app()
