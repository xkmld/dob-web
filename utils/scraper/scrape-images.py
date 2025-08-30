import os
import requests
import json
# script after scrape

input_folder_name = "data/scraped/"
save_image_folder = "data/scraped/images/"

# create folder if not exist
if not os.path.exists(save_image_folder):
    os.makedirs(save_image_folder)

all_files = os.listdir(input_folder_name)

#print(all_files)
all_files.remove("images")

def process_name(name):
    return name.replace(' ', '').lower() + ".jpg"

for file in all_files:
    with open(input_folder_name + file) as f:
          d = json.load(f)
          if (d['img'] is None):
              continue
          img_data = requests.get(d['img']).content
          with open(save_image_folder + process_name(d['name']), 'wb') as handler:
              handler.write(img_data)
          print(save_image_folder);
