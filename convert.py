import os
import subprocess
import re

import utils

def convert_to_webp(files):
    for file in files:
        out = re.sub(r'\.png$', '', file)
        cmd = 'tools\cwebp.exe -m 6 -q 90 -mt -resize 512 512 {file} -o {out}.webp'.format(file=file, out=out)
        subprocess.run(cmd)

def delete_pngs(files):
    for file in files:
        os.remove(file)

def convert(working_dir, download_folder):
    src = working_dir + os.sep + download_folder
    pngs = utils.get_png(src)
    convert_to_webp(pngs)
    delete_pngs(pngs)
