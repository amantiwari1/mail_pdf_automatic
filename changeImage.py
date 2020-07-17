#!/usr/bin/env python3
from PIL import Image
import os
mypath = os.path.expanduser("~/supplier-data/images/")
onlyfiles = [f for f in os.listdir(mypath) if f.endswith('.tiff')]
for i in onlyfiles:
    im = Image.open("{}{}".format(mypath,i))
    foo = im.convert('RGB')
    foo = foo.resize((600,400),Image.ANTIALIAS)
    foo.save("{}{}.jpeg".format(mypath,i.strip(".tiff")))
