#!/usr/bin/env python
# -*- coding: utf-8 -*-
#@time    : 2020/4/10 21:40
#@Author  : 小米
import os,zipfile

class Myzip:
    def __init__(self):
        pass

    @classmethod
    def compress_file(cls,version):
        root_path = "/report/"
        report_folder = os.path.split(os.path.dirname(__file__))[0] + root_path
        zip_path = os.path.join(report_folder,"%s_report.zip" % version)
        zip = zipfile.ZipFile(zip_path,"w",zipfile.ZIP_LZMA)
        file_list = []
        for root,folders,filenames in os.walk(report_folder):
            for folder in folders:
                file_list.append(os.path.join(root,folder))
            for filename in filenames:
                if not filename.endswith("zip") and version in filename:
                    file_list.append(os.path.join(root, filename))
        for file in file_list:
            #锚位置 path = file.split(root_path)[1])
            zip.write(file,file.split(root_path)[1])
        zip.close()
        return zip_path





# if __name__ == '__main__':
#     Myzip().compress_file("WoniuBoss")