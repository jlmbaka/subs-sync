__author__ = 'jeanlouis.mbaka'

import unittest
import srt
import os
import datetime


class TestSRT(unittest.TestCase):

    def test_load_srt_with_single_item(self):
        srt_file = 'srt_item.srt'
        expected = srt.Subtitle((1,
                                 '00:01:37,880',
                                 '00:01:41,726',
                                 'Back then, not sleeping,\nI\'d lay awake thinking about women.'))
        actual = srt.load_subtitles(srt_file)[0]
        self.assertEqual(expected, actual)

    def test_load_srt_with_multiple_items(self):
        srt_file = 'srt_three_items.srt'
        expected = [srt.Subtitle((721,
                                  '00:55:42,400',
                                  '00:55:43,561',
                                  'Marty.')),
                    srt.Subtitle((722,
                                  '00:55:58,640',
                                  '00:56:00,847',
                                  'But there were other times,')),
                    srt.Subtitle((723,
                                  '00:56:07,440',
                                  '00:56:11,445',
                                  'I thought I was mainlining\nthe secret truth of the universe.'))]

        actual = srt.load_subtitles(srt_file)
        self.assertListEqual(expected, actual)

    def test_add_60_seconds(self):
        expected = srt.Subtitle((1,
                                 '00:02:38,880',
                                 '00:02:42,726',
                                 'Back then, not sleeping,\nI\'d lay awake thinking about women.'))
        actual = srt.Subtitle((1,
                               '00:01:38,880',
                               '00:01:42,726',
                               'Back then, not sleeping,\nI\'d lay awake thinking about women.'))
        actual.add_time(datetime.timedelta(seconds=60))
        self.assertEqual(expected, actual)

    def test_add_minutes_and_seconds(self):
        expected = srt.Subtitle((1,
                                 '00:14:38,380',
                                 '00:14:42,226',
                                 'Back then, not sleeping,\nI\'d lay awake thinking about women.'))
        actual = srt.Subtitle((1,
                               '00:01:37,880',
                               '00:01:41,726',
                               'Back then, not sleeping,\nI\'d lay awake thinking about women.'))
        actual.add_time(datetime.timedelta(minutes=12, seconds=60.500))
        self.assertEqual(expected, actual)

    def test_subtract_60_seconds(self):
        expected = srt.Subtitle((1,
                                 '00:01:38,380',
                                 '00:01:42,226',
                                 'Back then, not sleeping,\nI\'d lay awake thinking about women.'))
        actual = srt.Subtitle((1,
                               '00:00:38,380',
                               '00:00:42,226',
                               'Back then, not sleeping,\nI\'d lay awake thinking about women.'))
        actual.add_time(datetime.timedelta(seconds=60))
        self.assertEqual(expected, actual)

    def test_write_subtitles_to_file(self):
        filename = 'result.srt'
        expected_subs = [srt.Subtitle((721,
                                  '00:55:42,400',
                                  '00:55:43,561',
                                  'Marty.')),
                    srt.Subtitle((722,
                                  '00:55:58,640',
                                  '00:56:00,847',
                                  'But there were other times,')),
                    srt.Subtitle((723,
                                  '00:56:07,440',
                                  '00:56:11,445',
                                  'I thought I was mainlining\nthe secret truth of the universe.'))]
        srt.write_to_file(filename, expected_subs)
        actual_subs = srt.load_subtitles(filename)
        self.assertEqual(expected_subs, actual_subs)

if __name__ == '__main__':
    unittest.main()