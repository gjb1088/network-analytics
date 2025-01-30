# Network Analytics and Automation Project

## Overview
This project is a network performance analytics and reporting system built using **AlmaLinux 9.5**, **Minikube**, and **AWX**. It automates the collection of network metrics like latency, download speed, and uptime, generating a daily report that is emailed to a specified recipient.

### Features
- Automates network metric collection:
  - **Latency** (in milliseconds)
  - **Download Speed** (in Mbps)
  - **Uptime** (in hours)
- Generates a professional PDF report with:
  - Visualized graphs (line charts) comparing metrics against home averages.
  - Summary section with metric highlights.
- Sends the report via email to a configured recipient.
- Securely handles sensitive credentials (email addresses and app passwords) using **Ansible Vault**.

---

## Requirements
### System Requirements
- **AlmaLinux 9.5**
- **Docker** and **Minikube** for Kubernetes containerization
- **AWX** for job automation
- **Git** for version control

### Software Dependencies
- Python libraries:
  - `matplotlib`
  - `fpdf2`
- DejaVu and Noto Color Emoji fonts (for emojis in the report)

---

## Setup Instructions

### 1. Clone the Repository
```bash
git clone <your-repo-url>
cd <your-repo-directory>
