import fitz  # PyMuPDF
import docx

def extract_text(file_path):
    """Extract text from PDF, DOCX, or TXT file."""
    if file_path.endswith(".pdf"):
        doc = fitz.open(file_path)
        text = "\n".join([page.get_text() for page in doc])
    elif file_path.endswith(".docx"):
        d = docx.Document(file_path)
        text = "\n".join([p.text for p in d.paragraphs if p.text.strip()])
    elif file_path.endswith(".txt"):
        with open(file_path, "r", encoding="utf-8") as f:
            text = f.read()
    else:
        raise ValueError("Unsupported file type.")
    return text