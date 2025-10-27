import streamlit as st
import pandas as pd


def week5():

    data2 = [
        [
            "1",
            "Machine Learning Operations (MLOps) with Vertex AI: Model Evaluation",
            "[Badge Link](https://www.cloudskillsboost.google/course_templates/1080?utm_source=gcaf-site&utm_medium=website&utm_campaign=arcade-facilitator25)",
        ],
        [
            "2",
            "Infrastructure and Application Modernization with Google Cloud",
            "[Badge Link](https://www.cloudskillsboost.google/course_templates/266)",
        ],
        [
            "3",
            "Machine Learning Operations (MLOps) with Vertex AI: Model Evaluation",
            "[Badge Link](https://www.cloudskillsboost.google/course_templates/1080)",
        ],
        [
            "4",
            "AI Infrastructure: Introduction to AI Hypercomputer",
            "[Badge Link](https://www.cloudskillsboost.google/course_templates/1404)",
        ],
        [
            "5",
            "Infrastructure and Application Modernization with Google Cloud",
            "[Badge Link](https://www.cloudskillsboost.google/course_templates/266)",
        ],
        [
            "6",
            "Responsible AI: Applying AI Principles with Google Cloud",
            "[Badge Link](https://www.cloudskillsboost.google/course_templates/388)",
        ],
        [
            "7",
            "Exploring Data Transformation with Google Cloud",
            "[Badge Link](https://www.cloudskillsboost.google/course_templates/267)",
        ],
        [
            "8",
            "Gen AI Agents: Transform Your Organization",
            "[Badge Link](https://www.cloudskillsboost.google/course_templates/1267)",
        ],
        [
            "9",
            "Building Complex End to End Self-Service Experiences in Dialogflow CX",
            "[Badge Link](https://www.cloudskillsboost.google/course_templates/1103)",
        ],
    ]

    # Convert to DataFrame
    df = pd.DataFrame(data2, columns=["S. No", "Course Name", "Badge"])

    col1, col2 = st.columns(2)
    with col1:
        st.markdown(df[0:5].to_markdown(index=False), unsafe_allow_html=True)
    with col2:
        st.markdown(df[5:].to_markdown(index=False), unsafe_allow_html=True)

    data3 = [
        [
            "1",
            "Skills Boost Arcade Trivia September 2025 Week 1",
            "[Badge Link](https://www.cloudskillsboost.google/games/6462)",
            "1q-trivia-09629",
        ],
        [
            "2",
            "Skills Boost Arcade Trivia September 2025 Week 2",
            "[Badge Link](https://www.cloudskillsboost.google/games/6463)",
            "1q-trivia-06231",
        ],
        [
            "3",
            "Skills Boost Arcade Trivia September 2025 Week 3",
            "[Badge Link](https://www.cloudskillsboost.google/games/6464)",
            "1q-trivia-09634",
        ],
        [
            "4",
            "Skills Boost Arcade Trivia September 2025 Week 4",
            "[Badge Link](https://www.cloudskillsboost.google/games/6461)",
            "1q-trivia-09628",
        ],
        [
            "5",
            "Level 1: Cloud Infrastructure and Data Foundation",
            "[Badge Link](https://www.cloudskillsboost.google/games/6466)",
            "1q-cloudinfra-0922",
        ],
        [
            "6",
            "Level 2: Building with Cloud Tools",
            "[Badge Link](https://www.cloudskillsboost.google/games/6467)",
            "1q-innovation-0909",
        ],
        [
            "7",
            "Level 3: Developer Essentials",
            "[Badge Link](https://www.cloudskillsboost.google/games/6468)",
            "1q-developer-09122",
        ],
        [
            "8",
            "Skills Boost Arcade Base Camp September 2025",
            "[Badge Link](https://www.cloudskillsboost.google/games/6465)",
            "1q-basecamp-09302",
        ],
        [
            "8",
            "From Notes to Hands-on!",
            "[Badge Link](https://www.cloudskillsboost.google/games/6482)",
            "1q-scribble-17902",
        ],
    ]

    # Convert to DataFrame
    df2 = pd.DataFrame(
        data3,
        columns=[
            "S. No",
            "Arcade Trivia/Game",
            "Badge Link",
            "access Code",
        ],
    )
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(df2[0:4].to_markdown(index=False), unsafe_allow_html=True)
    with col2:
        st.markdown(df2[4:].to_markdown(index=False), unsafe_allow_html=True)
