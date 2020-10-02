from requests_html import HTMLSession
import json
import uuid
import os

def get_info_and_links(url):
    links = list()

    with HTMLSession() as session:
        r = session.get(url)
        title = r.html.find('.mdCMN38Item01Ttl', first=True).text
        author = r.html.find('.mdCMN38Item01Author', first=True).text        
        imgs = r.html.find('.FnStickerPreviewItem')

        for i in imgs:
            links.append((json.loads(i.attrs['data-preview'])['staticUrl']))

    return title, author, links

def save(folder, links, url):
    if os.path.exists(folder):
        print('Folder already exists for ' + url + '. Skipping...')
        return

    os.mkdir(folder)

    with HTMLSession() as session:
        for i, link in enumerate(links):
            r = session.get(link, allow_redirects=True)
            open(folder + os.sep + str(i) + '.png', 'wb').write(r.content)

def download(working_dir, links, url):
    if len(links) <= 30:
        download_folder = str(uuid.uuid5(uuid.NAMESPACE_URL, url))
        folder = working_dir + os.sep + download_folder
        save(folder, links, url)
        return list(download_folder)
    
    download_folder1 = str(uuid.uuid5(uuid.NAMESPACE_URL, url + '_111'))
    folder = working_dir + os.sep + download_folder1
    save(folder, links[:len(links)//2], url)
    
    download_folder2 = str(uuid.uuid5(uuid.NAMESPACE_URL, url + '_222'))
    folder = working_dir + os.sep + download_folder2
    save(folder, links[len(links)//2:], url)

    return [download_folder1, download_folder2]
