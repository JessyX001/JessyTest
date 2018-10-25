# coding:utf-8

import json
from urlparse import parse_qs
from wsgiref.simple_server import make_server

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5
import base64

# 定义函数，参数是函数的两个参数，都是python本身定义的，默认就行了。
def application(environ, start_response):
    # 定义文件请求的类型和当前请求成功的code
    start_response('200 OK', [('Content-Type', 'text/html')])
    # environ是当前请求的所有数据，包括Header和URL，body，这里只涉及到get
    # 获取当前get请求的所有数据，返回是string类型
    params = parse_qs(environ['QUERY_STRING'])

    # 获取get中key为token的值
    method = params.get('method', [''])[0]
    data = params.get('token', [''])[0]
    
    # 获取公钥数据
    public_key_file = open('D:\\jsy_auto\\ghost-public.pem', 'r')
    pub_key_str = public_key_file.read()
    public_key_file.close()

    pubobj = RSA.importKey(pub_key_str)
    pubobj = PKCS1_v1_5.new(pubobj)
    res = []

    for i in range(0, len(data), 100):
        res.append(pubobj.encrypt(data[i:i + 100]))
    s = "".join(res)
    cipher_text = base64.b64encode(s)

    #组成一个数组，数组中只有一个字典
    dic = {'method':method,'code': cipher_text}
    
    return [json.dumps(dic)]


if __name__ == "__main__":
    port = 5088
    httpd = make_server("0.0.0.0", port, application)
    print "serving http on port {0}...".format(str(port))
    httpd.serve_forever()



