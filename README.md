# 🚀 Selenium Pytest Automation Framework

🟢 Continuous Testing | ⚡ Cloud Execution | 📊 Live Reports | 🧪 UI Automation

![CI](https://github.com/shyam1808/selenium-pytest-automation-framework/actions/workflows/pytest.yml/badge.svg)

[![Run Automation](https://img.shields.io/badge/Run-Automation-blue?style=for-the-badge\&logo=githubactions)](https://github.com/shyam1808/selenium-pytest-automation-framework/actions/workflows/pytest.yml)

[![Live Report](https://img.shields.io/badge/View-Live_Report-green?style=for-the-badge\&logo=googlechrome)](https://shyam1808.github.io/selenium-pytest-automation-framework/report.html)

---

# 📌 Project Overview

Enterprise-style **Selenium + Pytest UI Automation Framework** built with scalable architecture, CI/CD execution, and live reporting.

This project demonstrates real-world QA engineering practices:

✔ Page Object Model design
✔ Headless cloud execution
✔ Screenshot capture on failures
✔ Live HTML report hosted via GitHub Pages
✔ Modern GitHub Actions pipeline

---

# 🧰 Tech Stack

* Python
* Selenium WebDriver
* Pytest
* Pytest-HTML Reporting
* GitHub Actions (CI/CD)
* GitHub Pages
* Page Object Model (POM)

---

# 🏗️ Visual Framework Architecture

```text
                ┌──────────────────────┐
                │      Test Cases       │
                │       (tests/)        │
                └──────────┬───────────┘
                           │
                           ▼
                ┌──────────────────────┐
                │     Page Objects      │
                │       (pages/)        │
                └──────────┬───────────┘
                           │
                           ▼
                ┌──────────────────────┐
                │  Selenium WebDriver   │
                │   Browser Interaction │
                └──────────┬───────────┘
                           │
                           ▼
                ┌──────────────────────┐
                │   Application Under   │
                │         Test          │
                └──────────────────────┘
```

### Key Design Principles

* Separation of UI logic from test logic
* Reusable fixtures via `conftest.py`
* Maintainable test architecture
* CI-first automation design

---

# ⚙️ Visual CI/CD Execution Flow

```text
        Manual Run from GitHub CI
                    │
                    ▼
        ┌─────────────────────────┐
        │   GitHub Actions Runner  │
        └─────────────┬───────────┘
                      │
        Install Dependencies (pip)
                      │
                      ▼
        Run Pytest Suite (Headless)
                      │
                      ▼
        Generate HTML Report + Screenshots
                      │
                      ▼
        Deploy to GitHub Pages (Live URL)
                      │
                      ▼
        Recruiters View Report in Browser
```

---

# 📂 Project Structure

```text
selenium-pytest-automation-framework/
│
├── pages/        → Page Object Model classes
├── tests/        → Test scenarios
├── reports/      → HTML reports + screenshots
├── conftest.py   → Fixtures & hooks
├── pytest.ini    → Pytest configuration
└── .github/      → CI/CD workflows
```

---

# ▶️ Run Automation (Cloud Execution)

1. Open **Actions** tab
2. Click **Run Automation** button above
3. Wait for CI workflow to complete
4. Open **Live Report** link

No local setup required.

---

# 📊 Reporting & Observability

* HTML test report generated using pytest-html
* Screenshots embedded automatically on failures
* Public report hosted via GitHub Pages
* CI badge updates after every execution

🔗 Live Report
[https://shyam1808.github.io/selenium-pytest-automation-framework/report.html](https://shyam1808.github.io/selenium-pytest-automation-framework/report.html)

---

# 🧪 Execution Modes

| Environment    | Browser Mode     |
| -------------- | ---------------- |
| Local Machine  | Visible Browser  |
| GitHub Actions | Headless Browser |

Framework detects CI environment automatically.

---

# 🔐 Enterprise QA Features

✔ Modular automation architecture
✔ CI/CD pipeline integration
✔ Headless execution strategy
✔ Visual reporting dashboard
✔ Environment-aware framework design

---

# 👤 Author

Shyamal Srivastava
QA Automation Engineer | Selenium | Pytest | CI/CD
