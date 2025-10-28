import streamlit as st
import pandas as pd


def week4():

    data2 = [
        [
            "Skills Boost Arcade Trivia April 2025 Week 4",
            "[Badge Link](https://www.cloudskillsboost.google/games/6105?utm_source=qwiklabs&utm_medium=lp&utm_campaign=arcade25-April-trivia)",
            "1q-trivia-04553",
        ],
        [
            "Skills Boost Arcade Certification Zone April 2025",
            "[Badge Link](https://www.cloudskillsboost.google/games/6107?utm_source=qwiklabs&utm_medium=lp&utm_campaign=special-April-arcade25)",
            "1q-cert-04092",
        ],
    ]

    # Convert to DataFrame
    df2 = pd.DataFrame(
        data2, columns=["Arcade Trivia/Game", "Badge Link", "access Code"]
    )

    col1, col2, col3 = st.columns([2, 3, 2])
    with col2:
        st.markdown(df2.to_markdown(index=False), unsafe_allow_html=True)

    # Data for Google Cloud Badges
    data = [
        [
            "1",
            "Create and Manage Cloud Spanner Instances",
            "[Badge Link](https://www.cloudskillsboost.google/course_templates/643)",
        ],
        [
            "2",
            "Share Data Using Google Data Cloud",
            "[Badge Link](https://www.cloudskillsboost.google/course_templates/657)",
        ],
        [
            "3",
            "Build a Data Mesh with Dataplex",
            "[Badge Link](https://www.cloudskillsboost.google/course_templates/681)",
        ],
        [
            "4",
            "Build a Data Warehouse with BigQuery",
            "[Badge Link](https://www.cloudskillsboost.google/course_templates/624)",
        ],
        [
            "5",
            "Build a Website on Google Cloud",
            "[Badge Link](https://www.cloudskillsboost.google/course_templates/638)",
        ],
        [
            "6",
            "Build Infrastructure with Terraform on Google Cloud",
            "[Badge Link](https://www.cloudskillsboost.google/course_templates/636)",
        ],
        [
            "7",
            "Build LookML Objects in Looker",
            "[Badge Link](https://www.cloudskillsboost.google/course_templates/639)",
        ],
        [
            "8",
            "Create and Manage Bigtable Instances",
            "[Badge Link](https://www.cloudskillsboost.google/course_templates/650)",
        ],
        [
            "9",
            "Create and Manage Cloud Spanner Instances",
            "[Badge Link](https://www.cloudskillsboost.google/course_templates/643)",
        ],
        [
            "10",
            "Create and Manage Cloud SQL for PostgreSQL Instances",
            "[Badge Link](https://www.cloudskillsboost.google/course_templates/652)",
        ],
        [
            "11",
            "Develop Serverless Applications on Cloud Run",
            "[Badge Link](https://www.cloudskillsboost.google/course_templates/741)",
        ],
        [
            "12",
            "Engineer Data for Predictive Modeling with BigQuery ML",
            "[Badge Link](https://www.cloudskillsboost.google/course_templates/627)",
        ],
        [
            "13",
            "Migrate MySQL data to Cloud SQL using Database Migration Service",
            "[Badge Link](https://www.cloudskillsboost.google/course_templates/629)",
        ],
        [
            "14",
            "Mitigate Threats and Vulnerabilities with Security Command Center",
            "[Badge Link](https://www.cloudskillsboost.google/course_templates/759)",
        ],
        [
            "15",
            "Perform Predictive Data Analysis in BigQuery",
            "[Badge Link](https://www.cloudskillsboost.google/course_templates/655)",
        ],
        [
            "16",
            "Optimize Costs for Google Kubernetes Engine",
            "[Badge Link](https://www.cloudskillsboost.google/course_templates/656)",
        ],
        [
            "17",
            "Share Data Using Google Data Cloud",
            "[Badge Link](https://www.cloudskillsboost.google/course_templates/657)",
        ],
        [
            "18",
            "Optimize Costs for Google Kubernetes Engine",
            "[Badge Link](https://www.cloudskillsboost.google/course_templates/655)",
        ],
    ]

    # Convert to DataFrame
    df = pd.DataFrame(data, columns=["S. No", "Badge Name", "Badge Link"])

    # Display Data in Two Columns

    col1, col2 = st.columns(2)
    with col1:
        st.markdown(df[0:9].to_markdown(index=False), unsafe_allow_html=True)
    with col2:
        st.markdown(df[9:].to_markdown(index=False), unsafe_allow_html=True)
    col1, col2 = st.columns(2)
[
            "14",
            "Mitigate Threats and Vulnerabilities with Security Command Center",
            "[Badge Link](https://www.cloudskillsboost.google/course_templates/759)",
        ],
        [
            "15",
            "Perform Predictive Data Analysis in BigQuery",
            "[Badge Link](https://www.cloudskillsboost.google/course_templates/655)",
        ],
        [
            "16",
            "Optimize Costs for Google Kubernetes Engine",
            "[Badge Link](https://www.cloudskillsboost.google/course_templates/656)",
        ],
        [
            "17",
            "Share Data Using Google Data Cloud",
            "[Badge Link](https://www.cloudskillsboost.google/course_templates/657)",
        ],
        [
            "18",
            "Optimize Costs for Google Kubernetes Engine",
            "[Badge Link](https://www.cloudskillsboost.google/course_templates/655)",
        ],