#!/bin/bash
cd `dirname $0`
mkdir build
cd build

git clone https://github.com/yuji-morita/action-test.git && cd action-test

mkdocs build -d site

tags=$(git tag)
for tag in ${tags[@]}
do
    git checkout refs/tags/$tag > /dev/null 2>&1
    mkdocs build -d site/$tag
done

python3 version.py