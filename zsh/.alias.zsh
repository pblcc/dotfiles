# This file stores all the aliases of zsh
# github.com/pablocorbalann/dotfiles
alias zshconfig="source ~/.zshrc"
alias ohmyzshconfig="source ~/.oh-my-zsh"
alias functionsconfig="source ~/.functions"
alias l="ls -la"
alias c="clear"
alias t="tree"
alias v="vim"
alias p="python3.9"
alias bp="bpython3"
alias s="sudo"
alias please="sudo su"
alias pls="sudo su"
alias vv="echo 'w'"
alias r="rm -rf"
alias project="cd ~/project && tree"
alias new-project="rm -rf ~/project && mkdir ~/project && cd ~/project"
alias clean-project="cd ~/project && rm -rf *"
alias remove-project="cd .. && rm -rf ~/project"
alias copy='xclip -sel c < '
alias olive='cd ~/yt && chmod +x olive.AppImage && ./olive'
alias sa="sudo apt"
alias sag="sudo apt get"
alias sai='sudo apt install'
alias sagi='sudo apt-get install'
alias sagu="sudo apt-get update"
alias proton='protonvpn-cli'
alias proton-dsw='protonvpn-cli ks --off'
alias proton-esw='protonvpn-cli ks --always-on'
alias bwl='bitwarden list items'
alias bws='chmod +x ~/.bw/bw.AppImage && cd ~/.bw/ && ./bw.AppImage'
alias dotfiles=cd ~/github/dotfiles=''
alias i='sudo dpkg -i'
alias b='bash'
alias wifi='nmcli dev wifi'
alias mvgh='cd ~/github'
alias dja='django-admin'
alias show='cat'
alias etcher='cd ~/.balena && chmod +x etcher.AppImage && ./etcher.AppImage'
alias space='lsblk'
alias raspberry='mv ~/raspberry-pi && rpi-imager'
alias layout='setxkbmap'
alias pac='sudo pacman -S'
alias screenshot='import -window root pause 10 screenshot/%H-%M-%d%m%y.png'
alias export_path_bin='export PATH=/home/pablo/.local/bin:/sbin:/bin:/usr/local/sbin:/usr/local/bin:/usr/bin:/usr/sbin:/usr/bin/site_perl:/usr/bin/vendor_perl:/usr/bin/core_perl'
alias change_theme='bash ~/scripts/change_theme.sh'
alias copy='xclip -sel c <'
alias sound='alsamixer'
alias dots='cd ~/.dotfiles'
alias pyct='export PATH=/home/pablo/.local/bin:/home/pablo/.cargo/bin:/sbin:/bin:/usr/local/sbin:/usr/local/bin:/usr/bin:/usr/sbin:/usr/lib/jvm/default/bin:/usr/bin/site_perl:/usr/bin/vendor_perl:/usr/bin/core_perl:/var/lib/snapd/snap/bin && pycritty'
alias sc='import -window root -pause 10'
