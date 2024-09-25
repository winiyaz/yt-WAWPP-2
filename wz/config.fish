# Location of this is https://snips.sh/f/leQYOwBiIc
# You will call i for writing wih this code
# curl https://snips.sh/f/leQYOwBiIc > ~/.config/fish/config.fish
starship init fish | source

# --- This section is for fish --- #

# This is the exa command
alias e="exa -labBghHimnSuU --git --icons --octal-permissions --icons --color-scale --color=always --group-directories-first"

# Command Aliases
alias e="exa -labBghH --git --octal-permissions --icons --color-scale --color=always --group-directories-first"
alias el="exa -labBghHimnSuU --git -@ --octal-permissions --icons --color-scale --color=always --group-directories-first"
alias fzf="fzf --preview 'bat --style=numbers --color=always --line-range :500 {}'"

# Github aliases
alias gl="git log --oneline --decorate --graph"
alias gp="git add . && git commit && git push"
alias gb="git branch -a"
alias gsb="gb && git switch"
alias gpp="git add . && git commit --allow-empty --allow-empty-message && git push --progress"
alias pd="pnpm run dev --turbo"
alias gor="go run"



