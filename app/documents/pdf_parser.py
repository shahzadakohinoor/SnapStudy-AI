"""PDF content extractor."""

from pathlib import Path


def parse_pdf(file_path: str | Path) -> str:
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"PDF not found: {file_path}")

    try:
        from pypdf import PdfReader

        reader = PdfReader(str(path))
        text = [page.extract_text() or "" for page in reader.pages]
        return "\n".join(text).strip()
    except Exception as e:
        return f"[PDF Extraction Error: {e}]"