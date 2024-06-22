#!/bin/bash
# Usage: ./slides.sh <input_file> <output_file> <zotero_path> <press_path>

file_base="$1"
config_json="$2"

template=$(echo $config_json | jq -r '.template')
filters=$(echo $config_json | jq -r '.filters')

# Convert Markdown to TeX
pandoc "$file_base".md -o "$filebase.tex" \
    -t beamer --dpi=300 \
    --listings \
    --template="$template" \
    --metadata link-citations=true \
    --slide-level=3 \
    --biblatex \
    --lua-filter="$filters/header.lua" \
    --filter pandoc-crossref

# LaTeX compilation
lualatex "$base_file.tex"
biber "$base_file"
lualatex "$base_file.tex"
lualatex "$base_file.tex"

# Cleanup intermediate files
rm -f "$base_name".{aux,tex,bbl,bcf,blg,log,nav,out,run.xml,snm,toc,vrb}

# Open the final PDF
open "$base_file.pdf"