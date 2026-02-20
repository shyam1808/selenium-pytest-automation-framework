# 🚀 Selenium Pytest Automation Framework

🟢 Continuous Testing | ⚡ Cloud Execution | 📊 Live Reports | 🧪 UI Automation

![CI](https://github.com/shyam1808/selenium-pytest-automation-framework/actions/workflows/pytest.yml/badge.svg)



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
├── testData/     → Test data storage
├── utils/        → Utilities for reusable functions
├── conftest.py   → Fixtures & hooks
├── pytest.ini    → Pytest configuration
└── .github/      → CI/CD workflows
```

---

# ▶️ Run Automation (Cloud Execution)

This project supports public workflow execution — you can trigger the automation without any special access.

▶️ To run tests Open a Pull Request

1. Fork this repository
2. Make any small change
3. Create a Pull Request to main
4. GitHub Actions will automatically execute the Selenium + Pytest suite

No local setup required.

---

## 💻 Run Tests Locally

Follow these steps to execute the Selenium + Pytest suite on your machine.

### 1️⃣ Clone or Download the Repository

```bash
git clone <your-repo-url>
cd <your-project-folder>
```

### 2️⃣ Create Virtual Environment (Recommended)

```bash
python -m venv venv
```

Activate it:

**Mac/Linux**

```bash
source venv/bin/activate
```

**Windows**

```bash
venv\Scripts\activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run Tests with HTML Report

```bash
pytest -v --html=reports/report.html --self-contained-html
```

### 📊 View Report

After execution finishes view reports in reports/ repository



💡 Make sure Chrome browser is installed since tests run using Chrome.


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
