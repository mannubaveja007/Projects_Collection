import streamlit as st
import pandas as pd


def week3():

    # data2 = [
    #     [
    #         "1",
    #         "Work Meets Play: Faster Finance",
    #         "[Badge Link](https://www.cloudskillsboost.google/games/6434)",
    #         "1q-finance-10201",
    #     ],
    #     [
    #         "2",
    #         "Skills Boost Arcade Certification Zone August 2025",
    #         "[Badge Link](https://www.cloudskillsboost.google/games/6435)",
    #         "1q-cert-10811",
    #     ],
    # ]

    # # Convert to DataFrame
    # df2 = pd.DataFrame(
    #     data2, columns=["S. No", "Arcade Trivia/Game", "Badge Link", "access Code"]
    # )

    st.info(
        "For badges where the solution link is not provided, please copy the lab name and lab code, then search on YouTube for solutions from channels like Bthecy, Quicklab, or Cloud Hustlers."
    )

    # col1, col2, col3 = st.columns([1, 3, 1])
    # with col2:
    #     st.markdown(df2.to_markdown(index=False), unsafe_allow_html=True)

    # Data for Google Cloud Badges
    data = [
        [
            "2",
            "Set Up a Google Cloud Network",
            "[Badge Link](https://www.cloudskillsboost.google/course_templates/641)",
            "[Solution]()",
        ],
        [
            "3",
            "Store, Process, and Manage Data on Google Cloud - Console",
            "[Badge Link](https://www.cloudskillsboost.google/course_templates/658)",
            "[Solution](https://www.youtube.com/playlist?list=PLHfVKuKwHnWOpaKFGfTSXt8NSxWS4929C)",
        ],
        [
            "4",
            "Networking Fundamentals on Google Cloud",
            "[Badge Link](https://www.cloudskillsboost.google/course_templates/748)",
            "[Solution](https://www.youtube.com/watch?v=1GEBx0OA1do&list=PLHfVKuKwHnWNo4lXUyfKHn0l8HNYjjm_O)",
        ],
        [
            "5",
            "Integrate BigQuery Data and Google Workspace using Apps Script",
            "[Badge Link](https://www.cloudskillsboost.google/course_templates/737)",
            "[Copy Lab Name & Paste youtube]()",
        ],
        [
            "6",
            "Create a Streaming Data Lake on Cloud Storage",
            "[Badge Link](https://www.cloudskillsboost.google/course_templates/705)",
            "[Copy Lab Name & Paste youtube]()",
        ],
        [
            "7",
            "Get Started with Looker",
            "[Badge Link](https://www.cloudskillsboost.google/course_templates/647)",
            "[Copy Lab Name & Paste youtube]()",
        ],
        [
            "8",
            "Implement DevOps Workflows in Google Cloud",
            "[Badge Link](https://www.cloudskillsboost.google/course_templates/716)",
            "[Solution](https://www.youtube.com/watch?v=XjVt3kPR_gQ&list=PLHfVKuKwHnWOHWSjdrpBcjUKW5_n4c704)",
        ],
        [
            "9",
            "Create and Manage Cloud Spanner Instances",
            "[Badge Link](https://www.cloudskillsboost.google/course_templates/643)",
        ],
        [
            "10",
            "Share Data Using Google Data Cloud",
            "[Badge Link](https://www.cloudskillsboost.google/course_templates/657)",
        ],
        [
            "11",
            "Build a Data Mesh with Dataplex",
            "[Badge Link](https://www.cloudskillsboost.google/course_templates/681)",
        ],
        [
            "12",
            "Build a Data Warehouse with BigQuery",
            "[Badge Link](https://www.cloudskillsboost.google/course_templates/624)",
        ],
        [
            "13",
            "Build a Website on Google Cloud",
            "[Badge Link](https://www.cloudskillsboost.google/course_templates/638)",
        ],
        [
            "14",
            "Build Infrastructure with Terraform on Google Cloud",
            "[Badge Link](https://www.cloudskillsboost.google/course_templates/636)",
        ],
        [
            "15",
            "Build LookML Objects in Looker",
            "[Badge Link](https://www.cloudskillsboost.google/course_templates/639)",
        ],
        [
            "16",
            "Create and Manage Bigtable Instances",
            "[Badge Link](https://www.cloudskillsboost.google/course_templates/650)",
        ],
        [
            "17",
            "Create and Manage Cloud Spanner Instances",
            "[Badge Link](https://www.cloudskillsboost.google/course_templates/643)",
        ],
        [
            "18",
            "Create and Manage Cloud SQL for PostgreSQL Instances",
            "[Badge Link](https://www.cloudskillsboost.google/course_templates/652)",
        ],
        [
            "19",
            "Develop Serverless Applications on Cloud Run",
            "[Badge Link](https://www.cloudskillsboost.google/course_templates/741)",
        ],
        [
            "20",
            "Engineer Data for Predictive Modeling with BigQuery ML",
            "[Badge Link](https://www.cloudskillsboost.google/course_templates/627)",
        ],
        [
            "21",
            "Migrate MySQL data to Cloud SQL using Database Migration Service",
            "[Badge Link](https://www.cloudskillsboost.google/course_templates/629)",
        ],
    ]

    # Convert to DataFrame
    df = pd.DataFrame(
        data, columns=["S. No", "Badge Name", "Badge Link", "Solution Link"]
    )

    # Display Data in Two Columns

    col1, col2 = st.columns(2)
    with col1:
        st.markdown(df[0:10].to_markdown(index=False), unsafe_allow_html=True)
    with col2:
        st.markdown(df[10:].to_markdown(index=False), unsafe_allow_html=True)
    col1, col2 = st.columns(2)
