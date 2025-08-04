from flask import Flask, render_template, request
from ibm_watsonx_ai.foundation_models import Model
from ibm_watsonx_ai import Credentials
import re

#Project details from IBM Cloud
api_key="a_Y4ACT-LB_rWPd373JUZ9ElPZgELwqEw8839CWVkUj7"
service_url="https://au-syd.ml.cloud.ibm.com"
project_id = "82bce3df-8624-462d-b136-4fe097d1ed14"


#Credentials authentication
creds=Credentials(api_key=api_key, url=service_url)
model_id="ibm/granite-3-8b-instruct"
model=Model(model_id=model_id, credentials=creds, project_id=project_id)

#Flask app setup
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result= None
    if request.method == 'POST':
        startup_idea = request.form['idea']

        prompt = f"""
        You are an expert startup advisor and business consultant.

        Create a detailed and structured startup plan for the following idea:
        "{startup_idea}"

        Your response should include the following sections:

        Problem Statement – Clearly define the market problem and why it matters.
        Target Market & Customer Segments – Who will use this product/service? Include demographics and market size.
        Unique Selling Proposition (USP) – What makes this solution unique?
        Business Model Canvas – Summarize key partners, key activities, key resources, value propositions, customer relationships, channels, customer segments, cost structure, and revenue streams.
        Revenue Model – How will the startup make money?
        Go-to-Market Strategy – Step-by-step strategy for launching and gaining traction.
        Estimated Budget & Funding Needs – Rough cost breakdown for the first year and total funding required.
        Potential Investor Connections – Suggest investor types, networks, or funding platforms relevant to this idea.
        Risks & Challenges – Identify possible obstacles and propose mitigation strategies.

        Guidelines:
        - Use numbered sections exactly as listed.
        - Write all 9 sections completely before ending your answer.
        - Make it short and concise but comprehensive.
        - Use clear, professional language.
        - Avoid jargon and explain technical terms.
        - Provide actionable insights and realistic expectations.
        - Focus on practical steps and real-world applicability.
        - Be specific and avoid vague terms like "good", "large market", "popular".
        - Assume the reader is an aspiring entrepreneur seeking actionable advice.
        """

        params={
            "decoding_method": "sample",
            "temperature": 0.2,
            "max_new_tokens": 1000
        }

        try:
            raw_response = model.generate_text(prompt=prompt, params=params).strip()
            # Split into sections by numbered headings
            sections = re.split(r"(\d+\. [^\n]+)\n", raw_response)
            html = ""
            if len(sections) > 1:
                html += "<ol style='padding-left: 1.2em;'>"
                for i in range(1, len(sections), 2):
                    heading = sections[i].strip()
                    # Remove leading number and dot from heading for cleaner list
                    heading_text = re.sub(r"^\d+\.\s*", "", heading)
                    content = sections[i+1].strip() if i+1 < len(sections) else ""
                    html += f"<li><strong>{heading_text}</strong><br><div style='margin-left:1em'>{content.replace('\n', '<br>')}</div></li>"
                html += "</ol>"
                result = html
            else:
                result = raw_response.replace("\n", "<br>")
        except Exception as e:
            result = f"<span style='color:red;'>Error generating response: {e}</span>"

    return render_template('index.html', result=result)
    
if __name__ == '__main__':
    app.run(debug=True)