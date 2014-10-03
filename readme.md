# Sublime GotoAnythingEnhanced plugin

Prefill "goto anything" panel with value that likely will be entered to this
panel. Based on https://github.com/FordAldrich/GotoSelection glorious plugin.


### Demo

![Demo](https://github.com/shagabutdinov/sublime-enhanced-demos/raw/master/goto_anything_enhanced.gif "Demo")


### Installation

This plugin is part of [sublime-enhanced](http://github.com/shagabutdinov/sublime-enhanced)
plugin set. You can install sublime-enhanced and this plugin will be installed
automatically.

If you would like to install this package separately check "Installing packages
separately" section of [sublime-enhanced](http://github.com/shagabutdinov/sublime-enhanced)
package.


### WARNING

Because of sublime bug you need to hit "goto line down" after search panel is
appeared and selection were inserted.


### Features

When current selection contains class name it prefills goto anything with class
name. When current selection contains filename (or string that looks like file
name) it prefills goto anything with selected filename.


### Usage

Hit keyboard shortcut to open "goto anything" panel. If selection will contain
class or file name then selected text will be entered in panel.


### Commands

| Description        | Shortcut | Command palette                   |
|--------------------|----------|-----------------------------------|
| Show goto anything | f1       | GotoSelectionEnhanced: Show panel |


### Dependencies

None