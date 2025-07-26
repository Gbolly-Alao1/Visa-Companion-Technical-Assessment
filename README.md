# Risk Analyzer

A Python tool to analyze EB-1A immigration petition documents for potential Request for Evidence (RFE) risks using Google Gemini AI.

## Features
- Extracts and segments text from DOCX, PDF, or TXT files
- Analyzes each section for weaknesses and RFE risks
- Maps risks to EB-1A criteria
- Generates a structured risk report

## Requirements
- Python 3.8+
- Google Generative AI Python SDK (`google-generativeai`)
- `python-docx`
- `PyMuPDF` (for PDF support)

## Setup Instructions

1. **Clone or download this repository**

2. **Install dependencies**

   Open a terminal in the project directory and run:
   ```sh
   pip install -r requirements.txt
   ```
   Or, install manually:
   ```sh
   pip install google-generativeai python-docx pymupdf
   ```

3. **Set up your Google Generative AI API key**

   - Obtain an API key from Google AI Studio or your Google Cloud Console.
   - In `analysis.py`, replace the placeholder with your actual API key:
     ```python
     genai.configure(api_key="YOUR_API_KEY_HERE")
     ```

4. **Prepare your input document**

   - Place your petition file (DOCX, PDF, or TXT) in the project directory.
   - Update `main.py` to set the correct `input_file` name.

5. **Run the analyzer**

   In the terminal, run:
   ```sh
   python main.py
   ```
   The output report will be saved as `RFE_Risk_Report.docx` by default.

## File Overview
- `main.py` — Main entry point
- `analysis.py` — AI-powered risk analysis logic
- `segmentation.py` — Document sectioning
- `report.py` — Report generation
- `utils.py` — Text extraction utilities

## Notes
- For development/testing, you can use a sample text string instead of a file (see `main.py`).
- Make sure your API key has access to the correct Gemini model. If you get a model not found error, check the model name and your API access.

## License
MIT License
