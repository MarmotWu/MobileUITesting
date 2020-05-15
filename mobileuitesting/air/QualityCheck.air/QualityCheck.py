# -*- encoding=utf8 -*-
__author__ = "user5467"

from airtest.core.api import *

auto_setup(__file__)
# try:
touch(Template(r"tpl1583732941380.png", record_pos=(-0.13, 0.944), resolution=(1080, 2244)))
touch(Template(r"tpl1583732957417.png", record_pos=(0.369, -0.482), resolution=(1080, 2244)))
swipe(Template(r"tpl1583733089674.png", record_pos=(-0.364, 0.651), resolution=(1080, 2244)), vector=[0.0264, -0.6913])
swipe(Template(r"tpl1583733145187.png", record_pos=(-0.367, -0.056), resolution=(1080, 2244)), vector=[-0.0432, 0.726])



#新增
touch(Template(r"tpl1583733996438.png", record_pos=(-0.36, -0.366), resolution=(1080, 2244)))
sleep(2)
touch(Template(r"tpl1583733188899.png", record_pos=(0.323, -0.892), resolution=(1080, 2244)))
touch(Template(r"tpl1583733215366.png", record_pos=(0.008, -0.444), resolution=(1080, 2244)))
text("Airtest检查部门")
touch(Template(r"tpl1583733389488.png", record_pos=(0.008, -0.219), resolution=(1080, 2244)))
touch(Template(r"tpl1583733400720.png", record_pos=(-0.241, -0.088), resolution=(1080, 2244)))
touch(Template(r"tpl1583737082314.png", record_pos=(-0.003, -0.702), resolution=(1080, 2244)))
touch(Template(r"tpl1583734057114.png", record_pos=(0.0, 0.022), resolution=(1080, 2244)))
sleep(5)
touch(Template(r"tpl1583734074665.png", record_pos=(-0.051, -0.629), resolution=(1080, 2244)))
touch(Template(r"tpl1583734083860.png", record_pos=(-0.146, -0.484), resolution=(1080, 2244)))
swipe(Template(r"tpl1583734111296.png", record_pos=(-0.357, 0.519), resolution=(1080, 2244)), vector=[0.0072, -0.6092])
touch(Template(r"tpl1583735129829.png", record_pos=(-0.33, 0.327), resolution=(1080, 2244)))
text("Airtest整改要求")
touch(Template(r"tpl1583734147271.png", record_pos=(-0.053, 0.512), resolution=(1080, 2244)))
text("Airtest检查部位")
touch(Template(r"tpl1583733554836.png", record_pos=(0.035, 0.917), resolution=(1080, 2244)))
touch(Template(r"tpl1583733674919.png", record_pos=(-0.428, -0.894), resolution=(1080, 2244)))
sleep(1)


#编辑
touch(Template(r"tpl1583735600500.png", record_pos=(0.004, -0.736), resolution=(1080, 2244)))
touch(Template(r"tpl1583735609278.png", record_pos=(0.42, -0.9), resolution=(1080, 2244)))
touch(Template(r"tpl1583735617340.png", record_pos=(0.383, -0.732), resolution=(1080, 2244)))
swipe(Template(r"tpl1583734111296.png", record_pos=(-0.357, 0.519), resolution=(1080, 2244)), vector=[0.0072, -0.6092])
touch(Template(r"tpl1583735129829.png", record_pos=(-0.33, 0.327), resolution=(1080, 2244)))
text("Airtest整改要求-编辑测试")
touch(Template(r"tpl1583733554836.png", record_pos=(0.035, 0.917), resolution=(1080, 2244)))
touch(Template(r"tpl1583733674919.png", record_pos=(-0.428, -0.894), resolution=(1080, 2244)))
sleep(1)


#筛选
touch(Template(r"tpl1583735827092.png", record_pos=(0.425, -0.891), resolution=(1080, 2244)))
touch(Template(r"tpl1583735880415.png", record_pos=(0.08, -0.239), resolution=(1080, 2244)))
touch(Template(r"tpl1583735893999.png", record_pos=(-0.142, 0.006), resolution=(1080, 2244)))
touch(Template(r"tpl1583735903052.png", record_pos=(0.281, 0.889), resolution=(1080, 2244)))
assert_exists(Template(r"tpl1583736012774.png", record_pos=(0.025, -0.757), resolution=(1080, 2244)), "筛选不到新增数据")


#查看详情
touch(Template(r"tpl1583736067070.png", record_pos=(0.004, -0.744), resolution=(1080, 2244)))
assert_exists(Template(r"tpl1583736086468.png", record_pos=(-0.149, 0.068), resolution=(1080, 2244)), "详情不正确")


#删除新增数据
touch(Template(r"tpl1583735609278.png", record_pos=(0.42, -0.9), resolution=(1080, 2244)))
touch(Template(r"tpl1583736159061.png", record_pos=(0.369, -0.587), resolution=(1080, 2244)))
touch(Template(r"tpl1583736174640.png", record_pos=(0.31, 0.172), resolution=(1080, 2244)))





touch(Template(r"tpl1583733674919.png", record_pos=(-0.428, -0.894), resolution=(1080, 2244)))
sleep(1)
touch(Template(r"tpl1583733674919.png", record_pos=(-0.428, -0.894), resolution=(1080, 2244)))
sleep(1)
touch(Template(r"tpl1583732941380.png", record_pos=(-0.369, 0.945), resolution=(1080, 2244)))
# except :
#     #touch(Template(r"tpl1583733674919.png", record_pos=(-0.428, -0.894), resolution=(1080, 2244)))
#     #sleep(1)
#     n=1
#     while(n!=0):
#         if assert_not_exists(Template(r"tpl1583732941380.png", record_pos=(-0.13, 0.944), resolution=(1080, 2244)),"脚本失败")==None:
#             touch(Template(r"tpl1583733674919.png", record_pos=(-0.428, -0.894), resolution=(1080, 2244)))
#             sleep(1)
#         else : n=0
            
    