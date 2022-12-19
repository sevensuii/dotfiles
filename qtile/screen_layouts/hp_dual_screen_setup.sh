#!/bin/sh
#xrandr --newmode "1920x1080_60.00"  172.80  1920 2040 2248 2576  1080 1081 1084 1118  -HSync +Vsync
#xrandr --addmode VIRTUAL1 1920x1080_60.00
#xrandr --output eDP1 --mode 1920x1080 --pos 0x0 --rotate normal --output DP1 --off --output DP2 --off --output DP3 --off --output DP4 --off --output HDMI1 --primary --mode 2560x1440 -r 144 --pos 1920x0 --rotate normal --output VIRTUAL1 --mode 1920x1080_60.00 --pos 4480x0  --rotate normal --output VIRTUAL2 --off
xrandr --output eDP-1 --mode 1920x1080 --pos 0x0 --rotate normal --output DP-1 --off --output DP-2 --off --output DP-3 --off --output DP-4 --off --output HDMI-1 --primary --mode 2560x1440 -r 144 --pos 1920x0 --rotate normal

#                           ____________________________________
#                          |                                    |
#    ____________________  |                                    |
#   |                    | |                                    |
#   |                    | |                                    |
#   |                    | |           27" lg monitor           |
#   |                    | |                                    |
#   |______ LAPTOP ______| |                                    |
#   |                    | |                                    |
#   |____________________| |____________________________________|
#
