# Beta-Tester-Recruitment-Engine 

An automated system to discover, qualify, and recruit high-quality beta testers for early-stage developer products by leveraging the GitHub API.

## 📌 Overview

Finding the right beta testers is often the hardest part of launching a new developer tool. This engine automates the discovery process by scanning GitHub for active developers within specific technical ecosystems (React, Python, Kubernetes, etc.) and exporting their professional details into a format ready for outreach.

---

## ✨ Features

* **Targeted Discovery**: Search for developers based on specific programming languages and topics.
* **Quality Qualification**: Automatically filters for users with **>50 followers** to ensure you reach influential developers.
* **Data Extraction**: Retrieves names, public emails, follower counts, and repository stats.
* **Resilient Scripting**: Built-in **Retry Logic** and **Exponential Backoff** to handle GitHub API rate limits (403/429 errors) gracefully.
* **Outreach Ready**: Generates a `developers.csv` file formatted for direct upload to tools like **Smartlead** or **Instantly**.

---

## 🛠️ Prerequisites

* **Python 3.x**
* **GitHub Personal Access Token (PAT)**:
    1.  Go to [GitHub Settings > Developer Settings](https://github.com/settings/tokens).
    2.  Generate a new token (classic).
    3.  Select `read:user` and `user:email` scopes.

---

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/KgothatsoTheko/Beta-Tester-Recruitment-Engine
cd Beta-Tester-Recruitment-Engine
```
### 2. Install dependencies
```bash
pip install requests
```
### 3. Configure your Token
```bash
GITHUB_TOKEN = "your_github_token_here"
```
### 4. Run the Engine
```bash
python main.py
```
