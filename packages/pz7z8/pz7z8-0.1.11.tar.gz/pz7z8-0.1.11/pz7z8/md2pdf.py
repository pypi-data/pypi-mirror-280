#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#把md用pandoc转成pdf

import os,sys,re,pathlib

配置文件=pathlib.Path.joinpath(pathlib.Path(__file__).parent,"datafile","md2pdf.yaml")
头文件=pathlib.Path.joinpath(pathlib.Path(__file__).parent,"datafile","md2pdf.tex")

def filemtime(wj):
    if not os.path.isfile(wj):
        return 0
    return os.stat(wj).st_mtime

def pandoc(md):
    if os.path.isdir(md):
        for f in os.listdir(md):
            if not f.endswith(".md"):continue
            pandoc(os.path.join(md,f))
        return
    pdf=os.path.splitext(md)[0]+".pdf"
    if filemtime(md)>filemtime(pdf):
        配置文件2=os.path.join(os.path.split(md)[0],"md2pdf.yaml")
        if not os.path.isfile(配置文件2):
            配置文件2=""
        头文件2=os.path.join(os.path.split(md)[0],"md2pdf.tex")
        if not os.path.isfile(头文件2):
            头文件2=""
        cmd=f"pandoc -s -N --pdf-engine=xelatex -H {头文件2 or 头文件} -o {pdf} {配置文件2 or 配置文件} {md}"
        print(cmd)
        os.system(cmd)

def main():
    if len(sys.argv)<2:
        print("无参数,处理所有*.md")
        pandoc(".")
    for i in range(1,len(sys.argv)):
        pandoc(sys.argv[i])

if __name__ == "__main__":
    main()
