## SEO Optimization nginx 301 設定方式

### 如果同一個內容有很多網址產生，需要確認最後網址為何，單指設定 canonical 是不夠的，需要告知google正確訊號，不然爬蟲會針對它覺得網頁流量好的去索引，跳轉過程爬蟲只看最後一頁的狀態，第一頁要跳轉到後面都是設定301
#### 例如
#### test.com.tw/abc/24123
#### test.com.tw/news/abc/24123
#### 都是指的是相同網頁內容的話
#### canonical 設定標準網址是 test.com.tw/news/abc/24123
#### test.com.tw/abc/24123 就必須用 301 指向 test.com.tw/news/abc/24123

### 使用 http 入站的話，判斷讓他跳轉至 https，指定 301跳轉
```
if ($http_x_forwarded_proto = "http") {
    return 301 https://$host$request_uri;
}
```
### 如果有重複網頁的部分要透過網址或是ip跳轉的話可以修改下方方式
### 你最後的網址，例如 ： https://www.google.com.tw/$request_uri
### $request_uri 是入站帶進來的參數，如只要去首頁就可以刪掉
```
server {
    # 監聽port
    listen 443 ssl http2;

    ssl_certificate     xxx.pem;
    ssl_certificate_key xxx.key;

	server_name 你的網址
                你的IP;

	return 301 你最後的網址$request_uri;
}
```
### robots.txt，設定方式 
#### User-agent: *       ： 都可以爬
#### Disallow: /preview/ ： /preview/ ，不可以爬有帶有/preview的內容
#### Crawl-Delay: 10     ： 延遲時間，google表示他不吃這參數
#### Sitemap             ： 全站sitemap，這個建立有助於你網頁的索引
```
User-agent: *

Disallow: /preview/

Crawl-Delay: 10

Sitemap: 網址/sitemap.xml
Sitemap: 網址/google-news.xml

```


### sitemap 設定方式

#### XML Sitemap
#### loc     ： 你的網頁
#### lastmod ： YYYY-mm-ddTmm:hh:ssZ
#### 建議利用 python 在背景處理玩出，做成靜態檔案，可參考 sitemap.py ，資料庫連線方式可再去找適合你的方式

<https://developers.google.com/search/docs/guides/create-URLs>
```
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>你的網頁</loc>
    <lastmod>2024-09-24T08:50:58Z</lastmod>
  </url>
  <url>
    <loc>你的網頁</loc>
    <lastmod>2024-09-24T08:50:58Z</lastmod>
  </url>
  <url>
    <loc>你的網頁</loc>
    <lastmod>2024-09-24T08:50:58Z</lastmod>
  </url>
</urlset>
```

