TARGET="/usr/share/X11/xkb/rules/evdev.xml"
FRAGMENT="X11/evdev.xml.fragment"

with open(TARGET, "r") as f:
    content = f.read()

with open(FRAGMENT, "r") as f:
    fragment = f.read()

if "usumlauts" in content:
    place = content.index("usumlauts")
    begin = content.rindex("<layout>", 0, place)
    begin = content.rindex("\n", 0, begin)
    end = content.index("</layout>", place)
    end = content.index("\n", end)
    content = content[:begin] + content[end:]
    #delete old


place = content.index("</layoutList>")
place = content.rindex("\n", 0, place)
content = content[:place + 1] + fragment + content[place+1:]


with open(TARGET, "w") as f:
    f.write(content)
