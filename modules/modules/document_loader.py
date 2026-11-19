
from pathlib import Path
from pypdf import PdfReader

def load_scheme_document(file_path):
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"File not found: {path}")

    if path.suffix.lower() == ".txt":
        return path.read_bytes().decode("utf-8-sig", errors="replace")

    if path.suffix.lower() == ".pdf":
        reader = PdfReader(str(path))
        return "\n".join(
            page.extract_text() or ""
            for page in reader.pages
        )

    raise ValueError("Only TXT and PDF files are supported.")
