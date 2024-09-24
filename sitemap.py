#!/usr/bin/env python3

from datetime import datetime

xml_code = ('<?xml version="1.0" encoding="utf-8"?>\n'
    '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
)

try:
    xmlData = []
    xmlData.append(xml_code)
    # 你文章的timestamp 
    request_timestamp= 1727163250
    request_datetime  = datetime.utcfromtimestamp(request_timestamp).strftime('%Y-%m-%dT%H:%M:%S+08:00')
    
    # sitemap 指南
    # https://developers.google.com/search/docs/guides/create-URLs
    link = 'https://test.com.tw/abc/1234'

    row_data = '<url><loc>{}</loc><lastmod>{}</lastmod></url>'.format(link, request_datetime)
    xmlData.append(row_data)
    xmlData.append('</urlset>')
    
    content  = ''.join(xmlData)

    file = open('sitemap.xml', 'w', encoding='utf-8')
    file.write(content)
    file.close()

except RuntimeError as e:
    print(e)