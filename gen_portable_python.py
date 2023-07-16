import urllib.request
import os

# basic files for Python installation
py_list = ["core", "dev", "exe", "lib", "tcltk", "tools"]
# Python version
version = "3.11.4"
# Python msi download URL
ftp = "https://www.python.org/ftp/python/" + version + "/amd64/"
# location for Portable Python
path = "c:\\Python311"
# create directory
try:
    os.mkdir(path)
except:
    # path exists
    pass
# get Python installation msi files and extract into target dir
for i in py_list:
    filename = i + ".msi"
    url = ftp + filename
    # download basic python msi file
    urllib.request.urlretrieve(url, filename)
    os.system("msiexec.exe /a " + i + ".msi targetdir=" + path)
    # delete msi file
    os.remove(path + "\\" + i + ".msi")
