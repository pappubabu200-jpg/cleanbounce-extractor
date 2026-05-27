i# 📧 B2B Lead Scrubber & Extractor Pipeline

A secure, browser-side B2B email lead cleaning tool built with **Streamlit 1.35.0**. All processing happens client-side inside a sandboxed HTML component — your raw lead data never touches an external server or database.

---

## 🚀 Quick Start

```bash
# 1. Install Streamlit
pip install streamlit==1.35.0

# 2. Run the app
streamlit run b2b_lead_scrubber_enhanced.py

eatures
Core Pipeline
Email Extraction — Pulls emails from any pasted text (mixed formats, comma/newline separated, raw HTML, CSV dumps, etc.)
Smart Deduplication — Removes exact duplicates while preserving the unique set
Domain Filtering — Block free consumer providers (Gmail, Yahoo, Hotmail, Outlook, AOL, iCloud, ProtonMail, Yandex, Mail.ru, QQ, 163, GMX, Live, MSN, and 25+ more)
Username Pattern Filtering — Reject generic prefixes like admin, info, support, sales, noreply, first, last, jdoe, etc.
Substring Filtering — Catch fake/test emails containing xxxx, test, example, fake, temp, tempmail, trash
RFC-like Validation — Strict email format checking with 254-character length limits
Export & Output
Copy to Clipboard — One-click copy of the clean list
CSV Export — Three-column output: Email Address, Domain, Username with UTF-8 BOM support
JSON Export — Structured output with metadata and per-record timestamps
Timestamped Filenames — Never overwrite previous exports
UX Enhancements
Live Metrics Dashboard — Total extracted, clean leads, junk removed, clean rate percentage
Processing Stats — Unique count, duplicates removed, execution time in milliseconds
Junk Preview Panel — See exactly why emails were rejected with color-coded tags (DOMAIN, PREFIX, CONTAINS, INVALID)
Progress Bar — Visual feedback during pipeline execution
Toast Notifications — Success/error/info messages instead of browser alerts
Keyboard Shortcuts — Ctrl + Enter to run the pipeline instantly
Hover Actions — Select-all and clear buttons appear on output textarea
Advanced Options Panel — Toggle strict validation, auto-block free providers, case sensitivity, junk details
🛡️ Privacy & Security
100% Client-Side Processing
The entire scrubbing engine runs inside a sandboxed <iframe> via streamlit.components.v1. Your raw lead lists, customer data, and proprietary contact information are processed entirely in the user's browser. No HTTP requests are made. No data is logged, stored, or transmitted to any server.


##### Usage Guide

Step 1: Paste Raw Data
Drop any text into the input textarea. The extractor handles:
Plain comma-separated lists
Newline-separated dumps
Raw HTML or JSON snippets
Mixed formats with noise

####  Step 2: Configure Filters

| Filter                  | Default Value                                                                                          | Description                                    |
| ----------------------- | ------------------------------------------------------------------------------------------------------ | ---------------------------------------------- |
| Blocked Domains         | `gmail.com, yahoo.com, hotmail.com, outlook.com, aol.com, icloud.com, protonmail.com, mail.ru`         | Consumer/free email providers to reject        |
| Usernames Starting With | `first, last, jdoe, doe, flast, jane, john, admin, info, support, sales, marketing, noreply, no-reply` | Generic/local-part prefixes to reject          |
| Strings Containing      | `xxxx, test, example, fake, temp, tempmail, trash`                                                     | Substring patterns indicating fake/test emails |

Advanced toggles:

Strict email validation — Enforces RFC-like format rules
Auto-block free providers — Adds 25+ known free domains to the blocklist automatically
Case-insensitive matching — Normalizes everything to lowercase
Show rejected items — Displays the junk preview panel with rejection reasons

Step 3: Run the Pipeline

Click "Run Clean Sequence" or press Ctrl + Enter

Step 4: Review & Exportc
Check the metrics cards, inspect junk details if enabled, then:
Copy the clean list to clipboard
Download CSV for spreadsheet import
Export JSON for API ingestion

##### Architecture

Streamlit App (Python)
└── components.html() ──► Sandboxed Iframe
    └── Vanilla JS Engine
        ├── Regex Email Extraction
        ├── Normalization & Deduplication
        ├── Multi-layer Filtering Logic
        ├── Domain-grouped Sorting
        └── Export Generators (CSV/JSON)

###### Requirements

| Dependency | Version                                |
| ---------- | -------------------------------------- |
| Python     | 3.8+                                   |
| Streamlit  | 1.35.0                                 |
| Browser    | Chrome, Firefox, Safari, Edge (latest) |

 ####### Customization

:root {
    --bg: #0f172a;           /* Page background */
    --panel-bg: #1e293b;     /* Card background */
    --text: #f8fafc;         /* Primary text */
    --muted: #94a3b8;        /* Secondary text */
    --border: #334155;       /* Borders */
    --primary: #3b82f6;      /* Primary buttons/accent */
    --primary-hover: #2563eb;/* Primary hover state */
    --success: #22c55e;      /* Clean leads / success */
    --danger: #ef4444;       /* Junk / errors */
    --warning: #f59e0b;      /* Warnings */
    --accent: #8b5cf6;       /* Secondary accent */
    --copy-btn: #475569;     /* Copy button */
    --copy-hover: #64748b;   /* Copy button hover */
}

#######  Example Input / Output
Contact our team: john.smith@acme-corp.com, test@gmail.com,
admin@techstart.io, jdoe@yahoo.com, fake_xxxx@enterprise.com
sales@acme-corp.com, noreply@newsletter.ioc

############# Output (Clean):

john.smith@acme-corp.com
sales@acme-corp.com

##### Junk Rejected:
| Email                      | Reason                        |
| -------------------------- | ----------------------------- |
| `test@gmail.com`           | DOMAIN blocked                |
| `jdoe@yahoo.com`           | DOMAIN blocked + PREFIX match |
| `fake_xxxx@enterprise.com` | CONTAINS match                |
| `admin@techstart.io`       | PREFIX match                  |
| `noreply@newsletter.io`    | PREFIX match                  |


####Extending the Tool

To add new filter categories:
Add a new .filter-card in the .grid-filters section
Parse the new input in runScrubbingPipeline()
Add rejection logic to getRejectionReason()
Add a new tag style in CSS (optional)
Update metrics if needed

########### License
MIT License — free for personal and commercial use.
########### Built with 💙 using Streamlit 1.35.0


---

**[README.md](sandbox:///mnt/agents/output/README.md)** — download link if you need the file directly.


Usage Guide

# CleanBounce AI

AI-powered B2B Lead Cleaning Engine.

Features:
- Email extraction
- Bounce risk scoring
- Disposable email detection
- Domain intelligence
- India-first lead scoring
- CSV export

Built with:
- Streamlit
- Python
- Pandas
