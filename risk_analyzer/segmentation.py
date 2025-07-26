def segment_document(text):
    sections = {
        "personal_statement": "",
        "recommendation_letters": [],
        "criteria_sections": []
    }

    lines = text.split("\n")
    current_section = "personal_statement"

    for line in lines:
        lower_line = line.lower()
        if "recommendation" in lower_line or "to whom" in lower_line:
            current_section = "recommendation_letter"
            sections["recommendation_letters"].append(line)
        elif "evidence" in lower_line or "award" in lower_line:
            current_section = "criteria"
            sections["criteria_sections"].append(line)
        else:
            if current_section == "personal_statement":
                sections["personal_statement"] += line + "\n"
            elif current_section == "recommendation_letter":
                sections["recommendation_letters"][-1] += line + "\n"
            else:
                sections["criteria_sections"][-1] += line + "\n"

    return sections