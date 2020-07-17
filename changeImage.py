#!/usr/bin/env python3
from PIL import Image
import os
mypath = os.path.expanduser("~/supplier-data/images/")
onlyfiles = [f for f in os.listdir(mypath) if f.endswith('.tiff')]
for i in onlyfiles:
    im = Image.open("{}{}".format(mypath,i))
    rgb_im = im.convert('RGB')
    rgb_im.save("{}{}.jpeg".format(mypath,i[:3]).strip(".tiff"))
