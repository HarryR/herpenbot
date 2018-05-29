#!/usr/bin/env python
from os import path
from wordcloud import WordCloud

with open('data/topics-mumsnet-filtered.txt') as handle:
    text = handle.read()

model = WordCloud().generate(text)
img = model.to_image()
img.save('test.jpg')
