# NHTSA (Consumer Complaints Text Analysis)

This repo contains a small exploratory analysis of **NHTSA consumer complaints** for the **1st generation Chevrolet Colorado (model years 2004–2012)**.

The original purpose of the analysis was to investigate the prevalence of **spontaneous fire complaints** in the 2005 Chevrolet Colorado after a personal incident. In the original dataset pulled at the time, **22.1%** of captured complaints included both keywords **"FIRE"** and **"BLOWER"**.

> Note: NHTSA data and site structure can change over time. Results may differ depending on when/what you scrape.

---

## What’s in the repo

- `NHTSA+Analysis.py` – a Python script exported from a notebook-style workflow. It uses Selenium to browse NHTSA pages and BeautifulSoup to extract complaint text.
- `init.py` – placeholder (currently empty).

---

## Requirements

- Python **3.10+**
- Firefox + **geckodriver** available on your PATH (for Selenium)
- Python packages:
  - `selenium`
  - `beautifulsoup4`

Install dependencies:

```bash
python3 -m pip install -U pip
python3 -m pip install selenium beautifulsoup4
```

---

## Running the analysis

From the repo directory:

```bash
python3 "NHTSA+Analysis.py"
```

The script will:

1. Iterate model years **2004–2012**
2. Visit NHTSA vehicle pages for multiple body styles
3. Expand complaint entries and collect complaint text into memory
4. Print keyword-match counts and percentages

---

## Text processing / NLP (how it works)

This project does **lightweight text processing**, not a full NLP pipeline. The goal is to collect complaint narratives and do simple keyword-based inspection.

At a high level:

1. **Collect raw complaint text**
   - Selenium navigates NHTSA vehicle pages and expands complaint entries.
   - The script parses the loaded HTML with BeautifulSoup and pulls the complaint narrative paragraphs.
   - Each complaint’s text is appended into an in-memory list (`full_list`).

2. **Normalize for searching (implicit)**
   - The script currently converts each complaint entry to a Python `str(...)` before searching.
   - No explicit normalization is applied yet (e.g., lowercasing, punctuation stripping, stemming/lemmatization).

3. **Keyword matching**
   - The analysis searches for hard-coded keywords like `"FIRE"`, `"BLOWER"`, and `"SIGNAL"` using Python substring checks (`"..." in text`).
   - Matching complaints are printed, and the script reports counts + percentage of total complaints.

If you want this to be more “NLP-like”, common next steps would be:
- consistent casing (e.g., `.upper()`), whitespace normalization, and punctuation handling
- regex-based matching with word boundaries
- tokenization and frequency counts
- exporting a structured dataset (CSV/JSON) for later analysis

## Notes / Caveats

- This is an **exploratory** project and the script is not yet production-hardened.
- Selenium automation against a public site can be brittle (page structure, popups, rate limiting).
- If you plan to run this repeatedly, consider adding:
  - request throttling/backoff
  - caching downloaded pages
  - exporting results to CSV/JSON

---

## Disclaimer

This project is for research/educational use. It is not legal advice, safety advice, or a substitute for professional investigation.
