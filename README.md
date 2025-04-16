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
git clone https://github.com/gjb1088/network-analytics.git
cd network-analytics
```

### 2. Build the Docker Image
Use Minikube's local Docker environment to build the custom AWX Execution Environment:
```bash
eval $(minikube docker-env)
docker build -t custom-awx-ee:latest .
```

### 3. Configure AWX
1. Import the playbook into AWX from this repository.
2. Add the following **AWX credentials**:
   - Email username and recipient.
   - App password for the email service.
3. Set up **Ansible Vault** for storing sensitive credentials:
   - Encrypt credentials with the `ansible-vault` command.
   - Reference the encrypted variables in the playbook.

### 4. Run the Job
1. Launch the AWX job template for the playbook.
2. The job will:
   - Collect network metrics.
   - Generate a PDF report.
   - Email the report to the recipient.

---

## File Structure
```
.
├── Dockerfile                     # Docker setup for the AWX Execution Environment
├── generate_graphs.py             # Python script to generate latency and speed graphs
├── generate_pdf_report.py         # Python script to create the PDF report
├── network_analytics.yml          # Ansible playbook to automate the entire workflow
├── emoji_images/                  # PNG images of icons used in the report
│   ├── latency.png
│   ├── speed.png
│   └── uptime.png
└── README.md                      # Project documentation
```

---

## Security Considerations
1. Use **Ansible Vault** to encrypt sensitive variables like email credentials.
2. Avoid committing plaintext credentials or sensitive information to public repositories.

---

## Contributions
Feel free to fork the repository and submit pull requests for new features or improvements.

---

## License
This project is licensed under the MIT License.

---

## 👨‍💻 Creator

**George Burnite**  
*Cyberpunk Sysadmin. Infrastructure Alchemist. Creator of Burn.IT.*

[![LinkedIn](https://img.shields.io/badge/LinkedIn-GeorgeBurnite-blue)](https://www.linkedin.com/in/george-burnite-9a0799163/)

---
