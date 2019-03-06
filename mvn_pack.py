# coding=utf-8
import glob
import os
import subprocess
from sys import exit


def log(msg):
    print(msg)


class Mvn_Pack:
    TEMPLATE_IMPORT = 'mvn install:install-file -Dfile="{0}" -DpomFile="{1}"'
    TEMPLATE_EXPORT = 'mvn org.apache.maven.plugins:maven-dependency-plugin:2.10:copy-dependencies -Dmdep.addParentPoms=true -Dmdep.copyPom=true'

    def __init__(self) -> None:
        super().__init__()
        self.out = []

    def gen_import(self, dep_dir):
        files = glob.glob(dep_dir)
        if len(files) == 0:
            print('請放到jar、pom目錄')
            exit(0)

        for pomFile in files:
            target_file = pomFile
            jar_file = pomFile.replace('.pom', '.jar')
            if os.path.exists(jar_file):
                target_file = jar_file
            exe = Mvn_Pack.TEMPLATE_IMPORT.format(target_file, pomFile)
            self.out.append(exe)

        for exe in self.out:
            log(exe)

        log('共{0}個檔案將匯入Local'.format(len(self.out)))
        if input('確定執行(Y)?') == 'Y':
            self.do_import()
        else:
            log('程序中止')
            return

    def gen_export(self, ):
        if len(glob.glob('pom.xml')) == 0:
            print('請放到pom.xml目錄')
            exit(0)

        subprocess.Popen(Mvn_Pack.TEMPLATE_EXPORT).wait()
        os.system('copy mvn_pack_run.exe .\\target\\dependency\\')
        print('將 .\\target\\dependency 拷貝到另外一台電腦，執行mvn_pack_run.exe進行匯入')

    def do_import(self):
        for exe in self.out:
            subprocess.Popen(exe).wait()
