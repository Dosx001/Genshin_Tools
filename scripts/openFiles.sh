#!/bin/bash
if [ $# == 0 ]
then
    vim -p website/views.py pity_counter/views.py Genshin_Tools/settings.py \
        "+vs website/urls.py | tabn" \
        "+vs pity_counter/urls.py | tabn" \
        "+tabmove 0"
elif [ $1 == 'h' ]
then
    vim -p website/templates/website/base.html \
        website/templates/website/home.html \
        pity_counter/templates/pity_counter/pity_counter.html
fi
