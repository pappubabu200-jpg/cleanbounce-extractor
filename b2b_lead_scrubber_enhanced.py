import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="CleanBounce AI",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.title("🚀 CleanBounce AI")
st.caption("Smart B2B Lead Cleaning Engine")

uploaded_file = st.file_uploader(
    "📂 Upload CSV or TXT",
    type=["csv", "txt"]
)

uploaded_content = ""

if uploaded_file is not None:
    uploaded_content = uploaded_file.read().decode("utf-8", errors="ignore")

html_code = f"""
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<style>
:root {{
    --bg: #0f172a;
    --panel-bg: #1e293b;
    --text: #f8fafc;
    --muted: #94a3b8;
    --border: #334155;
    --primary: #3b82f6;
    --success: #22c55e;
    --danger: #ef4444;
}}

* {{
    box-sizing: border-box;
}}

body {{
    background: var(--bg);
    color: var(--text);
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 10px;
}}

.container {{
    background: var(--panel-bg);
    padding: 24px;
    border-radius: 14px;
    border: 1px solid var(--border);
}}

textarea {{
    width: 100%;
    height: 180px;
    background: var(--bg);
    color: var(--text);
    border: 1px solid var(--border);
    border-radius: 10px;
    padding: 14px;
    font-family: monospace;
}}

.btn {{
    padding: 12px 22px;
    border: none;
    border-radius: 10px;
    cursor: pointer;
    font-weight: bold;
    margin-top: 14px;
}}

.btn-primary {{
    background: var(--primary);
    color: white;
}}

.metrics {{
    display: grid;
    grid-template-columns: repeat(auto-fit,minmax(160px,1fr));
    gap: 14px;
    margin-top: 20px;
}}

.metric {{
    background: var(--bg);
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 18px;
    text-align: center;
}}

.metric h2 {{
    margin: 0;
    font-size: 30px;
}}

.metric p {{
    margin: 6px 0 0;
    color: var(--muted);
}}

.output {{
    margin-top: 20px;
}}

.toast {{
    position: fixed;
    right: 20px;
    bottom: 20px;
    background: var(--success);
    color: white;
    padding: 14px 20px;
    border-radius: 10px;
    z-index: 999;
}}

.top-domains {{
    margin-top: 18px;
    background: var(--bg);
    border-radius: 10px;
    padding: 14px;
    border: 1px solid var(--border);
}}

.progress {{
    width: 100%;
    height: 10px;
    background: #111827;
    border-radius: 20px;
    overflow: hidden;
    margin-top: 16px;
    display: none;
}}

.progress-bar {{
    height: 100%;
    width: 0%;
    background: var(--primary);
    transition: width 0.3s ease;
}}
</style>
</head>

<body>

<div class="container">

<h3>📥 Paste Raw Leads</h3>

<textarea id="inputText">{uploaded_content}</textarea>

<div class="progress" id="progressWrap">
    <div class="progress-bar" id="progressBar"></div>
</div>

<button class="btn btn-primary" onclick="runScrubber()">
    🚀 Run Clean Sequence
</button>

<div class="metrics">

<div class="metric">
    <h2 id="totalCount">0</h2>
    <p>Total Emails</p>
</div>

<div class="metric">
    <h2 id="cleanCount">0</h2>
    <p>Clean B2B</p>
</div>

<div class="metric">
    <h2 id="junkCount">0</h2>
    <p>Blocked</p>
</div>

<div class="metric">
    <h2 id="dupCount">0</h2>
    <p>Duplicates Removed</p>
</div>

</div>

<div class="top-domains">
    <strong>🏢 Top Domains</strong>
    <div id="topDomains">None</div>
</div>

<div class="output">
    <h3>✅ Clean Output</h3>
    <textarea id="outputText" readonly></textarea>
</div>

</div>

<script>

const BLOCKED = [
'gmail.com',
'yahoo.com',
'hotmail.com',
'outlook.com',
'icloud.com'
];

function showToast(msg) {{
    const toast = document.createElement('div');
    toast.className = 'toast';
    toast.innerText = msg;
    document.body.appendChild(toast);

    setTimeout(() => {{
        toast.remove();
    }}, 2500);
}}

function animateProgress() {{
    const wrap = document.getElementById('progressWrap');
    const bar = document.getElementById('progressBar');

    wrap.style.display = 'block';

    let width = 0;

    const interval = setInterval(() => {{
        width += 10;
        bar.style.width = width + '%';

        if(width >= 100) {{
            clearInterval(interval);

            setTimeout(() => {{
                wrap.style.display = 'none';
                bar.style.width = '0%';
            }}, 500);
        }}
    }}, 100);
}}

function runScrubber() {{

    animateProgress();

    showToast('Extracting emails...');
    
    setTimeout(() => {{
        showToast('Removing consumer domains...');
    }}, 500);

    setTimeout(() => {{
        showToast('Generating clean B2B list...');
    }}, 1000);

    const raw = document.getElementById('inputText').value;

    const regex = /[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+(?:\\.[a-zA-Z0-9-]+)+/g;

    const found = raw.match(regex) || [];

    const normalized = found.map(x => x.toLowerCase());

    const unique = [...new Set(normalized)];

    let clean = [];
    let junk = [];

    unique.forEach(email => {{

        const domain = email.split('@')[1];

        if(BLOCKED.includes(domain)) {{
            junk.push(email);
        }} else {{
            clean.push(email);
        }}

    }});

    document.getElementById('totalCount').innerText = found.length;
    document.getElementById('cleanCount').innerText = clean.length;
    document.getElementById('junkCount').innerText = junk.length;
    document.getElementById('dupCount').innerText = found.length - unique.length;

    document.getElementById('outputText').value = clean.join('\\n');

    const domainMap = {{}};

    clean.forEach(email => {{
        const d = email.split('@')[1];
        domainMap[d] = (domainMap[d] || 0) + 1;
    }});

    const top = Object.entries(domainMap)
        .sort((a,b)=>b[1]-a[1])
        .slice(0,5);

    document.getElementById('topDomains').innerText =
        top.map(d => d[0] + ' (' + d[1] + ')').join(', ');

    showToast('Clean sequence completed!');
}}

</script>

</body>
</html>
"""

components.html(html_code, height=900, scrolling=True)

st.markdown("---")
st.caption("🚀 CleanBounce AI • Smart B2B Lead Cleaning")
