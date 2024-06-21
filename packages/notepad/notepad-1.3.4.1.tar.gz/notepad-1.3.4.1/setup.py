import sys,os
from setuptools import setup

try:
    os.chdir(os.path.split(__file__)[0])
except OSError:pass

try:
    long_desc=open("README.rst",encoding="gbk").read()
except OSError:
    long_desc=notepad.__doc__

try:os.rename("pynotepad.pyw","notepad.py")
except OSError:pass
import notepad

setup(
    name='notepad',
    version=notepad.__version__+".1",
    description="A featured open-source text editor using tkinter.一款功能齐全的tkinter文本编辑器程序。",
    long_description=long_desc,
    author=notepad.__author__,
    author_email=notepad.__email__,
    url="https://github.com/qfcy/Python/blob/main/pynotepad.pyw",
    py_modules=['notepad'], #这里是代码所在的文件名称
    keywords=["text","editor","notepad","tkinter","notepad","文本编辑器"],
    classifiers=[
        'Programming Language :: Python',
        "Topic :: Text Editors",
        "Topic :: Software Development :: User Interfaces",
        "Natural Language :: Chinese (Simplified)"],
    requires=["chardet","windnd"]
)
try:os.rename("notepad.py","pynotepad.pyw")
except OSError:pass
