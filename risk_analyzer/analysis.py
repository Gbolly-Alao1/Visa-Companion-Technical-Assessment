import google.generativeai as genai
import json

genai.configure(api_key="AIzaSyBQWuhUKnlMf79HLwQkU1Xvxfj_tR09IHs")  # Replace with your real API key
model = genai.GenerativeModel("models/gemini-1.5-flash")

def analyze_with_gemini(section_text):
    # EB-1A Criteria Reference for the AI
    eb1a_criteria = {
        "1": "Receipt of lesser nationally or internationally recognized prizes or awards for excellence",
        "2": "Membership in associations in the field for which classification is sought",
        "3": "Published material about the alien in professional or major trade publications",
        "4": "Evidence of the alien's participation as a judge of the work of others",
        "5": "Evidence of the alien's original scientific, scholarly, artistic, athletic, or business-related contributions",
        "6": "Evidence of the alien's authorship of scholarly articles in the field",
        "7": "Evidence of the display of the alien's work in the field at artistic exhibitions or showcases",
        "8": "Evidence that the alien has performed in a leading or critical role for organizations",
        "9": "Evidence that the alien has commanded a high salary or other significantly high remuneration",
        "10": "Evidence of commercial successes in the performing arts"
    }
    
    prompt = f"""
    You are a senior USCIS adjudicator with 15+ years of experience reviewing EB-1A petitions. You have personally reviewed thousands of cases and know exactly what triggers RFEs (Requests for Evidence).

    CRITICAL CONTEXT: EB-1A petitions must demonstrate extraordinary ability through at least 3 of 10 specific criteria. You are looking for weaknesses that would make you, as a USCIS officer, issue an RFE.

    EB-1A CRITERIA REFERENCE:
    {json.dumps(eb1a_criteria, indent=2)}

    COMMON RFE TRIGGERS YOU SHOULD IDENTIFY:
    - Vague, generic claims that could apply to anyone in the field
    - Unsupported statements without quantifiable evidence
    - Lack of independent third-party verification
    - Template language that appears across multiple letters
    - Claims of "extraordinary ability" without comparative context
    - Missing documentation or weak supporting evidence
    - Inconsistencies in timeline, achievements, or field expertise
    - Overstated impact without measurable metrics
    - Self-serving statements without external validation

    YOUR TASK: Analyze the petition text below with the scrutiny of a USCIS adjudicator. For each potential weakness you identify:

    1. Extract the exact problematic text
    2. Explain why this would concern a USCIS officer
    3. Map it to the specific EB-1A criterion it affects
    4. Assess the severity and likelihood of triggering an RFE
    5. Provide specific, actionable improvement suggestions with example language

    ANALYSIS REQUIREMENTS:
    - Be thorough and detailed in your explanations
    - Focus on substantive issues that would genuinely concern USCIS
    - Provide specific, implementable recommendations
    - Include suggested replacement language where appropriate

    PETITION TEXT TO ANALYZE:
    {section_text}

    Return your analysis as a JSON array with this exact structure:
    [
        {{
            "criterion": "Criterion X: [Full criterion name]",
            "risk": "[Detailed description of the specific weakness and why it's problematic]",
            "severity": "Low/Medium/High",
            "rfe_likelihood": "Low/Medium/High",
            "excerpt": "[Exact text from petition that is problematic]",
            "uscis_concern": "[Specific reason why USCIS would flag this]",
            "suggestion": "[Detailed improvement recommendation]",
            "improved_language": "[Example of how to rewrite the problematic text]",
            "evidence_needed": "[List of additional evidence that would strengthen this claim]"
        }}
    ]

    IMPORTANT: 
    - Identify at least 3-5 substantive issues if they exist
    - Be specific about what evidence is missing or weak
    - Provide concrete examples of better language
    - Focus on issues that would realistically trigger an RFE
    - Return ONLY the JSON array, no additional text
    """

    response = model.generate_content(prompt)
    try:
        # Clean the response text in case there's extra formatting
        response_text = response.text.strip()
        if response_text.startswith('```json'):
            response_text = response_text[7:-3]  # Remove ```json and ```
        elif response_text.startswith('```'):
            response_text = response_text[3:-3]   # Remove ``` and ```
        
        return json.loads(response_text)
    except json.JSONDecodeError as e:
        print(f"JSON parsing error: {e}")
        print(f"Raw response: {response.text}")
        # Return empty array if parsing fails
        return []
    except Exception as e:
        print(f"Error in analysis: {e}")
        return []



# def analyze_with_gemini(section_text):
    