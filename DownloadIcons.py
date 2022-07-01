from PIL import Image
from bs4 import *
import requests
import os
from files_manage import create_folder
import threading


class DownloadIconsThread(object):
    def __init__(self, items, folder_name, url, interval=1):
        self.url = url
        self.interval = interval
        self.items = items
        self.folder_name = folder_name

        thread = threading.Thread(target=self.run, args=())
        thread.daemon = True
        thread.start()

    def run(self):
        try:
            download_icons(items=self.items, folder_name=self.folder_name, url=self.url)
        except requests.exceptions.RequestException as e:
            print('Error downloading icons', e)


def download_images(images, folder_name, exceptions=[], replacing=[], names={}):
    count = 0

    # checking if images is not zero
    if len(images) != 0:
        for i, image in enumerate(images):
            clas = str(image).replace('<img ', '').split('=')[0]
            file_name = str(image).replace(f'<img {clas}=\"', '').split('\"')[0]
            file_name = file_name.replace('＋', '+')
            if [e for e in exceptions if e.lower() not in file_name.lower()]:
                continue
            for rep in replacing:
                file_name = file_name.replace(rep, '')
            entry = file_name.split('.')[0]
            if names:
                if entry not in names:
                    continue
            if names.get(entry):
                file_name = file_name.replace(entry, names[entry])
            file_name = file_name.replace(entry, names[entry])
            dest_file = os.path.join(folder_name, file_name)
            if os.path.exists(dest_file):
                continue

            for e in ["data-srcset", "data-src", "data-fallback-src", "src"]:
                image_link = image.get(e, '')
                if image_link:
                    break
            if not image_link:
                continue

            try:
                r = requests.get(image_link).content
                try:
                    r = str(r, 'utf-8')
                except UnicodeDecodeError:
                    if not os.path.exists(dest_file):
                        with open(dest_file, "wb+") as f:
                            f.write(r)
                        resize_image(dest_file)
                    count += 1
            except requests.exceptions.RequestException as e:
                print(f'Error downloading icon: {image_link}', e)


def resize_image(image, size=70):
    if os.path.exists(image):
        im = Image.open(image)
        width, height = im.size
        if width > size:
            im1 = im.resize((size, size))
            im1.save(image)


def download_icons(items, url='https://zelda.fandom.com/wiki/Material#Breath_of_the_Wild', folder_name='asdf'):
    r = requests.get(url)

    # Parse HTML Code
    soup = BeautifulSoup(r.text, 'html.parser')

    # find all images in URL
    images = soup.findAll('img')

    # Call folder create function
    create_folder(folder_name)
    download_images(images, folder_name, exceptions=['botw'], replacing=['BotW ', ' Icon'], names=items)


def generate_weapons_icons(win):
    unnacc = ["Hero's Sword", 'Lantern', 'Lightscale Trident', 'Master Sword (Broken/Unequippable)',
              'Master Sword (near malice, no charge)', 'Master Sword (no near malice, no charge)',
              'One-Hit Obliterator']
    for i in win.weapons:
        if '★' in i:
            continue
        if not os.path.exists(os.path.join(r'res\icons', f'{win.weapons[i]}.png')):
            if i not in unnacc:
                DownloadIconsThread(win.weapons, r'res\icons', url='https://zelda.fandom.com/wiki/Weapon')
                DownloadIconsThread(win.weapons, r'res\icons', url='https://zelda.fandom.com/wiki/Bow')
                DownloadIconsThread(win.weapons, r'res\icons', url='https://zelda.fandom.com/wiki/Shield')
                return


def generate_food_icons(win):
    for i in win.items:
        if '★' in i:
            continue
        if not os.path.exists(os.path.join(r'res\icons', f'{win.items[i]}.png')):
            print(i)
            DownloadIconsThread(win.items, r'res\icons',
                                url='https://zelda.fandom.com/wiki/Material#Breath_of_the_Wild')
            DownloadIconsThread(win.items, r'res\icons',
                                url='https://zelda.fandom.com/wiki/Food#Breath_of_the_Wild')
            return


def generate_armors_icons(win):
    for i in win.armors:
        if '★' in i:
            continue
        if not os.path.exists(os.path.join(r'res\icons', f'{win.armors[i]}.png')):
            print(i)
            DownloadIconsThread(win.armors, r'res\icons', url='https://zelda.fandom.com/wiki/Armor#Breath_of_the_Wild')
            return
