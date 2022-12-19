from typing import List  # noqa: F401

from libqtile import layout, hook, bar
#from libqtile import widget
from qtile_extras import widget
from qtile_extras.bar import Bar
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from qtile_extras.widget.decorations import RectDecoration, BorderDecoration

import os
import subprocess
import psutil
import fontawesome as fa

mod = "mod4"
# terminal = guess_terminal()
# terminal = "gnome-terminal"
# terminal = "alacritty"
# terminal = 'tabby'
terminal = 'kitty'
browser = "brave"
# file_manager = "nemo"

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Change keyboard layout
    # Key([mod], "space", lazy.widget["keyboardlayout"].next_keyboard(), desc="Next keyboard layout."),

    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    #Key([mod], "space", lazy.layout.next(),
    #    desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    Key([mod], "Left", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "Right", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "Down", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "Up", lazy.layout.up(), desc="Move focus up"),

    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(),
        desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(),
        desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "Left", lazy.layout.shuffle_left(),
        desc="Move window to the left"),
    Key([mod, "shift"], "Right", lazy.layout.shuffle_right(),
        desc="Move window to the right"),
    Key([mod, "shift"], "Down", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "Up", lazy.layout.shuffle_up(), desc="Move window up"),
    
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "Left", lazy.layout.grow_left(),
        desc="Grow window to the left"),
    Key([mod, "control"], "Right", lazy.layout.grow_right(),
        desc="Grow window to the right"),
    Key([mod, "control"], "Down", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "Up", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    
    # Apps laucher and selector of active windows
    # I keep this because I also use powertoys on windows
    Key(["mod1"], "space", lazy.spawn(
        "rofi -show drun"), desc="Launch Rofi"),
    Key(['mod1'], 'Tab', lazy.spawn(
        'rofi -show'), desc='Rofi show open apps'),
    
    # Switch focus of monitors
    Key([mod], "period", lazy.prev_screen()),
    Key([mod], "comma", lazy.next_screen()),
    
    # Screenshots (using KDE default)
    # Key([], "Print", lazy.spawn(
    #     "flameshot gui"), desc="Lauch Flameshot GUI"),
    # Key([mod], 'Print', lazy.spawn(
    #     'flameshot screen'), desc='Takes screenshot of current screen'),
    # Key([mod, 'shift'], 'Print', lazy.spawn(
    #     'flameshot full'), desc='Takes screenshot of the entire workspace'),
    
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "shift"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control", 'shift'], "r", lazy.restart(), desc="restart Qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    #Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    
    Key([], "XF86Launch3", lazy.spawn(os.path.expanduser("~/.config/qtile/Scripts/rog_kb_menu")), desc="Keyboard RBG controll"),
    Key(["mod1"], "w", lazy.spawn(os.path.expanduser("~/.config/qtile/Scripts/wifi_menu")), desc="Launch Wi-fi menu script")]
