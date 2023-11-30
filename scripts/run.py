import os
import eyed3
import datetime

root_folder = "."  # Replace with the path to your root directory

prev_artwork_name = None

for folder_name in sorted(os.listdir(root_folder)):
    folder_path = os.path.join(root_folder, folder_name)
    
    if os.path.isdir(folder_path):
        artwork_name = f"{folder_name}.jpg"
        square_name = f"{folder_name}_square.jpg"
        thumb_name = f"{folder_name}_thumb.jpg"
        mp3_name = f"{folder_name}.mp3"
        
        mp3_path = os.path.join(folder_path, mp3_name)
        
        if os.path.exists(mp3_path):
            audiofile = eyed3.load(mp3_path)
            
            # Extract recording date from the MP3 metadata
            recording_date = datetime.datetime.strptime(str(audiofile.tag.recording_date), '%Y-%m-%d').date()
            
            # Extract patch notes from the MP3 metadata's comments
            patch_notes = ""
            for comment in audiofile.tag.comments:
                patch_notes = comment.text
                break
        else:
            recording_date = datetime.datetime.now().date()
            patch_notes = ""
        
        with open(os.path.join(root_folder, folder_name, "index.md"), "w") as md_file:
            md_file.write("---\n")
            md_file.write(f"title: \"{folder_name[3:].replace('_', ' ').title()}\"\n")
            md_file.write(f"date: {recording_date}\n")
            md_file.write("draft: false\n")
            tags = ["Art"]
            if os.path.exists(mp3_path):
                tags.append("Music")
            md_file.write("tags: " + str(tags) + "\n")
            md_file.write("type: \"custom-type/exp\"\n")
            md_file.write(f"artwork: {artwork_name}\n")
            md_file.write(f"square: {square_name}\n")
            md_file.write(f"thumb: {thumb_name}\n")
            if os.path.exists(mp3_path):
                md_file.write(f"mp3: {mp3_name}\n")
            md_file.write("artist: AncientAndroid\n")
            md_file.write("description: \"\"\n")
            md_file.write(f"patchNotes: \"{patch_notes}\"\n")
            if prev_artwork_name:
                md_file.write(f"nextPage: /works/2021/{prev_artwork_name}/\n")
            md_file.write("---\n")
        prev_artwork_name = folder_name
