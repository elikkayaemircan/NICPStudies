#!/usr/bin/bash

flavPath=/eos/experiment/ship/user/eelikkaya/NICPStudies/GeantEvents/nu_e

for f in $( ls "$flavPath"/above ); do
    if [[ -d "$flavPath"/Saved/"$f" ]]; then
        echo "WARN duplicated folder $f"
        if [[ !  -d "$flavPath"/Saved/0"$f" ]]; then
            echo "WARN duplication recovered with name 0$f"
            mv "$flavPath"/above/"$f" "$flavPath"/Saved/0"$f"
        fi
        if [[ ! -d "$flavPath"/Saved/1"$f"  ]]; then
            echo "WARN duplication recovered with name 1$f"
            mv "$flavPath"/above/"$f" "$flavPath"/Saved/1"$f"
        fi
    else
        echo "OK to move $f"
        mv "$flavPath"/above/"$f" "$flavPath"/Saved/
    fi
done
