#!/bin/sh
cat data/topics-mumsnet.txt | cut -f 2- -d '=' | sed -e 's/$/./g' > data/topics-mumsnet-filtered.txt
