from pypdf import PdfReader


def extract_text_from_pdf(pdf_path):

    reader = PdfReader(pdf_path)

    with open("extracted_text.txt", "w", encoding="utf-8") as output:

        for page_number, page in enumerate(reader.pages, start=1):

            text = page.extract_text() or ""

            output.write(f"\n--- Page {page_number} ---\n")
            output.write(text)

    return "PDF processed successfully"