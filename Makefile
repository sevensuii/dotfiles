# Makefile para manejar la configuración de los dotfiles

## Variables
PICOM_PID = $(shell pgrep picom)
QTILE_PID = $(shell pgrep qtile)
KWIN_PID = $(shell pgrep kwin_x11)

help:
	@echo 'Usage: make [target]'
	@echo
	@echo 'Targets:'
	@egrep '^(.+)\:\ ##\ (.+)' ${MAKEFILE_LIST} | column -t -c 2 -s ':#'

## WM commands
change-from-qtile-to-kwin: ## Change from Qtile to Kwin
	@echo 'Changing from Qtile to Kwin'
	systemctl --user disable plasma-custom-wm.service
	systemctl --user unmask plasma-kwin_x11.service
	@echo 'Kwin is enabled and will start on next login'

change-from-kwin-to-qtile: ## Change from Kwin to Qtile
	@echo 'Changing from Kwin to Qtile'
	systemctl --user mask plasma-kwin_x11.service
	systemctl --user enable plasma-custom-wm.service
	@echo 'Qtile is enabled and will start on next login'

stop-qtile-and-start-kwin: ## Stop Qtile and start Kwin
	@echo 'Stopping Qtile and starting Kwin'
	kill -9 ${QTILE_PID} ${PICOM_PID} && kwin_x11 --replace


stop-kwin-and-start-qtile: ## Stop Kwin and start Qtile
	@echo 'Stopping Kwin and starting Qtile'
	kill -9 ${KWIN_PID} && /usr/bin/qtile start && picom


## Dotfiles commands
copy-dotfiles-to-config:
	@echo 'Not for now, SORRY'

copy-lattebars-to-dotfiles:
	cp $HOME/.config/latte/* $HOME/git_repos/dotfiles/qtile_inside_kde/latte/