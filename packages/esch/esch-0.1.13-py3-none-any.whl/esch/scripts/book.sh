#!/bin/bash

# Configuration base dir has chapters sorted by number
base_dir=$1
config_json=$2

chapter_files=$(ls $base_dir/*.md | sort -V)

# Create a temporary file for intermediate processing
chapter_files_tmp=$(mktemp)
for file in $chapter_files; do
    echo $file >> $chapter_files_tmp
done

# Convert the Markdown files to LaTeX with Pandoc
pandoc $(cat $chapter_files_tmp) -o $base_dir/book.tex \
    --biblatex \
    --slide-level=3 \
    --filter=pandoc-crossref

# Compile the LaTeX file with pdflatex and biber
pdflatex $base_dir/book.tex
biber $base_dir/book
pdflatex $base_dir/book.tex
pdflatex $base_dir/book.tex

# Cleanup intermediate files
rm -f $base_dir/book.{aux,log,nav,out,snm,toc,bcf,blg,run.xml,bbl,tex} $chapter_files_tmp > /dev/null 2>&1

# Open the final PDF file
open $base_dir/book.pdf

