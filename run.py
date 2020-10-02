import os

import download
import resize
import convert
import utils

from config import URLS
from config import WORKING_FOLDER
from config import OVERRIDES

if not os.path.exists(WORKING_FOLDER):
    os.mkdir(WORKING_FOLDER)

sticker_packs = list()

for url in URLS:
    title, author, links = download.get_info_and_links(url)
    download_folders = download.download(WORKING_FOLDER, links, url)
    for download_folder in download_folders:
        resize.resize(WORKING_FOLDER, download_folder)
        convert.convert(WORKING_FOLDER, download_folder)
        sticker_packs.append(utils.gen_sticker_pack(WORKING_FOLDER, download_folder, title, author))

for override in OVERRIDES:
    resize.resize(WORKING_FOLDER, override['download_folder'])
    convert.convert(WORKING_FOLDER, override['download_folder'])
    sticker_packs.append(utils.gen_sticker_pack(WORKING_FOLDER, override['download_folder'], override['title'], override['author']))

utils.gen_json(WORKING_FOLDER, sticker_packs)

print('\n\n\nCopy contents of {} to ./Android/app/src/main/assets\n'.format(WORKING_FOLDER))

print('Modify app_name in ./app/src/main/res/values/strings.xml to use a unique name.\n')
print('Modify applicationId in ./app/build.gradle to use a unique id.\n')

print('cd Android')
print('gradlew.bat assemble')
