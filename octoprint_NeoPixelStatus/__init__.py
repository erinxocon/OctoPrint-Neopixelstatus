# coding=utf-8
from __future__ import absolute_import
from . import opc
from . import color_utils
import octoprint.plugin


class NeopixelstatusPlugin(octoprint.plugin.StartupPlugin,
                           octoprint.plugin.ProgressPlugin):

    def __init__(self):
        self.client = opc.Client('127.0.0.1:7890')
        self.num_pixels = 30
        self.frame_rate = 1/5

    def _put_blank_pixels(self):
        blank = [(0, 0, 0)] * self.num_pixels
        self._logger.debug(blank)
        self.client.put_pixels(blank)
        self.client.put_pixels(blank)
        self._logger.info("blank pixels put")

    def on_after_startup(self):
        self._logger.info("Hello World, from the neopixel plugin!")
        #put blank pixels to start with
        self._put_blank_pixels()

    def on_print_progress(self, storage, path, progress):
        self._logger.info('Storage: {0}, Path: {1}, Progress: {2}'.format(storage, path, progress))


__plugin_name__ = "Neopixelstatus Plugin"
__plugin_implementation__ = NeopixelstatusPlugin()