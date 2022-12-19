# Sevensuii's dotfiles
This is a collection of my dotfiles. I use them to configure my system. I use Arch Linux, but most of the dotfiles should work on other distros as well.

# Table of contents
- [Sevensuii's dotfiles](#sevensuiis-dotfiles)
- [Table of contents](#table-of-contents)
  - [Preview](#preview)
    - [Qtile with Arch linux](#qtile-with-arch-linux)
    - [Qtile integrated with KDE Plasma](#qtile-integrated-with-kde-plasma)
  - [Installation](#installation)
    - [Create all sym links](#create-all-sym-links)
    - [Make necesary scripts executable](#make-necesary-scripts-executable)
    - [Installation of required packages](#installation-of-required-packages)
    - [Installation required pip packages](#installation-required-pip-packages)
    - [AUR packages](#aur-packages)
    - [Compositor](#compositor)
    - [Shell](#shell)
    - [Login manager (SDDM)](#login-manager-sddm)
    - [Audio](#audio)
    - [Adding user to video group](#adding-user-to-video-group)
    - [End of installation](#end-of-installation)
  - [Keybindings](#keybindings)
  - [Software used](#software-used)


## Preview
---

### Qtile with Arch linux
![Qtile preview 1](https://)

![Qtile preview 2](https://)

### Qtile integrated with KDE Plasma

![Qtile integrated with KDE Plasma 1](https://)

![Qtile integrated with KDE Plasma 2](https://)

## Installation
---

**If you want to use the KDE version, head to [this document](https://)**

Clone the repository

```bash
git clone https://github.com/sevensuii/dotfiles.git
```

I prefer to use sym links to keep changes in the repository, but you can copy the files if you want.

### Create all sym links

```bash
ln -sf "${HOME}"/git_repos/dotfiles/cava "${HOME}"/.config/cava & \
ln -sf "${HOME}"/git_repos/dotfiles/dunst "${HOME}"/.config/dunst & \
ln -sf "${HOME}"/git_repos/dotfiles/config.fish "${HOME}"/.config/fish/config.fish & \
ln -sf "${HOME}"/git_repos/dotfiles/kitty "${HOME}"/.config/kitty & \
ln -sf "${HOME}"/git_repos/dotfiles/neofetch "${HOME}"/.config/neofetch & \
ln -sf "${HOME}"/git_repos/dotfiles/qtile "${HOME}"/.config/qtile & \
ln -sf "${HOME}"/git_repos/dotfiles/starship.toml "${HOME}"/.config/starship.toml
```

### Make necesary scripts executable

```bash
chmod +x "${HOME}"/git_repos/dotfiles/qtile/autostart.sh & \
chmod +x "${HOME}"/git_repos/dotfiles/qtile/Scripts/*
```

### Installation of required packages

```bash
sudo pacman -Syyu neofetch htop nitrogen xorg fish rofi qtile dunst \
    python-dbus linux-headers base base-devel p7zip unzip tar python-pip \
    papirus-icon-theme cmatrix pamixer feh alsa-utils pavucontrol alacritty \
    git vim curl flameshot pulseaudio playerctl scrot ttf-fantasque-sans-mono \
    brightnessctl bc bashtop acpi github-cli wget shfmt lxsession nautilus kitty \
    starship php composer nano network-manager-applet openvpn gnome-keyring sysstat \
    xdotool arandr
```


### Installation required pip packages

```bash
pip3 install psutil fontawesome dbus-next --user
```

### AUR packages

My aur helper is paru, but you can use any other.

If you want to use paru, install it with (you need to have rust installed):

```bash
git clone https://aur.archlinux.org/paru.git
cd ./paru
makepkg -si
```

Install the AUR packages:

```bash
# Installing lsd, exa and qtile-extras
paru -S -S lsd exa qtile-extras-git
# Installing JetBrains Mono Font, Cascadia Code and all Nerd Fonts
paru -S nerd-fonts-cascadia-code nerd-fonts-fira-code nerd-fonts-fantasque-sans-mono nerd-fonts-jetbrains-mono \
    nerd-fonts-roboto-mono nerd-fonts-ubuntu
# Installing pipes.sh, cava and brave-nightly-bin
paru -S pipes.sh cava brave-nightly-bin
# Installing pfetch as the fetch tool
paru -S pfetch
```

Now make `vol_script` executable:

```bash
sed -i "s|    icon_path = .*|    icon_path = $HOME/.config/dunst/icons|" "${HOME}"/.config/dunst/dunstrc
```

### Compositor

For this installation I like to use picom jonaburg's fork

```bash
paru -S picom-jonaburg-git
ln -sf "${HOME}"/git_repos/dotfiles/picom/jonaburg_picom.conf "${HOME}"/.config/picom/picom.conf
```

### Shell

My default shell is fish, skip if you want to use bashor any other shell.

```bash
chsh -s /usr/bin/fish
```

### Login manager (SDDM)

```bash
sudo pacman -S sddm
paru -S sddm-theme-sugar-candy-git
sudo sed -i 's/Current=.*/Current=Sugar-Candy/' /usr/lib/sddm/sddm.conf.d/default.conf
sudo systemctl enable sddm.service
```

### Audio 

Enable the pulseaudio service if it's not enabled:

```bash
systemctl --user enable pulseaudio
```

### Adding user to video group

```bash
sudo usermod -aG video "$USER"
```

### End of installation

Reboot the system and enjoy your new setup.

## Keybindings
---

## Software used
---
| Software                                                                          | Description            |
|-----------------------------------------------------------------------------------|------------------------|
| [networkmanager](https://wiki.archlinux.org/title/NetworkManager)                 | Self explanatory       |
| [network-manager-applet](https://wiki.archlinux.org/title/NetworkManager)         | NetworkManager systray |
| [pulseaudio](https://wiki.archlinux.org/title/PulseAudio)                         | Self explanatory       |
| [pavucontrol](https://archlinux.org/packages/extra/x86_64/pavucontrol)            | Pulseaudio GUI         |
| [brightnessctl](https://archlinux.org/packages/community/x86_64/brightnessctl)    | Brightness control     |
| [dunst](https://wiki.archlinux.org/title/Dunst)                                   | Notifications          |
| [rofi](https://wiki.archlinux.org/title/Rofi)                                     | Application launcher   |
| [qtile](https://wiki.archlinux.org/title/Qtile)                                   | Window manager         |
| [kitty](https://wiki.archlinux.org/title/Kitty)                                   | Terminal emulator      |
| [neofetch](https://archlinux.org/packages/community/any/neofetch/)                | System info            |
| [nautilus](https://wiki.archlinux.org/title/Nautilus)                             | File manager           |
| [picom](https://wiki.archlinux.org/title/Picom)                                   | Compositor             |
| [flameshot](https://archlinux.org/packages/community/x86_64/flameshot/)           | Screenshot tool        |

