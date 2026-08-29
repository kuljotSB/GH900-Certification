# Vulnerable Python App for CodeQL Demo

This app is intentionally vulnerable for CodeQL scanning demonstrations.

## Setup

1. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run the app:
   ```
   python app.py
   ```

## Vulnerabilities

- **Flask 1.0**: Known CVE-2018-1000656
- **PyYAML 4.2b1**: Known CVEs (unsafe load)
- **requests 2.19.1**: Known CVE-2018-18074

**Do not use this app in production.**