"""
This module contains all the key maps of my Qtile configuration, the
key maps have been setted up in the most similar way as vim.

For more information check: github.com/pablocorbalann/dotfiles/tree/main/qtile
"""

# Import the packages (just qtile)
from libqtile.config import Key
from libqtile.command import lazy


mod = "mod4" # Mod4 is the "Windows" key, in QWERTY between CTRL/FN and ALT

keys = [Key(key[0], key[1], *key[2:]) for key in [

    # ------------ Window Configs ------------
    # Switch between windows in the current group
    ([mod], "j", lazy.layout.down()),
    ([mod], "k", lazy.layout.up()),
    ([mod], "h", lazy.layout.left()),
    ([mod], "l", lazy.layout.right()),
    # Change window sizes (MonadTall)
    ([mod, "shift"], "l", lazy.layout.grow()),
    ([mod, "shift"], "h", lazy.layout.shrink()),
    # Toggle floating
    ([mod, "shift"], "f", lazy.window.toggle_floating()),
    # Move windows up or down in current stack
    ([mod, "shift"], "j", lazy.layout.shuffle_down()),
    ([mod, "shift"], "k", lazy.layout.shuffle_up()),
    # Toggle between different layouts as defined below
    ([mod], "Tab", lazy.next_layout()),
    ([mod, "shift"], "Tab", lazy.prev_layout()),
    # Close the window
    ([mod], "q", lazy.window.kill()),
    # Switch focus of monitors
    ([mod], "z", lazy.next_screen()),
    ([mod], "z", lazy.prev_screen()),
    # Restart Qtile
    ([mod, "control"], "r", lazy.restart()),
    ([mod, "control"], "q", lazy.shutdown()),
    ([mod], "r", lazy.spawncmd()),

    # ------------ App Configs ------------
    # Menu
    ([mod], "m", lazy.spawn("rofi -show drun")),
    # Window Nav
    ([mod, "shift"], "m", lazy.spawn("rofi -show")),
    # Browser
    ([mod], "b", lazy.spawn("firefox")),
    # File Explorer
    ([mod], "e", lazy.spawn("ranger")),
    # Terminal
    ([mod], "t", lazy.spawn("alacritty")),
    # Redshift
    ([mod], "r", lazy.spawn("redshift -O 2400")),
    ([mod, "shift"], "r", lazy.spawn("redshift -x")),
    # Screenshot
    ([mod], "s", lazy.spawn("scrot ~/screenshots/%Y-%m-%d-%T-screenshot.png ")),

    # ------------ Hardware Configs ------------
    # Volume
    ([], "XF86AudioLowerVolume", lazy.spawn(
        "pactl set-sink-volume @DEFAULT_SINK@ -5%"
    )),
    ([], "XF86AudioRaiseVolume", lazy.spawn(
        "pactl set-sink-volume @DEFAULT_SINK@ +5%"
    )),
    ([], "XF86AudioMute", lazy.spawn(
        "pactl set-sink-mute @DEFAULT_SINK@ toggle"
    )),
    # Brightness
    ([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +10%")),
    ([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 10%-")),
]]
