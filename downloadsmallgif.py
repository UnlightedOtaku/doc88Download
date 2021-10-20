# 对于某些doc88的文档 使用的是四个gif拼成一页的方式
# 把每个gif都下载下来
# 随后再进行拼接
import requests
import re
import datetime
import time


# 首先普通请求一次，找到imgHostKey和totalPage 分辨率大小size
p_code = '6913506539924'
url = f'https://m.doc88.com/p-{p_code}.html'
header = {
    'Referer': 'http://m.doc88.com/',
    # 'User-Agent': 'Mozilla/5.0 (Linux; Android 9; ONEPLUS A6010 Build/PKQ1.180716.001; wv) AppleWebKit/537.36 (KHTML, '
    #               'like Gecko) Version/4.0 Chrome/76.0.3809.89 Mobile Safari/537.36 T7/11.19 SP-engine/2.15.0 '
    #               'baiduboxapp/11.19.0.11 (Baidu; P1 9) '
    'User-Agent': 'Mozilla/5.0 (Linux; Android 4.4.2; Nexus 4 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.114 Mobile Safari/537.36'
}
result = requests.get(url,headers=header)
return_data = result.text
# print(return_data)

# 一张图片的url为： https://{imgHostKey}.doc88.com/p.do?id={pcode}-{page}-{resolution}-0-4-{part}(可以为00,01,10,11对应左上，右上，左下，右下)-2-1-{hour}(当前小时数)
# https://mt7.doc88.com/p.do?id=7844760731971-1-960-0-4-00-2-1-15


# 使用正则表达式从返回结果中找到imgHostKey和totalPage
pattern1 = 'var imgHostKey = ".*"'
pattern2 = 'var totalPage = ".*"'
result1 = re.search(pattern1,return_data)
imgHostKey = result1.group(0).split('=')[-1].strip().strip('"')
print(imgHostKey)
result2 = re.search(pattern2,return_data)
totalPage = int(result2.group(0).split('=')[-1].strip().strip('"'))
print(totalPage)
resolution_height = r'var resolution_height = \d*'
resolution_height = re.search(resolution_height,return_data)

resolution_height = int(resolution_height.group(0).split('=')[-1].strip())
resolution_width = r'var resolution_width = \d*'
resolution_width = re.search(resolution_width,return_data)

resolution_width = int(resolution_width.group(0).split('=')[-1].strip())

# size = min(resolution_height,resolution_width)
size = max(resolution_height,resolution_width)
print("使用imgswitch时记得改size为:%s"%size)


# 获取当前小时
hour = datetime.datetime.now().strftime("%H")
aList = ['00','01','10','11']
# 下载全部图片
# 构造url下载gif
for page in range(1, totalPage+1):
    # 频繁访问会被服务器禁止爬取
    if page % 5 == 0:
        time.sleep(3)
    for part in aList:
        imgUrl = f'https://{imgHostKey}.doc88.com/p.do?id={p_code}-{page}-{size}-0-4-{part}-2-1-{hour}'
        # print(imgUrl)
        file_name = str(page) + '_' + part 
        result = requests.get(imgUrl,headers=header)
        # print(result.content)
        if result.content:
            with open(f'./{file_name}.gif', 'wb') as f:
                    f.write(result.content)
        else:
            # 频繁访问会被服务器禁止爬取
            print('爬取失败的url为:')
            print(imgUrl)
            time.sleep(10)
            result = requests.get(imgUrl,headers=header)
            # print(result.content)
            if result.content:
                with open(f'./{file_name}.gif', 'wb') as f:
                        f.write(result.content)
