from pypdf import PdfReader

reader = PdfReader("sample.pdf")

with open("extracted_text.txt", "w", encoding="utf-8") as output:

    for page_number, page in enumerate(reader.pages, start=1):

        text = page.extract_text() or ""

        output.write(f"\n--- Page {page_number} ---\n")
        output.write(text)