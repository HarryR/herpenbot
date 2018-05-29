#!/usr/bin/env python
import markovify
import cPickle as pickle
import os
import string

dump_file = 'data/data.pickle'

sources = [
    'data/topics-mumsnet-filtered.txt',
    'data/topics-erowid.txt',
    'data/literotica-all.txt',
]

printable = set(string.printable)

filter_printable = lambda x: filter(lambda y: y in printable, x)

if os.path.exists(dump_file):
    with open(dump_file, 'rb') as handle:
        model = markovify.Text.from_dict(pickle.load(handle))
else:
    print("Generating combined model (once-off)...")
    model = None
    for source_file in sources:
        with open(source_file, 'r') as handle:
            print("Loading", source_file)
            text = filter_printable(handle.read())
            new_model = markovify.Text(text, retain_original=False)
            model = markovify.combine( [model, new_model], [ 1.0, 1.0 ] ) if model else new_model
    with open(dump_file, 'wb') as handle:
        pickle.dump(model.to_dict(), handle)
        handle.flush()

if __name__ == "__main__":
    for i in range(0, 100):
        x = model.make_sentence()
        #x = model.make_sentence_with_start('AIBU')
        #x = model.make_short_sentence(50)
        if x:
            print x
    
