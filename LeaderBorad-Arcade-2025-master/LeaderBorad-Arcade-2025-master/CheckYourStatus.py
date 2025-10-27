import streamlit as st
import pandas as pd


def app():
    st.markdown(
        """
    <style>
        @font-face {
            font-family: 'Poppins';
            src: url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap');
        }
    </style>
    <h2 style='text-align: center; font-family: Poppins, sans-serif; color: #1ABC9C; font-weight:600; padding: 10px;'>
        🔍 Check Your Status
    </h2>
    """,
        unsafe_allow_html=True,
    )

    # 1) Upload CSV
    uploaded_file = "data.csv"
    # 2) Read & preprocess
    df = pd.read_csv(uploaded_file)

    if all(
        col in df.columns
        for col in [
            "# of Skill Badges Completed",
            "# of Trivia Games Completed",
            "# of Arcade Games Completed",
            "# of Lab-free Courses Completed",
        ]
    ):
        df["Total Arcade points"] = (
            (df["# of Skill Badges Completed"] // 2)
            + df["# of Trivia Games Completed"]
            + df["# of Arcade Games Completed"]
        ).astype(int)

    # 3) Ask the user for their profile‑ID (or a substring of it)
    profile_input = st.text_input(
        "Enter your unique Cloud Skill Boost Profile URL",
        placeholder="e.g.  https://www.cloudskillsboost.google/public_profiles//1234abcd",
    )

    if profile_input:
        # substring‐match so they can paste the whole URL or just the ID
        mask = df.astype(str).apply(
            lambda col: col.str.contains(profile_input, na=False)
        )
        # any column matching? but better to match only your ID column:
        # mask = df["Google Cloud Skills Boost Profile URL"].str.contains(profile_input, na=False)
        matched = df[mask.any(axis=1)]

        if matched.empty:
            st.error("❌ No profile found.  Check your ID/URL and try again.")
        else:
            # assume first match is the one
            user_row = matched.iloc[0]
            # build a two‑column DataFrame
            status_df = pd.DataFrame(
                {"Field": user_row.index, "Value": user_row.values}
            )
            st.subheader("🎉 Your Status")
            st.dataframe(status_df)
