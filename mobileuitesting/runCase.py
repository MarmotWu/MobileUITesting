# -*- coding: utf-8 -*-
from airtest.cli.runner import AirtestCase,run_script
import airtest.report.report as report
from conf.settings import *
from argparse import *
import argparse
import shutil,os,io,jinja2,datetime
from lib.common import RetryFunc
from lib.common import setMsg
from lib import video
from airtest.core.helper import device_platform
from airtest.core.api import auto_setup, log, connect_device


class Air_Case_Handler(AirtestCase):
    def __init__(self,dev_id):
        super(Air_Case_Handler, self).__init__()
        if deviceType.upper() == "WEB":
            pass
        else:
            self.dev = connect_device(dev_id)

    def setUp(self):
        super(Air_Case_Handler, self).setUp()

    def tearDown(self):
        super(Air_Case_Handler,self).tearDown()


    def run_air(self,air_dir,device,case='ALL'):
        start_time = datetime.datetime.now()
        start_time_fmt = start_time.strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
        results = []
        root_log = log_path
        if os.path.isdir(root_log):
            #shutil.rmtree(root_log)
            pass
        else:
            os.makedirs(root_log)

        #setMsg("吴国君_胡彪","BV测试",'开始执行APP_Android_UI自动化脚本')
        AirTestCase_list =[]
        if case=='ALL':
            for module in os.listdir(air_path):
                if module!='__init__.py':
                    for file in os.listdir(os.path.join(air_path,module)):
                        file = module+'@'+file
                        AirTestCase_list.append(file)
        else:
            for file in os.listdir(os.path.join(air_path,case)):
                file = case+'@'+file
                AirTestCase_list.append(file)
        print(AirTestCase_list)
        for files in AirTestCase_list:
            if files.endswith(".air") and str(files.split(".")[0]).split('@')[1] not in ['CommonStart','CommonEnd']:
                file =files.split('@')[1]
                Module = files.split('@')[0]
                air_dir_module = os.path.join(air_dir,Module)
                airDirName = file.replace(".air","")
                script = os.path.join(air_dir_module,file)
                air_log_start, air_log_end= os.path.join(root_path,r"log\CommonStart"),os.path.join(root_path,r"log\CommonEnd")
                air_log = os.path.join(root_path,"log\\" + airDirName+'_'+datetime.datetime.now().strftime("%Y%m%d%H%M%S"))

                if os.path.isdir(air_log):
                    #print(air_log)
                    shutil.rmtree(air_log)

                else:
                    os.makedirs(air_log)

                html = os.path.join(air_log,"log.html")
                if deviceType.upper() == "WEB":
                    args = Namespace(log=air_log, recording=None, script=script,
                                         language="zh")
                elif deviceType.upper() == "APP":
                    args = Namespace(device=device, log = air_log, recording=airDirName+".mp4", script=script,language="zh")
                else:
                    args = Namespace(device=device, log=air_log, recording=None, script=script,
                                         language="zh")
                try:
                    #run_script(Namespace(device=device, log = air_log_start,recording='CommonStart.mp4',script=os.path.join(air_dir,'CommonStart.air'),language="zh"),AirtestCase)
                    run_script(args,AirtestCase)
                    #setMsg("吴国君_胡彪","BV测试",airDirName+'_UI自动化脚本执行成功')
                except:
                    setMsg("吴国君","BV测试",airDirName+'_UI自动化脚本执行失败')
                    run_script(Namespace(device=device, log = air_log_end,recording='CommonEnd.mp4',script=os.path.join(air_dir,'Common\CommonEnd.air'),language="zh"),AirtestCase)
                finally:
                    rpt = report.LogToHtml(script, air_log)
                    rpt.report("log_template.html", output_file=html)
                    result = {}
                    result["name"] = air_log.split("\\")[-1]
                    result["result"] = rpt.test_result
                    results.append(result)


        end_time = datetime.datetime.now()
        end_time_fmt = end_time.strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]


        duration = (end_time - start_time).seconds


        env = jinja2.Environment(
            loader=jinja2.FileSystemLoader(template_path),
            extensions=(),
            autoescape=True
        )

        template = env.get_template(template_name, template_path)
        project_name = root_path.split("\\")[-1]
        success = 0
        fail = 0
        for res in results:
            if res['result']:
                success += 1
            else:
                fail += 1
        report_name = "report_"+end_time.strftime("%Y%m%d%H%M%S")+".html"
        html = template.render({"results": results,"device":device,"stime":start_time_fmt,'etime':end_time_fmt,'duration':duration,"project":project_name,"success":success,"fail":fail})
        output_file = os.path.join(root_path,"report" ,report_name)
        with io.open(output_file, 'w', encoding="utf-8") as f:
            f.write(html)

if __name__ == "__main__":
    for device in devices:
        test = Air_Case_Handler(device)
        parser = argparse.ArgumentParser(description='manual to this script')
        parser.add_argument('--Module', type=str, default = 'ALL')
        args = parser.parse_args()
        test.run_air(air_path,device,case=args.Module)
    print('end')