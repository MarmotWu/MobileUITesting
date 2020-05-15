#coding = utf-8
#author:chenjq
import os
deviceType = "app"                                                             #设备类别：app、win和web
devices = ['Android:///']                            		#设备信息，只有当deviceType为app是有效
root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))         #工程根目录
air_path = os.path.join(root_path,'air')                                        #脚本目录
log_path =os.path.join(root_path,'log')                                         #日志目录
template_path=os.path.join(root_path,'template')                                #测试报告模板目录
report_path=os.path.join(root_path,'report')                                    #测试报告路径
data_path = os.path.join(root_path, 'data')                                     #测试数据目录
template_name ="summary_template.html"                                          #测试报告模板名称
clear_report = False                                                            #是否清空旧测试报告
