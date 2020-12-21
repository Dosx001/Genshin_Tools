#!/bin/bash
if [ $# == 0 ]
then
    vim -p website/urls.py users/urls.py pity_counter/urls.py random_event/urls.py \
        quest_log/urls.py resource_converter/urls.py Genshin_Tools/urls.py \
        "+vs website/views.py | tabn" \
        "+vs users/views.py | tabn" \
        "+vs pity_counter/views.py | tabn" \
        "+vs random_event/views.py | tabn" \
        "+vs quest_log/views.py | tabn" \
        "+vs resource_converter/views.py | tabn" \
        "+vs Genshin_Tools/settings.py | tabmove 0"
elif [ $1 == 'h' ]
then
    vim -p website/static/random_event/main.js \
        website/static/pity_counter/main.js \
        website/static/quest_log/main.js \
        website/static/resource_converter/main.js \
        "+vs random_event/templates/random_event.html | tabn" \
        "+vs pity_counter/templates/pity_counter/pity_counter.html | tabn" \
        "+vs quest_log/templates/quest_log.html | tabn" \
        "+vs resource_converter/templates/resource_converter.html | tabn" \
        "+tabe website/templates/website/base.html | tabmove 0"
elif [ $1 == 'c' ]
then
    vim -p website/static/random_event/styles.css \
        website/static/pity_counter/styles.css \
        website/static/quest_log/styles.css \
        website/static/resource_converter/styles.css \
        website/static/website/main.css \
        "+vs random_event/templates/random_event.html | tabn" \
        "+vs pity_counter/templates/pity_counter/pity_counter.html | tabn" \
        "+vs quest_log/templates/quest_log.html | tabn" \
        "+vs resource_converter/templates/resource_converter.html | tabn" \
        "+vs website/templates/website/base.html | tabmove 0"
fi
