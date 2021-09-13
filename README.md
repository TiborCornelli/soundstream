To create an executable run the following commands your command line


If you don't have pyinstaller installed yet run

```
pip install pyinstaller
```

Afterwards, change into the soundstream directory

```
cd <path/to/soundstream>
```

and create the executable

```
pyinstaller -F --noconsole -nsoundstream --paths=pyinstaller  gui.py
```