import streamlit as st
import streamlit.components.v1 as components
import re
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
    background: linear-gradient(90deg,#0ea5e9,#2563eb);
    color: white;
    border-radius: 12px;
    border: none;
    padding: 12px;
    font-weight: bold;
}
.stSelectbox > div > div {
    background-color: #0f172a;
    border-color: #1e293b;
    color: #e2e8f0;
}
.stat-box {
    background: #0f172a;
    border: 1px solid #1e293b;
    border-radius: 14px;
    padding: 18px;
    text-align: center;
}
.stat-num { font-size: 32px; font-weight: 800; color: #38bdf8; }
.stat-label { font-size: 13px; color: #94a3b8; margin-top: 4px; }
.url-chip {
    display: inline-block;
    background: #1e293b;
    color: #94a3b8;
    border-radius: 8px;
    padding: 4px 10px;
    font-size: 12px;
    margin: 3px;
    font-family: monospace;
    word-break: break-all;
}
</style>
""", unsafe_allow_html=True)

# =====================================================
# SEO METADATA
# =====================================================

st.markdown("""
<head>
<meta name="description" content="Bulk URL Opener — Open hundreds of URLs at once. Free tool with deduplication, auto-https, batch opening, validation, and TXT import/export." />
<meta name="keywords" content="bulk URL opener, open multiple URLs, batch URL opener, open all links, URL tool" />
<meta property="og:title" content="Bulk URL Opener — CleanBounce AI Tools" />
<meta property="og:description" content="Paste hundreds of URLs and open them all in one click. Free, fast, no login required." />
</head>
""", unsafe_allow_html=True)

# =====================================================
# HEADER
# =====================================================

if st.button("← Back to Home", key="back_home"):
    st.switch_page("home.py")

st.markdown("""
<h1 style='font-size:42px;font-weight:800;margin-bottom:0;line-height:1.1;color:white;'>
🔗 Bulk URL Opener
</h1>
<p style='font-size:16px;color:#94a3b8;margin-top:8px;margin-bottom:24px;'>
Paste multiple URLs and open them all at once. Includes deduplication, validation, auto-https, and session saving.
</p>
""", unsafe_allow_html=True)

# =====================================================
# SIDEBAR OPTIONS
# =====================================================

st.sidebar.header("⚙️ Options")

auto_https = st.sidebar.checkbox("Auto-add https:// prefix", value=True)
remove_dupes = st.sidebar.checkbox("Remove duplicate URLs", value=True)
validate_urls = st.sidebar.checkbox("Validate URL format", value=True)
batch_size = st.sidebar.selectbox(
    "Batch size (URLs per group)",
    [5, 10, 20, 50, 100],
    index=1
)

st.sidebar.markdown("---")
st.sidebar.markdown("""
### 📋 Features
✅ Open all URLs at once  
✅ Auto-add https://  
✅ Remove duplicates  
✅ URL validation  
✅ Batch opening  
✅ TXT import/export  
✅ Session saving  
✅ Mobile friendly  
""")

# =====================================================
# URL VALIDATION HELPER
# =====================================================

URL_PATTERN = re.compile(
    r'^(https?://)?' 
    r'(([a-zA-Z0-9\-]+\.)+[a-zA-Z]{2,})'
    r'(:\d+)?'
    r'(/[^\s]*)?$'
)

def normalize_url(url: str, add_https: bool) -> str:
    url = url.strip()
    if not url:
        return ""
    if add_https and not url.startswith(('http://', 'https://')):
        url = 'https://' + url
    return url

def is_valid_url(url: str) -> bool:
    try:
        return bool(URL_PATTERN.match(url))
    except Exception:
        return False

# =====================================================
# INPUT
# =====================================================

tab_paste, tab_upload = st.tabs(["📋 Paste URLs", "📂 Upload TXT File"])

raw_input = ""

with tab_paste:
    raw_input = st.text_area(
        "Paste your URLs here (one per line)",
        height=220,
        placeholder="https://example.com\nhttps://google.com\ndomain.com/page\n..."
    )

with tab_upload:
    uploaded = st.file_uploader("Upload a .txt file with one URL per line", type=["txt"])
    if uploaded:
        raw_input = uploaded.read().decode("utf-8", errors="ignore")
        st.success(f"Loaded {len(raw_input.splitlines())} lines from file.")

# =====================================================
# PROCESS
# =====================================================

process_btn = st.button("⚡ Process & Prepare URLs", use_container_width=True)

if "processed_urls" not in st.session_state:
    st.session_state.processed_urls = []
if "invalid_urls" not in st.session_state:
    st.session_state.invalid_urls = []

if process_btn and raw_input.strip():
    lines = [l.strip() for l in raw_input.splitlines() if l.strip()]
    normalized = [normalize_url(l, auto_https) for l in lines]
    normalized = [u for u in normalized if u]

    if remove_dupes:
        seen = set()
        deduped = []
        for u in normalized:
            if u.lower() not in seen:
                seen.add(u.lower())
                deduped.append(u)
        normalized = deduped

    if validate_urls:
        valid = [u for u in normalized if is_valid_url(u)]
        invalid = [u for u in normalized if not is_valid_url(u)]
    else:
        valid = normalized
        invalid = []

    st.session_state.processed_urls = valid
    st.session_state.invalid_urls = invalid
    st.rerun()

# =====================================================
# RESULTS
# =====================================================

if st.session_state.processed_urls:
    valid_urls = st.session_state.processed_urls
    invalid_urls = st.session_state.invalid_urls
    total_batches = (len(valid_urls) + batch_size - 1) // batch_size

    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.markdown(f"""
        <div class="stat-box">
            <div class="stat-num">{len(valid_urls)}</div>
            <div class="stat-label">Valid URLs</div>
        </div>""", unsafe_allow_html=True)
    with c2:
        st.markdown(f"""
        <div class="stat-box">
            <div class="stat-num">{len(invalid_urls)}</div>
            <div class="stat-label">Invalid / Skipped</div>
        </div>""", unsafe_allow_html=True)
    with c3:
        st.markdown(f"""
        <div class="stat-box">
            <div class="stat-num">{total_batches}</div>
            <div class="stat-label">Batches of {batch_size}</div>
        </div>""", unsafe_allow_html=True)
    with c4:
        st.markdown(f"""
        <div class="stat-box">
            <div class="stat-num">{batch_size}</div>
            <div class="stat-label">URLs per Batch</div>
        </div>""", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # =====================================================
    # OPEN ALL — JavaScript Component
    # =====================================================

    urls_json = json.dumps(valid_urls)
    batch_size_js = batch_size

    html_component = f"""
    <!DOCTYPE html>
    <html>
    <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        * {{ box-sizing: border-box; margin: 0; padding: 0; }}
        body {{
            background: #050816;
            color: #e2e8f0;
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
            padding: 16px;
        }}
        .btn-row {{ display: flex; gap: 10px; flex-wrap: wrap; margin-bottom: 16px; }}
        button {{
            padding: 12px 24px;
            border: none;
            border-radius: 12px;
            font-size: 14px;
            font-weight: 700;
            cursor: pointer;
            transition: opacity 0.2s;
        }}
        button:hover {{ opacity: 0.85; }}
        #btn-open-all {{
            background: linear-gradient(90deg, #0ea5e9, #2563eb);
            color: white;
            flex: 1;
            min-width: 160px;
        }}
        #btn-open-batch {{
            background: linear-gradient(90deg, #7c3aed, #a855f7);
            color: white;
            flex: 1;
            min-width: 160px;
        }}
        #btn-reset {{
            background: #1e293b;
            color: #94a3b8;
            min-width: 100px;
        }}
        #status {{
            background: #0f172a;
            border: 1px solid #1e293b;
            border-radius: 12px;
            padding: 14px 18px;
            font-size: 13px;
            color: #94a3b8;
            min-height: 46px;
            display: flex;
            align-items: center;
            gap: 10px;
        }}
        .dot {{ 
            width: 10px; height: 10px; border-radius: 50%;
            background: #38bdf8; display: inline-block;
            animation: pulse 1.2s infinite;
        }}
        @keyframes pulse {{ 0%,100% {{ opacity:1; }} 50% {{ opacity:0.3; }} }}
        .url-list {{
            max-height: 280px;
            overflow-y: auto;
            background: #0f172a;
            border: 1px solid #1e293b;
            border-radius: 12px;
            padding: 12px;
            margin-top: 12px;
        }}
        .url-item {{
            display: flex; align-items: center; gap: 8px;
            padding: 6px 0;
            border-bottom: 1px solid #1e293b;
            font-size: 12px;
            font-family: monospace;
        }}
        .url-item:last-child {{ border-bottom: none; }}
        .url-link {{ color: #38bdf8; text-decoration: none; word-break: break-all; flex: 1; }}
        .url-link:hover {{ text-decoration: underline; }}
        .badge {{
            background: #1e293b; color: #64748b;
            border-radius: 6px; padding: 2px 8px;
            font-size: 10px; white-space: nowrap;
        }}
        .badge.opened {{ background: #064e3b; color: #34d399; }}
        .progress-bar {{
            height: 6px; background: #1e293b; border-radius: 3px;
            margin-top: 12px; overflow: hidden;
        }}
        .progress-fill {{
            height: 100%; background: linear-gradient(90deg, #0ea5e9, #7c3aed);
            border-radius: 3px; transition: width 0.3s;
            width: 0%;
        }}
        .note {{
            font-size: 11px; color: #64748b; margin-top: 10px; line-height: 1.5;
        }}
    </style>
    </head>
    <body>
    <div class="btn-row">
        <button id="btn-open-all" onclick="openAll()">🚀 Open All {len(valid_urls)} URLs</button>
        <button id="btn-open-batch" onclick="openBatch()">📦 Open Next Batch ({batch_size_js})</button>
        <button id="btn-reset" onclick="resetBatch()">↺ Reset</button>
    </div>

    <div id="status">Ready — click a button to start opening URLs.</div>
    <div class="progress-bar"><div class="progress-fill" id="progress-fill"></div></div>

    <div class="url-list" id="url-list"></div>

    <p class="note">
        ⚠️ Pop-up blockers may prevent multiple tabs from opening simultaneously.
        Use <b>Batch mode</b> to open {batch_size_js} at a time, or allow pop-ups for this site.
        All URLs open in new tabs.
    </p>

    <script>
    const URLS = {urls_json};
    const BATCH = {batch_size_js};
    let batchIndex = 0;
    const opened = new Set();

    function renderList() {{
        const el = document.getElementById('url-list');
        el.innerHTML = URLS.map((url, i) => `
            <div class="url-item">
                <span style="color:#475569;min-width:28px;font-size:11px;">#${{i+1}}</span>
                <a class="url-link" href="${{url}}" target="_blank" rel="noopener">${{url}}</a>
                <span class="badge ${{opened.has(i) ? 'opened' : ''}}" id="badge-${{i}}">
                    ${{opened.has(i) ? '✓ Opened' : 'Pending'}}
                </span>
            </div>
        `).join('');
    }}

    function setStatus(msg, active) {{
        const el = document.getElementById('status');
        el.innerHTML = active ? `<span class="dot"></span> ${{msg}}` : msg;
    }}

    function updateProgress() {{
        const pct = (opened.size / URLS.length) * 100;
        document.getElementById('progress-fill').style.width = pct + '%';
    }}

    function markOpened(i) {{
        opened.add(i);
        const badge = document.getElementById('badge-' + i);
        if (badge) {{ badge.textContent = '✓ Opened'; badge.className = 'badge opened'; }}
        updateProgress();
    }}

    async function openAll() {{
        setStatus('Opening all URLs — please allow pop-ups if prompted...', true);
        for (let i = 0; i < URLS.length; i++) {{
            window.open(URLS[i], '_blank', 'noopener');
            markOpened(i);
            await new Promise(r => setTimeout(r, 80));
        }}
        setStatus(`✅ Done! Opened ${{URLS.length}} URLs.`, false);
        batchIndex = URLS.length;
    }}

    async function openBatch() {{
        if (batchIndex >= URLS.length) {{
            setStatus('✅ All URLs have been opened! Click Reset to start again.', false);
            return;
        }}
        const end = Math.min(batchIndex + BATCH, URLS.length);
        const slice = URLS.slice(batchIndex, end);
        setStatus(`Opening batch: URLs ${{batchIndex + 1}}–${{end}}...`, true);
        for (let i = 0; i < slice.length; i++) {{
            window.open(slice[i], '_blank', 'noopener');
            markOpened(batchIndex + i);
            await new Promise(r => setTimeout(r, 80));
        }}
        batchIndex = end;
        const remaining = URLS.length - batchIndex;
        if (remaining > 0) {{
            setStatus(`✅ Batch done! ${{remaining}} URLs remaining. Click again for next batch.`, false);
        }} else {{
            setStatus('✅ All URLs opened!', false);
        }}
    }}

    function resetBatch() {{
        batchIndex = 0;
        opened.clear();
        updateProgress();
        renderList();
        setStatus('Reset. Ready to open URLs again.', false);
    }}

    renderList();

    // localStorage session save
    try {{
        localStorage.setItem('cleanbounce_urls', JSON.stringify(URLS));
    }} catch(e) {{}}
    </script>
    </body>
    </html>
    """

    components.html(html_component, height=520, scrolling=False)

    # =====================================================
    # EXPORT
    # =====================================================

    st.markdown("### 📥 Export")
    col_exp1, col_exp2 = st.columns(2)

    with col_exp1:
        txt_content = "\n".join(valid_urls)
        st.download_button(
            "⬇ Download Valid URLs (.txt)",
            txt_content,
            file_name="valid_urls.txt",
            mime="text/plain",
            use_container_width=True
        )

    with col_exp2:
        st.text_area("Copy all URLs", txt_content, height=150)

    # =====================================================
    # INVALID URLS
    # =====================================================

    if invalid_urls:
        with st.expander(f"⚠️ {len(invalid_urls)} Invalid / Skipped URLs"):
            for u in invalid_urls:
                st.markdown(f"`{u}`")

elif process_btn:
    st.warning("No URLs found. Please paste at least one URL.")

# =====================================================
# FAQ
# =====================================================

st.markdown("---")
st.markdown("""
<h2 style='color:#f8fafc;font-size:22px;font-weight:700;margin-bottom:16px;'>❓ FAQ</h2>
""", unsafe_allow_html=True)

with st.expander("Why aren't all my tabs opening?"):
    st.markdown("""
    Most browsers block multiple pop-ups by default. To allow all tabs to open:
    - Chrome: Click the pop-up blocked icon in the address bar → Allow
    - Firefox: Click "Options" on the blocked pop-up bar → Allow
    - Use **Batch mode** (smaller groups) as a workaround — it often succeeds better than opening 100 at once.
    """)

with st.expander("What does 'Auto-add https' do?"):
    st.markdown("""
    If a URL doesn't start with `http://` or `https://`, the tool automatically prepends `https://`.
    So `example.com/page` becomes `https://example.com/page`.
    """)

with st.expander("Are my URLs stored anywhere?"):
    st.markdown("""
    URLs are saved temporarily in your browser's **localStorage** for session continuity.
    Nothing is sent to any server or retained after you close the tab.
    """)

with st.expander("Can I open URLs from a file?"):
    st.markdown("""
    Yes! Switch to the **Upload TXT File** tab and upload a `.txt` file with one URL per line.
    The tool will parse and process them exactly like pasted input.
    """)

with st.expander("What's the maximum number of URLs I can open?"):
    st.markdown("""
    There's no hard limit in the tool itself, but browsers may throttle or block more than
    ~20 simultaneous tabs. Use **batch mode** with groups of 5–10 for the most reliable results.
    """)

st.caption("🔗 Bulk URL Opener • CleanBounce AI Tools")
