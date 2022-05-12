# doc88Download
python下载道客巴巴手机端文档


-----------------------------------------------------------------------------

说明

道客巴巴的文档在手机端有三种 

1 没有手机端（那用我的代码肯定爬不了） 

2 一页是一张gif     

3 一页由四张gif组合而成



**第2种** 可以尝试一下使用doc88.py
使用python下载道客巴巴gif文件并自动合并为pdf

使用前请先确保安装了必要的库：

pip install PyMuPDF

pip install requests

没有python的可以直接下exe, 不保证可以运行


**第3种**的先用downloadsmallgif.py 下载小图片然后用imgswitch.py对图片进行拼接。

注意：downloadsmallgif.py和imgswitch.py仅为简单演示 并没有创建文件夹等操作并且imgswitch.py也仅仅合并了第一页的gif，后续合并其他页的gif和合并pdf请自便。



