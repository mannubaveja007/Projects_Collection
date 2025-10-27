import streamlit as st
import pandas as pd


def app():

    # Data extracted from the spreadsheet with hidden links
    st.markdown(
        """
### 📌 **Important Notes**  
- ✅ **You have to complete 16 Lab Free Courses before August 30, 2025.** 
- 🎯 *Plan your daily lab completions efficiently.*  
- 📅 **Deadlines are strict.** Complete your tasks on time!  
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
    <h2 style='text-align: center; font-family: Poppins, sans-serif; color: #00A86B; font-weight:600; padding: 10px;'>
        🌟 Lab-Free Courses & Guidelines 🚀
    </h2>
    """,
        unsafe_allow_html=True,
    )

    data = [
        [
            "1",
            "Digital Transformation with Google Cloud",
            "[Badge Link](https://www.cloudskillsboost.google/course_templates/266?utm_source=gcaf-site&utm_medium=website&utm_campaign=arcade-facilitator25)",
        ],
        [
            "2",
            "Exploring Data Transformation with Google Cloud",
            "[Badge Link](https://www.cloudskillsboost.google/course_templates/267?utm_source=gcaf-site&utm_medium=website&utm_campaign=arcade-facilitator25)",
        ],
        [
            "3",
            "Infrastructure and Application Modernization with Google Cloud",
            "[Badge Link](https://www.cloudskillsboost.google/course_templates/265?utm_source=gcaf-site&utm_medium=website&utm_campaign=arcade-facilitator25)",
        ],
        [
            "4",
            "Scaling with Google Cloud Operations",
            "[Badge Link](https://www.cloudskillsboost.google/course_templates/271?utm_source=gcaf-site&utm_medium=website&utm_campaign=arcade-facilitator25)",
        ],
        [
            "5",
            "Innovating with Google Cloud Artificial Intelligence",
            "[Badge Link](https://www.cloudskillsboost.google/course_templates/946?utm_source=gcaf-site&utm_medium=website&utm_campaign=arcade-facilitator25)",
        ],
        [
            "6",
            "Trust and Security with Google Cloud",
            "[Badge Link](https://www.cloudskillsboost.google/course_templates/945?utm_source=gcaf-site&utm_medium=website&utm_campaign=arcade-facilitator25)",
        ],
        [
            "7",
            "Google Drive",
            "[Badge Link](https://www.cloudskillsboost.google/course_templates/199?utm_source=gcaf-site&utm_medium=website&utm_campaign=arcade-facilitator25)",
        ],
        [
            "8",
            "Google Docs",
            "[Badge Link](https://www.cloudskillsboost.google/course_templates/195?utm_source=gcaf-site&utm_medium=website&utm_campaign=arcade-facilitator25)",
        ],
        [
            "9",
            "Google Slides",
            "[Badge Link](https://www.cloudskillsboost.google/course_templates/197?utm_source=gcaf-site&utm_medium=website&utm_campaign=arcade-facilitator25)",
        ],
        [
            "10",
            "Google Meet",
            "[Badge Link](https://www.cloudskillsboost.google/course_templates/198?utm_source=gcaf-site&utm_medium=website&utm_campaign=arcade-facilitator25)",
        ],
        [
            "11",
            "Google Sheets",
            "[Badge Link](https://www.cloudskillsboost.google/course_templates/196?utm_source=gcaf-site&utm_medium=website&utm_campaign=arcade-facilitator255)",
        ],
        [
            "12",
            "Google Calendar",
            "[Badge Link](https://www.cloudskillsboost.google/course_templates/201?utm_source=gcaf-site&utm_medium=website&utm_campaign=arcade-facilitator25)",
        ],
        [
            "13",
            "Responsible AI: Applying AI Principles with Google Cloud",
            "[Badge Link](https://www.cloudskillsboost.google/course_templates/388?utm_source=gcaf-site&utm_medium=website&utm_campaign=arcade-facilitator25)",
        ],
        [
            "14",
            "Responsible AI for Digital Leaders with Google Cloud",
            "[Badge Link](https://www.cloudskillsboost.google/course_templates/1069?utm_source=gcaf-site&utm_medium=website&utm_campaign=arcade-facilitator25)",
        ],
        [
            "15",
            "Customer Experience with Google AI Architecture",
            "[Badge Link](https://www.cloudskillsboost.google/course_templates/1002?utm_source=gcaf-site&utm_medium=website&utm_campaign=arcade-facilitator25)",
        ],
        [
            "16",
            "Machine Learning Operations (MLOps) with Vertex AI: Model Evaluation",
            "[Badge Link](https://www.cloudskillsboost.google/course_templates/1080?utm_source=gcaf-site&utm_medium=website&utm_campaign=arcade-facilitator25)",
        ],
        # [
        #     "17",
        #     "Infrastructure and Application Modernization with Google Cloud",
        #     "[Badge Link](https://www.cloudskillsboost.google/course_templates/266)",
        # ],
        # [
        #     "18",
        #     "Machine Learning Operations (MLOps) with Vertex AI: Model Evaluation",
        #     "[Badge Link](https://www.cloudskillsboost.google/course_templates/1080)",
        # ],
        # [
        #     "19",
        #     "AI Infrastructure: Introduction to AI Hypercomputer",
        #     "[Badge Link](https://www.cloudskillsboost.google/course_templates/1404)",
        # ],
        # [
        #     "20",
        #     "Infrastructure and Application Modernization with Google Cloud",
        #     "[Badge Link](https://www.cloudskillsboost.google/course_templates/266)",
        # ],
        # [
        #     "21",
        #     "Responsible AI: Applying AI Principles with Google Cloud",
        #     "[Badge Link](https://www.cloudskillsboost.google/course_templates/388)",
        # ],
        # [
        #     "22",
        #     "Exploring Data Transformation with Google Cloud",
        #     "[Badge Link](https://www.cloudskillsboost.google/course_templates/267)",
        # ],
    ]

    # Convert to DataFrame
    df = pd.DataFrame(data, columns=["S. No", "Course Name", "Badge"])

    col1, col2 = st.columns(2)
    with col1:
        st.markdown(df[0:9].to_markdown(index=False), unsafe_allow_html=True)
    with col2:
        st.markdown(df[9:].to_markdown(index=False), unsafe_allow_html=True)


if __name__ == "__main__":
    app()
