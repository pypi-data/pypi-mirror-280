#!/bin/bash

# Configuration base dir has chapters sorted by number
base_dir=$1
base_dir_name=$(basename $base_dir)
config_json=$2

chapter_files=$(ls $base_dir/*.md | sort -V)

# Create a temporary file for intermediate processing

# full_book=$(base_dir)/$base_dir_name.md
# /Users/syrkis/.pyenv/versions/3.11.7/lib/python3.11/site-packages/esch/scripts/book.sh: line 15: /decarbonizer.md: Read-only file system
# fix
full_book=$(mktemp).md

for file in $chapter_files; do
    cat $file >> $full_book
done

# Convert the Markdown files to LaTeX with Pandoc
pandoc $full_book -o $base_dir/$base_dir_name.tex \
    --biblatex \
    --slide-level=3 \
    --filter=pandoc-crossref

# Compile the LaTeX file with pdflatex and biber
pdflatex $base_dir/$base_dir_name.tex
biber $base_dir/$base_dir_name
pdflatex $base_dir/$base_dir_name.tex
pdflatex $base_dir/$base_dir_name.tex

# Cleanup intermediate files
rm -f $base_dir/$base_dir_name.{aux,log,nav,out,snm,toc,bcf,blg,run.xml,bbl,tex} $full_book > /dev/null 2>&1

# Open the final PDF file
open $base_dir/$base_dir_name.pdf


