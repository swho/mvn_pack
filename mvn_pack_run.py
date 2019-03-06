# coding=utf-8
from mvn_pack import Mvn_Pack

op = input('1=執行匯出(放到pom.xml底下   2=執行匯入(和pom、jar放在一起):')

if op == '1':
    Mvn_Pack().gen_export()
elif op == '2':
    Mvn_Pack().gen_import('.\\*.pom')
else:
    print('end')
