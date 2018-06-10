# coding: utf-8
import re
#ファイルの読み込み
ifile_1=open('col1.txt', 'r')
ifile_2=open('col2.txt', 'r')

#一行ずつ処理をする
lines_1=ifile_1.readlines()
lines_2=ifile_2.readlines()

#結果用
resultLine=[]
for i in range(min(len(lines_1),len(lines_2))):
    #col1から改行コードを削除
    line_1=re.sub('\n','',lines_1[i])
    resultLine.append(line_1)
    #\tで繋げる
    resultLine.append('\t')
    resultLine.append(lines_2[i])
    #文字列化
    str=''.join(resultLine)

#テキストファイルの書き出し
ofile=open('col1+2.txt', 'w')
ofile.write(str)
ofile.close()