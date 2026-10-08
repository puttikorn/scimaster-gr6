#!/usr/bin/env python3
import os
import sys
import fitz  # PyMuPDF

pdf_path = "Documents/arduino_learning.pdf"
output_file = "arduino_pdf_content.txt"
output_dir = "extracted_text_arduino"

os.makedirs(output_dir, exist_ok=True)

try:
    doc = fitz.open(pdf_path)
    total_pages = len(doc)
    print(f"Total pages: {total_pages}")
    print("=" * 60)

    with open(output_file, "w", encoding="utf-8") as out:
        for i in range(total_pages):
            page = doc[i]
            text = page.get_text()
            
            # If page text is very sparse (e.g. image-only), we can fallback if needed, but this PDF has direct text
            page_path = os.path.join(output_dir, f"page_{i+1}.txt")
            with open(page_path, "w", encoding="utf-8") as pf:
                pf.write(text)
            
            header = f"\n{'='*60}\nPAGE {i+1}\n{'='*60}\n"
            out.write(header + text + "\n")
            
            print(f"Processed Page {i+1}/{total_pages} ({len(text)} chars)")

    print(f"\nFull content saved to {output_file} and {output_dir}/")
except Exception as e:
    print(f"Error: {e}", file=sys.stderr)
    sys.exit(1)
