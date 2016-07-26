#!/usr/bin/env python
# -*- coding: gbk -*-
# 'julian;jom;lewis;manu;jessica;yoko;wilson;abby'

def rtxim(commit_url='null',message="你",name="abby"):
    httpClient = None
    helloMsg = 'Hello Developer! \n\nAbby 的产品需求更新了 \n\n赶快去瞧瞧\n\nhttp://github.panli.com/abby/PanliByAbby/commits/master'
    robotM = '\n\n  我是来自运维团队的R2机器人的消息通知'
    devs = 'julian'
    sessionid = '{B242-486b-8487}'
    print commit_url
    print message
    print name
    try:
        params = urllib.urlencode({'sender': 'robot', 'pwd': 'robot', 'receivers': devs, 'msg': helloMsg+robotM, 'sessionid': sessionid})
        headers = {'Content-type': 'application/x-www-form-urlencoded', 'Accept': 'text/plain'}
        httpClient = httplib.HTTPConnection('172.20.7.29', 8012, timeout=10)
        httpClient.request('POST', '/SendIM.cgi', params, headers)
        response = httpClient.getresponse()
        print response.status
        print response.reason
        print response.read()
        print response.getheaders()
    except Exception, e:
        print e
    finally:
        if httpClient:
            httpClient.close()
    return msg