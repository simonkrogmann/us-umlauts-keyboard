# us-umlauts-keyboard
A US keyboard layout with German, Spanish and Catalan special characters and other useful symbols. These characters can be accessed with AltGr (lowercase) and AltGr+Shift (uppercase):

| Character | On Key | Notes |
| --------- | --------- | ----- |
| ä | a |
| ö | o |
| ï | i |
| ü | u |
| ß | s |
| ñ | n |
| ¡ | 1 (!) |
| § | 3 |
| ¿ | / (?) |
| € | e and 5 |
| ç | c |
| £ | l |
| μ | m |
| @ | q | Make it easier for Germans to type their e-mail address on your device |
| · | . |


Additionally, on Linux, AltGr+\` is a dead key for creating accents:

AltGr+\` for á, é, ... and Shift+AltGr+\` for à, è, ...

## Installation

### Linux
Layouts for X11 and kbd are included.
Run `./install` with sudo rights.
For Gnome and Ubuntu everything should work now.
For i3 put `setxkbmap us-umlauts` into your configuration after the installation.

### Windows
Download and install the Microsoft Keyboard Layout Creator Tool.
You may need to download .NET Framework 2.0, if the installation fails.
Search the internet fro an up-to-date link if necessary.
Load `windows/us-umlauts.klc` into Keyboard Layout Creator and build it.
Some warnings related to double definitions and characters not being in the default system code page should be normal.
