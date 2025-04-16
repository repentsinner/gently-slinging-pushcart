#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
import os
picdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'pic')
libdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'lib')
if os.path.exists(libdir):
    sys.path.append(libdir)

import logging
from waveshare_epd import epd4in0e
import time
from PIL import Image,ImageDraw,ImageFont
import traceback

logging.basicConfig(level=logging.DEBUG)
logging.getLogger("PIL.TiffImagePlugin").setLevel(logging.CRITICAL + 1)


try:
    logging.info("epd4in0e Demo")

    epd = epd4in0e.EPD()   
    logging.info("init and Clear")
    epd.init()
    
    # read image file - Image can open jpg just fine and dither it, no need for
    # such aggressive pre-processing
    Himage = Image.open(os.path.join(picdir, 'good_neighbor.jpg'))
    Himage = Himage.rotate(180)
    epd.display(epd.getbuffer(Himage))
    
    logging.info("Goto Sleep...")
    epd.sleep()
        
except IOError as e:
    logging.info(e)
    
except KeyboardInterrupt:    
    logging.info("ctrl + c:")
    epd4in0e.epdconfig.module_exit(cleanup=True)
    exit()
