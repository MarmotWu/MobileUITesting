# -*- encoding=utf8 -*-
__author__ = "user5467"

from airtest.core.api import *

auto_setup(__file__)

touch(Template(r"tpl1583732941380.png", record_pos=(-0.13, 0.944), resolution=(1080, 2244)))
touch(Template(r"tpl1583732957417.png", record_pos=(0.369, -0.482), resolution=(1080, 2244)))
swipe(Template(r"tpl1583733089674.png", record_pos=(-0.364, 0.651), resolution=(1080, 2244)), vector=[0.0264, -0.6913])
swipe(Template(r"tpl1583733145187.png", record_pos=(-0.367, -0.056), resolution=(1080, 2244)), vector=[-0.0432, 0.726])
touch(Template(r"tpl1584063568441.png", record_pos=(-0.115, -0.588), resolution=(1080, 2244)))
touch(Template(r"tpl1584063582086.png", record_pos=(-0.004, -0.656), resolution=(1080, 2244)))
assert_exists(Template(r"tpl1584063599540.png", record_pos=(0.003, -0.123), resolution=(1080, 2244)), "BIM工程展示不正确")

#消耗量
touch(Template(r"tpl1584082763377.png", record_pos=(-0.117, 0.884), resolution=(1080, 2244)))
assert_exists(Template(r"tpl1584082942272.png", record_pos=(0.019, -0.115), resolution=(1080, 2244)), "点击消耗展示不正确")

touch(Template(r"tpl1584064952918.png", record_pos=(-0.437, -0.891), resolution=(1080, 2244)))
sleep(1)
touch(Template(r"tpl1584064952918.png", record_pos=(-0.437, -0.891), resolution=(1080, 2244)))
sleep(1)
touch(Template(r"tpl1584064952918.png", record_pos=(-0.437, -0.891), resolution=(1080, 2244)))
sleep(1)
touch(Template(r"tpl1583732941380.png", record_pos=(-0.13, 0.944), resolution=(1080, 2244)))

