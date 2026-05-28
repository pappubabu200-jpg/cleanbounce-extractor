import streamlit as st

st.set_page_config(
    page_title="CleanBounce AI",
    page_icon="📧",
    layout="wide",
    initial_sidebar_state="expanded"
)

pg = st.navigation(
    [
        st.Page("home.py", title="CleanBounce AI", icon="📧", default=True),
        st.Page(
            "tools/bulk_url_opener.py",
            title="Bulk URL Opener",
            icon="🔗",
            url_path="bulk-url-opener"
        ),
        st.Page(
            "tools/fake_email_generator.py",
            title="Fake Email Generator",
            icon="✉️",
            url_path="fake-email-generator"
        ),
    ],
    position="sidebar"
)

pg.run()
