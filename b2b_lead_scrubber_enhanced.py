import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="B2B Lead Scrubber - India & Sales Edition",
    page_icon="🇮🇳",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.title("🇮🇳 B2B Lead Scrubber - India & Sales Edition")
st.caption("Keeps Indian business domains + sales/marketing emails. Blocks consumer & junk only.")

html_code = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<style>
:root {
    --bg: #0f172a; --panel-bg: #1e293b; --text: #f8fafc; --muted: #94a3b8;
    --border: #334155; --primary: #3b82f6; --primary-hover: #2563eb;
    --success: #22c55e; --danger: #ef4444; --warning: #f59e0b;
    --copy-btn: #475569; --copy-hover: #64748b; --accent: #8b5cf6;
    --india: #ff9933; --sales: #10b981;
}
* { box-sizing: border-box; }
body { font-family: 'Segoe UI', system-ui, sans-serif; background: var(--bg); color: var(--text); margin: 0; padding: 10px; }
.container { background: var(--panel-bg); padding: 25px; border-radius: 12px; border: 1px solid var(--border); max-width: 1200px; margin: 0 auto; }
.section-block { margin-bottom: 24px; }
.block-title { display: block; font-weight: 600; font-size: 13px; margin-bottom: 10px; text-transform: uppercase; letter-spacing: 0.5px; color: var(--muted); }
textarea { width: 100%; height: 160px; padding: 14px; border: 1px solid var(--border); border-radius: 10px; font-family: 'Consolas', monospace; font-size: 13px; background: var(--bg); color: var(--text); box-sizing: border-box; resize: vertical; }
textarea:focus { outline: none; border-color: var(--primary); box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.15); }
.grid-filters { display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 16px; }
.filter-card { background: var(--bg); padding: 16px; border-radius: 10px; border: 1px solid var(--border); }
.filter-card h4 { margin: 0 0 10px 0; font-size: 13px; color: var(--text); display: flex; align-items: center; gap: 6px; }
.filter-input { width: 100%; padding: 10px 12px; border: 1px solid var(--border); border-radius: 8px; font-size: 13px; background: var(--panel-bg); color: var(--text); }
.filter-hint { font-size: 11px; color: var(--muted); margin-top: 6px; display: block; }
.action-bar { display: flex; gap: 12px; flex-wrap: wrap; margin: 24px 0; }
.btn { padding: 12px 24px; font-size: 13px; font-weight: 600; border-radius: 8px; cursor: pointer; border: none; transition: all 0.2s; }
.btn-primary { background: linear-gradient(135deg, var(--primary), var(--primary-hover)); color: white; }
.btn-primary:hover { background: linear-gradient(135deg, var(--primary-hover), #1d4ed8); }
.btn-copy { background: var(--copy-btn); color: var(--text); }
.btn-copy:hover { background: var(--copy-hover); }
.btn-secondary { background: #334155; color: var(--text); }
.btn-success { background: linear-gradient(135deg, var(--success), #16a34a); color: white; }
.btn:disabled { opacity: 0.5; cursor: not-allowed; }
.metrics-container { display: grid; grid-template-columns: repeat(auto-fit, minmax(140px, 1fr)); gap: 16px; margin-bottom: 24px; }
.metric-card { padding: 16px; border-radius: 10px; text-align: center; border: 1px solid var(--border); }
.metric-card.clean { background: linear-gradient(135deg, #052e16, #064e3b); border-color: #14532d; }
.metric-card.india { background: linear-gradient(135deg, #7c2d12, #9a3412); border-color: #ea580c; }
.metric-card.sales { background: linear-gradient(135deg, #064e3b, #065f46); border-color: #10b981; }
.metric-card.junk { background: linear-gradient(135deg, #450a0a, #7f1d1d); border-color: #991b1b; }
.metric-card.total { background: linear-gradient(135deg, #1e3a5f, #1e40af); border-color: #3b82f6; }
.metric-label { display: block; font-size: 11px; color: var(--muted); margin-bottom: 4px; }
.metric-value { font-size: 26px; font-weight: 700; }
.metric-card.clean .metric-value { color: var(--success); }
.metric-card.india .metric-value { color: #fdba74; }
.metric-card.sales .metric-value { color: #6ee7b7; }
.metric-card.junk .metric-value { color: var(--danger); }
.metric-card.total .metric-value { color: #60a5fa; }
.toast-container { position: fixed; bottom: 24px; right: 24px; display: flex; flex-direction: column; gap: 8px; z-index: 9999; }
.toast { background: var(--success); color: white; padding: 14px 24px; border-radius: 10px; font-size: 14px; font-weight: 600; box-shadow: 0 8px 24px rgba(0,0,0,0.3); animation: slideIn 0.3s ease, fadeOut 0.3s ease 2.7s forwards; }
.toast.error { background: var(--danger); }
.toast.info { background: var(--primary); }
@keyframes slideIn { from { transform: translateX(100%); opacity: 0; } to { transform: translateX(0); opacity: 1; } }
@keyframes fadeOut { from { opacity: 1; } to { opacity: 0; } }
.stats-detail { background: var(--bg); border-radius: 8px; padding: 12px 16px; margin-top: 12px; font-size: 12px; color: var(--muted); display: none; }
.stats-detail.visible { display: block; }
.stats-detail span { color: var(--text); font-weight: 600; }
.tag-pill { display: inline-flex; align-items: center; gap: 4px; padding: 2px 8px; border-radius: 4px; font-size: 11px; font-weight: 600; margin-left: 6px; }
.tag-pill.india { background: rgba(255, 153, 51, 0.2); color: #fdba74; }
.tag-pill.sales { background: rgba(16, 185, 129, 0.2); color: #6ee7b7; }
.tag-pill.blocked { background: rgba(239, 68, 68, 0.15); color: #fca5a5; }
.tag-pill.invalid { background: rgba(148, 163, 184, 0.15); color: #cbd5e1; }
.junk-preview { max-height: 120px; overflow-y: auto; background: var(--bg); border-radius: 8px; padding: 10px; margin-top: 12px; font-family: monospace; font-size: 12px; color: var(--danger); display: none; }
.junk-preview.visible { display: block; }
.junk-preview-item { padding: 2px 0; border-bottom: 1px solid rgba(239, 68, 68, 0.1); }
.section-header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px; }
.clear-btn { background: none; border: none; color: var(--muted); font-size: 12px; cursor: pointer; padding: 4px 8px; border-radius: 4px; }
.clear-btn:hover { color: var(--danger); background: rgba(239, 68, 68, 0.1); }
</style>
</head>
<body>

<div class="container">
    <div class="section-block">
        <div class="section-header">
            <label class="block-title">1. Raw Input String Data</label>
            <button class="clear-btn" onclick="clearInput()">Clear</button>
        </div>
        <textarea id="inputText" placeholder="Paste text blocks containing emails...&#10;&#10;Example: sales@tcs.com, rajesh@flipkart.co.in, marketing@zoho.com, test@gmail.com"></textarea>
    </div>

    <div class="section-block">
        <label class="block-title">2. Lead Scrubbing Automation Matrix</label>
        <div class="grid-filters">
            <div class="filter-card">
                <h4>🚫 Blocked Consumer Domains</h4>
                <input type="text" id="blockedDomains" class="filter-input" value="gmail.com, yahoo.com, hotmail.com, outlook.com, aol.com, icloud.com, protonmail.com, mail.ru, yandex.com, gmx.com, live.com, msn.com, qq.com, 163.com">
                <span class="filter-hint">Only consumer/free domains blocked. Business domains pass.</span>
            </div>
            <div class="filter-card">
                <h4>🛑 Blocked Usernames</h4>
                <input type="text" id="startsWithFilters" class="filter-input" value="test, fake, temp, tempmail, trash, noreply, no-reply, first, last, jdoe, doe, flast, jane, john, admin, info, support">
                <span class="filter-hint">SALES & MARKETING usernames are KEPT. Only junk prefixes blocked.</span>
            </div>
            <div class="filter-card">
                <h4>⚠️ Strings Containing</h4>
                <input type="text" id="containsFilters" class="filter-input" value="xxxx, example, fakeemail, tempmail, trashmail, guerrillamail">
                <span class="filter-hint">Reject emails containing fake/temp substrings</span>
            </div>
        </div>
    </div>

    <div class="action-bar">
        <button class="btn btn-primary" onclick="runScrubbingPipeline()">
            Run Clean Sequence
        </button>
        <button class="btn btn-copy" id="copyBtn" onclick="copyToClipboard()" disabled>
            Copy Clean List
        </button>
        <button class="btn btn-secondary" id="csvBtn" onclick="exportCSV()" disabled>
            Download CSV
        </button>
        <button class="btn btn-success" id="jsonBtn" onclick="exportJSON()" disabled>
            Export JSON
        </button>
    </div>

    <div class="metrics-container">
        <div class="metric-card total">
            <span class="metric-label">Total Extracted</span>
            <span id="totalCount" class="metric-value">0</span>
        </div>
        <div class="metric-card india">
            <span class="metric-label">🇮🇳 Indian Business</span>
            <span id="indiaCount" class="metric-value">0</span>
        </div>
        <div class="metric-card sales">
            <span class="metric-label">💼 Sales/Marketing</span>
            <span id="salesCount" class="metric-value">0</span>
        </div>
        <div class="metric-card clean">
            <span class="metric-label">Other B2B Clean</span>
            <span id="cleanCount" class="metric-value">0</span>
        </div>
        <div class="metric-card junk">
            <span class="metric-label">Junk Thrown Away</span>
            <span id="junkCount" class="metric-value">0</span>
        </div>
    </div>

    <div class="stats-detail" id="statsDetail">
        Unique emails found: <span id="uniqueCount">0</span> | 
        Duplicates removed: <span id="dupCount">0</span> | 
        Processing time: <span id="procTime">0ms</span>
    </div>

    <div class="junk-preview" id="junkPreview"></div>

    <div class="section-block">
        <div class="section-header">
            <label class="block-title">3. Verified Clean Output List</label>
        </div>
        <textarea id="outputText" readonly placeholder="Cleaned workspace output records map here..."></textarea>
    </div>
</div>

<div class="toast-container" id="toastContainer"></div>

<script>
const FREE_PROVIDERS = [
    'gmail.com', 'yahoo.com', 'hotmail.com', 'outlook.com', 'aol.com',
    'icloud.com', 'me.com', 'mac.com', 'protonmail.com', 'proton.me',
    'zoho.com', 'yandex.com', 'mail.ru', 'gmx.com', 'gmx.net',
    'live.com', 'msn.com', 'qq.com', '163.com', '126.com',
    'sina.com', 'sohu.com', 'foxmail.com', 'ymail.com', 'rocketmail.com'
];

const INDIAN_TLDS = ['.in', '.co.in', '.ac.in', '.edu.in', '.gov.in', '.nic.in', '.org.in', '.net.in', '.res.in', '.gen.in', '.firm.in', '.ind.in'];
const SALES_PREFIXES = ['sales', 'marketing', 'bizdev', 'business', 'partnerships', 'affiliates', 'growth', 'revenue', 'commercial', 'bd', 'sdr', 'bdr', 'account', 'enterprise', 'channel', 'reseller', 'distributor'];

function showToast(message, type) {
    type = type || 'success';
    var container = document.getElementById('toastContainer');
    var toast = document.createElement('div');
    toast.className = 'toast ' + type;
    var icons = { success: 'OK', error: 'ERR', info: 'INFO' };
    toast.innerHTML = '<span>' + (icons[type] || 'OK') + '</span> ' + message;
    container.appendChild(toast);
    setTimeout(function() { toast.remove(); }, 3000);
}

function clearInput() {
    document.getElementById('inputText').value = '';
    document.getElementById('inputText').focus();
}

function updateButtonStates() {
    var hasOutput = !!document.getElementById('outputText').value;
    document.getElementById('copyBtn').disabled = !hasOutput;
    document.getElementById('csvBtn').disabled = !hasOutput;
    document.getElementById('jsonBtn').disabled = !hasOutput;
}

function validateEmail(email) {
    return /^[^\\s@]+@[^\\s@]+\\.[^\\s@]+$/.test(email) && email.length <= 254;
}

function isIndianDomain(domain) {
    return INDIAN_TLDS.some(function(tld) { return domain.endsWith(tld); });
}

function isSalesEmail(username) {
    return SALES_PREFIXES.some(function(prefix) { return username === prefix || username.startsWith(prefix + '.'); });
}

function getRejectionReason(email, username, domain, domainsToBlock, startsWithArr, containsArr) {
    if (!validateEmail(email)) {
        return { reason: 'invalid', tag: '<span class="tag-pill invalid">INVALID</span>' };
    }
    var isDomainBlocked = domainsToBlock.some(function(d) {
        return domain === d || domain.endsWith('.' + d);
    });
    if (isDomainBlocked) {
        return { reason: 'domain', tag: '<span class="tag-pill blocked">CONSUMER</span>' };
    }
    var matchesStart = startsWithArr.some(function(p) {
        return username.startsWith(p);
    });
    if (matchesStart) {
        return { reason: 'start', tag: '<span class="tag-pill blocked">JUNK-PREFIX</span>' };
    }
    var matchesContains = containsArr.some(function(c) {
        return email.indexOf(c) !== -1;
    });
    if (matchesContains) {
        return { reason: 'contains', tag: '<span class="tag-pill blocked">FAKE</span>' };
    }
    return null;
}

function runScrubbingPipeline() {
    var startTime = performance.now();
    var rawData = document.getElementById('inputText').value;
    
    if (!rawData.trim()) {
        showToast('Please paste some data first!', 'error');
        return;
    }

    var emailRegex = /[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+(?:\\.[a-zA-Z0-9-]+)+/g;
    var matches = rawData.match(emailRegex) || [];
    
    var normalized = [];
    for (var i = 0; i < matches.length; i++) {
        var email = matches[i].trim().replace(/\\.+$/, '').replace(/^\\./, '').toLowerCase();
        if (email.indexOf('@') !== -1 && email.length > 3) {
            normalized.push(email);
        }
    }
    
    var uniqueEmails = [];
    var seen = {};
    for (var j = 0; j < normalized.length; j++) {
        if (!seen[normalized[j]]) {
            seen[normalized[j]] = true;
            uniqueEmails.push(normalized[j]);
        }
    }
    var dupCount = normalized.length - uniqueEmails.length;
    
    var domainsToBlock = document.getElementById('blockedDomains').value
        .split(',').map(function(s) { return s.trim().toLowerCase(); })
        .filter(function(s) { return !!s; });
    
    var startsWithArr = document.getElementById('startsWithFilters').value
        .toLowerCase().split(',').map(function(s) { return s.trim(); })
        .filter(function(s) { return !!s; });
    var containsArr = document.getElementById('containsFilters').value
        .toLowerCase().split(',').map(function(s) { return s.trim(); })
        .filter(function(s) { return !!s; });
    
    var cleanList = [];
    var indiaList = [];
    var salesList = [];
    var junkList = [];
    
    for (var m = 0; m < uniqueEmails.length; m++) {
        var email = uniqueEmails[m];
        var atIndex = email.lastIndexOf('@');
        if (atIndex === -1 || atIndex === 0 || atIndex === email.length - 1) {
            junkList.push({ email: email, reason: 'invalid', tag: '<span class="tag-pill invalid">INVALID</span>' });
            continue;
        }
        
        var username = email.substring(0, atIndex);
        var domain = email.substring(atIndex + 1);
        
        // Check if Indian business domain
        var indian = isIndianDomain(domain);
        // Check if sales/marketing email
        var sales = isSalesEmail(username);
        
        var rejection = getRejectionReason(email, username, domain, domainsToBlock, startsWithArr, containsArr);
        
        if (rejection) {
            junkList.push({ email: email, reason: rejection.reason, tag: rejection.tag });
        } else {
            var entry = { email: email, username: username, domain: domain };
            if (indian) {
                indiaList.push(entry);
            } else if (sales) {
                salesList.push(entry);
            } else {
                cleanList.push(entry);
            }
        }
    }
    
    // Sort all lists
    var sortFn = function(a, b) {
        if (a.domain !== b.domain) return a.domain.localeCompare(b.domain);
        return a.email.localeCompare(b.email);
    };
    indiaList.sort(sortFn);
    salesList.sort(sortFn);
    cleanList.sort(sortFn);
    
    // Build output: Indian first, then Sales, then other B2B
    var allClean = [];
    for (var i1 = 0; i1 < indiaList.length; i1++) allClean.push(indiaList[i1].email);
    for (var i2 = 0; i2 < salesList.length; i2++) allClean.push(salesList[i2].email);
    for (var i3 = 0; i3 < cleanList.length; i3++) allClean.push(cleanList[i3].email);
    
    var outputLines = allClean.join('\\n');
    document.getElementById('outputText').value = outputLines;
    document.getElementById('totalCount').innerText = normalized.length;
    document.getElementById('indiaCount').innerText = indiaList.length;
    document.getElementById('salesCount').innerText = salesList.length;
    document.getElementById('cleanCount').innerText = cleanList.length;
    document.getElementById('junkCount').innerText = junkList.length;
    document.getElementById('uniqueCount').innerText = uniqueEmails.length;
    document.getElementById('dupCount').innerText = dupCount;
    document.getElementById('procTime').innerText = Math.round(performance.now() - startTime) + 'ms';
    
    document.getElementById('statsDetail').classList.add('visible');
    
    updateButtonStates();
    
    var msg = 'Found ' + allClean.length + ' clean leads';
    if (indiaList.length > 0) msg += ' (' + indiaList.length + ' Indian)';
    if (salesList.length > 0) msg += ' (' + salesList.length + ' Sales)';
    msg += '!';
    showToast(msg);
}

function copyToClipboard() {
    var outputField = document.getElementById('outputText');
    if (!outputField.value) return;
    
    if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(outputField.value).then(function() {
            showToast('Copied to clipboard!');
        }).catch(function() {
            fallbackCopy(outputField);
        });
    } else {
        fallbackCopy(outputField);
    }
}

function fallbackCopy(field) {
    field.select();
    field.setSelectionRange(0, 99999);
    try {
        document.execCommand('copy');
        showToast('Copied to clipboard!');
    } catch (e) {
        showToast('Copy failed. Please select and copy manually.', 'error');
    }
}

function exportCSV() {
    var val = document.getElementById('outputText').value;
    if (!val) return;
    
    var lines = val.split('\\n').filter(function(l) { return l.trim(); });
    var timestamp = new Date().toISOString().slice(0, 19).replace(/:/g, '-');
    
    var csvRows = ['Email Address,Domain,Username,Category'];
    for (var i = 0; i < lines.length; i++) {
        var line = lines[i];
        var atIdx = line.lastIndexOf('@');
        var user = line.substring(0, atIdx);
        var domain = line.substring(atIdx + 1);
        var category = 'B2B';
        if (INDIAN_TLDS.some(function(t) { return domain.endsWith(t); })) category = 'Indian';
        if (SALES_PREFIXES.some(function(p) { return user === p || user.startsWith(p + '.'); })) category = 'Sales/Marketing';
        csvRows.push('"' + line + '","' + domain + '","' + user + '","' + category + '"');
    }
    
    var csvContent = '\\uFEFF' + csvRows.join('\\n');
    var blob = new Blob([csvContent], { type: 'text/csv;charset=utf-8;' });
    var link = document.createElement('a');
    link.href = URL.createObjectURL(blob);
    link.setAttribute('download', 'india_sales_leads_' + timestamp + '.csv');
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
    URL.revokeObjectURL(link.href);
    
    showToast('CSV downloaded!');
}

function exportJSON() {
    var val = document.getElementById('outputText').value;
    if (!val) return;
    
    var lines = val.split('\\n').filter(function(l) { return l.trim(); });
    var timestamp = new Date().toISOString().slice(0, 19).replace(/:/g, '-');
    
    var data = [];
    for (var i = 0; i < lines.length; i++) {
        var line = lines[i];
        var atIdx = line.lastIndexOf('@');
        var user = line.substring(0, atIdx);
        var domain = line.substring(atIdx + 1);
        var category = 'B2B';
        if (INDIAN_TLDS.some(function(t) { return domain.endsWith(t); })) category = 'Indian';
        if (SALES_PREFIXES.some(function(p) { return user === p || user.startsWith(p + '.'); })) category = 'Sales/Marketing';
        data.push({
            email: line,
            username: user,
            domain: domain,
            category: category,
            extracted_at: new Date().toISOString()
        });
    }
    
    var jsonContent = JSON.stringify({
        metadata: {
            exported_at: new Date().toISOString(),
            total_records: data.length,
            indian_leads: data.filter(function(d) { return d.category === 'Indian'; }).length,
            sales_leads: data.filter(function(d) { return d.category === 'Sales/Marketing'; }).length,
            tool: 'B2B Lead Scrubber - India & Sales Edition'
        },
        leads: data
    }, null, 2);
    
    var blob = new Blob([jsonContent], { type: 'application/json' });
    var link = document.createElement('a');
    link.href = URL.createObjectURL(blob);
    link.setAttribute('download', 'india_sales_leads_' + timestamp + '.json');
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
    URL.revokeObjectURL(link.href);
    
    showToast('JSON exported!');
}

document.addEventListener('keydown', function(e) {
    if ((e.ctrlKey || e.metaKey) && e.key === 'Enter') {
        e.preventDefault();
        runScrubbingPipeline();
    }
});
</script>
</body>
</html>
"""

components.html(html_code, height=850, scrolling=True)

st.markdown("---")
st.caption("🇮🇳 Indian domains (.in, .co.in, etc.) + 💼 Sales/Marketing emails are PRESERVED. Only consumer/junk blocked.")