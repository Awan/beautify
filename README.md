# beautify

![image](https://user-images.githubusercontent.com/42554663/84741013-d380ae80-afc7-11ea-8eb5-0cf57162eab5.png)

A simple Python script which uses [feh](https://github.com/derf/feh) to set wallpapers at given time.

### Usage:

First time you have to run it from a terminal. It will ask you for your wallpapers collection path, give it absolute path to your wallpapers collection. Then you can use systemd to run it automatically on every reboot or your init system or just put it 
in your ~/.xinitrc

There is a [post](https://abdullah.today/wallpaper-automation/) explaining the
usage.

For systemd, just move the beautify.service to ~/.config/systemd/user/ and execute:

```bash
pip install --user appdirs
git clone https://gitlab.com/Abdullah/beautify.git
cd beautify
mkdir -p ~/.local/bin/
mkdir -p ~/.config/systemd/user/
cp beautify.py ~/.local/bin/beautify
cp beautify.service ~/.config/systemd/user/
chmod +x ~/.local/bin/beautify
systemctl enable --user beautify.service
systemctl start --user beautify.service
```


