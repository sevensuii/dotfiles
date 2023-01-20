#!/bin/bash

cd ~/.config/qtile/

## Background
# feh --bg-scale ./Wallpapers/unix.jpg &
nitrogen --restore &

## Compositor
picom &

## Optimus manager
#optimus-manager-qt &

## Asus ROG RGB keyboard

## Change keyboard layouts
#setxkbmap -layout us,es 
#setxkbmap -option 'grp:meta_space_toggle'

## Kill plasmashell starting windows
#pid_plasmashell=$(pgrep plasmashell)
#kill $pid_plasmashell
#
glances -w --disable-webui &

## Streamdeck
# num_proceses=$(ps -ef | grep streamdeck | wc -l)
# # check if $num_proceses is less or equal to 1
# if [ $num_proceses -le 1 ]; then
#     streamdeck --no-ui &
# fi
