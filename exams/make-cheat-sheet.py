"""Tile cheat-sheet.pdf (tall single-column pages) into a two-sided
letter-landscape sheet, two columns per side: cheat-sheet-print.pdf.

cheat-sheet.tex is typeset at 12pt on column pages of size COLW x COLH
inches. Here each column page is shrunk by SCALE and placed four across.
Usage: python make-cheat-sheet.py  (after compiling cheat-sheet.tex)
"""
import pymupdf

SCALE = 0.80         # 12pt * 0.80 = 9.6pt printed
NCOL = 2
PAGE_W, PAGE_H = 11 * 72, 8.5 * 72
MARGIN, GAP = 0.25 * 72, 0.12 * 72

src = pymupdf.open("cheat-sheet.pdf")
out = pymupdf.open()
colw = (PAGE_W - 2 * MARGIN - (NCOL - 1) * GAP) / NCOL
n_sides = -(-len(src) // NCOL)
if n_sides > 2:
    print(f"WARNING: {len(src)} column pages need {n_sides} sides, not 2")
for side in range(n_sides):
    page = out.new_page(width=PAGE_W, height=PAGE_H)
    for c in range(NCOL):
        k = side * NCOL + c
        if k >= len(src):
            break
        r = src[k].rect
        w, h = r.width * SCALE, r.height * SCALE
        x0 = MARGIN + c * (colw + GAP)
        page.show_pdf_page(pymupdf.Rect(x0, MARGIN, x0 + w, MARGIN + h), src, k)
        if c > 0:
            xs = x0 - GAP / 2
            page.draw_line((xs, MARGIN), (xs, PAGE_H - MARGIN), width=0.3)
out.save("cheat-sheet-print.pdf")
print(f"{len(src)} column pages -> {n_sides} sides, column width {colw/72:.3f} in")
