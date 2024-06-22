#!/bin/bash

# Configuration base dir has chapters sorted by number
base_dir=$1
base_dir_name=$(basename "$base_dir")
config_json=$2

chapter_files=$(ls "$base_dir"/*.md | sort -V)

# Create a temporary file for intermediate processing
full_book=$(mktemp)

# Concatenate all chapter files and clean the content
for file in $chapter_files; do
    # Remove control characters and non-UTF8 characters
    cat "$file" | tr -d '\000-\031' | iconv -f utf-8 -t utf-8 -c >> "$full_book"
    # Add a newline between chapters
    echo -e "\n\n" >> "$full_book"
done

# Convert the Markdown files to PDF with Pandoc
pandoc "$full_book" -o "$base_dir/$base_dir_name.pdf" \
    --biblatex \
    --slide-level=3 \
    --filter=pandoc-crossref \
    --pdf-engine=xelatex \
    -V mainfont="DejaVu Serif" \
    -V monofont="DejaVu Sans Mono"

# Cleanup intermediate files
rm -f "$full_book"

# Open the final PDF file
open "$base_dir/$base_dir_name.pdf"