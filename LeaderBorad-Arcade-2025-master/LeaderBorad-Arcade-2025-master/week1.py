import streamlit as st
import pandas as pd


def week1():

    # Data for Google Cloud Badges
    data = [
        [
            "1",
            "Analyze BigQuery Data in Connected Sheets",
            "[Badge Link](https://www.cloudskillsboost.google/course_templates/632?catalog_rank=%7B%22rank%22%3A49%2C%22num_filters%22%3A1%2C%22has_search%22%3Afalse%7D)",
            "[Solution](https://www.youtube.com/playlist?list=PL2QxKmNdTMQ7ffSTLYXXzHARXDqMRDCO9)",
        ],
        [
            "2",
            "Analyze Images with the Cloud Vision API",
            "[Badge Link](https://www.cloudskillsboost.google/course_templates/633?catalog_rank=%7B%22rank%22%3A66%2C%22num_filters%22%3A1%2C%22has_search%22%3Afalse%7D)",
            "[Solution](https://www.youtube.com/playlist?list=PL2QxKmNdTMQ5yZ5jbp1oHO1jc2cjCLnh5)",
        ],
        [
            "3",
            "Analyze Sentiment with Natural Language API",
            "[Badge Link](https://www.cloudskillsboost.google/course_templates/667?catalog_rank=%7B%22rank%22%3A73%2C%22num_filters%22%3A1%2C%22has_search%22%3Afalse%7D)",
            "[Solution](https://www.youtube.com/playlist?list=PL2QxKmNdTMQ4d0iiXtKI-yZV68uH42-e9)",
        ],
        [
            "4",
            "Analyze Speech and Language with Google APIs",
            "[Badge Link](https://www.cloudskillsboost.google/course_templates/634?catalog_rank=%7B%22rank%22%3A62%2C%22num_filters%22%3A1%2C%22has_search%22%3Afalse%7D)",
            "[Solution](https://www.youtube.com/playlist?list=PL2QxKmNdTMQ7V0KxGcgjO5ZySQA5HNJ8m)",
        ],
        [
            "5",
            "App Building with AppSheet",
            "[Badge Link](https://www.cloudskillsboost.google/course_templates/635?catalog_rank=%7B%22rank%22%3A52%2C%22num_filters%22%3A1%2C%22has_search%22%3Afalse%7D)",
            "[Solution](https://www.youtube.com/playlist?list=PL2QxKmNdTMQ5LUEH1yNyrR6AEjU3DRXjN)",
        ],
        [
            "6",
            "App Engine: 3 Ways",
            "[Badge Link](https://www.cloudskillsboost.google/course_templates/671?catalog_rank=%7B%22rank%22%3A58%2C%22num_filters%22%3A1%2C%22has_search%22%3Afalse%7D)",
            "[Solution](https://www.youtube.com/playlist?list=PL2QxKmNdTMQ68ij2ch5MfZU4Rp5kOzM5t)",
        ],
        [
            "7",
            "Get Started with Pub/Sub",
            "[Badge Link](https://www.cloudskillsboost.google/course_templates/728)",
            "[Solution](https://www.youtube.com/watch?v=nDDIobuamAo)",
        ],
        [
            "8",
            "Build Google Cloud Infrastructure for AWS Professionals",
            "[Badge Link](https://www.cloudskillsboost.google/course_templates/687?catalog_rank=%7B%22rank%22%3A45%2C%22num_filters%22%3A1%2C%22has_search%22%3Afalse%7D)",
            "[Solution](https://www.youtube.com/playlist?list=PL2QxKmNdTMQ6ydk7_V2ioOGJoWfSYsfRE)",
        ],
        [
            "9",
            "Build Google Cloud Infrastructure for Azure Professionals",
            "[Badge Link](https://www.cloudskillsboost.google/course_templates/688?catalog_rank=%7B%22rank%22%3A46%2C%22num_filters%22%3A1%2C%22has_search%22%3Afalse%7D)",
            "[Solution](https://www.youtube.com/playlist?list=PL2QxKmNdTMQ4Har7DhVqdqZVg_hjxNYXA)",
        ],
        [
            "10",
            "Create a Secure Data Lake on Cloud Storage",
            "[Badge Link](https://www.cloudskillsboost.google/course_templates/704?catalog_rank=%7B%22rank%22%3A63%2C%22num_filters%22%3A1%2C%22has_search%22%3Afalse%7D)",
            "[Solution](https://www.youtube.com/playlist?list=PL2QxKmNdTMQ5hNVlRslMPqnFz1ysYGw9F)",
        ],
        [
            11,
            "Build Real World AI Applications with Gemini and Imagen",
            "[Badge Link](https://www.cloudskillsboost.google/course_templates/1076?catalog_rank=%7B%22rank%22%3A83%2C%22num_filters%22%3A1%2C%22has_search%22%3Afalse%7D)",
            "[Solution](https://www.youtube.com/playlist?list=PL2QxKmNdTMQ7IWI1lt-l2in9ToxNLz5hE)",
        ],
        [
            12,
            "Cloud Functions: 3 Ways",
            "[Badge Link](https://www.cloudskillsboost.google/course_templates/696?catalog_rank=%7B%22rank%22%3A55%2C%22num_filters%22%3A1%2C%22has_search%22%3Afalse%7D)",
            "[Solution](https://www.youtube.com/playlist?list=PL2QxKmNdTMQ5_SpnV8E2Y9zBUpXxSHeps)",
        ],
        [
            13,
            "Cloud Speech API: 3 Ways",
            "[Badge Link](https://www.cloudskillsboost.google/course_templates/700?catalog_rank=%7B%22rank%22%3A75%2C%22num_filters%22%3A1%2C%22has_search%22%3Afalse%7D)",
            "[Solution](https://www.youtube.com/playlist?list=PL2QxKmNdTMQ6erxmi1eQzZKt2-X6DrMpl)",
        ],
        [
            14,
            "Configure Service Accounts and IAM Roles for Google Cloud",
            "[Badge Link](https://www.cloudskillsboost.google/course_templates/702?catalog_rank=%7B%22rank%22%3A77%2C%22num_filters%22%3A1%2C%22has_search%22%3Afalse%7D)",
            "[Solution](https://www.youtube.com/playlist?list=PL2QxKmNdTMQ62ag1lO7gN42Ft64NJotPe)",
        ],
        [
            15,
            "Using the Google Cloud Speech API",
            "[Badge Link](https://www.cloudskillsboost.google/course_templates/756?catalog_rank=%7B%22rank%22%3A71%2C%22num_filters%22%3A1%2C%22has_search%22%3Afalse%7D)",
            "[Solution](https://www.youtube.com/playlist?list=PL2QxKmNdTMQ6LHKTlUg959p5Tum1R3A3z)",
        ],
    ]

    # Convert to DataFrame
    df = pd.DataFrame(
        data, columns=["S. No", "Badge Name", "Badge Link", "Solution Link"]
    )
    st.info(
        """
        🚨 **Important Message:**  
        Please ensure you complete all badges and arcade games/levels before **20 August**. After this date, they will expire and cannot be claimed.  
        Arcade games/levels are the highest priority—focus on them first!  
        I am not responsible for any loss if you miss the deadline.  
        **Complete everything before August 20 to avoid missing out!**
        
        ⚠️ If you leave any badges or arcade games/levels incomplete, you will not be able to claim goodies for the top milestone.
        """
    )

    # Display Data in Two Column

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown(df[0:5].to_markdown(index=False), unsafe_allow_html=True)
    # with col2:
    #     st.markdown(df[8:15].to_markdown(index=False), unsafe_allow_html=True)

    # data2 = [
    #     [
    #         "16",
    #         "Skills Boost Arcade Trivia August 2025 Week 1",
    #         "[Badge Link](https://www.cloudskillsboost.google/games/6397)",
    #         "1q-trivia-2050",
    #         "[Solution Link](https://youtube.com/playlist?list=PL5aOhqv5LVIqLSjmB47rjGeeuPQLRfCIu&si=dDY5hlQc4Ndgmo8k)",
    #     ],
    #     [
    #         "17",
    #         "Skills Boost Arcade Trivia August 2025 Week 2",
    #         "[Badge Link](https://www.cloudskillsboost.google/games/6398)",
    #         "1q-trivia-7310",
    #         "[Solution Link](https://youtube.com/playlist?list=PL5aOhqv5LVIrkh4A7rH9wmujuACGPxGQP&si=Q6mzBnx8keRlKGyR)",
    #     ],
    #     [
    #         "18",
    #         "Skills Boost Arcade Trivia August 2025 Week 3",
    #         "[Badge Link](https://www.cloudskillsboost.google/games/6399)",
    #         "1q-trivia-2290",
    #         "[Solution Link](https://youtube.com/playlist?list=PL5aOhqv5LVIr-cQejoSCJrKTLUd-v2trF&si=8LhptJf8gMzFMciq)",
    #     ],
    #     [
    #         "19",
    #         "Skills Boost Arcade Trivia August 2025 Week 4",
    #         "[Badge Link](https://www.cloudskillsboost.google/games/6400)",
    #         "1q-trivia-5131",
    #         "[Solution Link](https://youtube.com/playlist?list=PL5aOhqv5LVIqbtKSUeYOH4YgoyL6liIxE&si=5TNn6HkER_sc2aS2)",
    #     ],
    #     [
    #         "20",
    #         "Level 1: Application Design and Delivery",
    #         "[Badge Link](https://www.cloudskillsboost.google/games/6394)",
    #         "1q-appdesign-0245",
    #         "[Solution Link](https://youtube.com/playlist?list=PL2QxKmNdTMQ7d45QitwIpSnN6dPvzNLLn&si=UzluLebyRwAtbxR8)",
    #     ],
    #     [
    #         "21",
    #         "Level 2: Building with Cloud Tools",
    #         "[Badge Link](https://www.cloudskillsboost.google/games/6395)",
    #         "1q-cloudtool-3109",
    #         "[Solution Link](https://youtube.com/playlist?list=PL2QxKmNdTMQ7MUE_2fTtAxtj1W3uFXNHk&si=jFBy8Pxdfhw2NOhu)",
    #     ],
    #     [
    #         "22",
    #         "Level 3: Terraform Essentials",
    #         "[Badge Link](https://www.cloudskillsboost.google/games/6396)",
    #         "1q-terraform-0480",
    #         "[Solution Link](https://youtube.com/playlist?list=PL5aOhqv5LVIq81Uk3dM48PXFGLBL8uPGm&si=TmOoNS30dP3nrsNZ)",
    #     ],
    #     [
    #         "23",
    #         "The Arcade Base Camp August",
    #         "[Badge Link](https://www.cloudskillsboost.google/games/6393)",
    #         "1q-basecamp-2930",
    #         "[Solution Link](https://youtube.com/playlist?list=PL2QxKmNdTMQ6O7tYNfvj7yBJaclvWmXa4&si=PrVkkzQVvcZO-Bpu)",
    #     ],
    # ]

    # # Convert to DataFrame
    # df2 = pd.DataFrame(
    #     data2,
    #     columns=[
    #         "S. No",
    #         "Arcade Trivia/Game",
    #         "Badge Link",
    #         "access Code",
    #         "Solution Link",
    #     ],
    # )
    # (col1, col2) = st.columns(
    #     [
    #         2,
    #         2,
    #     ]
    # )
    # with col2:
    #     st.markdown(df2[4:8].to_markdown(index=False), unsafe_allow_html=True)
    # with col1:
    #     st.markdown(df2[0:4].to_markdown(index=False), unsafe_allow_html=True)
