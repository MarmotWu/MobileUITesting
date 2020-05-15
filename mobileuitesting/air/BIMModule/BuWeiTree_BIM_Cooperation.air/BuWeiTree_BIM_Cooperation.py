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


#创建协作
touch(Template(r"tpl1584080539735.png", record_pos=(0.117, 0.672), resolution=(1080, 2244)))
sleep(1)
touch(Template(r"tpl1584080914793.png", record_pos=(0.34, -0.895), resolution=(1080, 2244)))
touch(Template(r"tpl1584064143097.png", record_pos=(-0.014, -0.321), resolution=(1080, 2244)))
text("AirTest创建主题-协作-工程")
sleep(1)
touch(Template(r"tpl1584064733387.png", record_pos=(0.024, 0.031), resolution=(1080, 2244)))
touch(Template(r"tpl1584070791962.png", record_pos=(-0.207, 0.168), resolution=(1080, 2244)))
touch(Template(r"tpl1584070904895.png", record_pos=(-0.039, -0.644), resolution=(1080, 2244)))
touch(Template(r"tpl1584070917158.png", record_pos=(-0.023, -0.517), resolution=(1080, 2244)))
touch(Template(r"tpl1584070926848.png", record_pos=(-0.002, -0.387), resolution=(1080, 2244)))
sleep(1)
touch(Template(r"tpl1584070939303.png", record_pos=(0.006, -0.264), resolution=(1080, 2244)))
touch(Template(r"tpl1584070946023.png", record_pos=(0.042, -0.142), resolution=(1080, 2244)))
touch(Template(r"tpl1584064235451.png", record_pos=(0.424, -0.899), resolution=(1080, 2244)))
touch(Template(r"tpl1584081051995.png", record_pos=(-0.013, 0.029), resolution=(1080, 2244)))
touch(Template(r"tpl1584081062794.png", record_pos=(-0.246, -0.087), resolution=(1080, 2244)))
touch(Template(r"tpl1584064261073.png", record_pos=(0.401, -0.894), resolution=(1080, 2244)))
sleep(8)
assert_exists(Template(r"tpl1584081355558.png", record_pos=(0.003, -0.742), resolution=(1080, 2244)), "未获取到创建的协作")
touch(Template(r"tpl1584081355558.png", record_pos=(0.003, -0.742), resolution=(1080, 2244)))
sleep(1)
touch(Template(r"tpl1584081438279.png", record_pos=(0.0, 0.103), resolution=(1080, 2244)))
sleep(1)
assert_exists(Template(r"tpl1584081459025.png", record_pos=(-0.03, -0.142), resolution=(1080, 2244)), "未获取到工程图形")
touch(Template(r"tpl1584064952918.png", record_pos=(-0.437, -0.891), resolution=(1080, 2244)))
touch(Template(r"tpl1584065052773.png", record_pos=(0.426, -0.888), resolution=(1080, 2244)))
touch(Template(r"tpl1584065060085.png", record_pos=(-0.303, 0.435), resolution=(1080, 2244)))
touch(Template(r"tpl1584065067153.png", record_pos=(0.307, 0.169), resolution=(1080, 2244)))
touch(Template(r"tpl1584064952918.png", record_pos=(-0.437, -0.891), resolution=(1080, 2244)))
sleep(1)
touch(Template(r"tpl1584064952918.png", record_pos=(-0.437, -0.891), resolution=(1080, 2244)))
sleep(1)
touch(Template(r"tpl1584064952918.png", record_pos=(-0.437, -0.891), resolution=(1080, 2244)))
sleep(1)
touch(Template(r"tpl1584064952918.png", record_pos=(-0.437, -0.891), resolution=(1080, 2244)))
sleep(1)
touch(Template(r"tpl1583732941380.png", record_pos=(-0.13, 0.944), resolution=(1080, 2244)))