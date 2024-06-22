#!/bin/bash
# Usage: ./slides.sh <input_file> <output_file> <zotero_path> <press_path>

input_file="$1"
output_file="$2"
Zoteropath="$3"
Presspath="$4"

base_name="${input_file%.md}"

# Convert Markdown to TeX
pandoc "$input_file" -o "$base_name.tex" \
    -t beamer --dpi=300 \
    --listings \
    --template="$Presspath/templates/slides.tex" \
    --metadata link-citations=true \
    --slide-level=3 \
    --biblatex \
    --lua-filter="$Presspath/filters/header.lua" \
    --filter pandoc-crossref

# LaTeX compilation
lualatex "$base_name.tex"
biber "$base_name"
lualatex "$base_name.tex"
lualatex "$base_name.tex"

# Move the output to the desired location
mv "$base_name.pdf" "$output_file"

# Cleanup intermediate files
rm -f "$base_name".{aux,tex,bbl,bcf,blg,log,nav,out,run.xml,snm,toc,vrb}