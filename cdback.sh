function cd() {
        [ -d "$@" ] &&
        export OLDPWDS="`python $CDBACK/cdback.py cd \"$@\"`"
        builtin cd "$@"
}

function back() {
        HEAD="`python $CDBACK/cdback.py head`"
        export OLDPWDS="`python $CDBACK/cdback.py tail`"
        builtin cd "$HEAD"
}