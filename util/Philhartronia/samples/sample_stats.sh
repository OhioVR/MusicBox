#!/bin/bash

## copyright yourname

## about

## how to use

# stop for errors
set -e 
echo total files:
find Philhartronia -type f | wc -l
du -h Philhartronia
