import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="B2B Lead Scrubber Pro", 
    page_icon="📧", 
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for the Streamlit wrapper
st.markdown("""
<style>
    .main .block-container { padding-top: 1rem; }
    .stAlert { border-radius: 8px; }
    div[data-testid="stToolbar"] { display: none; }
</style>
""", unsafe_allow_html=True)

st.title("📧 B2B Lead Scrubber & Extractor Pipeline")
st.caption("Secure browser-side pipeline. Your leads list never touches external server databases.")

# Enhanced HTML component with significant improvements
html_code = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        :root {
            --bg: #0f172a;
            --panel-bg: #1e293b;
            --text: #f8fafc;
            --muted: #94a3b8;
            --border: #334155;
            --primary: #3b82f6;
            --primary-hover: #2563eb;
            --success: #22c55e;
            --danger: #ef4444;
            --warning: #f59e0b;
            --copy-btn: #475569;
            --copy-hover: #64748b;
            --accent: #8b5cf6;
        }

        * { box-sizing: border-box; }

        body {
            font-family: 'Inter', system-ui, -apple-system, sans-serif;
            background-color: var(--bg);
            color: var(--text);
            margin: 0;
            padding: 10px;
            line-height: 1.5;
        }

        .container {
            background: var(--panel-bg);
            padding: 25px;
            border-radius: 12px;
            border: 1px solid var(--border);
            max-width: 1200px;
            margin: 0 auto;
        }

        .section-block { margin-bottom: 24px; }

        .block-title {
            display: block;
            font-weight: 600;
            font-size: 13px;
            margin-bottom: 10px;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            color: var(--muted);
        }

        textarea {
            width: 100%;
            height: 160px;
            padding: 14px;
            border: 1px solid var(--border);
            border-radius: 10px;
            font-family: 'JetBrains Mono', 'Fira Code', monospace;
            font-size: 13px;
            background: var(--bg);
            color: var(--text);
            box-sizing: border-box;
            resize: vertical;
            transition: border-color 0.2s, box-shadow 0.2s;
        }

        textarea:focus { 
            outline: none; 
            border-color: var(--primary);
            box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.15);
        }

        textarea::placeholder { color: #475569; }

        .grid-filters {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
            gap: 16px;
        }

        .filter-card {
            background: var(--bg);
            padding: 16px;
            border-radius: 10px;
            border: 1px solid var(--border);
            transition: border-color 0.2s;
        }

        .filter-card:hover { border-color: var(--primary); }

        .filter-card h4 { 
            margin: 0 0 10px 0; 
            font-size: 13px; 
            color: var(--text); 
            display: flex;
            align-items: center;
            gap: 6px;
        }

        .filter-input {
            width: 100%;
            padding: 10px 12px;
            border: 1px solid var(--border);
            border-radius: 8px;
            font-size: 13px;
            box-sizing: border-box;
            background: var(--panel-bg);
            color: var(--text);
            transition: border-color 0.2s;
        }

        .filter-input:focus {
            outline: none;
            border-color: var(--primary);
        }

        .filter-hint {
            font-size: 11px;
            color: var(--muted);
            margin-top: 6px;
            display: block;
        }

        .action-bar { 
            display: flex; 
            gap: 12px; 
            flex-wrap: wrap; 
            margin: 24px 0; 
            align-items: center;
        }

        .btn {
            padding: 12px 24px;
            font-size: 13px;
            font-weight: 600;
            border-radius: 8px;
            cursor: pointer;
            border: none;
            transition: all 0.2s;
            display: inline-flex;
            align-items: center;
            gap: 8px;
            position: relative;
            overflow: hidden;
        }

        .btn:active { transform: translateY(1px); }

        .btn-primary { 
            background: linear-gradient(135deg, var(--primary), var(--primary-hover)); 
            color: white; 
            box-shadow: 0 4px 14px rgba(59, 130, 246, 0.3);
        }
        .btn-primary:hover { 
            background: linear-gradient(135deg, var(--primary-hover), #1d4ed8); 
            box-shadow: 0 6px 20px rgba(59, 130, 246, 0.4);
        }

        .btn-copy { 
            background: var(--copy-btn); 
            color: var(--text); 
        }
        .btn-copy:hover { background: var(--copy-hover); }

        .btn-secondary { 
            background: #334155; 
            color: var(--text); 
        }
        .btn-secondary:hover { background: #475569; }

        .btn-success {
            background: linear-gradient(135deg, var(--success), #16a34a);
            color: white;
            box-shadow: 0 4px 14px rgba(34, 197, 94, 0.3);
        }
        .btn-success:hover {
            background: linear-gradient(135deg, #16a34a, #15803d);
            box-shadow: 0 6px 20px rgba(34, 197, 94, 0.4);
        }

        .btn:disabled {
            opacity: 0.5;
            cursor: not-allowed;
            transform: none !important;
        }

        .metrics-container { 
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(140px, 1fr));
            gap: 16px; 
            margin-bottom: 24px; 
        }

        .metric-card {
            padding: 16px;
            border-radius: 10px;
            text-align: center;
            border: 1px solid var(--border);
            transition: transform 0.2s;
        }
        .metric-card:hover { transform: translateY(-2px); }

        .metric-card.clean { background: linear-gradient(135deg, #052e16, #064e3b); border-color: #14532d; }
        .metric-card.junk { background: linear-gradient(135deg, #450a0a, #7f1d1d); border-color: #991b1b; }
        .metric-card.total { background: linear-gradient(135deg, #1e3a5f, #1e40af); border-color: #3b82f6; }
        .metric-card.rate { background: linear-gradient(135deg, #3f1d5c, #6b21a8); border-color: #8b5cf6; }

        .metric-label { display: block; font-size: 11px; color: var(--muted); margin-bottom: 4px; }
        .metric-value { font-size: 26px; font-weight: 700; }
        .metric-card.clean .metric-value { color: var(--success); }
        .metric-card.junk .metric-value { color: var(--danger); }
        .metric-card.total .metric-value { color: #60a5fa; }
        .metric-card.rate .metric-value { color: #c4b5fd; }

        .output-wrapper {
            position: relative;
        }

        .output-actions {
            position: absolute;
            top: 8px;
            right: 8px;
            display: flex;
            gap: 6px;
            opacity: 0;
            transition: opacity 0.2s;
        }

        .output-wrapper:hover .output-actions { opacity: 1; }

        .icon-btn {
            background: rgba(30, 41, 59, 0.9);
            border: 1px solid var(--border);
            color: var(--muted);
            padding: 6px 10px;
            border-radius: 6px;
            cursor: pointer;
            font-size: 12px;
            transition: all 0.2s;
        }
        .icon-btn:hover { 
            background: var(--primary); 
            color: white; 
            border-color: var(--primary);
        }

        .progress-bar {
            width: 100%;
            height: 4px;
            background: var(--border);
            border-radius: 2px;
            margin-top: 12px;
            overflow: hidden;
            display: none;
        }

        .progress-bar.active { display: block; }

        .progress-fill {
            height: 100%;
            background: linear-gradient(90deg, var(--primary), var(--accent));
            border-radius: 2px;
            width: 0%;
            transition: width 0.3s ease;
        }

        .toast-container {
            position: fixed;
            bottom: 24px;
            right: 24px;
            display: flex;
            flex-direction: column;
            gap: 8px;
            z-index: 9999;
        }

        .toast {
            background: var(--success);
            color: white;
            padding: 14px 24px;
            border-radius: 10px;
            font-size: 14px;
            font-weight: 600;
            box-shadow: 0 8px 24px rgba(0,0,0,0.3);
            animation: slideIn 0.3s ease, fadeOut 0.3s ease 2.7s forwards;
            display: flex;
            align-items: center;
            gap: 8px;
        }

        .toast.error { background: var(--danger); }
        .toast.info { background: var(--primary); }

        @keyframes slideIn {
            from { transform: translateX(100%); opacity: 0; }
            to { transform: translateX(0); opacity: 1; }
        }

        @keyframes fadeOut {
            from { opacity: 1; }
            to { opacity: 0; }
        }

        .stats-detail {
            background: var(--bg);
            border-radius: 8px;
            padding: 12px 16px;
            margin-top: 12px;
            font-size: 12px;
            color: var(--muted);
            display: none;
        }

        .stats-detail.visible { display: block; }

        .stats-detail span { color: var(--text); font-weight: 600; }

        .toggle-advanced {
            background: none;
            border: none;
            color: var(--primary);
            font-size: 12px;
            cursor: pointer;
            padding: 4px 0;
            margin-top: 8px;
            display: flex;
            align-items: center;
            gap: 4px;
        }

        .toggle-advanced:hover { text-decoration: underline; }

        .advanced-panel {
            display: none;
            margin-top: 12px;
            padding-top: 12px;
            border-top: 1px solid var(--border);
        }

        .advanced-panel.open { display: block; }

        .checkbox-group {
            display: flex;
            flex-wrap: wrap;
            gap: 12px;
            margin-top: 8px;
        }

        .checkbox-item {
            display: flex;
            align-items: center;
            gap: 6px;
            font-size: 13px;
            color: var(--text);
            cursor: pointer;
        }

        .checkbox-item input[type="checkbox"] {
            width: 16px;
            height: 16px;
            accent-color: var(--primary);
            cursor: pointer;
        }

        .tag-pill {
            display: inline-flex;
            align-items: center;
            gap: 4px;
            padding: 2px 8px;
            border-radius: 4px;
            font-size: 11px;
            font-weight: 600;
            margin-left: 6px;
        }
        .tag-pill.blocked { background: rgba(239, 68, 68, 0.15); color: #fca5a5; }
        .tag-pill.start { background: rgba(245, 158, 11, 0.15); color: #fcd34d; }
        .tag-pill.contains { background: rgba(139, 92, 246, 0.15); color: #c4b5fd; }
        .tag-pill.invalid { background: rgba(148, 163, 184, 0.15); color: #cbd5e1; }

        .junk-preview {
            max-height: 120px;
            overflow-y: auto;
            background: var(--bg);
            border-radius: 8px;
            padding: 10px;
            margin-top: 12px;
            font-family: monospace;
            font-size: 12px;
            color: var(--danger);
            display: none;
        }

        .junk-preview.visible { display: block; }

        .junk-preview-item {
            padding: 2px 0;
            border-bottom: 1px solid rgba(239, 68, 68, 0.1);
        }

        .section-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 10px;
        }

        .clear-btn {
            background: none;
            border: none;
            color: var(--muted);
            font-size: 12px;
            cursor: pointer;
            padding: 4px 8px;
            border-radius: 4px;
            transition: all 0.2s;
        }
        .clear-btn:hover { color: var(--danger); background: rgba(239, 68, 68, 0.1); }

        ::-webkit-scrollbar { width: 8px; height: 8px; }
        ::-webkit-scrollbar-track { background: var(--bg); }
        ::-webkit-scrollbar-thumb { background: var(--border); border-radius: 4px; }
        ::-webkit-scrollbar-thumb:hover { background: #475569; }
    </style>
</head>
<body>

<div class="container">
    <div class="section-block">
        <div class="section-header">
            <label class="block-title">1. Raw Input String Data</label>
            <button class="clear-btn" onclick="clearInput()">🗑️ Clear</button>
        </div>
        <textarea id="inputText" placeholder="Paste text blocks containing emails like: jdoe@company.com, test@gmail.com, userxxxx@yahoo.com...&#10;&#10;Supports: comma-separated, newline-separated, or mixed formats."></textarea>
        <div class="progress-bar" id="progressBar">
            <div class="progress-fill" id="progressFill"></div>
        </div>
    </div>

    <div class="section-block">
        <label class="block-title">2. Lead Scrubbing Automation Matrix</label>
        <div class="grid-filters">
            <div class="filter-card">
                <h4>🚫 Blocked Domains</h4>
                <input type="text" id="blockedDomains" class="filter-input" value="gmail.com, yahoo.com, hotmail.com, outlook.com, aol.com, icloud.com, protonmail.com, mail.ru">
                <span class="filter-hint">Comma-separated list of domains to reject</span>
            </div>
            <div class="filter-card">
                <h4>🛑 Usernames Starting With</h4>
                <input type="text" id="startsWithFilters" class="filter-input" value="first, last, jdoe, doe, flast, jane, john, admin, info, support, sales, marketing, noreply, no-reply">
                <span class="filter-hint">Reject emails where local part starts with these</span>
            </div>
            <div class="filter-card">
                <h4>⚠️ Strings Containing</h4>
                <input type="text" id="containsFilters" class="filter-input" value="xxxx, test, example, fake, temp, tempmail, trash">
                <span class="filter-hint">Reject emails containing any of these substrings</span>
            </div>
        </div>

        <button class="toggle-advanced" onclick="toggleAdvanced()">
            <span id="advIcon">▶</span> Advanced Options
        </button>

        <div class="advanced-panel" id="advancedPanel">
            <div class="checkbox-group">
                <label class="checkbox-item">
                    <input type="checkbox" id="strictMode" checked>
                    Strict email validation (RFC-like)
                </label>
                <label class="checkbox-item">
                    <input type="checkbox" id="blockFreeProviders" checked>
                    Auto-block known free providers
                </label>
                <label class="checkbox-item">
                    <input type="checkbox" id="caseSensitive" checked>
                    Case-insensitive matching
                </label>
                <label class="checkbox-item">
                    <input type="checkbox" id="showJunkDetails">
                    Show rejected items
                </label>
            </div>
        </div>
    </div>

    <div class="action-bar">
        <button class="btn btn-primary" id="runBtn" onclick="runScrubbingPipeline()">
            ▶ Run Clean Sequence
        </button>
        <button class="btn btn-copy" id="copyBtn" onclick="copyToClipboard()" disabled>
            📋 Copy Clean List
        </button>
        <button class="btn btn-secondary" id="csvBtn" onclick="exportCSV()" disabled>
            📄 Download CSV
        </button>
        <button class="btn btn-success" id="jsonBtn" onclick="exportJSON()" disabled>
            📦 Export JSON
        </button>
    </div>

    <div class="metrics-container">
        <div class="metric-card total">
            <span class="metric-label">Total Extracted</span>
            <span id="totalCount" class="metric-value">0</span>
        </div>
        <div class="metric-card clean">
            <span class="metric-label">Clean B2B Leads</span>
            <span id="cleanCount" class="metric-value">0</span>
        </div>
        <div class="metric-card junk">
            <span class="metric-label">Junk Thrown Away</span>
            <span id="junkCount" class="metric-value">0</span>
        </div>
        <div class="metric-card rate">
            <span class="metric-label">Clean Rate</span>
            <span id="cleanRate" class="metric-value">0%</span>
        </div>
    </div>

    <div class="stats-detail" id="statsDetail">
        Unique emails found: <span id="uniqueCount">0</span> | 
        Duplicates removed: <span id="dupCount">0</span> | 
        Processing time: <span id="procTime">0ms</span>
    </div>

    <div class="junk-preview" id="junkPreview"></div>

    <div class="section-block output-wrapper">
        <div class="section-header">
            <label class="block-title">3. Verified Clean Output List</label>
            <div class="output-actions">
                <button class="icon-btn" onclick="selectAllOutput()" title="Select All">✓</button>
                <button class="icon-btn" onclick="clearOutput()" title="Clear">✕</button>
            </div>
        </div>
        <textarea id="outputText" readonly placeholder="Cleaned workspace output records map here..."></textarea>
    </div>
</div>

<div class="toast-container" id="toastContainer"></div>

<script>
// Known free email providers for auto-blocking
const FREE_PROVIDERS = [
    'gmail.com', 'yahoo.com', 'hotmail.com', 'outlook.com', 'aol.com',
    'icloud.com', 'me.com', 'mac.com', 'protonmail.com', 'proton.me',
    'zoho.com', 'yandex.com', 'mail.ru', 'gmx.com', 'gmx.net',
    'live.com', 'msn.com', 'qq.com', '163.com', '126.com',
    'sina.com', 'sohu.com', 'foxmail.com', 'ymail.com', 'rocketmail.com'
];

function showToast(message, type = 'success') {
    const container = document.getElementById('toastContainer');
    const toast = document.createElement('div');
    toast.className = `toast ${type}`;

    const icons = { success: '✓', error: '✗', info: 'ℹ' };
    toast.innerHTML = `<span>${icons[type] || '✓'}</span> ${message}`;

    container.appendChild(toast);
    setTimeout(() => toast.remove(), 3000);
}

function setProgress(percent) {
    const bar = document.getElementById('progressBar');
    const fill = document.getElementById('progressFill');
    bar.classList.add('active');
    fill.style.width = percent + '%';
    if (percent >= 100) setTimeout(() => bar.classList.remove('active'), 500);
}

function toggleAdvanced() {
    const panel = document.getElementById('advancedPanel');
    const icon = document.getElementById('advIcon');
    panel.classList.toggle('open');
    icon.textContent = panel.classList.contains('open') ? '▼' : '▶';
}

function clearInput() {
    document.getElementById('inputText').value = '';
    document.getElementById('inputText').focus();
}

function clearOutput() {
    document.getElementById('outputText').value = '';
    updateButtonStates();
}

function selectAllOutput() {
    const output = document.getElementById('outputText');
    if (!output.value) return;
    output.select();
    output.setSelectionRange(0, 99999);
}

function updateButtonStates() {
    const hasOutput = !!document.getElementById('outputText').value;
    document.getElementById('copyBtn').disabled = !hasOutput;
    document.getElementById('csvBtn').disabled = !hasOutput;
    document.getElementById('jsonBtn').disabled = !hasOutput;
}

function validateEmail(email) {
    // More robust regex - closer to RFC 5322 but practical
    const strictMode = document.getElementById('strictMode').checked;
    if (!strictMode) {
        return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);
    }
    // Stricter validation
    const re = /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$/;
    return re.test(email) && email.length <= 254;
}

function getRejectionReason(email, username, domain, domainsToBlock, startsWithArr, containsArr) {
    if (!validateEmail(email)) return { reason: 'invalid', tag: '<span class="tag-pill invalid">INVALID</span>' };

    const isDomainBlocked = domainsToBlock.some(d => domain === d || domain.endsWith('.' + d));
    if (isDomainBlocked) return { reason: 'domain', tag: '<span class="tag-pill blocked">DOMAIN</span>' };

    const matchesStart = startsWithArr.some(p => username.startsWith(p));
    if (matchesStart) return { reason: 'start', tag: '<span class="tag-pill start">PREFIX</span>' };

    const matchesContains = containsArr.some(c => email.includes(c));
    if (matchesContains) return { reason: 'contains', tag: '<span class="tag-pill contains">CONTAINS</span>' };

    return null;
}

function runScrubbingPipeline() {
    const startTime = performance.now();
    const rawData = document.getElementById('inputText').value;

    if (!rawData.trim()) {
        showToast('Please paste some data first!', 'error');
        return;
    }

    setProgress(20);

    // Improved regex - handles more edge cases
    const emailRegex = /[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)+/g;
    const matches = rawData.match(emailRegex) || [];

    setProgress(40);

    const caseInsensitive = document.getElementById('caseSensitive').checked;

    // Normalize and deduplicate
    let normalized = matches.map(e => {
        let email = e.trim().replace(/\.+$/, '').replace(/^\./, '');
        if (caseInsensitive) email = email.toLowerCase();
        return email;
    }).filter(e => e.includes('@') && e.length > 3);

    const uniqueEmails = [...new Set(normalized)];
    const dupCount = normalized.length - uniqueEmails.length;

    setProgress(60);

    // Parse filters
    let domainsToBlock = document.getElementById('blockedDomains').value
        .split(',').map(s => s.trim().toLowerCase()).filter(Boolean);

    if (document.getElementById('blockFreeProviders').checked) {
        domainsToBlock = [...new Set([...domainsToBlock, ...FREE_PROVIDERS])];
    }

    const startsWithArr = document.getElementById('startsWithFilters').value
        .toLowerCase().split(',').map(s => s.trim()).filter(Boolean);
    const containsArr = document.getElementById('containsFilters').value
        .toLowerCase().split(',').map(s => s.trim()).filter(Boolean);

    setProgress(80);

    let cleanList = [];
    let junkList = [];

    uniqueEmails.forEach(email => {
        const atIndex = email.lastIndexOf('@');
        if (atIndex === -1 || atIndex === 0 || atIndex === email.length - 1) {
            junkList.push({ email, reason: 'invalid', tag: '<span class="tag-pill invalid">INVALID</span>' });
            return;
        }

        const username = email.substring(0, atIndex);
        const domain = email.substring(atIndex + 1);

        const rejection = getRejectionReason(email, username, domain, domainsToBlock, startsWithArr, containsArr);

        if (rejection) {
            junkList.push({ email, ...rejection });
        } else {
            cleanList.push(email);
        }
    });

    cleanList.sort((a, b) => {
        const domainA = a.split('@')[1] || '';
        const domainB = b.split('@')[1] || '';
        if (domainA !== domainB) return domainA.localeCompare(domainB);
        return a.localeCompare(b);
    });

    setProgress(100);

    // Update UI
    document.getElementById('outputText').value = cleanList.join('\n');
    document.getElementById('totalCount').innerText = normalized.length;
    document.getElementById('cleanCount').innerText = cleanList.length;
    document.getElementById('junkCount').innerText = junkList.length;
    document.getElementById('uniqueCount').innerText = uniqueEmails.length;
    document.getElementById('dupCount').innerText = dupCount;
    document.getElementById('procTime').innerText = Math.round(performance.now() - startTime) + 'ms';

    const totalProcessed = cleanList.length + junkList.length;
    const rate = totalProcessed > 0 ? Math.round((cleanList.length / totalProcessed) * 100) : 0;
    document.getElementById('cleanRate').innerText = rate + '%';

    document.getElementById('statsDetail').classList.add('visible');

    // Junk preview
    const junkPreview = document.getElementById('junkPreview');
    if (document.getElementById('showJunkDetails').checked && junkList.length > 0) {
        junkPreview.innerHTML = junkList.slice(0, 50).map(j => 
            `<div class="junk-preview-item">${j.tag} ${j.email}</div>`
        ).join('') + (junkList.length > 50 ? `<div style="color:var(--muted)">... and ${junkList.length - 50} more</div>` : '');
        junkPreview.classList.add('visible');
    } else {
        junkPreview.classList.remove('visible');
    }

    updateButtonStates();

    if (cleanList.length > 0) {
        showToast(`Found ${cleanList.length} clean B2B leads!`);
    } else if (junkList.length > 0) {
        showToast('All emails were filtered out. Adjust your filters.', 'info');
    } else {
        showToast('No emails found in input.', 'error');
    }
}

function copyToClipboard() {
    const outputField = document.getElementById('outputText');
    if (!outputField.value) return;

    navigator.clipboard.writeText(outputField.value).then(() => {
        showToast('Copied to clipboard!');
    }).catch(err => {
        // Fallback
        outputField.select();
        outputField.setSelectionRange(0, 99999);
        document.execCommand('copy');
        showToast('Copied to clipboard!');
    });
}

function exportCSV() {
    const val = document.getElementById('outputText').value;
    if (!val) return;

    const lines = val.split('\n').filter(l => l.trim());
    const timestamp = new Date().toISOString().slice(0, 19).replace(/:/g, '-');

    // Proper CSV escaping
    const csvRows = lines.map(line => {
        const escaped = line.replace(/"/g, '""');
        return `"${escaped}"`;
    });

    const csvContent = "\uFEFFEmail Address,Domain,Username\n" + 
        lines.map(line => {
            const atIdx = line.lastIndexOf('@');
            const user = line.substring(0, atIdx);
            const domain = line.substring(atIdx + 1);
            return `"${line}","${domain}","${user}"`;
        }).join("\n");

    const blob = new Blob([csvContent], { type: 'text/csv;charset=utf-8;' });
    const link = document.createElement("a");
    link.href = URL.createObjectURL(blob);
    link.setAttribute("download", `cleanbounce_leads_${timestamp}.csv`);
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
    URL.revokeObjectURL(link.href);

    showToast('CSV downloaded!');
}

function exportJSON() {
    const val = document.getElementById('outputText').value;
    if (!val) return;

    const lines = val.split('\n').filter(l => l.trim());
    const timestamp = new Date().toISOString().slice(0, 19).replace(/:/g, '-');

    const data = lines.map(line => {
        const atIdx = line.lastIndexOf('@');
        return {
            email: line,
            username: line.substring(0, atIdx),
            domain: line.substring(atIdx + 1),
            extracted_at: new Date().toISOString()
        };
    });

    const jsonContent = JSON.stringify({
        metadata: {
            exported_at: new Date().toISOString(),
            total_records: data.length,
            tool: 'B2B Lead Scrubber Pro'
        },
        leads: data
    }, null, 2);

    const blob = new Blob([jsonContent], { type: 'application/json' });
    const link = document.createElement("a");
    link.href = URL.createObjectURL(blob);
    link.setAttribute("download", `cleanbounce_leads_${timestamp}.json`);
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
    URL.revokeObjectURL(link.href);

    showToast('JSON exported!');
}

// Keyboard shortcuts
document.addEventListener('keydown', function(e) {
    if (e.ctrlKey || e.metaKey) {
        if (e.key === 'Enter') {
            e.preventDefault();
            runScrubbingPipeline();
        } else if (e.key === 'c' && document.activeElement.id === 'outputText') {
            // Let native copy work
        }
    }
});

// Auto-run on paste with debounce
let pasteTimeout;
document.getElementById('inputText').addEventListener('paste', function() {
    clearTimeout(pasteTimeout);
    pasteTimeout = setTimeout(() => {
        if (document.getElementById('inputText').value.trim().length > 50) {
            // Optional: auto-run on large pastes
            // runScrubbingPipeline();
        }
    }, 300);
});
</script>
</body>
</html>
"""

components.html(html_code, height=800, scrolling=True)

st.markdown("---")
st.caption("💡 **Tip:** Use `Ctrl+Enter` to run the pipeline quickly. All processing happens in your browser — no data leaves your machine.")
