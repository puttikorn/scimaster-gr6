#!/usr/bin/env python3
import os
import sys
import fitz  # PyMuPDF
import subprocess
import tempfile

pdf_path = "Documents/สังคมศึกษา Gr6-MidFinnal.pdf"
output_file = "social_pdf_content.txt"
output_dir = "extracted_text_social"

os.makedirs(output_dir, exist_ok=True)

try:
    doc = fitz.open(pdf_path)
    total_pages = len(doc)
    print(f"Total pages: {total_pages}")
    print("=" * 60)

    with open(output_file, "w", encoding="utf-8") as out:
        for i in range(total_pages):
            page = doc[i]
            
            # Render page to high-res image (2x zoom)
            pix = page.get_pixmap(matrix=fitz.Matrix(2, 2))
            
            with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as tmp_img:
                tmp_img_name = tmp_img.name
                pix.save(tmp_img_name)
            
            # Run tesseract with Thai and English models
            cmd = ["tesseract", tmp_img_name, "stdout", "-l", "tha+eng", "--psm", "6"]
            proc = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            text = proc.stdout.strip()
            
            if os.path.exists(tmp_img_name):
                os.remove(tmp_img_name)
            
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
