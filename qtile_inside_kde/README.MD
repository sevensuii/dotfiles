# Qtile integration into KDE Plasma

I started working on this because I love how tiling window managers behave, but kwin wasn't enough for me, so I found I way to do it :)

For this I'm using Garuda Linux (DRAGONIZED)

In case you need to install KDE Plasma:

```bash
sudo pacman -S xorg plasma kde-applications latte-dock
```

And everything else you need along with Qtile

```bash
sudo pacman -S qtile fish rofi python-dbus unzip python-pip \
    wget kitty starship php composer openvpn xdotool exa nitrogen neofetch \
    bashtop
```
```bash
pip3 install psutil fontawesome dbus-next glances[all] --user
```
```bash
paru -S nerd-fonts-cascadia-code nerd-fonts-fantasque-sans-mono \
    nerd-fonts-jetbrains-mono nerd-fonts-roboto-mono nerd-fonts-ubuntu pfetch \
    qtile-extras-git playerctl picom-jonaburg-git cpupower-gui
```

And the theme is `Sweetified Plasma` or `Sweet Plasma`

### This works for KDE Plasma 5.25 and above


## Disable kwin

First you need prevent kwin from starting so you can start the WM you want

```sh
systemctl --user mask plasma-kwin_x11.service
```

Then create systemd folder for your services

```sh
mkdir -p ~/.config/systemd/user/
```

Now create the service that will start our WM with `vim ~/.config/systemd/user/plasma-custom-wm.service` and add this

```sh
[Install]
WantedBy=plasma-workspace.target

[Unit]
Description=Plasma Custom Window Manager (Qtile)
Before=plasma-workspace.target

[Service]
ExecStart=/usr/bin/qtile start
Slice=session.slice
Restart=on-failure
```

- `ExecStart` is the command to start the WM, in this case Qtile

Now it's time to reload the daemon so our service is now loaded into systemctl

```sh
systemctl daemon-reload --user && systemctl enable plasma-custom-wm.service --user
```

The last thing to do is restart or log out and then you can use Qtile inside KDE

### If you already hava a Qtile config, you'll need to tweak it a bit to work properly

## Setting up the environment

Link necesary config files

```bash
cp -r "$HOME"/git_repos/dotfiles/qtile_inside_kde/qtile "$HOME"/.config/ && \
cp -r "$HOME"/git_repos/dotfiles/qtile_inside_kde/picom "$HOME"/.config/ && \
cp -r "$HOME"/git_repos/dotfiles/qtile_inside_kde/latte/* "$HOME"/.config/latte/ && \
cp -r "$HOME"/git_repos/dotfiles/kitty "$HOME"/.config/ && \
cp -r "$HOME"/git_repos/dotfiles/fish "$HOME"/.config/ && \
cp -r "$HOME"/git_repos/dotfiles/neofetch "$HOME"/.config/ && \
cp -r "$HOME"/git_repos/dotfiles/starship.toml "$HOME"/.config/starship.toml && \
cp -r "$HOME"/git_repos/dotfiles/rofi "$HOME"/.config/ && \
chmod +x "$HOME"/git_repos/dotfiles/qtile_inside_kde/qtile/autostart.sh && \
chmod +x "$HOME"/git_repos/dotfiles/scripts/*
```

## Install KDE widgets

- [Command Output](https://www.pling.com/p/1166510)
- [Currently Playing](https://www.pling.com/p/1821551)

## Disable hidden `Windows Buttons` when maximized

Delete this from `~/.config/kwinrc`
```sh
[Windows]
BorderlessMaximizedWindows=true
```

### In case you're using latte, you need to disable it in latte's config