from PIL import Image
from bs4 import *
import requests
import os, sys
from files_manage import *
import time
import threading

class DownloadIconsThread(object):
    def __init__(self, items,folder_name, url, interval=1):
        self.url = url
        self.interval = interval
        self.items = items
        self.folder_name = folder_name

        thread = threading.Thread(target=self.run, args=())
        thread.daemon = True
        thread.start()

    def run(self):
        try:
            DownloadIcons(items=self.items, folder_name=self.folder_name, url=self.url)
        except:
            pass


def download_images(images, folder_name, exceptions=[], replacing=[], names={}):
    file_name = ''
    count = 0

    # checking if images is not zero
    if len(images) != 0:
        for i, image in enumerate(images):
            try:
                clas = str(image).replace('<img ', '').split('=')[0]
                file_name = str(image).replace(f'<img {clas}=\"', '').split('\"')[0]
                file_name = file_name.replace('＋','+')
            except:
                continue
            flag = False
            if exceptions:
                for e in exceptions:
                    if not e.lower() in file_name.lower():
                        flag = True
                        break
            if flag: continue
            if replacing:
                for rep in replacing:
                    file_name = file_name.replace(rep, '')
            entry = file_name.split('.')[0]
            if names:
                if not entry in names: continue
            try:
                file_name = file_name.replace(entry, names[entry])
            except:
                pass
            file_name = file_name.replace(entry, names[entry])

            if os.path.exists(f"{folder_name}/{file_name}"): continue

            try:
                image_link = image["data-srcset"]
            except:
                try:
                    image_link = image["data-src"]
                except:
                    try:
                        image_link = image["data-fallback-src"]
                    except:
                        try:
                            image_link = image["src"]
                        except:
                            continue
            try:

                r = requests.get(image_link).content
                try:
                    r = str(r, 'utf-8')
                except UnicodeDecodeError:
                    if not os.path.exists(f"{folder_name}/{file_name}"):
                        with open(f"{folder_name}/{file_name}", "wb+") as f:
                            f.write(r)
                        resizeImage(f"{folder_name}/{file_name}")
                    count += 1
            except:
                pass

def resizeImage(image, size=40):
    if not os.path.exists(image): return
    im = Image.open(image)
    width, height = im.size
    if width > size:
        im1 = im.resize((size,size))
        im1.save(image)

# MAIN FUNCTION START
def DownloadIcons(items, url='https://zelda.fandom.com/wiki/Material#Breath_of_the_Wild', folder_name='asdf'):
    r = requests.get(url)

    # Parse HTML Code
    soup = BeautifulSoup(r.text, 'html.parser')

    # find all images in URL
    images = soup.findAll('img')

    # Call folder create function
    create_folder(folder_name)
    download_images(images, folder_name, ['botw'], ['BotW ', ' Icon'], items)
   # print('All icons safely downloaded to ' + folder_name)

def do_weapons(win):
    flag = True
    for i in win.weapons:
        if '★' in i: continue
        if not os.path.exists(f'res\\icons\\{win.weapons[i]}.png'):
            if not i in ["Hero's Sword", 'Lantern', 'Lightscale Trident', 'Master Sword (Broken/Unequippable)', 'Master Sword (near malice, no charge)', 'Master Sword (no near malice, no charge)', 'One-Hit Obliterator']:
                flag = False
                break
    if flag: return
    DownloadIconsThread(win.weapons, 'res\\icons', url='https://zelda.fandom.com/wiki/Weapon')
    DownloadIconsThread(win.weapons, 'res\\icons', url='https://zelda.fandom.com/wiki/Bow')
    DownloadIconsThread(win.weapons, 'res\\icons', url='https://zelda.fandom.com/wiki/Shield')

def do_food(win):
    flag = True
    for i in win.items:
        if '★' in i: continue
        if not os.path.exists(f'res\\icons\\{win.items[i]}.png'):
            print(i)
            flag = False
            break
    if flag: return
    DownloadIconsThread(win.items, 'res\\icons', url='https://zelda.fandom.com/wiki/Material#Breath_of_the_Wild')
    DownloadIconsThread(win.items, 'res\\icons', url='https://zelda.fandom.com/wiki/Food#Breath_of_the_Wild')

def do_armors(win):
    flag = True
    for i in win.armors:
        if '★' in i: continue
        if not os.path.exists(f'res\\icons\\{win.armors[i]}.png'):
            print(i)
            flag = False
            break
    if flag: return
    DownloadIconsThread(win.armors, 'res\\icons', url='https://zelda.fandom.com/wiki/Armor#Breath_of_the_Wild')