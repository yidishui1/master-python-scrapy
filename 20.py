#��20��ģ���¼������Ŀ
#20.3 ģ���¼������Ŀ��дʵս
#(1)
# -*- coding: utf-8 -*-
import scrapy
import urllib.request
from scrapy.http import Request,FormRequest


class LoginspdSpider(scrapy.Spider):
    name = "loginspd"
    allowed_domains = ["douban.com"]
    #����ͷ��Ϣ������������Ĵ�����ģ����������ȡ
    header = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0"}
    #��дstart_requests()��������һ�λ�Ĭ�ϵ�ȡ�÷����е�����
    def start_requests(self):
        #������һ�ε�¼ҳ��Ȼ�����ص�����parse()
        return [Request("https://accounts.douban.com/login", meta={"cookiejar": 1}, callback=self.parse)]

    def parse(self, response):
        #��ȡ��֤��ͼƬ���ڵ�ַ����ȡ�󸳸�captcha��������ʱcaptchaΪһ���б�
        captcha=response.xpath('//img[@id="captcha_image"]/@src').extract()
        #��Ϊ��¼ʱ��ʱ��ҳ����֤�룬��ʱ��ҳû����֤��
        # ������Ҫ�жϴ�ʱ�Ƿ���Ҫ������֤�룬��captcha�б�����Ԫ�أ�˵������֤����Ϣ
        if len(captcha)>0:
            print("��ʱ����֤��")
            #���ý���֤��ͼƬ�洢�����صı��ص�ַ
            localpath="D:/Python35/myweb/part20/loginpjt/captcha.png"
            #���������е���֤��ͼƬ�洢�����أ��������ڱ���ֱ�ӽ��в鿴
            urllib.request.urlretrieve(captcha[0], filename=localpath)
            print("��鿴����ͼƬcaptcha.png�������Ӧ��֤�룺")
            #ͨ��input()�ȴ����������Ӧ����֤�벢����captcha_value����
            captcha_value=input()
            #����Ҫ���ݵ�post��Ϣ
            data={
                #���õ�¼�˺ţ���ʽΪ�˺��ֶ���:�����˺�
                "form_email":"weisuen007@163.com",
                #���õ�¼���룬��ʽΪ�����ֶ���:�������룬������Ҫ���˺����뻻���Լ���
                #��Ϊ������ɸ���Ŀ���Ѿ��޸�����
                "form_password":"weijc7789",
                #������֤�룬��ʽΪ��֤���ֶ���:������֤��
                "captcha-solution":captcha_value,
                #������Ҫת�����ַ������������Ҫ��ȡ��������ҳ������ת���������ҳ
                "redir":"https://www.douban.com/people/151968962/",
            }
        #����˵��captcha�б���û��Ԫ�أ�����ʱ����Ҫ������֤����Ϣ
        else:
            print("��ʱû����֤��")
            #����Ҫ���ݵ�post��Ϣ����ʱû����֤���ֶ�
            data={
                "form_email":"weisuen007@163.com",
                "form_password":"weijc7789",
                "redir": "https://www.douban.com/people/151968962/",
            }
        print("��¼�С�")
        #ͨ��FormRequest.from_response()���е�¼
        return [FormRequest.from_response(response,
                                          #����cookie��Ϣ
                                          meta={"cookiejar": response.meta["cookiejar"]},
                                          #����headers��Ϣģ��������
                                          headers=self.header,
                                          #����post���е�����
                                          formdata=data,
                                          #���ûص���������ʱ�ص�����Ϊnext()
                                          callback=self.next,
                                          )]
    def next(self,response):
        print("��ʱ�Ѿ���¼��ɲ���ȡ�˸������ĵ�����")
        #��ʱresponseΪ����������ҳ�е�����
        #����ͨ��Xpath���ʽ�ֱ���ȡ���������и��û��������Ϣ
        #��ҳ����Xpath���ʽ
        xtitle="/html/head/title/text()"
        #�ռǱ���Xpath���ʽ
        xnotetitle="//div[@class='note-header pl2']/a/@title"
        #�ռǷ���ʱ��Xpath���ʽ
        xnotetime="//div[@class='note-header pl2']//span[@class='pl']/text()"
        #�ռ�����Xpath���ʽ
        xnotecontent="//div[@class='mbtr2']/div[@class='note']/text()"
        #�ռ�����Xpath���ʽ
        xnoteurl="//div[@class='note-header pl2']/a/@href"

        #�ֱ���ȡ��ҳ���⡢�ռǱ��⡢�ռǷ���ʱ�䡢�ռ����ݡ��ռ�����
        title=response.xpath(xtitle).extract()
        notetitle = response.xpath(xnotetitle).extract()
        notetime = response.xpath(xnotetime).extract()
        notecontent = response.xpath(xnotecontent).extract()
        noteurl = response.xpath(xnoteurl).extract()
        print("��ҳ�����ǣ�"+title[0])
        #�����ж�ƪ�ռǣ�ͨ��forѭ�����α���
        for i in range(0,len(notetitle)):
            print("��"+str(i+1)+"ƪ���µ���Ϣ����:")
            print("���±���Ϊ��"+notetitle[i])
            print("���·���ʱ��Ϊ��" + notetime[i])
            print("��������Ϊ��" + notecontent[i])
            print("��������Ϊ��" + noteurl[i])




            
            print("------------")
