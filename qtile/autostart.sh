#!/bin/bash

cd ~/.config/qtile/

## Using feh to set the background on startup
# You can uncomment the line below, if you are doing the setup on your own.
# If you are running the setup script, it will add this line.
# feh --bg-scale <Path_To_Dotfiles>/Dotfiles/Wallpapres/5120x2880.jpg

## Using nitrogen to set wallpaper on startup
#nitrogen --restore &

## Starting compton compositor on startup for transparency
# If transparency is not working, try with vsync
picom &

#################################
# Start pulseaudio #            #
####################            #
                                #
pulseaudio --start              #
                                #
#################################

#################################################################################################
# Start polkit authentication agent #
#####################################

lxpolkit &
#nitrogen --set-scaled /home/sevensuii/Git-Repos/Dotfiles/Wallpapers/Mountains.jpg --save
feh --bg-scale ./Wallpapers/unix.jpg &

#################################################################################################

#############################
# NM Wifi applet #          #
##################          #
                            #
nm-applet &                 #
                            #
#############################

#####################################################################################
# Mousepad options #
####################

xinput --set-prop 'ASUE120A:00 04F3:319B Touchpad' 'libinput Tapping Enabled' 1
xinput --set-prop 'ELAN0709:00 04F3:31BF Touchpad' 'libinput Tapping Enabled' 1

#####################################################################################

#########################################################
# Screen options #
##################

./screen_layouts/auto_screen_selector.sh &
#~/.screenlayout/asus_dual_external_monitor.sh &

######################                                  
# End Screen options #                                                                 
#########################################################

#################################################
# Optimus manager graphical interface #
#######################################

optimus-manager-qt &

#################################################

#############################################
# Keyboard RGB initialization #
###############################

./Scripts/kb_start &

#############################################

#################################################################
# Streamdeck #
##############
num_proceses=$(ps -ef | grep streamdeck | wc -l)
# check if $num_proceses is less or equal to 1
if [ $num_proceses -le 1 ]; then
    streamdeck --no-ui &
fi
# deckmaster -deck /home/sevensuii/streamdeck_config/page1.deck &

#################################################################
