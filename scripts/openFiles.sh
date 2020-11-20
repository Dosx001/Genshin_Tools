#!/bin/bash
if [ $# == 0 ]
then
    vim -p website/urls.py pity_counter/urls.py Genshin_Tools/urls.py \
        "+vs website/views.py | tabn" \
        "+vs pity_counter/views.py | tabn" \
        "+vs Genshin_Tools/settings.py | tabmove 0"
elif [ $1 == 'h' ]
then
    vim -p website/templates/website/base.html \
        website/templates/website/home.html \
        pity_counter/templates/pity_counter/pity_counter.html
fi
