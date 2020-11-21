#!/bin/bash
if [ $# == 0 ]
then
    vim -p website/urls.py users/urls.py pity_counter/urls.py Genshin_Tools/urls.py \
        "+vs website/views.py | tabn" \
        "+vs users/views.py | tabn" \
        "+vs pity_counter/views.py | tabn" \
        "+vs Genshin_Tools/settings.py | tabmove 0"
elif [ $1 == 'h' ]
then
    vim -p website/templates/website/base.html \
        website/templates/website/home.html \
        website/templates/website/post_detail.html \
        website/templates/website/post_form.html \
        website/templates/website/user_posts.html \
        website/templates/website/post_confirm_delete.html \
        pity_counter/templates/pity_counter/pity_counter.html
fi
