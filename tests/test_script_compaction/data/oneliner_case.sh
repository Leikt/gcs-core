function _bash-it-history-init(){ safe_append_preexec '_bash-it-history-auto-save';safe_append_prompt_command '_bash-it-history-auto-load';};function _bash-it-history-auto-save(){ case $HISTCONTROLin *'noauto'* | *'autoload'*);:;;;;*'auto'*);history -a;;;;*);shopt -q histappend && history -a && return;;;;esac;};function _bash-it-history-auto-load(){ case $HISTCONTROLin *'noauto'*);:;;;;*'autosave'*);history -a;;;;*'autoloadnew'*);history -n;;;;*'auto'*);history -a && history -c && history -r;;;;*);:;;;;esac;};_bash_it_library_finalize_hook+=('_bash-it-history-init')