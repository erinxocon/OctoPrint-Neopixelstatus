# coding=utf-8
from __future__ import absolute_import
from . import opc
from . import color_utils
import octoprint.plugin
import octoprint.events
from time import sleep


class NeopixelstatusPlugin(octoprint.plugin.StartupPlugin,
                           octoprint.plugin.ProgressPlugin,
                           octoprint.plugin.EventHandlerPlugin):

    def __init__(self):
        #connect with the opc client (in my case a fadecady)
        self.client = opc.Client('127.0.0.1:7890')

        #constants that will eventually be settings
        self.num_pixels = 30
        self.frame_rate = 1/5
        self.current_progress = 0


    #Startup Plugin Stuff
    def on_startup(self, host, port):
        self._logger.info("Hello World, from the neopixel plugin!")
        self._logger.info('Host: {0}, Port: {1}'.format(host, port))

        #put blank pixels to start with
        self._put_blank_pixels()


    #Progress Plugin stuff
    def on_print_progress(self, storage, path, progress):
        self._logger.info('Storage: {0}, Path: {1}, Progress: {2}'.format(storage, path, progress))
        mapped_value = int(color_utils.remap(progress, 0, 100, 0, self.num_pixels))
        pixels = [(0, 0, 200)] * mapped_value
        self.current_progress = pixels
        self.client.put_pixels(pixels)



    #Event Manager Plugin stuff
    def on_event(self, event, payload):

        if event == octoprint.events.Events.PRINT_STARTED:
            color = (0, 0, 200)
            self._flash(color, 0.5, 3)
            self._put_blank_pixels()
            self._logger.info('Flashed colors, and print started.')

        elif event == octoprint.events.Events.PRINT_DONE:
            color = (0, 200, 0)
            self._flash(color, 0.5, 3)
            self._logger.info('Flashed colors, and print done.')

        elif event == octoprint.events.Events.FILE_SELECTED:
            color = (200, 200, 200)
            self._flash(color, 0.5, 1)
            self._put_blank_pixels()
            self._logger.info('Flashed colors, and file selected.')

        elif event == octoprint.events.Events.PRINT_CANCELLED:
            pixels = [(200, 0, 0)] * self.num_pixels
            self.client.put_pixels(pixels)
            self.client.put_pixels(pixels)
            self._logger.info('Flashed colors, and print cancelled.')

        elif event == octoprint.events.Events.PRINT_PAUSED:
            pixels = [(200, 200, 0)] * self.num_pixels
            self.client.put_pixels(pixels)
            self.client.put_pixels(pixels)
            self._logger.info('Flashed colors, and print paused.')

        elif event == octoprint.events.Events.PRINT_RESUMED:
            self._put_blank_pixels()
            self.client.put_pixels(self.current_progress)
            self.client.put_pixels(self.current_progress)
            self._logger.info('Got current progress, and put the pixels back up.')

    #Helpers

    #Flashes the strip of lights
    def _flash(self, color, delay, flashes):
        i = 0

        self._logger.info('Flashing in progress')

        #Create pixel with inpu color
        pixels = [color] * self.num_pixels

        #simple loop to flash the lights a certain number of times
        while i < flashes:
            self._put_blank_pixels()
            sleep(delay)
            self.client.put_pixels(pixels)
            self.client.put_pixels(pixels)
            sleep(delay)
            i += 1


    #Blanks the strip of pixels
    def _put_blank_pixels(self):
        #create blank pixel array
        blank = [(0, 0, 0)] * self.num_pixels
        self._logger.debug(blank)

        #put pixels twice to avoid dithering and fading
        self.client.put_pixels(blank)
        self.client.put_pixels(blank)
        self._logger.info('blank pixels put')


__plugin_name__ = "Neopixel Status Plugin"
__plugin_implementation__ = NeopixelstatusPlugin()