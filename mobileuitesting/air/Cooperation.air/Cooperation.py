# -*- encoding=utf8 -*-
__author__ = "user5467"

from airtest.core.api import *

auto_setup(__file__)

#try:

touch(Template(r"tpl1583732941380.png", record_pos=(-0.13, 0.944), resolution=(1080, 2244)))
touch(Template(r"tpl1583732957417.png", record_pos=(0.369, -0.482), resolution=(1080, 2244)))
swipe(Template(r"tpl1583733089674.png", record_pos=(-0.364, 0.651), resolution=(1080, 2244)), vector=[0.0264, -0.6913])
swipe(Template(r"tpl1583733145187.png", record_pos=(-0.367, -0.056), resolution=(1080, 2244)), vector=[-0.0432, 0.726])

#新建
touch(Template(r"tpl1583835320334.png",record_pos=(-0.11,0.071),resolution=(1080,2244)))
touch(Template(r"tpl1583835330781.png",record_pos=(0.325,-0.897),resolution=(1080,2244)))
touch(Template(r"tpl1583835339106.png",record_pos=(-0.004,-0.331),resolution=(1080,2244)))
text("AirTest创建主题")
touch(Template(r"tpl1583835404046.png",record_pos=(-0.033,0.023),resolution=(1080,2244)))
touch(Template(r"tpl1583835412227.png",record_pos=(-0.239,0.037),resolution=(1080,2244)))
touch(Template(r"tpl1583835426818.png",record_pos=(-0.002,-0.761),resolution=(1080,2244)))
touch(Template(r"tpl1583835448146.png",record_pos=(0.026,0.119),resolution=(1080,2244)))
touch(Template(r"tpl1583835459251.png",record_pos=(0.432,-0.896),resolution=(1080,2244)))
touch(Template(r"tpl1583835483487.png",record_pos=(0.399,-0.892),resolution=(1080,2244)))
sleep(2)

#详情
touch(Template(r"tpl1583835582031.png",record_pos=(0.017,-0.636),resolution=(1080,2244)))
sleep(3)
assert_exists(Template(r"tpl1583835693503.png",record_pos=(-0.205,-0.894),resolution=(1080,2244)),"没有获取到创建的协作")
touch(Template(r"tpl1583835720131.png",record_pos=(0.004,0.094),resolution=(1080,2244)))
sleep(3)
assert_exists(Template(r"tpl1583835739864.png",record_pos=(-0.153,-0.044),resolution=(1080,2244)),"没有获取到构件")
touch(Template(r"tpl1583835766631.png",record_pos=(-0.431,-0.887),resolution=(1080,2244)))
sleep(1)
touch(Template(r"tpl1583835766631.png",record_pos=(-0.431,-0.887),resolution=(1080,2244)))
sleep(1)

#筛选
touch(Template(r"tpl1583835814170.png",record_pos=(0.439,-0.894),resolution=(1080,2244)))
touch(Template(r"tpl1583835845483.png",record_pos=(0.057,-0.488),resolution=(1080,2244)))
sleep(1)
touch(Template(r"tpl1583836519878.png",record_pos=(0.031,0.133),resolution=(1080,2244)))
touch(Template(r"tpl1583835886568.png",record_pos=(0.269,0.883),resolution=(1080,2244)))
assert_exists(Template(r"tpl1583836602008.png",record_pos=(0.012,-0.632),resolution=(1080,2244)),"没有获取到创建的协作")

#编辑
touch(Template(r"tpl1583835943311.png",record_pos=(0.004,-0.611),resolution=(1080,2244)))
sleep(3)
touch(Template(r"tpl1583835961740.png",record_pos=(0.419,-0.889),resolution=(1080,2244)))
touch(Template(r"tpl1583835974321.png",record_pos=(-0.302,-0.357),resolution=(1080,2244)))
touch(Template(r"tpl1583836002654.png",record_pos=(-0.005,-0.042),resolution=(1080,2244)))
text("AirTest编辑详情描述")
touch(Template(r"tpl1583836027375.png",record_pos=(0.424,-0.892),resolution=(1080,2244)))
touch(Template(r"tpl1583835961740.png",record_pos=(0.419,-0.889),resolution=(1080,2244)))
touch(Template(r"tpl1583836078236.png",record_pos=(-0.269,-0.228),resolution=(1080,2244)))
touch(Template(r"tpl1583836087925.png",record_pos=(0.005,-0.451),resolution=(1080,2244)))
text("AirTest添加描述")
touch(Template(r"tpl1583836107135.png",record_pos=(0.376,0.895),resolution=(1080,2244)))

#通过
touch(Template(r"tpl1583835961740.png",record_pos=(0.419,-0.889),resolution=(1080,2244)))
touch(Template(r"tpl1583836716390.png",record_pos=(-0.119,-0.099),resolution=(1080,2244)))
touch(Template(r"tpl1583836735124.png",record_pos=(0.31,0.175),resolution=(1080,2244)))
assert_exists(Template(r"tpl1583836763923.png",record_pos=(-0.22,0.885),resolution=(1080,2244)),"没有通过")

touch(Template(r"tpl1583835961740.png",record_pos=(0.419,-0.889),resolution=(1080,2244)))
touch(Template(r"tpl1583836782808.png",record_pos=(-0.007,0.172),resolution=(1080,2244)))
touch(Template(r"tpl1583836735124.png",record_pos=(0.31,0.175),resolution=(1080,2244)))
sleep(10)
assert_not_exists(Template(r"tpl1583836602008.png",record_pos=(0.012,-0.632),resolution=(1080,2244)),"删除失败")


touch(Template(r"tpl1583733674919.png", record_pos=(-0.428, -0.894), resolution=(1080, 2244)))
sleep(1)
touch(Template(r"tpl1583733674919.png", record_pos=(-0.428, -0.894), resolution=(1080, 2244)))
sleep(1)
touch(Template(r"tpl1583732941380.png", record_pos=(-0.369, 0.945), resolution=(1080, 2244)))
    
