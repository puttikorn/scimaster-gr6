#!/usr/bin/env python3
"""Extract text from คณิตศาสตร์ Gr6 - MidFinal.pdf to understand the actual content."""
import sys
from pypdf import PdfReader

pdf_path = "คณิตศาสตร์ Gr6 - MidFinal.pdf"

try:
    reader = PdfReader(pdf_path)
    total_pages = len(reader.pages)
    print(f"Total pages: {total_pages}")
    print("=" * 60)

    with open("math_pdf_content.txt", "w", encoding="utf-8") as out:
        for i, page in enumerate(reader.pages):
            text = page.extract_text() or ""
            header = f"\n{'='*60}\nPAGE {i+1}\n{'='*60}\n"
            out.write(header + text + "\n")
            if i < 10:  # Print first 10 pages to console
                print(header + text[:500] + ("..." if len(text) > 500 else ""))

    print(f"\n\nFull content saved to math_pdf_content.txt")
except Exception as e:
    print(f"Error: {e}", file=sys.stderr)
    sys.exit(1)
