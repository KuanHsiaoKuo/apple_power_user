#!/bin/bash

# It will read the input and:
# [One liner to generate a Markdown TOC | by Andres Rodriguez | Medium](https://medium.com/@acrodriguez/one-liner-to-generate-a-markdown-toc-f5292112fd14)
# 1. Extract only the headers via grep (using $1 and $2 as first and last heading level)
# 2. Extract the header text via sed and created ':' separated records of the form '###:Full Text:Full Text'
# 3. Compose each TOC line via awk by replacing '#' with '  ' and stripping spaces and caps of reference
# TEST:
#   sudo chmod 777 toc_generator.sh
#   curl -s https://raw.githubusercontent.com/felixge/node-mysql/master/Readme.md | ./toc_generator.sh 2 2
# ADD TO COMMAND:
# 1. 将指令添加到alias_collection
# 2. source ~/.zshrc
# 3. curl -s https://raw.githubusercontent.com/felixge/node-mysql/master/Readme.md | toc 2 2

grep -E "^#{${1:-1},${2:-2}} " | \
sed -E 's/(#+) (.+)/\1:\2:\2/g' | \
awk -F ":" '{ gsub(/#/,"  ",$1); gsub(/[ ]/,"-",$3); print $1 "- [" $2 "](#" tolower($3) ")" }'