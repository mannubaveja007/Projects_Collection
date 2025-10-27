import streamlit as st
import pandas as pd


def week6():

    data2 = [
        [
            "1",
            "Skills Boost Arcade Trivia October 2025 Week 1",
            "[Badge Link](https://www.cloudskillsboost.google/course_templates/6556)",
            "1q-trivia-22930",
        ],
        [
            "2",
            "Skills Boost Arcade Trivia October 2025 Week 2",
            "[Badge Link](https://www.cloudskillsboost.google/course_templates/6557)",
            "1q-trivia-10310",
        ],
        [
            "3",
            "Skills Boost Arcade Trivia October 2025 Week 3",
            "[Badge Link](https://www.cloudskillsboost.google/course_templates/6558)",
            "1q-trivia-29579",
        ],
        [
            "4",
            "Skills Boost Arcade Trivia October 2025 Week 4",
            "[Badge Link](https://www.cloudskillsboost.google/course_templates/6559)",
            "1q-trivia-32105",
        ],
        [
            "5",
            "Skills Boost Arcade Base Camp October 2025",
            "[Badge Link](https://www.cloudskillsboost.google/course_templates/6551)",
            "1q-basecamp-01202",
        ],
        [
            "6",
            "Level 1: Scalable Systems",
            "[Badge Link](https://www.cloudskillsboost.google/course_templates/6560)",
            "1q-scalability-14841",
        ],
        [
            "7",
            "Level 2: Cloud Operations and Application Management",
            "[Badge Link](https://www.cloudskillsboost.google/course_templates/6550)",
            "1q-cloudops-103102",
        ],
        [
            "8",
            "Level 3: Generative AI",
            "[Badge Link](https://www.cloudskillsboost.google/course_templates/6554)",
            "1q-genai-10091",
        ],
        [
            "9",
            "Lights & Logics",
            "[Badge Link](https://www.cloudskillsboost.google/games/6571)",
            "1q-lights-52021",
        ],
        [
            "10",
            "Diwali Dialogues",
            "[Badge Link](https://www.cloudskillsboost.google/games/6570)",
            "1q-diwali-102017",
        ],
    ]
    df1 = pd.DataFrame(
        data2, columns=["S. No", "Arcade Games", "Badge", " Access Code"]
    )

    col1, col2, col3 = st.columns([3, 6, 1])
    with col2:
        st.markdown(df1[5:].to_markdown(index=False), unsafe_allow_html=True)

    # Convert to DataFrame
    df = pd.DataFrame(data2, columns=["S. No", "Arcade Trivia", "Link", " Access Code"])

    col1, col2, col3 = st.columns([3, 6, 1])
    with col2:
        st.markdown(df[0:5].to_markdown(index=False), unsafe_allow_html=True)
