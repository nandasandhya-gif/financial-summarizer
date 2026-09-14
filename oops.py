class DocumentProcessor:

    def __init__(self, file_path):
        self.file_path = file_path


document1 = DocumentProcessor("annual_report.pdf")

print(document1.file_path)