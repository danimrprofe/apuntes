# Alias para bash



##  Alias para DIRECTORIOS
```
alias .4='cd ../../../../'
alias .5='cd ../../../../..'
alias ag='cat .bash_aliases .bashrc .bash_functions | grep alias | grep'
alias alert='notify-send --urgency=low -i "$([ $? = 0 ] && echo terminal || echo error)" "$(history|tail -n1|sed -e '\''s/^\s*[0-9]\+\s*//;s/[;&|]\s*alert$//'\'')"'
alias c='clear'
alias ..='cd ..'
alias ...='cd ../../../'
alias ....='cd ../../../../'
alias .....='cd ../../../../'
alias cd.='cd ..'
alias cd..='cd ..'
alias CD='cd'
alias home='cd ~ && ll;'
```
## alias cleanPC='sudo apt-get -y autoclean && sudo apt-get -y clean && sudo apt-get -y autoremove'
```
alias display='eog -w'
alias e='exit'
alias egrep='egrep --color=auto'
alias emptyDir='find . -empty -type d -delete'
alias fgrep='fgrep --color=auto'
```
## alias -g A="| awk"
## alias -g C="| wc -l"
## alias -g G="| grep"
## alias -g H="| head"
## alias -g L="| less"
alias grep='grep --color=auto'
## alias -g S="| sed -e"
## alias -g T="| tail"

##  Alias HISTORY

```
alias hg='history | sort -u | grep'
alias h='history'

alias install='sudo apt-get -y install'
alias ipa='ip a | grep "inet "'
alias killfirefox="pkill -9 firefox"
alias killslack="pkill -9 slack"
```
##  Alias LS
```
alias la='ls -A'
alias lh='ls -lh'
alias light='xbacklight -set'
alias links='links2'
alias ll='ls -FGlAhp'
alias l='ls -CF'
alias lsdir='ls -ld */'
alias ls='ls --color=auto'
```
alias media='sshfs -o reconnect media@192.168.1.10:/mnt /home/"${USER}"/mnt/media_srv'
alias meng='cd ${HOME}/Dropbox/MEng_Stuff/MEng-Progress'


alias paux='ps aux | grep'
alias pg='ping -c 5 www.google.com'

##  Alias de RED
```
alias port='netstat -tulanp'
alias q='exit'
alias reboot='sudo shutdown -r now'
alias rm='rm -rvi'
alias search-installed='sudo dpkg --get-selections '
alias search='sudo apt search'
alias shutdown='sudo shutdown -h now'
alias shut='sudo shutdown now'
alias snano='sudo nano'
```
##  Alias para SERVICIOS
```
alias ssr='sudo systemctl restart'
alias sss='sudo systemctl status'
alias sstart='sudo systemctl start'
alias sstop='sudo systemctl stop'
```

##  Alias para LOGS
```
alias t10='tail -10'
alias t50='tail -50'
alias tf='tail -f'
alias t='tree -uRD'
alias uninstall='sudo apt-get --purge autoremove '
alias update='sudo apt -y update'
alias upgrade-pips='sudo pip freeze --local | grep -v '^\-e' | cut -d = -f 1  | xargs -n1 sudo pip install -U
alias upgrade='sudo apt-get -y update && sudo apt-get -y --allow-unauthenticated upgrade && sudo apt-get autoclean && sudo apt-get autoremove && exit 0'
    ## alias vdir='vdir --color=auto'
alias youtube="youtube-dl"
##  Apt
ccd() { builtin cd "$@" && clear && pwd && ll; }
        echo
        echo -e "\nAdditionnal information:$NC " ; uname -a
        echo -e "\n${RED}Current date :$NC " ; date
        echo -e "\n${RED}Current network location :$NC " ; scselect
        ## echo -e "\n${RED}DNS Configuration:$NC " ; scutil --dns
        echo -e "\n${RED}Machine stats :$NC " ; uptime
        echo -e "\n${RED}Public facing IP Address :$NC " ;myip
        echo -e "\n${RED}Users logged on:$NC " ; w -h
        echo -e "\nYou are logged on ${RED}$HOST"
##  Editores de texto
##  enable color support of ls and also add handy aliases
fi
if [ -x /usr/bin/dircolors ]; then
    ii() {
##    ii:  display useful host related informaton
##  Install and Remove Packages
##  Log into to Server
##  Network Start, Stop, and Restart
##  Redefinir para pedir confirmación
##  some more ls aliases
    test -r ~/.dircolors && eval "$(dircolors -b ~/.dircolors)" || eval "$(dircolors -b)"
##  Useful Alias
