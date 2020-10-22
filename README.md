# File filter
_The file filter listens a custom folder, when a new File is moved into it, automaticly filters it into a folder with a name,depending of the File extension, they will be ordered in different directories (ex. Image Folder, Music Folder, Text Folder...)_

_Is really usefull to have it in the Downloads folder, because let's be honest, nobody ever takes the time to tidy it regularly._

This is my first project with Python, to get started with the language, as you can see if you checked out the code, it, is very simple. If you have thought about some changes (or bugs) don't doubt it and contact me in my [Github](https://github.com/dtravesi).

## Let's get started 🚀

_This instructions will explain, how to proper execute the file filter in a custom folder, or have it as system service (linux)_


### Prerequisites 📋

* _Have **Python** installed_
* _Install pip (the python package installer if you didn't have it)_
* _Use the next command to install the next library, used for eventHandling and observing in a custom directory_
```
pip install watchdog
```

### Installation 🔧

The first thing to do, is set the folder you want to filter files (by default Downloads folder). This should be done in the [config.ini](config.ini)

_To have the filter running you can execute it each time you want to run it, but we strongly recomend to start a service_

### _Execute it with python:_

```
/usr/bin/python /home/user/file-filter/DownloadFilter.py
```

### _Create a service:_

The recommended way to use it is to create a [service](https://medium.com/@benmorel/creating-a-linux-service-with-systemd-611b5c8b91d6) (Linux based OS), that is running with the login or startup.

_Example of the service_

/etc/systemd/system/fileFilter.service

```
[Unit]
Description=Filters a custom folder

[Service]
User=user
ExecStart=/bin/python /home/user/file-filter/Filter.py

[Install]
WantedBy=multi-user.target
```
_Substitute your -user- above_

Start the created service:

```
systemctl enable fileFilter.service
```

```
systemctl start fileFilter.service
```

```
systemctl daemon-reload
```

Check if it's running or in case of exception while executing it (most errors are related to a wrong directory name in the [config.ini](config.ini) 🤓)

And... enjoy!! If you have the service started (and working), you should not worry more. It will filter your files.

## Build with 🛠️

* [Python](https://www.python.org/) - Used Language
* [Watchdog](https://pythonhosted.org/watchdog/) - Event handler and observer

## Authors ✒️

[Contributors](https://github.com/dtravesi/file-filter/contributors)

## Lincense 📄

Free to use, of course. If you use share it (blog, webpage...), just give credit to my github page :)

## Thank you 🎁

* If you found it usefull, I will appreciate you sharing the project 📢
* If you find some errors, have some mercy, is my _"hello world"_ in python. 🤓

---
⌨️ thanks! ❤️ By [dtravesi](https://github.com/dtravesi) 😊
