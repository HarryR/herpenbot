#!/usr/bin/env python
from __future__ import print_function
import sys
from prompt_toolkit.completion import Completer, Completion
from prompt_toolkit.history import InMemoryHistory
from prompt_toolkit.shortcuts import prompt

from generate import model


trim_word = lambda x: ' '.join(x.split(' ')[:2])


class MyCompleter(Completer):
    def get_completions(self, document, complete_event=None):
        choices = set()
        text = document.text_before_cursor
        if len(text.rstrip(' ')):
            last2 = text.strip(' ').split(' ')[-1]
            spacing = len(text) - len(text.rstrip(' '))
            for _ in range(0, 10):
                try:
                    #print('last2', last2)
                    res = model.make_sentence_with_start(last2, strict=False, tries=50)
                except KeyError:
                    continue
                if res:
                    res = trim_word(res)
                    if res not in choices:
                        choices.add(res)
                        yield Completion(res, -(spacing + len(last2)))
        else:
            for _ in range(0, 10):
                res = model.make_sentence()
                if res:
                    res = trim_word(res)
                    if res not in choices:
                        choices.add(res)
                        yield Completion(res, 0)


def main():
    options = {
        'history': InMemoryHistory(),
        'completer': MyCompleter(),
        'message': u'shitpost> ',
    }
    isatty = sys.stdin.isatty()
    if isatty:
        def get_command():
            return prompt(**options)
    else:
        get_command = sys.stdin.readline

    while True:
        try:
            command = get_command()
        except KeyboardInterrupt:
            continue
        except EOFError:
            break
        
        if not command:
            if isatty:
                continue
            else:
                break

        print("Command is", command)


if __name__ == "__main__":
    main()

