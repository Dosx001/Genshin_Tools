#!/bin/bash
if [ $# == 0 ]
then
    vim -p website/urls.py users/urls.py pity_counter/urls.py random_event/urls.py \
        quest_log/urls.py Genshin_Tools/urls.py \
        "+vs website/views.py | tabn" \
        "+vs users/views.py | tabn" \
        "+vs pity_counter/views.py | tabn" \
        "+vs random_event/views.py | tabn" \
        "+vs quest_log/views.py | tabn" \
        "+vs Genshin_Tools/settings.py | tabmove 0"
elif [ $1 == 'h' ]
then
    vim -p website/static/random_event/main.js \
        website/static/pity_counter/main.js \
        website/static/quest_log/main.js \
        "+vs random_event/templates/random_event.html | tabn" \
        "+vs pity_counter/templates/pity_counter/pity_counter.html | tabn" \
        "+vs quest_log/templates/quest_log.html | tabn" \
        "+tabe website/templates/website/base.html | tabmove 0"
fi
