# -*- encoding=utf8 -*-
__author__ = "user5467"

from airtest.core.api import *

auto_setup(__file__)

try:
    touch(Template(r"tpl1583732941380.png", record_pos=(-0.13, 0.944), resolution=(1080, 2244)))
    touch(Template(r"tpl1583732957417.png", record_pos=(0.369, -0.482), resolution=(1080, 2244)))
    swipe(Template(r"tpl1583733089674.png", record_pos=(-0.364, 0.651), resolution=(1080, 2244)), vector=[0.0264, -0.6913])
    swipe(Template(r"tpl1583733145187.png", record_pos=(-0.367, -0.056), resolution=(1080, 2244)), vector=[-0.0432, 0.726])
    # touch(Template(r"tpl1583733674919.png", record_pos=(-0.428, -0.894), resolution=(1080, 2244)))
    # sleep(1)
except :
    n=1
    while(n!=0):
        if assert_not_exists(Template(r"tpl1583732941380.png", record_pos=(-0.13, 0.944), resolution=(1080, 2244)),"脚本失败")==None:
            touch(Template(r"tpl1583733674919.png", record_pos=(-0.428, -0.894), resolution=(1080, 2244)))
            sleep(1)
        else : n=0