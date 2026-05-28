import streamlit as st
import re
import pandas as pd
from collections import Counter
import time

# =====================================================
# CONFIG
# =====================================================

st.set_page_config(
    page_title="CleanBounce AI",
    page_icon="📧",
    layout="wide",
    initial_sidebar_state="collapsed"
)

<<<<<<< HEAD
# =====================================================
# HIDE STREAMLIT UI
# =====================================================

st.markdown("""
<style>

#MainMenu {
    visibility: hidden;
}

header {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

</style>
""", unsafe_allow_html=True)

=======
                # =====================================================
                # HIDE STREAMLIT UI
                # ==================================================
                # Hide Streamlit UI
                st.markdown("""
                <style>
                #MainMenu {visibility: hidden;}
                header {visibility: hidden;}
                footer {visibility: hidden;}
                </style>
                """, unsafe_allow_html=True)

>>>>>>> 52dbdf3 (Final CleanBounce AI upgrade)
# =====================================================
# CUSTOM CSS
# =====================================================

st.markdown("""
<style>

.main {
    background-color: #050816;
}

.block-container {
    padding-top: 1rem;
}

h1,h2,h3,h4 {
    color: #f8fafc;
}

.stMetric {
    background-color: #0f172a;
    border-radius: 14px;
    padding: 15px;
    border: 1px solid #1e293b;
}

.stTextArea textarea {
    background-color: #020617;
    color: #e2e8f0;
    border-radius: 12px;
    font-family: monospace;
}

div[data-testid="stFileUploader"] {
    background-color: #0f172a;
    border: 1px solid #1e293b;
    padding: 15px;
    border-radius: 14px;
}

.stButton button {
    background: linear-gradient(90deg,#2563eb,#7c3aed);
    color: white;
    border-radius: 12px;
    border: none;
    padding: 12px;
    font-weight: bold;
}

</style>
""", unsafe_allow_html=True)

# =====================================================
# HEADER
# =====================================================

st.markdown("""
<h1 style='
font-size:52px;
font-weight:800;
margin-bottom:0;
line-height:1;
color:white;
'>
CleanBounce AI
</h1>
""", unsafe_allow_html=True)

st.markdown("""
<p style='
font-size:18px;
color:#94a3b8;
margin-top:5px;
'>
Smart B2B Lead Cleaning Engine with Validation & Bounce Risk
</p>
""", unsafe_allow_html=True)

# =====================================================
# SIDEBAR
# =====================================================

st.sidebar.header("⚙️ Settings")

allow_gmail = st.sidebar.checkbox(
    "Allow Gmail.com",
    value=True
)

allow_personal = st.sidebar.checkbox(
    "Allow Other Personal Emails",
    value=False
)

india_first = st.sidebar.checkbox(
    "India First (.in boost)",
    value=True
)

min_quality = st.sidebar.slider(
    "Minimum Quality Score",
    0,
    100,
    65
)

max_bounce_risk = st.sidebar.slider(
    "Max Bounce Risk %",
    0,
    100,
    45
)

st.sidebar.markdown("---")

st.sidebar.markdown("""
### 🚀 Pro Features

✅ Bounce Risk Detection  
✅ Disposable Email Detection  
✅ Quality Scoring  
✅ India Domain Prioritization  
✅ CSV Export  
✅ Duplicate Removal  
✅ Domain Analytics  
""")

# =====================================================
# DISPOSABLE DOMAINS
# =====================================================

DISPOSABLE_DOMAINS = {
    'tempmail.com',
    '10minutemail.com',
    'guerrillamail.com',
    'throwawaymail.com',
    'mailinator.com',
    'yopmail.com',
    'sharklasers.com',
    'dispostable.com',
    'temp-mail.org',
    'fakeemail.net',
    'trashmail.com'
}

# =====================================================
# TEST / PLACEHOLDER EMAIL FILTER
# =====================================================

TEST_PLACEHOLDERS = {

    # Generic
    'test',
    'testing',
    'sample',
    'demo',
    'temp',
    'temporary',
    'fake',
    'spam',
    'dummy',
    'user',
    'admin',

    # Jane First Variations
    'jane',
    'first',
    'janefirst',
    'jfirst',
    'jafirst',
    'janef',
    'jf',
    'jmf',
    'janemfirst',
    'firstjane',
    'firstj',
    'thejanefirst',
    'iamjanefirst',
    'janefirst1',

    # Jane Doe Variations
    'doe',
    'janedoe',
    'jdoe',
    'jadoe',
    'janed',
    'jd',
    'jmd',
    'janemdoe',
    'doejane',
    'doej',
    'thejanedoe',
    'iamjanedoe',
    'janedoe1',

    # Jane Last Variations
    'last',
    'janelast',
    'jlast',
    'jalast',
    'janel',
    'jl',
    'jml',
    'janemlast',
    'lastjane',
    'lastj',
    'thejanelast',
    'iamjanelast',
    'janelast1'
}

# =====================================================
# TEST EMAIL DETECTION FUNCTION
# =====================================================

def is_test_email(email):

    local = email.split('@')[0].lower().strip()

    # Remove dots, dashes, underscores, numbers
    local_clean = re.sub(
        r'[^a-z]',
        '',
        local
    )

    # Direct match
    if local_clean in TEST_PLACEHOLDERS:
        return True

    # Suspicious patterns
    suspicious_patterns = [
        'janefirst',
        'janedoe',
        'janelast',
        'test',
        'sample',
        'fake',
        'dummy'
    ]

    for pattern in suspicious_patterns:

        if pattern in local_clean:
            return True

    return False


# =====================================================
# FUNCTIONS
# =====================================================

def is_test_email(email):

    local = email.split('@')[0].lower().strip()

    local_clean = re.sub(
        r'[^a-z]',
        '',
        local
    )

    for placeholder in TEST_PLACEHOLDERS:

        if (
            placeholder in local
            or local_clean in [
                'jane',
                'doe',
                'john',
                'first',
                'last'
            ]
        ):
            return True

    return False


def is_valid_email(email):

    pattern = (
        r'^[a-zA-Z0-9._%+-]+'
        r'@[a-zA-Z0-9.-]+'
        r'\.[a-zA-Z]{2,}$'
    )

    if not re.match(pattern, email):
        return False

    if (
        email.count('@') > 1
        or '..' in email
        or email.startswith('.')
        or email.endswith('.')
    ):
        return False

    return True


def calculate_bounce_risk(email):

    domain = email.split('@')[1].lower()

    local_part = email.split('@')[0].lower()

    risk = 15

    if domain in DISPOSABLE_DOMAINS:
        risk += 70

    free_providers = {
        'gmail.com',
        'yahoo.com',
        'hotmail.com',
        'outlook.com',
        'icloud.com',
        'protonmail.com',
        'rediffmail.com',
        'aol.com'
    }

    if domain in free_providers:
        risk += 25

    role_keywords = [
        'info',
        'admin',
        'support',
        'sales',
        'contact',
        'hello',
        'noreply',
        'marketing'
    ]

    if any(
        role in local_part
        for role in role_keywords
    ):
        risk += 20

    if len(local_part) <= 3:
        risk += 15

    if len(local_part) > 30:
        risk += 10

    if domain.endswith('.in'):
        risk = max(10, risk - 18)

    return min(95, max(5, risk))


def extract_emails(text):

    pattern = (
        r'[a-zA-Z0-9._%+-]+'
        r'@[a-zA-Z0-9.-]+'
        r'\.[a-zA-Z]{2,}'
    )

    emails = re.findall(
        pattern,
        text.lower()
    )

    return list(set(emails))


def risk_label(risk):

    if risk <= 25:
        return "🟢 Low"

    elif risk <= 50:
        return "🟡 Medium"

    return "🔴 High"


def clean_leads(emails):

    clean = []

    blocked = []

    domain_count = Counter()

    gmail_domains = {'gmail.com'}

    personal_domains = {
        'yahoo.com',
        'hotmail.com',
        'outlook.com',
        'icloud.com',
        'protonmail.com',
        'aol.com',
        'rediffmail.com'
    }

    for email in emails:

        email = email.strip().lower()

        if not email:
            continue

        if '@' not in email:
            continue

        if not is_valid_email(email):

            blocked.append({
                "email": email,
                "reason": "Invalid Format",
                "risk": 100
            })

            continue

        if is_test_email(email):

            blocked.append({
                "email": email,
                "reason": "Test/Placeholder Email",
                "risk": 90
            })

            continue

        domain = email.split('@')[1]

        if (
            domain in gmail_domains
            and not allow_gmail
        ):

            blocked.append({
                "email": email,
                "reason": "Gmail Blocked",
                "risk": 60
            })

            continue

        if (
            domain in personal_domains
            and not allow_personal
        ):

            blocked.append({
                "email": email,
                "reason": "Personal Email",
                "risk": 55
            })

            continue

        bounce_risk = calculate_bounce_risk(email)

        quality = 100 - bounce_risk

        if (
            india_first
            and (
                domain.endswith('.in')
                or domain.endswith('.co.in')
            )
        ):
            quality += 12

        if (
            quality >= min_quality
            and bounce_risk <= max_bounce_risk
        ):

            clean.append({
                "email": email,
                "quality_score": round(quality, 1),
                "bounce_risk": round(bounce_risk, 1),
                "risk_level": risk_label(bounce_risk),
                "domain": domain
            })

            domain_count[domain] += 1

        else:

            reason = (
                "High Bounce Risk"
                if bounce_risk > max_bounce_risk
                else "Low Quality"
            )

            blocked.append({
                "email": email,
                "reason": reason,
                "risk": round(bounce_risk, 1)
            })

    return clean, blocked, domain_count

# =====================================================
# INPUT SECTION
# =====================================================

uploaded_file = st.file_uploader(
    "📂 Upload CSV / TXT / XLSX",
    type=["csv", "txt", "xlsx"]
)

raw_text = st.text_area(
    "Or paste raw emails / text here...",
    height=180,
    placeholder="Paste leads here..."
)

# =====================================================
# PIPELINE
# =====================================================

st.markdown("""
### ⚡ Processing Pipeline

✅ Email Extraction  
✅ Syntax Validation  
✅ Disposable Detection  
✅ Bounce Risk Analysis  
✅ Quality Scoring  
✅ Domain Intelligence  
""")

# =====================================================
# RUN BUTTON
# =====================================================

run = st.button(
    "🚀 Run Clean Sequence",
    use_container_width=True
)

# =====================================================
# EXECUTION
# =====================================================

if run:

    start_time = time.time()

    with st.spinner(
        "Validating emails & calculating bounce risk..."
    ):

        progress = st.progress(0)

        for i in range(100):
            time.sleep(0.01)
            progress.progress(i + 1)

        if uploaded_file:

            if uploaded_file.name.endswith('.csv'):

                df = pd.read_csv(uploaded_file)

            elif uploaded_file.name.endswith('.xlsx'):

                df = pd.read_excel(uploaded_file)

            else:

                text = uploaded_file.read().decode(
                    'utf-8',
                    errors='ignore'
                )

                raw_emails = extract_emails(text)

                df = pd.DataFrame({
                    'email': raw_emails
                })

            if 'email' not in df.columns:

                possible = [
                    c for c in df.columns
                    if 'mail' in c.lower()
                ]

                if possible:

                    df.rename(
                        columns={
                            possible[0]: 'email'
                        },
                        inplace=True
                    )

            raw_emails = (
                df['email']
                .dropna()
                .astype(str)
                .tolist()
            )

        else:

            raw_emails = extract_emails(raw_text)

        raw_emails = list(set(raw_emails))

        clean_data, blocked_data, domain_count = (
            clean_leads(raw_emails)
        )

        process_time = round(
            time.time() - start_time,
            2
        )

        total = len(raw_emails)

        clean_count = len(clean_data)

        blocked_count = len(blocked_data)

        st.markdown("## 📊 Analytics")

        col1, col2, col3, col4 = st.columns(4)

        col1.metric(
            "📧 Total Emails",
            f"{total:,}"
        )

        col2.metric(
            "✅ Clean Leads",
            f"{clean_count:,}"
        )

        col3.metric(
            "🚫 Blocked",
            f"{blocked_count:,}"
        )

        col4.metric(
            "⚡ Processing Time",
            f"{process_time}s"
        )

        low_risk = len([
            x for x in clean_data
            if x["bounce_risk"] <= 25
        ])

        medium_risk = len([
            x for x in clean_data
            if 25 < x["bounce_risk"] <= 50
        ])

        high_risk = len([
            x for x in clean_data
            if x["bounce_risk"] > 50
        ])

        c1, c2, c3 = st.columns(3)

        c1.success(f"🟢 Low Risk: {low_risk}")
        c2.warning(f"🟡 Medium Risk: {medium_risk}")
        c3.error(f"🔴 High Risk: {high_risk}")

        india_leads = len([
            x for x in clean_data
            if x["domain"].endswith(".in")
        ])

        st.info(
            f"🇮🇳 India-focused leads found: {india_leads}"
        )

        tab1, tab2, tab3 = st.tabs([
            "✅ Clean Leads",
            "🚫 Blocked Emails",
            "🏢 Domain Analysis"
        ])

        with tab1:

            if clean_data:

                clean_df = pd.DataFrame(clean_data)

                sort_option = st.selectbox(
                    "📌 Sort Leads By",
                    [
                        "Highest Quality",
                        "Lowest Bounce Risk",
                        "Alphabetical (A-Z)",
                        "Domain A-Z"
                    ]
                )

                if sort_option == "Highest Quality":

                    clean_df = clean_df.sort_values(
                        by="quality_score",
                        ascending=False
                    )

                elif sort_option == "Lowest Bounce Risk":

                    clean_df = clean_df.sort_values(
                        by="bounce_risk",
                        ascending=True
                    )

                elif sort_option == "Alphabetical (A-Z)":

                    clean_df = clean_df.sort_values(
                        by="email",
                        ascending=True
                    )

                else:

                    clean_df = clean_df.sort_values(
                        by="domain",
                        ascending=True
                    )

                st.dataframe(
                    clean_df,
                    use_container_width=True,
                    height=550
                )

                clean_text = "\n".join(
                    clean_df["email"].tolist()
                )

                st.text_area(
                    "📋 Copy Clean Leads",
                    clean_text,
                    height=180
                )

                csv = clean_df.to_csv(
                    index=False
                )

                st.download_button(
                    "⬇ Download Clean Leads CSV",
                    csv,
                    "clean_leads.csv",
                    "text/csv",
                    use_container_width=True
                )

            else:

                st.warning(
                    "No clean leads found."
                )

        with tab2:

            if blocked_data:

                blocked_df = pd.DataFrame(
                    blocked_data
                )

                st.dataframe(
                    blocked_df,
                    use_container_width=True
                )

            else:

                st.success(
                    "All emails passed validation!"
                )

        with tab3:

            if domain_count:

                top_df = pd.DataFrame(
                    domain_count.most_common(12),
                    columns=[
                        "Domain",
                        "Count"
                    ]
                )

                st.bar_chart(
                    top_df.set_index("Domain")
                )

                st.dataframe(
                    top_df,
                    use_container_width=True
                )

        avg_quality = round(
            sum(
                x["quality_score"]
                for x in clean_data
            ) / max(len(clean_data), 1),
            1
        )

        avg_risk = round(
            sum(
                x["bounce_risk"]
                for x in clean_data
            ) / max(len(clean_data), 1),
            1
        )

        st.markdown(f"""
        <div style="
        padding:20px;
        border-radius:18px;
        background:#0f172a;
        border:1px solid #1e293b;
        margin-top:20px;
        ">

        <h3>🤖 AI Lead Intelligence Summary</h3>

        <ul>
        <li>Average Lead Quality:
        <b>{avg_quality}</b></li>

        <li>Average Bounce Risk:
        <b>{avg_risk}%</b></li>

        <li>Clean Leads:
        <b>{clean_count}</b></li>

        <li>India Domains:
        <b>{india_leads}</b></li>
        </ul>

        </div>
        """, unsafe_allow_html=True)

        st.success(f"""
✅ Processing Complete!

• Kept {clean_count} high-quality B2B leads  
• Removed {blocked_count} risky/junk emails  
• Bounce risk scoring completed  
""")

else:

    st.info(
        "📂 Upload a file or paste emails to begin."
    )

# =====================================================
# FOOTER
# =====================================================

st.caption(
    "🚀 CleanBounce AI • Email Validation + Bounce Risk Scoring"
            )
