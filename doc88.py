# 使用之前需要pip install PyMuPDF
# pip install requests
import requests
import os
import glob
import fitz
import html
from urllib import parse
import json
# 第一步获取返回编码后的data
# p_code = 3995949474894
p_code = input('''请输入相应页面的p_code,
如https://m.doc88.com/p-3995949474894.html的p_code为 3995949474894 ：''')
print('下载中。。。')
header = {
    'Referer': 'http://m.doc88.com/',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 9; ONEPLUS A6010 Build/PKQ1.180716.001; wv) AppleWebKit/537.36 (KHTML, '
                  'like Gecko) Version/4.0 Chrome/76.0.3809.89 Mobile Safari/537.36 T7/11.19 SP-engine/2.15.0 '
                  'baiduboxapp/11.19.0.11 (Baidu; P1 9) '
}
url = 'https://m.doc88.com/' + 'doc.php?act=info&p_code=' + str(p_code) + '&key=3854933de90d1dbb321d8ca29eac130a&v=1'
result = requests.get(url, headers=header)
return_data = result.text


# 第二步 模拟JS 将data解码 得到gif的url
m_base64Str = ''
m_base64Count = 0
m_END_OF_INPUT = -1
m_base64Chars_r = [
    'P', 'J', 'K', 'L', 'M', 'N', 'O', 'I',
    '3', 'y', 'x', 'z', '0', '1', '2', 'w',
    'v', 'p', 'r', 'q', 's', 't', 'u', 'o',
    'B', 'H', 'C', 'D', 'E', 'F', 'G', 'A',
    'h', 'n', 'i', 'j', 'k', 'l', 'm', 'g',
    'f', 'Z', 'a', 'b', 'c', 'd', 'e', 'Y',
    'X', 'R', 'S', 'T', 'U', 'V', 'W', 'Q',
    '!', '5', '6', '7', '8', '9', '+', '4'
]
m_reverseBase64Chars = {element: index for index, element in enumerate(m_base64Chars_r)}


def m_setBase64Str(s):
    global m_base64Count, m_base64Str
    m_base64Str = s
    m_base64Count = 0


def utf8to16(s: str):
    # i = 0
    # length = len(s)
    # result = ''
    # while i < length:
    #     pass
    pass


def m_readReverseBase64():
    global m_base64Count, m_base64Str, m_reverseBase64Chars
    if not m_base64Str:
        return -1
    while 1:
        if m_base64Count >= len(m_base64Str):
            return -1
        nextCharacter = m_base64Str[m_base64Count]
        m_base64Count += 1
        try:
            if m_reverseBase64Chars[nextCharacter]:
                return m_reverseBase64Chars[nextCharacter]
        except:
            # print(m_reverseBase64Chars)
            # print(nextCharacter)
            pass
        if nextCharacter == 'P':
            return 0
    return -1


def m_ntos(n):
    n = hex(n)
    n = n[2:]
    if len(n) == 1:
        n = "0" + n[-1]
    n = '%' + n
    return html.unescape(n)


def decode_base64(s: str):
    m_setBase64Str(s)
    result = ''
    done = False
    m_END_OF_INPUT = -1
    inBuffer = [0, 0, 0, 0]
    inBuffer[0] = m_readReverseBase64()
    inBuffer[1] = m_readReverseBase64()
    while (not done) and (inBuffer[0] != m_END_OF_INPUT) and (inBuffer[1] != m_END_OF_INPUT):
        inBuffer[2] = m_readReverseBase64()
        inBuffer[3] = m_readReverseBase64()
        result += m_ntos((((inBuffer[0] << 2) & 0xff) | inBuffer[1] >> 4))
        if inBuffer[2] != m_END_OF_INPUT:
            result += m_ntos((((inBuffer[1] << 4) & 0xff) | inBuffer[2] >> 2))
            if inBuffer[3] != m_END_OF_INPUT:
                result += m_ntos((((inBuffer[2] << 6) & 0xff) | inBuffer[3]))
            else:
                done = True
        else:
            done = True
        inBuffer[0] = m_readReverseBase64()
        inBuffer[1] = m_readReverseBase64()
    return parse.unquote(result)


# print(decode_base64(
#     'GSyeBuVl3jfioIsUHuynoIsVHOsVoIsW1jFnoIs!0OHkoIsVBmB5oIsW0jkQoIsW1q1ioIsV0uHioIsQ2LMUoIsQBqEWoIsQHuHjoIs!HmBX3iXiHOtTBQyZEIpZDW!i2iyEFqplBmNEFqtkHqtEFqBW1WNEFqhXHmpEFqtiHjlEFqBS2qFEFqBV0WyEFqsRHmyEFqE!0qpEFqFn1THEFqFlHm1EFqnmHjPizKybHolQDQyk3jfi3iXiEONgHu1YFu5U3jfi2r3c3mpYBWHYEmVnFK363lJMpi3c3g1UEgtjFK363ld7oKyXoK360rRE3gFE3jfV2LPcoKyfoK362LETArR7oKyXoK360iRE3gFE3jfV2L3coKyfoK362LEWArR7oKyXoK360SRE3gFE3jfV2L3coKyfoK362LEVArR7oKyXoK361KRE3gFE3jfV2LMcoKyfoK362LEXArR7oKyXoK361rRE3gFE3jfV1TkcoKyfoK362LEXArR7oKyXoK361iRE3gFE3jfV1TBcoKyfoK362LEUArR7oKyXoK361SRE3gFE3jfV1TEcoKyfoK362LESArR7oKyXoK362KRE3gFE3jfV2LMcoKyfoK362LEUArR7oKyXoK362rRE3gFE3jfV1TEcoKyfoK362LEXAtUizKygCuBi2jMc3gFlBg1fBoyl3jfRzKyQCupUCK360qPS1KXiHWlmoQ1UEgtjFK363ld7oKyXoK360rRE3gtE3jZE3jJasN3SEltB0t1tsjJSttvSEudu0gNW1qN0ptsSqOdtGgNvHLJRpt0RCmduGgN1wtXiArR7oKyXoK360iRE3gtE3jZE3jJasN3SEltB0t1tsjJSttvSEudu0gNW1qN0ptsSqOdtGgN1sqJarLsREltq0NpNtjNRrOvXFjU9oKy9zIdE3gJE3jfTzNXiFtXi2lXi0OZvsjyStthRsVtr0IyttLyRCVBSEoBV0sRNtqy0CVt6EoHr0MXTtjJStt0SqOcn0kReHLJWwqVE3gUcGVXiENXi2jvcoKyVoK36oK3XClJr0gytuLNqtt3XElts0gNbtjyRFjsRqMtt0kRbtoZRpthXqMVs0gytsTy0FlBREstk0IB9wtXiArR7oKyXoK361rRE3gtE3jZE3jJasN3SEltB0t1tsjJSttvSEudu0gNW1qN0ptsSqOdtGgNb3qN0rLsRCttq0tpbsqJspuvXFjU9oKy9zIdE3gJE3jfWzNXiFtXi2lXi0OZvsjyStthRsVtr0IyttLyRCVBSEoBV0sRNtqy0CVt6EsVq0uZWtqJs0OvXtNJp0MXTtQZRqqVE3gUcGVXiENXi2jEcoKyVoK36oK3XClJr0gytuLNqtt3XElts0gNbtjyRFjsRqMtt0kRbtoZRqtBRtMVt0oNbHLJaEVvREsUVGgN1wtXiArR7oKyXoK362KRE3gtE3jZE3jJasN3SEltB0t1tsjJSttvSEudu0gNW1qN0ptsSqOdtGgN13qJaFjsRtO5k0OZvsqJaFlp6EsU9oKy9zIdE3gJE3jf5zNXiFtXi2lXi0OZvsjyStthRsVtr0IyttLyRCVBSEoBV0sRNtqy0CVt6Eq1B0NvTsTJaquvXEoBV0tp3soZRqqVE3gVF3iXiHWlmoQJnHWsi2i353iXiHWlmoWnYEQvi2iyfFIpXETZEzVXYHWlmzmpYBTh!zm1YDr3c3mldHWnYEQvi2iyfFIpXETZEzVXYDosQzmpYBTh!zm1YDr3c3gJABW9kHr363j052qs51LkU1Tv!2qvizKycDWFZDl9eBuVl3jfiFIynFmtcHoyTBWNe0q3X3iXiDmljCV9eBuVl3jfiFIynFmtcHoyTBWNe0q3X3iXiEotnDOlUGr360rXiFoJcDWNkoQpZDusi2i3R1qBS1ThV0qhW3iXiEOlj3jfiCIpUEI06oK9EzQJeHS5kDW0!2K5jDWVEzT3X0qlEzTPQoK8R0tXY0Tk51qkU2qvQ1Lh51N8R1jPeEO5g3gU='))
base64str = decode_base64(return_data)
s = json.loads(base64str)
# print(s)
gif_host = s['gif_host']
struct = s['struct']
gif_urls = s['gif_struct']
file_name = s['name']
gif_urls = json.loads(gif_urls)
# 第三步将gif存储起来
# print(gif_urls)
if os.path.exists(file_name):
    print('请先删除同名文件夹')
os.mkdir(file_name)
for index, element in enumerate(gif_urls):
    gif_url = gif_host + "/get-" + element['u'] + ".gif"
    result = requests.get(gif_url)
    with open(f'./{file_name}/'+f'{index}.gif'.rjust(7, '0'), 'wb') as f:
        f.write(result.content)


# 第四步合并gif为pdf
def pic2pdf(file_name):
    doc = fitz.open()
    for img in sorted(glob.glob(f"./{file_name}/*")):  # 读取图片，确保按文件名排序
        # print(img)
        imgdoc = fitz.open(img)  # 打开图片
        pdfbytes = imgdoc.convertToPDF()  # 使用图片创建单页的 PDF
        imgpdf = fitz.open("pdf", pdfbytes)
        doc.insertPDF(imgpdf)  # 将当前页插入文档
    if os.path.exists(f"./{file_name}/{file_name}.pdf"):
        os.remove(f"./{file_name}/{file_name}.pdf")
    doc.save(f"./{file_name}/{file_name}.pdf")  # 保存pdf文件
    doc.close()


pic2pdf(file_name)
print('下载完毕！')