# Asus Rog laptop

If you have a Asus, there is still some things to do after configuring Qtile

# Table of contents
- [Asus Rog laptop](#asus-rog-laptop)
- [Table of contents](#table-of-contents)
  - [Nvidia optimus](#nvidia-optimus)
  - [Asus battery command](#asus-battery-command)
  - [Zenpower3](#zenpower3)
  - [TLP](#tlp)
  - [Rogauracore](#rogauracore)

## Nvidia optimus

If the laptop has an Nvidia GPU, you need to install nvidia drivers and optimus manager.

```bash
sudo nvidia nvidia-utils 
paru -S optimus-manager optimus-manager-qt
```

In the file `/etc/optimus-manager/optimus-manager.conf` change the line `startup_mode` to:
    - `hybrid` 
    - `integrated`
    - `nvidia`

## Asus battery command

Battery related stuff and allows to set up the battery charge threshold.

```bash
paru -S bat-asus-battery-bin
```

To set the threshold

```bash
sudo bat-asus-battery --threshold 60
sudo bat-asus-battery --persist
```

## Zenpower3

This is a kernel module that allows us to read more sensors for Ryzen CPUs

```bash
paru -S zenpower3-dkms
```

## TLP

TLP is a power management tool that allows us to set up the CPU governor and other stuff.

```bash
paru -S tlp tlpui
```

## Rogauracore

This is a tool that allows us to control the keyboard backlight and effects for Asus laptops

```bash
paru -S rogauracore-git
```

You can use this script made with `Rofi` to control the keyboard backlight and effects

```bash

```

