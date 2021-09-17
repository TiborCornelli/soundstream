To create an executable run the following commands your command line:


If you don't have pyinstaller or pytube installed yet, run

```
pip install pytube
pip install pyinstaller
```

Afterwards, change into the soundstream directory

```
cd <path/to/soundstream>
```

and create the executable

```
pyinstaller -F --noconsole -n soundstream Soundstream/gui.py
```
A folder 'dist' will appear, containing the soundstream executable.
