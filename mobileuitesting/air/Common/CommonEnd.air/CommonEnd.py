# -*- encoding=utf8 -*-
__author__ = "user5467"

from airtest.core.api import *

auto_setup(__file__)
n,k=True,0
while(n):
    if k!=6:
        try:

            if assert_exists(Template(r"tpl1583732941380.png", record_pos=(-0.13, 0.944), resolution=(1080, 2244)))!=None:
                n=False
        except:
                touch(Template(r"tpl1583733674919.png", record_pos=(-0.428, -0.894), resolution=(1080, 2244)))
                sleep(1)
                k = k+1
    else:
        n=False
