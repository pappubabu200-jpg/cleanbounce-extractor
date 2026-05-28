import streamlit as st
import random
import string
import pandas as pd
import json

# =====================================================
# CSS
# =====================================================

st.markdown("""
<style>
#MainMenu { visibility: hidden; }
header { visibility: hidden; }
footer { visibility: hidden; }
.main { background-color: #050816; }
.block-container { padding-top: 1rem; }
h1,h2,h3,h4 { color: #f8fafc; }
.stTextArea textarea {
    background-color: #020617;
    color: #e2e8f0;
    border-radius: 12px;
    font-family: monospace;
    font-size: 13px;
}
.stButton button {
    background: linear-gradient(90deg,#7c3aed,#a855f7);
    color: white;
    border-radius: 12px;
    border: none;
    padding: 12px;
    font-weight: bold;
}
.stat-box {
    background: #0f172a;
    border: 1px solid #1e293b;
    border-radius: 14px;
    padding: 18px;
    text-align: center;
}
.stat-num { font-size: 32px; font-weight: 800; color: #a855f7; }
.stat-label { font-size: 13px; color: #94a3b8; margin-top: 4px; }
.format-badge {
    display: inline-block;
    background: #1e1b4b;
    color: #a5b4fc;
    border-radius: 8px;
    padding: 4px 12px;
    font-size: 12px;
    margin: 3px;
    font-family: monospace;
}
</style>
""", unsafe_allow_html=True)

# =====================================================
# SEO METADATA
# =====================================================

st.markdown("""
<head>
<meta name="description" content="Fake Email Generator — Generate realistic test emails in bulk. Choose formats, custom domains, export to CSV. Free, no login required." />
<meta name="keywords" content="fake email generator, test email generator, bulk email generator, dummy email, random email generator" />
<meta property="og:title" content="Fake Email Generator — CleanBounce AI Tools" />
<meta property="og:description" content="Generate hundreds of realistic fake/test emails instantly. Multiple formats, custom domains, CSV export." />
</head>
""", unsafe_allow_html=True)

# =====================================================
# DATA
# =====================================================

FIRST_NAMES = [
    "james", "emma", "liam", "olivia", "noah", "ava", "william", "sophia",
    "benjamin", "isabella", "lucas", "mia", "mason", "amelia", "elijah",
    "harper", "oliver", "evelyn", "jacob", "abigail", "michael", "emily",
    "ethan", "elizabeth", "daniel", "mila", "alexander", "ella", "henry",
    "scarlett", "jackson", "grace", "sebastian", "chloe", "aiden", "victoria",
    "matthew", "riley", "samuel", "aria", "david", "lily", "joseph", "aubrey",
    "carter", "zoey", "owen", "penelope", "wyatt", "layla", "john", "natalie",
    "jack", "camila", "luke", "luna", "jayden", "sofia", "dylan", "ellie",
    "grayson", "stella", "levi", "zoe", "isaac", "nora", "gabriel", "hannah",
    "julian", "lily", "mateo", "addison", "anthony", "aubrey", "jaxon", "eleanor",
    "lincoln", "savannah", "ryan", "brooklyn", "asher", "anna", "christian", "claire",
    "jonathan", "audrey", "evan", "bella", "amir", "riya", "arjun", "priya",
    "rahul", "ananya", "rohit", "divya", "sanjay", "neha", "vijay", "pooja"
]

LAST_NAMES = [
    "smith", "johnson", "williams", "brown", "jones", "garcia", "miller",
    "davis", "rodriguez", "martinez", "hernandez", "lopez", "gonzalez",
    "wilson", "anderson", "thomas", "taylor", "moore", "jackson", "martin",
    "lee", "perez", "thompson", "white", "harris", "sanchez", "clark",
    "ramirez", "lewis", "robinson", "walker", "young", "allen", "king",
    "wright", "scott", "torres", "nguyen", "hill", "flores", "green",
    "adams", "nelson", "baker", "hall", "rivera", "campbell", "mitchell",
    "carter", "roberts", "sharma", "patel", "singh", "verma", "gupta",
    "kumar", "mehta", "shah", "joshi", "nair", "reddy", "rao", "iyer",
    "chatterjee", "das", "chopra", "malhotra", "kapoor", "saxena", "bose"
]

DEFAULT_DOMAINS = [
    "example.com",
    "test.com",
    "testdomain.com",
    "devmail.io",
    "staging.dev",
    "mailtest.net",
    "qamail.org",
    "demoapp.io",
    "fakeinbox.com",
    "tempdev.io",
    "mockmail.net",
    "sandbox.email"
]

FORMAT_OPTIONS = {
    "firstname.lastname@domain": lambda f, l, n: f"{f}.{l}@{{domain}}",
    "firstname_lastname@domain": lambda f, l, n: f"{f}_{l}@{{domain}}",
    "firstnamelastname@domain": lambda f, l, n: f"{f}{l}@{{domain}}",
    "f.lastname@domain": lambda f, l, n: f"{f[0]}.{l}@{{domain}}",
    "flastname@domain": lambda f, l, n: f"{f[0]}{l}@{{domain}}",
    "firstname@domain": lambda f, l, n: f"{f}@{{domain}}",
    "firstname+number@domain": lambda f, l, n: f"{f}{n}@{{domain}}",
    "firstname.lastname+number@domain": lambda f, l, n: f"{f}.{l}{n}@{{domain}}",
    "randomstring@domain": lambda f, l, n: f"{''.join(random.choices(string.ascii_lowercase, k=random.randint(6,12)))}@{{domain}}",
}

# =====================================================
# HEADER
# =====================================================

# =====================================================
# TOP NAV BAR
# =====================================================

nav1, nav2, nav3, nav_spacer = st.columns([1.4, 1.4, 1.8, 4])
with nav1:
    if st.button("📧 Lead Scrubber", use_container_width=True):
        st.switch_page("home.py")
with nav2:
    if st.button("🔗 URL Opener", use_container_width=True):
        st.switch_page("tools/bulk_url_opener.py")
with nav3:
    if st.button("✉️ Email Generator", use_container_width=True):
        st.switch_page("tools/fake_email_generator.py")

st.markdown("<hr style='border-color:#1e293b;margin:8px 0 16px 0;'>", unsafe_allow_html=True)

st.markdown("""
<h1 style='font-size:42px;font-weight:800;margin-bottom:0;line-height:1.1;color:white;'>
✉️ Fake Email Generator
</h1>
<p style='font-size:16px;color:#94a3b8;margin-top:8px;margin-bottom:24px;'>
Generate realistic test emails in bulk. Choose formats, custom domains, and export instantly.
Perfect for QA testing, staging environments, and form validation.
</p>
""", unsafe_allow_html=True)

# =====================================================
# SIDEBAR OPTIONS
# =====================================================

st.sidebar.header("⚙️ Generator Settings")

count = st.sidebar.number_input(
    "Number of emails to generate",
    min_value=1,
    max_value=10000,
    value=50,
    step=10
)

selected_formats = st.sidebar.multiselect(
    "Email formats",
    list(FORMAT_OPTIONS.keys()),
    default=["firstname.lastname@domain", "f.lastname@domain", "firstname+number@domain"]
)

domain_mode = st.sidebar.radio(
    "Domain source",
    ["Built-in test domains", "Custom domain(s)"],
    index=0
)

custom_domains_input = ""
if domain_mode == "Custom domain(s)":
    custom_domains_input = st.sidebar.text_area(
        "Enter custom domains (one per line)",
        placeholder="mycompany.com\nteam.io\nstagingapp.net",
        height=100
    )

remove_dupes = st.sidebar.checkbox("Remove duplicates", value=True)

seed_val = st.sidebar.number_input(
    "Random seed (0 = random each time)",
    min_value=0,
    max_value=99999,
    value=0
)

st.sidebar.markdown("---")
st.sidebar.markdown("""
### 📋 Features
✅ Bulk generation  
✅ 9 email formats  
✅ Custom domains  
✅ Remove duplicates  
✅ CSV & TXT export  
✅ Copy to clipboard  
✅ Reproducible seed  
""")

# =====================================================
# FORMAT PREVIEW
# =====================================================

st.markdown("#### 📐 Available Formats")
for fmt in list(FORMAT_OPTIONS.keys()):
    highlight = "background:#1e1b4b;border:1px solid #4338ca;" if fmt in selected_formats else ""
    st.markdown(
        f'<span class="format-badge" style="{highlight}">{fmt}</span>',
        unsafe_allow_html=True
    )

st.markdown("<br>", unsafe_allow_html=True)

# =====================================================
# GENERATE
# =====================================================

gen_btn = st.button("🎲 Generate Emails", use_container_width=True)

if "generated_emails" not in st.session_state:
    st.session_state.generated_emails = []

if gen_btn:
    if not selected_formats:
        st.error("Please select at least one email format.")
    else:
        if seed_val > 0:
            random.seed(seed_val)

        if domain_mode == "Custom domain(s)" and custom_domains_input.strip():
            domains = [d.strip() for d in custom_domains_input.splitlines() if d.strip()]
        else:
            domains = DEFAULT_DOMAINS

        emails = []
        attempts = 0
        max_attempts = count * 5

        while len(emails) < count and attempts < max_attempts:
            attempts += 1
            fn = random.choice(FIRST_NAMES)
            ln = random.choice(LAST_NAMES)
            num = random.randint(1, 999)
            domain = random.choice(domains)
            fmt_key = random.choice(selected_formats)
            template = FORMAT_OPTIONS[fmt_key](fn, ln, num)
            email = template.format(domain=domain)

            if remove_dupes and email in emails:
                continue
            emails.append(email)

        if remove_dupes:
            emails = list(dict.fromkeys(emails))

        st.session_state.generated_emails = emails
        st.rerun()

# =====================================================
# DISPLAY RESULTS
# =====================================================

if st.session_state.generated_emails:
    emails = st.session_state.generated_emails

    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown(f"""
        <div class="stat-box">
            <div class="stat-num">{len(emails)}</div>
            <div class="stat-label">Emails Generated</div>
        </div>""", unsafe_allow_html=True)
    with c2:
        unique_domains = len(set(e.split('@')[1] for e in emails))
        st.markdown(f"""
        <div class="stat-box">
            <div class="stat-num">{unique_domains}</div>
            <div class="stat-label">Unique Domains</div>
        </div>""", unsafe_allow_html=True)
    with c3:
        fmt_count = len(selected_formats)
        st.markdown(f"""
        <div class="stat-box">
            <div class="stat-num">{fmt_count}</div>
            <div class="stat-label">Formats Used</div>
        </div>""", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # Tabs: table, copy, export
    tab_table, tab_copy, tab_export = st.tabs([
        "📋 Email Table", "📝 Copy as Text", "⬇ Export"
    ])

    with tab_table:
        df = pd.DataFrame({
            "email": emails,
            "local": [e.split('@')[0] for e in emails],
            "domain": [e.split('@')[1] for e in emails],
        })
        sort_col = st.selectbox("Sort by", ["email", "domain", "local"])
        df = df.sort_values(by=sort_col).reset_index(drop=True)
        df.index = df.index + 1
        st.dataframe(df, use_container_width=True, height=400)

    with tab_copy:
        st.markdown("**Copy all generated emails:**")
        all_text = "\n".join(emails)
        st.text_area("Generated Emails", all_text, height=350, label_visibility="collapsed")
        st.caption(f"{len(emails)} emails • Select all (Ctrl+A) and copy")

    with tab_export:
        col_e1, col_e2 = st.columns(2)
        with col_e1:
            csv_df = pd.DataFrame({"email": emails})
            csv_data = csv_df.to_csv(index=False)
            st.download_button(
                "⬇ Download as CSV",
                csv_data,
                file_name="fake_emails.csv",
                mime="text/csv",
                use_container_width=True
            )
        with col_e2:
            st.download_button(
                "⬇ Download as TXT",
                "\n".join(emails),
                file_name="fake_emails.txt",
                mime="text/plain",
                use_container_width=True
            )

        st.markdown("**Export as JSON:**")
        json_data = json.dumps({"emails": emails, "count": len(emails)}, indent=2)
        st.download_button(
            "⬇ Download as JSON",
            json_data,
            file_name="fake_emails.json",
            mime="application/json",
            use_container_width=True
        )

# =====================================================
# FAQ
# =====================================================

st.markdown("---")
st.markdown("""
<h2 style='color:#f8fafc;font-size:22px;font-weight:700;margin-bottom:16px;'>❓ FAQ</h2>
""", unsafe_allow_html=True)

with st.expander("What are fake emails used for?"):
    st.markdown("""
    Fake/test emails are used for:
    - **QA testing** — filling forms and testing validation logic
    - **Staging environments** — populating test databases with realistic-looking data
    - **Load testing** — generating large volumes of test data
    - **Dev demos** — showing apps with realistic email addresses
    - **Email tool testing** — verifying extraction/parsing tools (like CleanBounce AI)
    """)

with st.expander("Are these emails real? Can I actually send to them?"):
    st.markdown("""
    **No — these are purely synthetic emails for testing purposes.**
    The domains used (e.g. `example.com`, `test.com`) are reserved test domains
    that do not accept mail. Do not use these for actual outreach campaigns.
    """)

with st.expander("What is the 'Random seed' option?"):
    st.markdown("""
    Setting a seed value makes the generator produce the **same list of emails** every time
    you click Generate with the same settings. This is useful for reproducible test data.
    Set it to `0` for a different random output each time.
    """)

with st.expander("Can I use my own company domain?"):
    st.markdown("""
    Yes! Switch the **Domain source** to "Custom domain(s)" in the sidebar and enter your
    own domains. This is useful for generating realistic-looking internal test data
    for your organization's staging environment.
    """)

with st.expander("How many emails can I generate at once?"):
    st.markdown("""
    You can generate up to **10,000 emails** at once. For very large sets, generation
    may take a couple of seconds. All processing is done in your Replit session — no data is sent externally.
    """)

with st.expander("How do I remove duplicates?"):
    st.markdown("""
    Enable the **"Remove duplicates"** checkbox in the sidebar (on by default).
    The generator deduplicates by exact email string before returning results.
    """)

st.caption("✉️ Fake Email Generator • CleanBounce AI Tools")
