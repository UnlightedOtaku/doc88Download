# doc88Download
不让爷下载，爷偏要下 python给爷爬使用python下载道客巴巴文件并自动合并为pdf
使用前请先确保安装了必要的库：
pip install PyMuPDF
pip install requests
没有python的可以直接下[exe](https://github.com/UnlightedOtaku/doc88Download/releases/download/1.0/doc88.exe)
不保证可以运行
### **流程：访问构造的url获取base64编码后的值 将其解码 获取gif链接 下载gif 拼接gif为pdf**

**爬取地址来源电脑端不太好爬** 

**爬移动端 把网址的www改成m 再把UA改成移动端的（这一步浏览器不是很好用 我用的burp改的）**

只有一个js 文件（太棒了）

从js中找图片的地址 以下为大致过程 **可不看**

查找img 没有src 

查找src 找到

var gif_url = gif_host+"/get-"+pageinfo.url+".gif";

 $('#page-index-'+page).attr('src',gif_url);

再找gif_host和pageinfo.url

gif_host = 'https://gif.doc88.com'

pageinfo来自pageinfos[n]

pageinfos = JSON.parse(struct);  

var struct = jsonRes.struct;

var jsonRes = JSON.parse(base64Str);

var base64Str = m_decodeBase64(data);

一路找下来 

m_decodeBase64是个变体base64编码（想办法把这个js代码自己转换为python代码）

data为ajax返回数据

url = '/doc.php?act=info&p_code='+3995949474894+'&key=3854933de90d1dbb321d8ca29eac130a&v=1'

pcode就是页面代号 如  https://m.doc88.com/p-3995949474894.html 就是3995949474894



