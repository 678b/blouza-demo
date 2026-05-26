Blouza – Hackathon Demo (Claude-Powered Telemedicine System)
 Important Notice

This repository contains a simplified hackathon demonstration version of the Blouza platform.

It is NOT the full production codebase.

The full Blouza system is a secure, production-grade healthcare platform with:

EMR (Electronic Medical Records)
Hospital workflow automation
Secure authentication systems
Encrypted patient data handling
Payment and subscription systems
Messaging, file transfer, and telemedicine modules

Due to privacy, security, and healthcare data protection requirements, the complete production backend is not publicly shared.

This repository focuses only on:

 Claude AI integration
 Core telemedicine concept demonstration
 Simplified architecture for judging and review

 Project Overview

Blouza is an AI-powered telemedicine and electronic medical record (EMR) system designed to improve healthcare access, reduce hospital workload, and enhance patient triage efficiency.

The system integrates Claude AI to assist in:

Symptom interpretation
Medical department routing
Urgency classification (triage)
Patient intake structuring

This hackathon version demonstrates how AI can be embedded into healthcare workflows to support faster and more accurate decision-making.

 Key Features (Demo Version)
1. AI Symptom Triage (Claude Powered)

Patients submit symptoms and Claude returns:

Possible medical department
Urgency level (LOW / MEDIUM / HIGH / EMERGENCY)
Human-readable explanation
2. Smart Telemedicine Flow
Patient symptom input
AI analysis
Structured output for hospital use
3. Simplified Appointment Flow
Basic appointment booking endpoint (demo only)
Simulated scheduling process
Claude AI Integration

Blouza uses Anthropic Claude API for medical reasoning support.

Example Use Case:

Patient input:

"I have chest pain and shortness of breath"

Claude output:

Department: Cardiology
Urgency: HIGH
Explanation: Possible cardiovascular risk symptoms requiring immediate evaluation
Why Claude?

Claude was selected for:

Strong reasoning capabilities
Safety-focused responses
High-quality natural language medical structuring
System Architecture (Simplified Demo)
High-Level Architecture
Patient
   ↓
Flask Web App (Blouza Demo Backend)
   ↓
Claude AI API (Symptom Analysis Engine)
   ↓
AI Response (Department + Urgency + Explanation)
   ↓
Hospital Decision Support Layer

Full Production Architecture (Not Included Here)

The production Blouza system includes additional secure modules:

User authentication (patients + hospitals)
EMR database (SQLAlchemy)
Appointment scheduling system
Messaging system (secure hospital-user chat)
File upload & lab results storage
Video consultation system (Jitsi integration)
Push notifications (FCM + WebPush)
Payment & subscription system
Audit logging & session security

These components are intentionally excluded from this repository for security and privacy reasons.

 Tech Stack (Demo Version)
Python (Flask)
Claude AI API (Anthropic)
REST API architecture
JSON-based communication
HTML (basic UI for demo flow)
 Example API Endpoint
POST /ai-triage

Request:

{
  "symptoms": "fever, headache, and body weakness"
}

Response:

{
  "input_symptoms": "fever, headache, and body weakness",
  "claude_analysis": "Department: General Medicine\nUrgency: MEDIUM\nExplanation: ..."
}
 Hackathon Value

This project demonstrates:

Real-world AI integration (Claude in healthcare)
Practical telemedicine workflow
AI-assisted clinical decision support
Scalable architecture for hospital systems
Ethical AI usage in healthcare (triage support, not diagnosis replacement)
 Limitations of This Demo

To keep this repository safe and lightweight:

No real patient database included
No production authentication system
No payment or billing system
No hospital private workflows
No sensitive credentials exposed
Impact Vision

Blouza aims to:

Reduce hospital waiting times
Improve patient triage accuracy
Digitize hospital workflows in Rwanda and beyond
Assist doctors with AI-powered insights
Expand access to healthcare through technology
 Author

Built by Brian HIRWA NTWALI, a software devolper based in Kigali, Rwanda
Focused on healthcare innovation, AI systems, and digital transformation in African healthcare systems.
