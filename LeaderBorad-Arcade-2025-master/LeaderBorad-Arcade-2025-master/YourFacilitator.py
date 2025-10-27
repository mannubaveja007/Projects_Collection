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
    <h2 style='text-align: center; font-family: Poppins, sans-serif; color: #FF9800; font-weight:600; padding: 10px;'>
        🤝 Meet Your Facilitator!
    </h2>
    """,
        unsafe_allow_html=True,
    )

    # Custom CSS for styling

    st.markdown(
        """
            <style>
                @font-face {
                    font-family: 'Poppins';
                    src: url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap');
                }
                .profile-container {
                    text-align: center;
                    padding: 20px;
                    background-color: #F4F6F6;
                    border-radius: 12px;
                    box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
                }
                .profile-image {
                    border-radius: 50%;
                    width: 150px;
                    height: 150px;
                    object-fit: cover;
                    margin-bottom: 10px;
                }
                .profile-name {
                    font-size: 24px;
                    font-weight: bold;
                    color: #2C3E50;
                }
                .profile-role {
                    font-size: 18px;
                    color: #16A085;
                    font-weight: 600;
                }
                .profile-contact {
                    font-size: 16px;
                    color: #34495E;
                }
                .social-links a {
                    margin: 0 10px;
                    text-decoration: none;
                    color: #0077B5;
                    font-size: 18px;
                }
                .social-links a:hover {
                    color: #005582;
                }
            </style>

            <div class='profile-container'>
                <div class='profile-name'>Mayank Sharma</div>
                <div class='profile-role'>Google Cloud Facilitator</div>
                <p class='profile-contact'>Mayank is passionate about cloud technologies and is here to guide you through the journey of learning and innovation.</p>
                <div class='social-links'>
                    <a href='https://www.linkedin.com/in/mayanksharmams' target='_blank'>🔗 LinkedIn</a> |
                    <a href='https://wa.me/9557560564' target='_blank'>📱 WhatsApp</a>
                </div>
            </div>
            """,
        unsafe_allow_html=True,
    )


if __name__ == "__main__":
    app()
