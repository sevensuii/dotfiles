#!/bin/bash 

machine_name=$(cat /etc/hostname)

echo $machine_name
 cd ~/.config/qtile/screen_layouts/

### Known computers
LCR084P='lcr084p'
EVILCORP='EvilCorp'
FSOCIETY='fsociety'

### Screen outputs
CONNECTED='connected';
DISCONNECTED='disconnected'
HDMI=$(xrandr | grep HDMI | cut -d ' ' -f 2);
DP1=$(xrandr | grep DP-1-0.8 | cut -d ' ' -f 2);

if [[ $EVILCORP == $machine_name ]]; then 
    if [[ ($CONNECTED == $HDMI) && ($CONNECTED == $DP1) ]]; then 
        notify-send ' Aplicando configuracion para HDMI y DP'
        ./asus_dual_external_monitor.sh 
        #./asus_triple_monitor.sh
    elif [[ ($CONNECTED == $HDMI) && ($DISCONNECTED == $DP1) ]]; then
        notify-send ' solo hdmi esta conectado'
    elif [[ ($DISCONNECTED == $HDMI) && ($DISCONNECTED == $DP1) ]]; then
        notify-send ' Aplicando configuracion para solo portatil'
        ./asus_one_laptop_monitor.sh
    fi
elif [[ $LCR084P == $machine_name ]]; then
    if [[ $CONNECTED == $HDMI ]]; then
        notify-send ' Aplicando configuracion para HDMI'
        ./hp_dual_screen_setup.sh
    else 
        notify-send ' Aplicando configuracion para solo portatil'
        ./hp_one_laptop_monitor.sh
    fi
fi
