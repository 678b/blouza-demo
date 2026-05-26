from flask import Flask, request, jsonify, render_template, session
from datetime import datetime
import os
import anthropic

app = Flask(__name__)
app.secret_key = "demo_secret_key"

# ----------------------------
# CLAUDE AI SETUP
# ----------------------------
client = anthropic.Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY")
)

def analyze_symptoms_with_claude(symptoms):
    """
    Claude-powered medical triage assistant
    """
    prompt = f"""
You are a medical triage assistant for a telemedicine system.

Analyze the following patient symptoms:
{symptoms}

Return:
1. Possible department (e.g. Cardiology, General Medicine, Dermatology)
2. Urgency level (LOW, MEDIUM, HIGH, EMERGENCY)
3. Short explanation in simple language
"""

    response = client.messages.create(
        model="claude-3-haiku-20240307",
        max_tokens=300,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.content[0].text


# ----------------------------
# CORE FEATURE (CLAUDE POWERED)
# ----------------------------
@app.route("/ai-triage", methods=["POST"])
def ai_triage():
    data = request.json
    symptoms = data.get("symptoms")

    if not symptoms:
        return jsonify({"error": "No symptoms provided"}), 400

    result = analyze_symptoms_with_claude(symptoms)

    return jsonify({
        "input_symptoms": symptoms,
        "claude_analysis": result
    })


# ----------------------------
# SIMPLE APPOINTMENT FLOW (DEMO)
# ----------------------------
@app.route("/book", methods=["POST"])
def book():
    data = request.json

    return jsonify({
        "message": "Appointment booked (demo mode)",
        "patient": data.get("name"),
        "time": datetime.utcnow().isoformat()
    })


# ----------------------------
# HOME
# ----------------------------
@app.route("/")
def home():
    return """
    <h1>Blouza AI Telemedicine Demo</h1>
    <p>Claude-powered symptom triage system</p>
    """


if __name__ == "__main__":
    app.run(debug=True)