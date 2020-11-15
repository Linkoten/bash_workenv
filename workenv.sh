#!/bin/bash

function workenv42(){
	wmctrl -n 3
	wmctrl -s 0
	firefox --new-window https://signin.intra.42.fr/users/sign_in --new-tab & sleep 1
	firefox --new-tab https://www.google.com & sleep 1
	wmctrl -s 1
	terminator -l 42 & sleep 1
	exit 0
}

function workenvp(){
	wmctrl -n 3
	wmctrl -s 0
	firefox --new-window https://www.google.com & sleep 1
	wmctrl -s 1
	terminator -l project & sleep 1
	exit 0
}
function workenvc(){
	let a=0
	let count=1
	shift
	wmctrl -n $1
	shift
	while (( $# > 1 ))
	do
		wmctrl -s $a
		$1 & sleep 1
		shift
		let a=a+1
		let count=count+1
	done
	wmctrl -s $1
	exit 0
}

while test $# -gt 0
do
    case "$1" in
        42) workenv42
			;;
		project) workenvp
			;;
		-c) workenvc "$@"
			;;
    esac
    shift
done

exit 0
