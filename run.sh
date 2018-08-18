#!/usr/bin/env bash

# ./run.sh first last
# ./run.sh Soramichi Akiyama

first=$1
last=$2

filename="dblp_${first}_${last}.lsp"
echo $filename
cp dblp.lsp $filename
sed -e "s/##first##/${first}/g" -i $filename
sed -e "s/##last##/${last}/g" -i $filename

./data_retrieve.py $first $last
gcl -load $filename

rm -f ${first}_${last}_data.lsp
rm -f $filename
