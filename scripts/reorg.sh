#!/bin/bash

# Iterate over the main artwork images
for artwork in artworks/*.jpg; do
    # Extract base filename without extension
    base_name=$(basename "$artwork" .jpg)

    # Convert spaces to underscores
    new_base_name=${base_name// /_}

    # Create a new directory for the artwork
    mkdir "$new_base_name"

    # Move and rename main artwork
    mv "$artwork" "$new_base_name/$new_base_name.jpg"

    # Check if the thumb exists and move/rename it
    if [[ -f "artworks/thumbs/${base_name}.jpg" ]]; then
        mv "artworks/thumbs/${base_name}.jpg" "$new_base_name/$new_base_name"_thumb.jpg
    fi

    # Check if the square version exists and move/rename it
    if [[ -f "artworks/square/$base_name.jpg" ]]; then
        mv "artworks/square/$base_name.jpg" "$new_base_name/$new_base_name"_square.jpg
    fi

    # Check if the mp3 exists and move/rename it
    if [[ -f "exp3-sounds/$base_name.mp3" ]]; then
        mv "exp3-sounds/$base_name.mp3" "$new_base_name/$new_base_name".mp3
    fi
done
