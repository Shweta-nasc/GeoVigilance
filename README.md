🌍 GeoVigilance
 AI-Driven Rockfall Prediction
GeoVigilance is a state-of-the-art predictive maintenance system designed for open-pit mining safety. It utilizes an ensemble AI model to forecast rockfall risks by synthesizing real-time IoT telemetry with historical geological patterns.

🎯 The Mission
In open-pit mining, slope stability is a critical safety factor. GeoVigilance moves safety protocols from reactive to proactive by providing a 3-tier safety score based on high-frequency sensor data.

Risk Scoring System
🔴 High: Critical instability detected. Immediate evacuation and structural reinforcement required.

🟡 Medium: Minor shifts or environmental triggers noted. Restricted access and increased inspection frequency.

🟢 Low: Stable conditions. Standard operations may proceed.

🧩 System Architecture
The model processes four primary data streams to generate its prediction:

Tiltmeters: Measuring minute angular displacements in rock faces.

Seismic Activity: Monitoring micro-vibrations and ground tremors.

Weather Data: Integrating precipitation levels and temperature fluctuations (freeze-thaw cycles).

Historical Records: Correlation with past failure events and geological mapping.

🛠 Tech Stack
Data Science & Modeling
<p align="left">
<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
<img src="https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white" />
<img src="https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white" />
<img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white" />
</p>

Infrastructure & IoT
<p align="left">
<img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white" />
<img src="https://img.shields.io/badge/MQTT-660066?style=for-the-badge&logo=mqtt&logoColor=white" />
<img src="https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white" />
<img src="https://img.shields.io/badge/Redis-DC382D?style=for-the-badge&logo=redis&logoColor=white" />
</p>

DevOps & Deployment
<p align="left">
<img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white" />
<img src="https://img.shields.io/badge/AWS-232F3E?style=for-the-badge&logo=amazon-aws&logoColor=white" />
<img src="https://img.shields.io/badge/Terraform-7B42BC?style=for-the-badge&logo=terraform&logoColor=white" />
<img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" />
</p>

🚀 Deployment Pipeline
GeoVigilance is built for high availability and low latency:

Edge Processing: Initial data filtering occurs near the sensors to reduce bandwidth.

Cloud Inference: Data is transmitted via MQTT to a FastAPI backend hosted on AWS Elastic Kubernetes Service (EKS).

Storage: Sensor time-series data is managed by TimescaleDB for efficient querying.

Monitoring: A Streamlit dashboard provides site managers with a real-time "Heat Map" of the mine's stability.

⚙️ Getting Started
Prerequisites
Python 3.9+

Docker Desktop

Access to AWS CLI (for cloud deployment)

Installation
Clone the Repo

Bash
git clone https://github.com/Shweta-nasc/GeoVigilance.git
Environment Setup

Bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
Run Local Inference Server

Bash
uvicorn main:app --reload


GeoVigilance | Empowering Mine Safety through Intelligent Observations.
