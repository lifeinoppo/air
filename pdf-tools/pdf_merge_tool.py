#!/usr/bin/env python3
# encoding: utf-8

import zipfile
import PyPDF2
import io

# 新建一个空白pdf
pdfWriter = PyPDF2.PdfFileWriter()

# 循环获取pdf
zip = zipfile.ZipFile('fba.zip', 'r')

# 循环获取文件list
for filename in zip.namelist():

    # 过滤MAC自己生成的多余文件
    if filename.startswith('__MACOSX'):
        continue

    # 过滤只要pdf结尾的文件（因为目录可能包含 ./ ../）
    if filename.endswith('.pdf'):

        # zip 打开一个文件
        pdf = zip.open(filename, 'r')

        # 不生成临时文件 直接用BytesIO从二进制流中生成一个文件对象，避免生成临时文件然后再删除多余操作
        buf = io.BytesIO(pdf.read())

        # 用PyPDF工具读取pdf
        pdfReader = PyPDF2.PdfFileReader(buf)

        # 获取到总页数后range生成list循环获取每页
        for pageNum in range(pdfReader.numPages):

            # 把pdf所有页卸乳pdfWriter
            pdfWriter.addPage(pdfReader.getPage(pageNum))

# 打开（新建）一个 pdf 文件
pdfOutput = open('marge.pdf', 'wb')

# 把pdfWriter内容写如新建的文件
pdfWriter.write(pdfOutput)

# 关闭资源
pdfOutput.close()





