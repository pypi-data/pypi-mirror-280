#!/bin/bash

file_base=$1
config_json=$2

template=$(echo $config_json | jq -r '.template')
filters=$(echo $config_json | jq -r '.filters')

# Create a temporary file with mktemp
temp_md=$(mktemp).md

# Enable autoEqnLabels
sed '1s/^---$/---\nautoEqnLabels: true/' "$file_base.md" > "$temp_md"

# inject self promotion
python "$filters/bio.py" "$temp_md"

# Convert Markdown to TeX
pandoc "$temp_md" -o "$base_file.tex" \
    -t beamer --dpi=300 \
    --listings \
    --template="$template" \
    --metadata link-citations=true \
    --slide-level=3 \
    --biblatex \
    --lua-filter="$filters/header.lua" \
    --filter pandoc-crossref


# Add allowframebreaks to all frames
python "$filters/frames.py" "$base_file.tex"

# Remove \passthrough commands to allow inline `code`.
python "$filters/passthrough.py" "$base_file.tex"

# Replace 'pdflatex' with 'lualatex' or 'lualatex'
if ! lualatex "$base_file.tex"; then
    echo "lualatex failed"
    exit 1
fi

if ! biber "$base_file"; then
    echo "biber failed"
    exit 1
fi

if ! lualatex "$base_file.tex"; then
    echo "lualatex failed"
    exit 1
fi

if ! lualatex "$base_name.tex"; then
    echo "lualatex failed"
    exit 1
fi

# Cleanup intermediate files
rm -f "$base_file".{aux,tex,bbl,bcf,blg,log,nav,out,run.xml,snm,toc,vrb} "$temp_md" > /dev/null 2>&1

# Open the PDF
open "$base_file.pdf"