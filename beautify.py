#!/usr/bin/env python3

import subprocess as sp
import errno
import json
from time import sleep
from pathlib import Path


config_file = Path(sp.os.getenv('HOME')).joinpath('.beautifyrc')
walls_dir = ''


def getting_started():
    global walls_dir
    if sp.os.path.exists(config_file):
        with open(config_file, 'r') as f:
            data = json.load(f)
            walls_dir = data.get('walls_dir')
    else:
        print("Looks like you haven't configured beautify yet. Lets do it now.")
        config = {}
        walls_dir = input("Where are your wallpapers located? Type the absolute path. ")
        config['walls_dir'] = walls_dir
        with open(config_file, 'w+') as f:
            json.dump(config, f)


getting_started()

try:
    walls = sp.os.listdir(walls_dir)
except IOError as e:
    if e.errno is errno.ENOENT:
        print("You have mistyped the wallpapers directory. Please recheck and try again.")
        sp.os.remove(config_file)
        getting_started()


walls_file = str(Path(sp.os.getenv('HOME')).joinpath('.fehbg'))
for i in range(len(walls)):
    walls[i] = str(Path(walls_dir).joinpath(walls[i]))


def beautify():
    for i in walls:
        sp.run(['sh', walls_file])
        with open(walls_file, 'w+') as f:
            print(f"""#!/bin/sh
feh --bg-scale {i}
""", file=f)
            f.close()
        sleep(1)


beautify()
