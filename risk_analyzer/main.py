import os
print("Current working directory:", os.getcwd())
print("Files in directory:", os.listdir())
from analysis import analyze_with_gemini
from report import generate_report
from segmentation import segment_document
from utils import extract_text

def main():
    print("Main function started...")

    # input_file = "sample_petition.docx"
    output_file = "RFE_Risk_Report.docx"

    print("Extracting text...")
    sample_text = """
personal_statement
I, Dr. John Smith, am applying for EB-1A classification for extraordinary ability in AI. I contributed to industry innovations, though no third-party validation is included.

RECOMMENDATION LETTER
To Whom It May Concern,
Dr. Smith is excellent and a great professional.
Sincerely,
Jane Doe

EVIDENCE OF ORIGINAL CONTRIBUTIONS
Developed an AI algorithm but limited external citations.

EVIDENCE OF JUDGING OTHERS' WORK
Claimed judging competitions, no documented proof.

AWARDS
Received Top Innovator Award, no media coverage attached.

"""

# Instead of:
# text = extract_text(input_file)
    text = sample_text
    #text = extract_text(input_file)

    print("Segmenting document...")
    sections = segment_document(text)

    findings = []

    print("Analyzing personal statement...")
    findings.extend(analyze_with_gemini(sections["personal_statement"]))

    print("Analyzing recommendation letters...")
    for letter in sections["recommendation_letters"]:
        findings.extend(analyze_with_gemini(letter))

    print("Analyzing evidence sections...")
    for criteria in sections["criteria_sections"]:
        findings.extend(analyze_with_gemini(criteria))

    print("Generating report...")
    generate_report(findings, output_file)

    print(f"✅ Report generated: {output_file}")

if __name__ == "__main__":
    main()