# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from typing import List  # noqa: F401

from libqtile import layout, hook, bar
#from libqtile import widget
from qtile_extras import widget
from qtile_extras.bar import Bar
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from qtile_extras.widget.decorations import RectDecoration, BorderDecoration

# Importing keys and colours
from Keybindings import *
from Colours_Decor import *
#from BarThemes import *



from qtile_extras.popup.toolkit import (
PopupRelativeLayout,
PopupImage,
PopupText
)

import os
import subprocess
import psutil
import fontawesome as fa
import functools

# use uname to load diferent modules depending on which machine I'm on
import platform
# machine_name possible values declared as CONST values
LCR084P     = 'lcr084p'     #-> work laptop
EVILCORP    = 'EvilCorp'    #-> ssd usb linux installation
FSOCIETY    = 'fsociety'    #-> personal laptop
machine_name = platform.uname().node


@hook.subscribe.startup
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.run([home])

#groups = [Group(i) for i in "123456789"]

groups = [
    Group("1", label=fa.icons["firefox"]+' '),
    Group("2", label=fa.icons["terminal"]+' '),
    Group("3", label=fa.icons["code"]+' '),
    Group("4", label=fa.icons["database"]+' '),
    Group("5", label=fa.icons["folder"]+' '),
    Group("6", label=fa.icons["github-alt"]+' '),
    Group("7", label=fa.icons["spotify"]+' '),
    Group("8", label = fa.icons["video"]+' '),
    #Group("9", label = fa.icons["firefox"]),
]

for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(
                    i.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )

layouts = [
    #layout.Columns(border_focus_stack=["#d75f5f", "#8f3d3d"], border_width=4),
    #layout.Bsp(margin=8, border_focus="#d75f5f", fair=False, border_on_single=True),
    layout.Columns(border_focus_stack=["#533a7b", "#533a7b"], border_width=3, margin=8, border_focus="#d75f5f"),
    layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    #layout.MonadTall(),
    #layout.Floating(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    #layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font="JetBrains Mono",
    fontsize=16,
    padding=5,
)

##################################
## Bar themes                   ##
##################################

#<|------------------------------- DEFAULT ---------------------------------------|>#
default_theme_widgets = [
    widget.TextBox("", background="#00000000", foreground=foreground_colour_icon, fontsize=28, mouse_callbacks={"Button1" : lazy.spawn("rofi -show drun")}),
    widget.CurrentLayoutIcon(),
    widget.CurrentLayout(**decor_layout, foreground=foreground_colour),
    #widget.CPU(format=fa.icons["microchip"]+" {freq_current}GHz {load_percent}%",**decor_wallpaper),
    widget.CPU(format=fa.icons["microchip"]+" {load_percent}%", foreground=foreground_colour, **decor_CPU),

    ### CPU TEMP WIDGET
    widget.GenPollText(update_interval=5, func=lambda: " {}".format(subprocess.check_output(os.path.expanduser("~/.config/qtile/Scripts/ryzen_cpu_temp")).decode("utf-8")),
                    background="#00000000", foreground=foreground_colour, **decor_Temp) if machine_name in ('EvilCorp','fsociety4fun') else widget.TextBox(""),
    widget.GenPollText(update_interval=5, func=lambda: " {}".format(subprocess.check_output(os.path.expanduser("~/.config/qtile/Scripts/standart_cpu_temp")).decode("utf-8")),
                    background="#00000000", foreground=foreground_colour, **decor_Temp) if machine_name in (LCR084P) else widget.TextBox(""),

    ### RAM WIDGET
    widget.Memory(background="#00000000", foreground=foreground_colour,
                measure_mem='G', format=fa.icons["server"] + "{MemUsed: .2f} GB", **decor_ram),

    ### FAN RPM WIDGET
    widget.GenPollText(update_interval=10, func=lambda: " {} RPM".format(subprocess.check_output(os.path.expanduser("~/.config/qtile/Scripts/fan_speed_text")).decode("utf-8")),
                    background="#00000000", foreground=foreground_colour, **decor_RPM) if machine_name in (EVILCORP,FSOCIETY) else widget.TextBox(""),

    #widget.Net(interface="wlp3s0", background="#00000000", foreground=foreground_colour,
    #            format=fa.icons["wifi"]+" ", **decor_Wifi),
    #widget.Net(interface="wlo1", background="#00000000", foreground=foreground_colour,
    #           format=fa.icons["wifi"]+" {up}", **decor_Wifi),

    # ##### Spacer
    widget.Spacer(length=bar.STRETCH),
    ##### Spacer

    widget.GroupBox(highlight_method="line", highlight_color="#00000000", foreground=foreground_colour,
                    rounded=True, **decor_groupbox, hide_unused=False, active="#000000", margin_x=6,
                    borderwidth=4),

    ##### Spacer
    widget.Spacer(length=bar.STRETCH),
    ##### Spacer

    widget.Prompt(**decor_ram),
    widget.Systray(background="#00000000", icon_size=20),

    ### SYSTEM UPDATES
    # widget.CheckUpdates(background="#00000000", foreground="#FF0000", display_format=' {updates}',
    #                     colour_have_updates="#000000", colour_no_updates="#000000", **decor_ram),
    # Can also use fa.icons["microchip"], fa.icons["chart-bar"]

    ### KEYBOARD LAYOUT WIDGET
    widget.KeyboardLayout(configured_keyboards=['us', 'es'], background='#00000000'), 

    # BATTERY STATUS AND ICONS
    widget.GenPollText(update_interval=1, func=lambda: "{}%".format(subprocess.check_output(os.path.expanduser("~/.config/qtile/Scripts/bat_poll")).decode("utf-8")),
                    background="#00000000", foreground=foreground_colour, **decor_battery) if machine_name in (LCR084P) else widget.TextBox(""),
    # use this when `bat` or `bat-asus-battery` commmands are installed
    widget.GenPollText(update_interval=3, func=lambda: "{}".format(subprocess.check_output(os.path.expanduser("~/.config/qtile/Scripts/bat_poll_asus")).decode("utf-8")),
                    background="#00000000", foreground=foreground_colour, **decor_battery) if machine_name in (EVILCORP,FSOCIETY) else widget.TextBox(""),

    ### CALENDAR AND CLOCK
    widget.Clock(format=fa.icons["calendar"] + " %d-%m-%y %a",
                background="#00000000", foreground=foreground_colour, **decor_Day, mouse_callbacks={"Button1" : lazy.spawn("kalendar")}),
    widget.Clock(format=" %H:%M:%S %p",
                background="#00000000", foreground=foreground_colour, **decor_Date),

    ### POWER MENU
    widget.TextBox("", background="#00000000",foreground=foreground_colour_icon, fontsize=20, mouse_callbacks={"Button1" : lazy.function(show_power_menu)}),
]

#<|------------------------------- ONE DARK ---------------------------------------|>#
one_dark_colors = {
    "background": "1e2127",
    "foreground": "abb2bf",
    "black":      "5c6370",
    "red":        "e06c75",
    "green":      "98c379",
    "yellow":     "d19a66",
    "blue":       "61afef",
    "magenta":    "c678dd",
    "cyan":       "56b6c2",
    "white":      "828791"
}

icon = lambda char, foreground, background: widget.TextBox(
    font="Font Awesome 6 Free Solid",
    text=char,
    background=background,
    foreground=foreground,
)

separator = lambda color: widget.Sep(
    background=color,
    foreground=color,
)

separator_background_color = functools.partial(separator, color=one_dark_colors["background"])

one_dark_widgets = [
    widget.TextBox("", background=one_dark_colors["background"], foreground=foreground_colour_icon, fontsize=28, mouse_callbacks={"Button1" : lazy.spawn("rofi -show drun")}),
    widget.CurrentLayoutIcon(background=one_dark_colors["background"]),
    # icon("", foreground=one_dark_colors["blue"], background=one_dark_colors["background"]),
    #             widget.CurrentLayout(
    #                 background=one_dark_colors["background"],
    #                 foreground=foreground_colour_icon
    #             ),
    # separator(color=one_dark_colors["background"]),
    widget.GroupBox(
                    font="Font Awesome 6 Free Solid",
                    highlight_method="block",
                    this_current_screen_border=one_dark_colors["cyan"],
                    #this_other_screen_border=theme["blue"],
                    #this_current_screen=theme["background"],
                    block_highlight_text_color=one_dark_colors["background"],
                    inactive=one_dark_colors["black"],
                    borderwidth=0,
                    rounded=False,
                    padding_x=10,
                    padding_y=8,
                    margin_x=0
                    #margin=0
                ),

    ## SEPARATOR
    separator(color=one_dark_colors["background"]),
                widget.WindowName(),
    ## SEPARATOR

    ### Timers to keep my working time registry
    ### Timer 1
    widget.GenPollText(update_interval=1, func=lambda: "祥 T1:{}".format(subprocess.check_output(['python',os.path.expanduser(home+'/git_repos/dotfiles/streamdeck_apps/chrono/app.py'),'timer','1','estado']).decode("utf-8")), 
                    background=one_dark_colors["background"], foreground=one_dark_colors['cyan']) if machine_name in (LCR084P,EVILCORP) else widget.TextBox(""),
    widget.GenPollText(update_interval=1, func=lambda: "祥 T2:{}".format(subprocess.check_output(['python',os.path.expanduser(home+'/git_repos/dotfiles/streamdeck_apps/chrono/app.py'),'timer','2','estado']).decode("utf-8")), 
                    background=one_dark_colors["background"], foreground=one_dark_colors['yellow']) if machine_name in (LCR084P,EVILCORP) else widget.TextBox(""),
    separator(color=one_dark_colors["background"]),
    # icon("\ufa1a", background=one_dark_colors["background"], foreground=one_dark_colors["yellow"]),
    #             widget.GenPollText(update_interval=1, func=lambda: "T1{}%".format(subprocess.check_output(os.path.expanduser("~/.config/qtile/timers/app.py timer 1 estado")).decode("utf-8")),
    #                 background=one_dark_colors["background"], foreground=one_dark_colors["white"]),
    # widget.GenPollText(update_interval=1, func=lambda: "{}%".format(subprocess.check_output(os.path.expanduser("python ~/.config/qtile/timers/app.py timer 1 estado"))),
    #                 background=one_dark_colors["background"], foreground=one_dark_colors["white"]) if machine_name in (LCR084P) else widget.TextBox(""),

    widget.Systray(fontsize=12, background=one_dark_colors["background"]),
    
    widget.KeyboardLayout(configured_keyboards=['us', 'es'], background=one_dark_colors["background"]), 

    ### UPDATES
    icon("\uf021", foreground=one_dark_colors["magenta"], background=one_dark_colors["background"]),
                widget.CheckUpdates(
                    distro="Arch",
                    display_format='{updates}', #
                    no_update_string="O.O",
                    colour_no_updates=one_dark_colors["magenta"],
                    colour_have_updates=one_dark_colors["red"],
                    background=one_dark_colors["background"],
                    foreground=one_dark_colors["magenta"]
                ),
    separator(color=one_dark_colors["background"]),

    # separator(one_dark_colors["background"]),
    # icon("\uf1eb", background=one_dark_colors["background"], foreground=one_dark_colors["red"]),
    #             widget.Net(
    #                 format="{down} ↓↑{up}",
    #                 prefix="M",
    #                 foreground=one_dark_colors["red"],
    #             ),
    
    ### RAM
    widget.Memory(measure_mem="G", format=" {MemUsed:.1f}/{MemTotal:.1f} GiB",
                    background=one_dark_colors["background"], foreground=one_dark_colors["green"]),
    separator(color=one_dark_colors["background"]),

    ### CPU USAGE AND TEMP
     icon("\uf2db", background=one_dark_colors["background"], foreground=one_dark_colors["yellow"]),
                 widget.CPU(format="{load_percent:>4.1f}%", background=one_dark_colors["background"], foreground=one_dark_colors["yellow"]),
    widget.GenPollText(update_interval=5, func=lambda: "{}".format(subprocess.check_output(os.path.expanduser(home+"/git_repos_dotfiles/scripts/ryzen_cpu_temp")).decode("utf-8")),
                    background=one_dark_colors["background"], foreground=one_dark_colors["yellow"]) if machine_name in (EVILCORP,FSOCIETY) else widget.TextBox(""),
    widget.GenPollText(update_interval=5, func=lambda: "{}".format(subprocess.check_output(os.path.expanduser(home+"/git_repos_dotfiles/scripts/standart_cpu_temp")).decode("utf-8")),
                    background=one_dark_colors["background"], foreground=one_dark_colors["yellow"]) if machine_name in (LCR084P) else widget.TextBox(""),
                separator(color=one_dark_colors["background"]),

    # BATTERY STATUS AND ICONS
    widget.GenPollText(update_interval=1, func=lambda: "{}%".format(subprocess.check_output(os.path.expanduser(home+"/git_repos_dotfiles/scripts/bat_poll")).decode("utf-8")),
                    background=one_dark_colors["background"], foreground=one_dark_colors["white"]) if machine_name in (LCR084P) else widget.TextBox(""),
    # use this when `bat` or `bat-asus-battery` commmands are installed
    widget.GenPollText(update_interval=3, func=lambda: "{}".format(subprocess.check_output(os.path.expanduser(home+"/git_repos_dotfiles/scripts/bat_poll_asus")).decode("utf-8")),
                    background=one_dark_colors['background'], foreground=one_dark_colors['white']) if machine_name in (EVILCORP,FSOCIETY) else widget.TextBox(""),
    separator(color=one_dark_colors["background"]),

    ### DATE AND TIME
    icon("\uf017", foreground=one_dark_colors["cyan"], background=one_dark_colors["background"]),
                widget.Clock(format="%B %-d, %R", background=one_dark_colors["background"], foreground=one_dark_colors["cyan"]),
    separator(color=one_dark_colors["background"]),

    ### POWER MENU
    widget.TextBox("",background=one_dark_colors["background"],foreground=foreground_colour_icon, fontsize=20, mouse_callbacks={"Button1" : lazy.function(show_power_menu)}),

]

##################################
## End Bar themes               ##
##################################

#<>-----------------------<>  Theme selector  <>-----------------------<>#
actual_theme = one_dark_widgets
#<>-----------------------<>  Theme selector  <>-----------------------<>#


extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            actual_theme,
            27,
            border_width=[0, 0, 0, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"],  # Borders are magenta
            background="#1e2127",
            #margin = [5,5,5,5],
            # opacity=1,
        ),
    ),
]


# Drag floating layouts.
mouse = [
    Drag(["mod1"], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag(["mod1"], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click(["mod1"], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
