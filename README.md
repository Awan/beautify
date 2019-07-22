# beautify

A simple Python script which uses [feh](https://github.com/derf/feh) to set wallpapers at given time.
First time you have to run it from a terminal. It will ask you for your wallpapers collection path, give it absolute path to your wallpapers collection. Then you can use systemd to run it automatically on every reboot or your init system or just put it 
in your ~/.xinitrc

For systemd, just move the beautify.service to ~/.config/systemd/user/ and execute:

- `systemctl enable --user beautify.service`
- `systemctl start --user beautify.service`
