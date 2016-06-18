/*
 * View model for OctoPrint-Neopixelstatus
 *
 * Author: Erin O'Connell
 * License: MIT
 */
$(function() {
    function NeopixelstatusViewModel(parameters) {
        var self = this;

        // assign the injected parameters, e.g.:
        // self.loginStateViewModel = parameters[0];
        // self.settingsViewModel = parameters[1];

        // TODO: Implement your plugin's view model here.
    }

    // view model class, parameters for constructor, container to bind to
    OCTOPRINT_VIEWMODELS.push([
        NeopixelstatusViewModel,

        // e.g. loginStateViewModel, settingsViewModel, ...
        [ /* "loginStateViewModel", "settingsViewModel" */ ],

        // e.g. #settings_plugin_NeoPixelStatus, #tab_plugin_NeoPixelStatus, ...
        [ /* ... */ ]
    ]);
});
