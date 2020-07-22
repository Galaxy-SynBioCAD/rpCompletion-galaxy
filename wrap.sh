#!/bin/bash

output=$1

tmp=`mktemp --dry-run`
outpath=`dirname $tmp`
outdir=`basename $output`
cd $outpath
mkdir $outdir

python -m rpcompletion "${@:2:3}" $output "${@:5}"

tar czf $outdir.tar.gz $outdir
mv $outdir.tar.gz $output
rm -rf $outdir
