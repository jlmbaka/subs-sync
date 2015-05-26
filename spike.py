__author__ = 'jeanlouis.mbaka'

import re

if __name__ == '__main__':

    split_test_str = 'abc 123\n\ndef 456\n\n\tbonjour\nca va?'
    print(split_test_str.split('\n\n'))

    text = "1\n00:01:37,880 --> 00:01:41,726\nBack then, not sleeping,\nI'd lay awake thinking about women.\n\n"

    seq = '10\n2\n 00:01:37,880 --> 00:01:41,726\n'
    seq_pattern = re.compile(r'(\d+)\n')
    print(seq_pattern.search(seq).groups())

    time = '00:01:37,880 --> 00:01:41,726\n'
    time_pattern = re.compile(r'(\d{2}:\d{2}:\d{2},\d{3})[ ]-->[ ](\d{2}:\d{2}:\d{2},\d{3})\n')
    print(time_pattern.search(time).groups())

    sentence = "00:01:37,880 --> 00:01:41,726\n Back then,  not sleeping,\n I'd lay awake thinking about women.\n\n 2"
    save = r'([[]*[\S]*[ ]*]+\n]*)'
    save2 = r'([\S*\s*\S*]*)'
    dialog_pattern = re.compile(r'([\S*\s*\S*]*)')
    print(dialog_pattern.search(sentence).groups())

    # srt_pattern = re.compile(r'''
    #     (\d+) # sequence number
    #     \n # separator
    #     (\d{2}:\d{2}:\d{2},d{3}) --> (\d{2}:\d{2}:\d{2},d{3})
    #     \n
    #     ([[\W][ ]]*) #sentence
    #     \n{2} # end of subtitle sequence
    #     ''', re.VERBOSE)
    # res = srt_pattern.search(text).groups()

    # phonePattern = re.compile(r'^(\d{3})\D+(\d{3})\D+(\d{4})\D+(\d+)$')
    # res = phonePattern.search('800 555 1212 1234').groups()
    # print(res)