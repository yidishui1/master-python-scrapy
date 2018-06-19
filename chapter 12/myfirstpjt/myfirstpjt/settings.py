# -*- coding: utf-8 -*-

# Scrapy settings for myfirstpjt project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'myfirstpjt'

SPIDER_MODULES = ['myfirstpjt.spiders']
NEWSPIDER_MODULE = 'myfirstpjt.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'myfirstpjt (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

#(2)
#IP池设置
'''如果要设置IP代理此请开启
IPPOOL=[
    {"ipaddr": "60.13.187.162:63000"},
    {"ipaddr": "222.185.137.182:6666"},
    {"ipaddr": "58.247.135.174:63000"},
    {"ipaddr": "221.5.54.6:808"},
    {"ipaddr": "122.114.31.177:808"},
    {"ipaddr": "61.135.217.7:80"},
    {"ipaddr": "59.56.252.38:63000"},
    {"ipaddr": "220.191.103.223:6666"},
    {"ipaddr": "113.200.241.202:63000"},
    {"ipaddr": "171.221.202.181:63000"},
    {"ipaddr": "14.118.255.222:6666"},
    {"ipaddr": "14.118.255.138:6666"},
    {"ipaddr": "121.231.155.219:6666"},
    {"ipaddr": "117.86.12.69:18118"},
    {"ipaddr": "117.63.78.4:6666"},
    {"ipaddr": "125.120.203.129:6666"},
    {"ipaddr": "223.145.228.166:6666"},
    {"ipaddr": "110.73.9.160:8123"},
    {"ipaddr": "222.42.136.15:63000"},
    {"ipaddr": "183.167.217.152:63000"},
]
'''
'''如果要设置用户代理池请开启'''
#(5)
#用户代理（user-agent）池设置
UAPOOL=[
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.22 Safari/537.36 SE 2.X MetaSr 1.0",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:48.0) Gecko/20100101 Firefox/48.0",
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.5"
]

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'myfirstpjt.middlewares.MyCustomSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
'''如果要设置IP代理池请开启
DOWNLOADER_MIDDLEWARES = {
    #'myfirstpjt.middlewares.MyCustomDownloaderMiddleware': 543,
    'scrapy.contrib.downloadermiddleware.httpproxy.HttpProxyMiddleware':123,
    'myfirstpjt.middlewares.IPPOOLS':125
}
'''
'''如果要设置用户代理池请开启'''
DOWNLOADER_MIDDLEWARES = {
    #'myfirstpjt.middlewares.MyCustomDownloaderMiddleware': 543,
    'scrapy.contrib.downloadermiddleware.useragent.UserAgentMiddleware':2,
    'myfirstpjt.uamid.Uamid':1
}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'myfirstpjt.pipelines.SomePipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
