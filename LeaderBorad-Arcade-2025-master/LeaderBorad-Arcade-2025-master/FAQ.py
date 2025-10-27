import streamlit as st


def app():

    st.markdown(
        """
    <style>
        @font-face {
            font-family: 'Poppins';
            src: url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap');
        }
    </style>
    <h2 style='text-align: center; font-family: Poppins, sans-serif; color: #FF5733; font-weight:600; padding: 10px;'>
        📝 Before Registration
    </h2>
    """,
        unsafe_allow_html=True,
    )
    registration_faqs = [
        {
            "question": "Who is eligible to participate in the program?",
            "answer": "You must have an email ID created on or after July 31, 2025 and be 18 years or older. If not, Please fill your age more than 18 years even if you are not 18 years old.",
        },
        {
            "question": " Can you please share the guide to register for the program?",
            "answer": "Sure! You can find the registration guide here: https://docs.google.com/document/d/1gyC64WWuQQqAYXIjngKxTHa5IjmVFMaRoq17MnJ9TmA/edit?tab=t.0",
        },
        {
            "question": "How do I set up my Google Cloud Skill Boost account?",
            "answer": "Go to the Google Cloud Skill Boost link and create your account using the same email ID you used for program participation. Check the Steps from 1 to 5 using the link https://docs.google.com/document/d/1gyC64WWuQQqAYXIjngKxTHa5IjmVFMaRoq17MnJ9TmA/edit?tab=t.0",
        },
        {
            "question": "How do I update my profile settings on Google Cloud Skill Boost?",
            "answer": "After logging in, click your profile picture at the top left, go to settings, scroll to 'Leaderboards & Leagues', check all the boxes, and click update.",
        },
        {
            "question": "How can I check my Google Cloud Skill Boost profile ID?",
            "answer": "After logging in, click your profile picture at the top left, go to settings, scroll to 'public profile', and copy the URL. The profile ID is the last part of the URL after 'profile/' (e.g., https://www.cloudskillsboost.google/public_profile/123456789).",
        },
        {
            "question": "How do I subscribe to the Arcade program?",
            "answer": "Visit the Arcade website, click on the 'Subscribe Here' button, and fill the form using the same email from your account created on or after July 31, 2025. Make sure to use the same email ID for both the program and Google Cloud Skill Boost account.",
        },
        {
            "question": "What information should I have ready before filling out the registration form?",
            "answer": "You should have your Google Cloud Skill Boost profile ID, the referral code (GCAF25C2-IN-LWW-AM7), your correct email address, and your personal details like name, gender, country, and year of graduation.",
        },
    ]

    for faq in registration_faqs:
        with st.expander(faq["question"]):
            st.write(faq["answer"])

    st.markdown(
        """
    <style>
        @font-face {
            font-family: 'Poppins';
            src: url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap');
        }
    </style>
    <h2 style='text-align: center; font-family: Poppins, sans-serif; color: #3498DB; font-weight:600; padding: 10px;'>
        ✅ Post-Registration Process
    </h2>
    """,
        unsafe_allow_html=True,
    )

    post_registration_faqs = [
        {
            "question": "What happens after I submit the registration form?",
            "answer": "You will receive an email with a copy of your form. Check that the referral code is correct and then join the group for further updates and credits information and send the screenshot of the referral code to the General Group. I will verify by 👍🏻 in the group.",
        },
        {
            "question": "What is the referral code for the program?",
            "answer": "The referral code is GCAF25C2-IN-LWW-AM7. Be sure to copy it exactly as shown.",
        },
        {
            "question": "What if I enter incorrect information on the form?",
            "answer": "Incomplete or incorrect details, such as spelling mistakes or extra spaces, may lead to disqualification from the program.",
        },
        {
            "question": "What do we have to do after filling the registration form and verifying the referral code from the group?",
            "answer": "After verifying the referral code, you will receive a confirmation email with further instructions to redeem your credits after 24 hours. Follow the instructions carefully to ensure you receive your credits.",
        },
        {
            "question": "How do I redeem my credits?",
            "answer": "Follow the YouTube link to redeem your credits: https://youtu.be/5qDvS0yLTds?si=B99X68FRdFBQVYn8",
        },
        {
            "question": "After redeeming my credits, what do I have to do?",
            "answer": "After redeeming your credits, you are good to go. You can start performing the tasks and challenges in the program. Make sure to check your email for any updates or additional instructions.",
        },
        {
            "question": "What if I don't receive the credits redeem email?",
            "answer": "If you don't receive the email within 24 hours, please check your spam folder. If it's not there, contact the Facilitator for assistance.",
        },
        {
            "question": "Follow the youtube video but not able to redeem the credits?",
            "answer": "If you are still unable to redeem your credits, please contact the facilitator for further assistance. Make sure to provide details of the issue you're facing.",
        },
    ]

    for faq in post_registration_faqs:
        with st.expander(faq["question"]):
            st.write(faq["answer"])

    st.markdown(
        """
    <style>
        @font-face {
            font-family: 'Poppins';
            src: url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap');
        }
    </style>
    <h2 style='text-align: center; font-family: Poppins, sans-serif; color: #2ECC71; font-weight:600; padding: 10px;'>
        🎓 Lab-Free Courses
    </h2>
    """,
        unsafe_allow_html=True,
    )

    lab_free_faqs = [
        {
            "question": "What are Lab-Free Courses?",
            "answer": "Lab-Free Courses are training modules that do not require Google Cloud credits and can be completed immediately as part of the program.",
        },
        {
            "question": "How many Lab-Free Courses do I need to complete for ultimate Milestone?",
            "answer": "You need to complete at least 16 out of the 18 available Lab-Free Courses to reach the ultimate milestone.",
        },
        {
            "question": "Where can I find the list of Lab-Free Courses?",
            "answer": "You can find the list of Lab-Free Courses in the shared Excel sheet: https://docs.google.com/spreadsheets/d/1tsuDsrCssWUiQTHo88rvKBsYZcp4SdSOYrPU0aSYxtM/edit?usp=sharing  or please check the Lab-Free Courses section on this website.",
        },
        {
            "question": "Why should I complete Lab-Free Courses?",
            "answer": "Completing these courses helps you get started with Google Cloud and is a mandatory requirement for earning program swags.",
        },
        {
            "question": "When should I complete the Lab-Free Courses?",
            "answer": "These courses should be completed as soon as possible before August 31, 2025 to ensure a ultimate MileStone.",
        },
        {
            "question": "What happens after completing Lab-Free Courses?",
            "answer": "Once completed, you can move on to credit-based labs, Arcade Trivia, Arcade Games, and structured weekly tasks assigned by the facilitator. If you want you can complete them in any order.",
        },
        {
            "question": "Are solutions available for Lab-Free Courses?",
            "answer": "Yes, solutions for some courses have been provided in the shared document. You will need to find the remaining answers on your own.",
        },
        {
            "question": "Is Video is neccesary to watch for Lab-Free Courses?",
            "answer": "No, it is not necessary to watch the videos for Lab-Free Courses. You can just complete the quiz to earn badges.",
        },
    ]

    for faq in lab_free_faqs:
        with st.expander(faq["question"]):
            st.write(faq["answer"])

    st.markdown(
        """
    <style>
        @font-face {
            font-family: 'Poppins';
            src: url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap');
        }
    </style>
    <h2 style='text-align: center; font-family: Poppins, sans-serif; color: #F39C12; font-weight:600; padding: 10px;'>
        🚀 Lab-Based Courses
    </h2>
    """,
        unsafe_allow_html=True,
    )

    lab_based_faqs = [
        {
            "question": "What are Lab-Based Courses?",
            "answer": "Lab-Based Courses require Google Cloud credits to complete and are a key part of the program.",
        },
        {
            "question": "What are the weekly mandatory tasks?",
            "answer": "Each week, you must complete Arcade Badges, Arcade Trivia, and Arcade Games. Trivia and Games must be completed within the assigned week.",
        },
        {
            "question": "What happens if I miss a weekly task?",
            "answer": "You can complete a missed badge in the following week, but Arcade Trivia and Games must be done on time. No delays are allowed. if missed, you will not be able to earn the badge for that week and left with goodies and swags.",
        },
        {
            "question": "How many labs can I complete per day?",
            "answer": "Google Cloud Platform allows a maximum of 15 labs per day, so plan accordingly to stay on track.",
        },
        {
            "question": "Where can I check my progress and leaderboard ranking?",
            "answer": "Your progress and leaderboard will be updated soon on this website, showing your completed milestones, badges, trivia, and games.",
        },
        {
            "question": "What is the deadline for Arcade Trivia and Arcade Games?",
            "answer": "Go to the Arcade triva and games or level or base camp. Click on it and you will find the deadline for each task.",
        },
        {
            "question": "Where can I find Arcade Trivia and Games?",
            "answer": "You can access them at: https://go.cloudskillsboost.google/arcade",
        },
        {
            "question": "What if I fail to complete tasks on time?",
            "answer": "Failure to complete tasks within deadlines will affect your progress and could result in missing out on program benefits.",
        },
        {
            "question": "How to get the Access Code for Arcade Trivia and Games?",
            "answer": "Before clicking on the Arcade Trivia and Games, see it properly with you 2 eyes. You will find the access code there. If you are not able to find it, please leave the program.",
        },
        {
            "question": "How to solve Arcade Trivia and Games labs?",
            "answer": "When you perfrom any lab, Just copy and paste the name of the lab in the youtube. Find the solution from following channels : quick labs, btechy, cloud huslers. Watch the video which has exact same name of the lab.",
        },
        {
            "question": "What if I still not able to solve the lab?",
            "answer": "Try to copy and paste the Lab code in youtube, it is just below the lab name.",
        },
    ]

    for faq in lab_based_faqs:
        with st.expander(faq["question"]):
            st.write(faq["answer"])

    st.markdown(
        """
    <style>
        @font-face {
            font-family: 'Poppins';
            src: url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap');
        }
    </style>
    <h2 style='text-align: center; font-family: Poppins, sans-serif; color: #F39C12; font-weight:600; padding: 10px;'>
        🚀 General Question
    </h2>
    """,
        unsafe_allow_html=True,
    )

    lab_based_faqs = [
        {
            "question": "How many lab we solve in a day?",
            "answer": "You can solve 15 labs in a day.",
        },
        {
            "question": "What if lab limit is reached?",
            "answer": "If you reach the lab limit, you can wait for 2 hours to get a chance of 1 lab.",
        },
        {
            "question": "What is top priority task?",
            "answer": "Top priority task is Arcade Badges/Games/Trivia then Skill Badges then Lab-Free Courses",
        },
        {
            "question": "What if I miss the deadline for Arcade Trivia and Arcade Games?",
            "answer": "If you miss the deadline, you will not be able to earn the badge for that week and will be left with goodies and swags for top milestone.",
        },
        {
            "question": "How to check my progress?",
            "answer": "You can check the progress in the leaderboard. It will be updated soon on this website. Till then, you can check your progress by copy and pasting your cloud skill boost profile ID in the incognito mode.",
        },
        {
            "question": "What if I am not able to solve the weekly Badges?",
            "answer": "If you are not able to solve the weekly Badges, you have another week to solve it. But it will affect your progress as you have limit of 15 labs per day.",
        },
    ]

    for faq in lab_based_faqs:
        with st.expander(faq["question"]):
            st.write(faq["answer"])
