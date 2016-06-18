# coding=utf-8
from __future__ import absolute_import

import octoprint.plugin

class NeopixelstatusPlugin(octoprint.plugin.StartupPlugin,
                           octoprint.plugin.ProgressPlugin):

    def on_after_startup(self):
        self._logger.info("Hello World, from the neopixel plugin!")

    def on_print_progress(self, storage, path, progress):
        self._logger.info('Storage: {0}, Path: {1}, Progress: {2}'.format(storage, path, progress))


__plugin_name__ = "Neopixelstatus Plugin"
__plugin_implementation__ = NeopixelstatusPlugin()