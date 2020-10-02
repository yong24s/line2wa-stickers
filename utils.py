import os
import json
import re

def atof(text):
    try:
        retval = float(text)
    except ValueError:
        retval = text
    return retval

def natural_keys(text):
    '''
    alist.sort(key=natural_keys) sorts in human order
    http://nedbatchelder.com/blog/200712/human_sorting.html
    (See Toothy's implementation in the comments)
    float regex comes from https://stackoverflow.com/a/12643073/190597
    '''
    return [ atof(c) for c in re.split(r'[+-]?([0-9]+(?:[.][0-9]*)?|[.][0-9]+)', text) ]

def get_filetype(source, filetype, include_fullpath=False):
    r = list()
    files = os.listdir(source)

    for file in files:
        if file.endswith(filetype):
            path = file
            if include_fullpath:
                path = source + os.sep + file
            
            r.append(path)

    return r

def get_png(source):
    return get_filetype(source, '.png', True)

def get_webp(source):
    return get_filetype(source, '.webp')

def gen_json(working_dir, sticker_packs):
    data = dict()
    data['sticker_packs'] = sticker_packs
    with open(working_dir + os.sep + 'contents.json', 'w') as f:
        json.dump(data, f)

def gen_sticker_pack(working_folder, download_folder, title, author):
    data = dict()
    
    data['name'] = title
    data['publisher'] = author

    data['image_data_version'] = '1'
    data['avoid_cache'] = False
    data['stickers'] = list()

    images = get_webp(working_folder + os.sep + download_folder)
    images.sort(key=natural_keys)
    for image in images:
        i = dict()
        i['image_file'] = image
        data['stickers'].append(i)
    
    if len(data['stickers']) > 0:
        data['tray_image_file'] = data['stickers'][0]['image_file']

    data['identifier'] = download_folder

    return data
