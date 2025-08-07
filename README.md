#BizCreate – Startup Blueprint Generator

An AI-powered Flask web app that generates a complete startup business plan using **IBM watsonx.ai Granite models**.  
Entrepreneurs can describe their idea in simple terms, and the app delivers a **structured business blueprint** including:

- **Problem Statement**
- **Target Market & Customer Segments**
- **Unique Selling Proposition (USP)**
- **Business Model Canvas**
- **Revenue Model**
- **Go-to-Market Strategy**
- **Estimated Budget & Funding Needs**
- **Potential Investor Connections**
- **Risks & Challenges**

#Features
- **AI-Driven Planning** – Uses IBM Granite to generate detailed, actionable startup plans.
- **Clean Web Interface** – Built with Flask for simplicity and ease of use.
- **Structured Output** – Provides 8-9 key sections.
- **Formatted & Readable** – Bold headings for clarity.

#Demo Screenshot (VSC Functioning, for Jupyter the output is generated in the notebook itself.)
<img width="1896" height="904" alt="Screenshot 2025-08-04 232451" src="https://github.com/user-attachments/assets/6b5e90ce-bc40-4267-9cd8-48f3d1185aee" />

#Tech Stack
- **Frontend**: HTML, CSS (VSC file)
- **Backend**: Python (Flask) (Done in Jupyter Notebook as well as VSCode), Jupyter doesn't consist of Flask Logic whereas VSC does.
- **AI Model**: IBM watsonx.ai Granite
- **Hosting**: Runs locally (can be deployed to IBM Cloud, Render etc.)

#Key Points (If using VSC File)
- Please create a virtual environment (.venv) for smooth functioning.
- Install necessary dependencies for proper output such as pip install flask ibm-watsonx-ai

#License

This project is licensed under the **MIT License** – you’re free to use, modify, and distribute the source code.

However, this project uses **IBM watsonx.ai Granite models** via IBM Cloud.  
Use of IBM services is subject to [IBM Cloud Terms of Use](https://www.ibm.com/cloud/terms) and the  
[watsonx.ai Service Description](https://www.ibm.com/support/customer/csol/terms/?id=i126-9967&lc=en).  
You must have an IBM Cloud account and comply with their licensing when running this project.

#Clone the repository
```bash
git clone https://github.com/MCodes18/bizcreate-startup-blueprint-generator.git
cd bizcreate-startup-blueprint-generator
