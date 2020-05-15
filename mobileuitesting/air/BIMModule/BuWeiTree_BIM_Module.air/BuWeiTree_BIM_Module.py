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


#模型
touch(Template(r"tpl1584070498635.png", record_pos=(-0.35, 0.669), resolution=(1080, 2244)))
touch(Template(r"tpl1584070517997.png", record_pos=(-0.179, -0.02), resolution=(1080, 2244)))
touch(Template(r"tpl1584070525299.png", record_pos=(-0.305, -0.014), resolution=(1080, 2244)))
assert_exists(Template(r"tpl1584068200071.png", record_pos=(-0.365, -0.488), resolution=(1080, 2244)), "属性页面不正确")
touch(Template(r"tpl1584063937211.png", record_pos=(-0.438, -0.895), resolution=(1080, 2244)))
sleep(2)

#状态
touch(Template(r"tpl1584064400628.png", record_pos=(-0.005, -0.01), resolution=(1080, 2244)))
assert_exists(Template(r"tpl1584064007596.png", record_pos=(0.032, 0.087), resolution=(1080, 2244)), "状态页面不正确")
touch(Template(r"tpl1584063937211.png", record_pos=(-0.438, -0.895), resolution=(1080, 2244)))
sleep(2)

#协作
touch(Template(r"tpl1584064055354.png", record_pos=(0.296, 0.033), resolution=(1080, 2244)))
touch(Template(r"tpl1584064558912.png", record_pos=(0.373, 0.907), resolution=(1080, 2244)))
sleep(1)
touch(Template(r"tpl1584064143097.png", record_pos=(-0.014, -0.321), resolution=(1080, 2244)))
text("AirTest创建主题-模型-构件")
sleep(1)
touch(Template(r"tpl1584068087338.png", record_pos=(-0.012, 0.031), resolution=(1080, 2244)))
touch(Template(r"tpl1584064189798.png", record_pos=(-0.241, -0.098), resolution=(1080, 2244)))
sleep(1)
touch(Template(r"tpl1584064733387.png", record_pos=(0.024, 0.031), resolution=(1080, 2244)))
touch(Template(r"tpl1584064209241.png", record_pos=(-0.24, -0.036), resolution=(1080, 2244)))
sleep(2)
touch(Template(r"tpl1584064701094.png", record_pos=(-0.209, -0.034), resolution=(1080, 2244)))
touch(Template(r"tpl1584064235451.png", record_pos=(0.424, -0.899), resolution=(1080, 2244)))
touch(Template(r"tpl1584064261073.png", record_pos=(0.401, -0.894), resolution=(1080, 2244)))
sleep(8)
assert_exists(Template(r"tpl1584064812039.png", record_pos=(0.013, -0.623), resolution=(1080, 2244)), "未获取到创建的协作")
touch(Template(r"tpl1584064867923.png", record_pos=(0.036, -0.616), resolution=(1080, 2244)))
sleep(1)
touch(Template(r"tpl1584064903636.png", record_pos=(0.022, 0.092), resolution=(1080, 2244)))
assert_exists(Template(r"tpl1584064940457.png", record_pos=(-0.153, -0.018), resolution=(1080, 2244)), "请填写测试点")
assert_exists(Template(r"tpl1584065003417.png", record_pos=(-0.191, -0.773), resolution=(1080, 2244)), "部位树获取不正确")

touch(Template(r"tpl1584064952918.png", record_pos=(-0.437, -0.891), resolution=(1080, 2244)))
sleep(1)
touch(Template(r"tpl1584065052773.png", record_pos=(0.426, -0.888), resolution=(1080, 2244)))
touch(Template(r"tpl1584065060085.png", record_pos=(-0.303, 0.435), resolution=(1080, 2244)))
touch(Template(r"tpl1584065067153.png", record_pos=(0.307, 0.169), resolution=(1080, 2244)))


#资料
touch(Template(r"tpl1584065036712.png", record_pos=(0.09, -0.774), resolution=(1080, 2244)))
touch(Template(r"tpl1584064558912.png", record_pos=(0.373, 0.907), resolution=(1080, 2244)))
touch(Template(r"tpl1584068087338.png", record_pos=(-0.012, 0.031), resolution=(1080, 2244)))
touch(Template(r"tpl1584064189798.png", record_pos=(-0.241, -0.098), resolution=(1080, 2244)))
sleep(1)
touch(Template(r"tpl1584064733387.png", record_pos=(0.024, 0.031), resolution=(1080, 2244)))
sleep(1)
touch(Template(r"tpl1584064209241.png", record_pos=(-0.24, -0.036), resolution=(1080, 2244)))
sleep(3)
touch(Template(r"tpl1584068533015.png", record_pos=(-0.16, -0.046), resolution=(1080, 2244)))
touch(Template(r"tpl1584064235451.png", record_pos=(0.424, -0.899), resolution=(1080, 2244)))
sleep(2)
touch(Template(r"tpl1584065159273.png", record_pos=(0.011, -0.318), resolution=(1080, 2244)))
touch(Template(r"tpl1584065165224.png", record_pos=(-0.331, -0.765), resolution=(1080, 2244)))
touch(Template(r"tpl1584065204870.png", record_pos=(0.138, 0.944), resolution=(1080, 2244)))
touch(Template(r"tpl1584065213986.png", record_pos=(0.435, 0.028), resolution=(1080, 2244)))
touch(Template(r"tpl1584065220720.png", record_pos=(-0.194, -0.034), resolution=(1080, 2244)))
touch(Template(r"tpl1584067221972.png", record_pos=(0.174, -0.767), resolution=(1080, 2244)))
touch(Template(r"tpl1584065436724.png", record_pos=(0.34, -0.891), resolution=(1080, 2244)))
sleep(3)
touch(Template(r"tpl1584065445726.png", record_pos=(0.25, 0.95), resolution=(1080, 2244)))
sleep(3)
touch(Template(r"tpl1584065463123.png", record_pos=(0.238, 0.175), resolution=(1080, 2244)))
sleep(1)

#材料
touch(Template(r"tpl1584067275109.png", record_pos=(0.248, -0.77), resolution=(1080, 2244)))
assert_exists(Template(r"tpl1584067281457.png", record_pos=(-0.336, -0.661), resolution=(1080, 2244)), "材料页面")


#消耗量
touch(Template(r"tpl1584067530913.png", record_pos=(0.411, -0.781), resolution=(1080, 2244)))
assert_exists(Template(r"tpl1584067538816.png", record_pos=(0.022, 0.076), resolution=(1080, 2244)),"消耗量页面获取失败")
touch(Template(r"tpl1584064952918.png", record_pos=(-0.437, -0.891), resolution=(1080, 2244)))
sleep(1)
touch(Template(r"tpl1584064952918.png", record_pos=(-0.437, -0.891), resolution=(1080, 2244)))
sleep(1)
touch(Template(r"tpl1584064952918.png", record_pos=(-0.437, -0.891), resolution=(1080, 2244)))
sleep(1)
touch(Template(r"tpl1584064952918.png", record_pos=(-0.437, -0.891), resolution=(1080, 2244)))
sleep(1)
touch(Template(r"tpl1583732941380.png", record_pos=(-0.13, 0.944), resolution=(1080, 2244)))









