__author__ = 'jeanlouis.mbaka'

import sys, getopt
import os
import re
import time
from dateutil import parser
from datetime import datetime
from datetime import timedelta

class Subtitle():
    """
    Subtitle model - Represents an .srt file unit subtitle

    it is presented as follows:
    sequence_no\n
    start --> end\n
    message
    \n

    A message can be on several lines.
    """

    def to_datetime(self, time_str):
        time_str = time_str.replace(',', '.')
        return parser.parse(time_str)

    # def __init__(self, sequence_no, start, end, message):
    #     self.sequence_no = sequence_no
    #     self.start = self.to_datetime(start)
    #     self.end = self.to_datetime(end)
    #     self.message = message

    def __init__(self, srt_item):
        self.sequence_no = int(srt_item[0])
        self.start = self.to_datetime(srt_item[1])
        self.end = self.to_datetime(srt_item[2])
        self.message = srt_item[3]

    def __str__(self):

        return '{0}\n{1} --> {2}\n{3}\n\n'.format(self.sequence_no,
                                                "{0:02d}:{1:02d}:{2:02d},{3:000d}".format(self.start.hour,
                                                                                     self.start.minute,
                                                                                     self.start.second,
                                                                                     self.start.microsecond//1000),
                                                "{0:02d}:{1:02d}:{2:02d},{3:000d}".format(self.end.hour,
                                                                                     self.end.minute,
                                                                                     self.end.second,
                                                                                     self.end.microsecond//1000),
                                                self.message) #'hr:min:sec,millis

    def __eq__(self, other):
        return isinstance(other, Subtitle) and self.sequence_no == other.sequence_no and self.start == other.start and \
               self.end == other.end and self.message == other.message

    def add_time(self, timedelta):
        self.start += timedelta
        self.end += timedelta

    def subtract_time(self, timedelta):
        self.start -= timedelta
        self.start -= timedelta


def read_srt_file(filename):
    """
    Read the content of an subtitle file (.srt),

    :param filename: srt filename
    :return: the text content of the srt file as a string
    """
    line_number = 0
    text = ""
    with open(filename, encoding='utf-8') as srt_file:
        for a_line in srt_file:
            line_number += 1
            text += a_line
    return text


def write_srt_file(filename, srt):
    """
    Writes a single srt object string representation to the given filename.
    :param filename:
    :param srt:
    :return:
    """
    with open(filename, mode='a', encoding='utf-8') as srt_file:
        srt_file.write(srt.__string__)


def tokenise_srt_text(srt_file_text_content):
    return srt_file_text_content.strip().split('\n\n')


def compile_regex_pattern():
    return re.compile(r'''
            (\d+) # sequence number
            \n # separator
            (\d{2}:\d{2}:\d{2},\d{3})[ ]-->[ ](\d{2}:\d{2}:\d{2},\d{3}) # start time --> end time
            \n # separator
            ([\S*\s*\S*]*) # dialog
        ''', re.VERBOSE)


def load_subtitles(srt_file):

    srt_file_text = read_srt_file(srt_file)
    srt_file_items = tokenise_srt_text(srt_file_text)
    pattern = compile_regex_pattern()

    subtitles = []
    for srt_item in srt_file_items:
        search_results = pattern.search(srt_item)
        if search_results is not None:
            search_results_groups = search_results.groups()
            subtitles.append(Subtitle(search_results_groups))

    return subtitles

def write_to_file(filename, subtitles):
    with open(filename, mode='a', encoding='utf-8') as srt_file:
        for item in subtitles:
            srt_file.writelines(str(item))

if __name__ == '__main__':

    # # source srt and destination srt
    # src_srt = ""
    # dst_srt = ""

    # # Read arguments from the second position
    # argv = sys.argv[1:]

    # target_directory = ""

    # try:
    #     # opts that require argument must be followed by a colon (:) e.g. d:
    #     opts, args = getopt.getopt(argv, "hs:d:D", ["src=", "dst=", "delay="])
    # except getopt.GetoptError:
    #     # Error: print usage
    #     print("sub-sync.py -s <path_to_srt_file> -d <dst_srt> -D <delay_in_milliseconds>")
    #     sys.exit(2)

    # for opt, arg in opts:
    #     if opt == "-h":
    #         # Help: print usage
    #         print("sub-sync.py -s <path_to_srt_file> -d <dst_srt> -D <delay_in_milliseconds>")
    #         sys.exit()
    #     elif opt in ("-d", "--src"):
    #         target_directory = arg
    
    # print("Directory is {0}".format(target_directory))

    src_srt = r'C:\Users\jeanlouis.mbaka\Music\AAA\True.Detective.COMPLETE.S01.Season.1.720p.HDTV.x264-PublicHD\true.detective.s01e06.720p.hdtv.x264-2hd.srt'
    dst_srt = r'C:\Users\jeanlouis.mbaka\Music\AAA\True.Detective.COMPLETE.S01.Season.1.720p.HDTV.x264-PublicHD\true.detective.s01e06.720p.hdtv.x264-2hd.shiffed.srt'

    subtitles = load_subtitles(src_srt)
    for sub in subtitles:
        sub.add_time(timedelta(seconds=59))
    write_to_file(dst_srt, subtitles)