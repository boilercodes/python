#!/usr/bin/env bash
while getopts a:d:n: flag
do
    # shellcheck disable=SC2220
    case "${flag}" in
        a) author=${OPTARG};;
        d) description=${OPTARG};;
        n) name=${OPTARG};;
    esac
done

TitleCaseConverter() {
    sed 's/.*/\L&/; s/[a-z]*/\u&/g' <<<"$1"
}

folder="${name,,}"
folder="${folder//-/_}"

title="${folder//_/ }"
title="$(TitleCaseConverter "$title")"

repo="$author/$name"

# Change pyproject.toml
sed -i "s|rmenai-blueprints/python|$name|g" pyproject.toml # Separator is |
sed -i "s/My Python template/$description/g" pyproject.toml # Remove description
sed -i "s/rmenai <rami.menai@outlook.com>/$author/g" pyproject.toml # Replace authors

# Change LICENSE
sed -i "s/python-structure/$name/g" LICENSE

# Change SECURITY.md
sed -i "s/rmenai/$author/g" SECURITY.md

# Change .github/pull_request_template.md
sed -i "s|rmenai/python-structure|$repo|g" .github/pull_request_template.md

# Change README.md
cp -f .github/temp/README.md README.md # Override file
sed -i "s/{title}/$title/g" README.md
sed -i "s/{description}/$description/g" README.md
sed -i "s|{repo}|$repo|g" README.md # Separator is |
