"""Image preprocessing and OCR text reading."""

from pathlib import Path


def extract_image_text(image_path: str | Path) -> str:
    path = Path(image_path)
    if not path.exists():
        raise FileNotFoundError(f"Image not found: {image_path}")

    try:
        from PIL import Image
        import pytesseract

        img = Image.open(path)
        return pytesseract.image_to_string(img).strip()
    except Exception as e:
        return f"[OCR Fallback / Error: Ensure Tesseract is installed. Details: {e}]"