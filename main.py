import sys
import string

type = "DI"
module = "X20DI9371"
string2paste = "DI_Raw[%s].IN[%s]"
modules = 19
channels = 12
letter = ""
print(sys.argv[0])

for mod in range(1, modules+1):
    if mod <= 1:
        letter = ""
    else:
        letter = string.ascii_lowercase[mod-2]
    for chn in range(1, channels+1):
        if chn < 10:
            number = "0" + str(chn)
        else:
            number = str(chn)
        if type == "AI":
            print("\t" + (string2paste % (mod, chn)) + " AT %IW.\"" + module + letter +"\".AnalogInput" + number+";")
        if type == "DI":
            print("\t" + (string2paste % (mod, chn)) + " AT %IX.\"" + module + letter + "\".DigitalInput" + number + ";")
        if type == "DO":
            print("\t" + (string2paste % (mod, chn)) + " AT %QX.\"" + module + letter + "\".DigitalOutput" + number + ";")
