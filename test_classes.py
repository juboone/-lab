import unittest
from classes import *


class Television(unittest.TestCase):

    def test_television_defaults(self):
        tv = Television()
        assert tv.status == False
        assert tv.channel == 0
        assert tv.volume == 0

    def test_television_power(self):
        tv = Television()
        tv.power()
        assert tv.status == True
        tv.power()
        assert tv.status == False

    def test_television_channel_up(self):
        tv = Television()
        tv.power()
        tv.channel_up()
        assert tv.channel == 1
        tv.channel_up()
        assert tv.channel == 2
        tv.channel_up()
        assert tv.channel == 0

    def test_television_channel_down(self):
        tv = Television()
        tv.power()
        tv.channel_down()
        assert tv.channel == 3
        tv.channel_down()
        assert tv.channel == 2
        tv.channel_down()
        assert tv.channel == 0

    def test_television_volume_up(self):
        tv = Television()
        tv.power()
        tv.volume_up()
        assert tv.volume == 1
        tv.volume_up()
        assert tv.volume == 2
        tv.volume_up()
        assert tv.volume == 2

    def test_television_volume_down(self):
        tv = Television()
        tv.power()
        tv.volume_down()
        assert tv.volume == 0
        tv.volume_down()
        assert tv.volume == 0
        tv.volume_down()
        assert tv.volume == 0

if __name__ == '__main__':
    unittest.main()
