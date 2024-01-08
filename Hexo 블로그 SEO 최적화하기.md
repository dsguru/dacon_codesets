---
title: Hexo 블로그 SEO 최적화하기
date: 2023-11-15 20:04
authors: Hardy
categories: Blog
tags:
  - "#Hexo"
  - "#SEO"
---

## 1. 개요
---
블로그를 운영하려면 SEO 최적화는 필수라고 할 수 있습니다.
최적화가 되면 구글에서 좀 더 상위 노출을 할 수 있기 때문입니다. 그래서 SEO 최적화 관련 강의를 하는 사람들도 볼 수 있습니다.
블로그를 어떤 이유로 운영하던 이왕 작성한 글이 구글에 노출되면 더욱 좋다고 생각됩니다.
그래서 이번 글에서는 SEO 최적화를 하는 방법과 구글 서치 콘솔과 구글 애널리틱스를 연결하는 방법에 대해 얘기해보겠습니다.

각각 진행한 후에 `hexo s` 명령어를 입력하여 확인한 후 배포하시기 바랍니다.



## 2. 특정 링크 제외
---
Hexo 블로그를 운영하면 의미없는 `URL`이 있기 마련입니다.
이런 `URL`은 SEO 최적화하기 위해서 제거해야 합니다.

```
$ npm install hexo-autonofollow --save
```

`npm`을 이용해 설치하며, `hexo-autonofollow`는 `nofollow` 속성을 자동으로 추가하거나 관리하는 기능을 제공합니다.

```
nofollow:  
      enable: true  
      exclude:
         - URL
```

따로 관리를 하기 위해서 테마 안에 있는 `_config.yml` 파일에 위의 내용을 넣으면 됩니다.



## 3. 대표 URL 설정
---
다음은 대표 URL을 넣어보도록 하겠습니다. 아래의 명령어를 입력합니다.

```
$ npm install --save hexo-auto-canonical
```

그 다음 테마 안에 있는 `layout/common/head.ejs` 에 들어가면 됩니다.
저는 `Hueman` 테마를 사용하며 다른 테마의 경우 경로가 다를 수 있습니다.
그리고 아래의 내용을 추가합니다. 파일 안에 `<%- meta(page) %>`가 있는데 그 밑에 넣으시면 됩니다.

```
<%- autoCanonical(config, page) %>
```



## 4. Sitemap 생성
---
이제 `Sitemap`을 생성하겠습니다. 아래의 명령어를 입력합니다.

```
$ npm install hexo-generator-seo-friendly-sitemap --save
```

`Sitemap`은 검색 엔진이 웹 사이트의 페이지를 효과적으로 색인화하고 검색 결과에 노출시킬 수 있도록 도움을 줍니다.

그 다음 Hexo에 있는 `_config.yml` 에서 아래의 내용을 넣어줍니다.

```
sitemap:
  path: sitemap.xml
```



## 5. Feed 생성
---
`Feed`는 블로그의 새로운 글이나 업데이트된 글에 대한 피드를 생성하는 데 사용합니다.
아래의 명령어를 입력합니다.

```
$ npm install hexo-generator-feed --save
```

그 다음 Hexo의 `_config.yml` 파일에서 아래의 내용을 넣습니다.

```
feed:
  type:
    - rss2
  path:
    - rss2.xml
  limit: 100
```

그리고 Hexo 폴더의 `_config.yml`에 들어가 아래의 내용을 넣어줍니다.

```
rss: /rss2.xml
```



## 6. robots.txt 생성
---
`robots.txt`는 웹 크롤러에게 웹 사이트의 적절한 동작 방식을 알려주기 위한 것입니다.
다시 말해 검색 엔진 로봇이 특정 페이지를 크롤링하거나 색인화하지 않아야 할 경우를 정의합니다.
아래의 명령어를 입력합니다.

```
$ npm install hexo-generator-robotstxt --save
```

그리고 `_config.yml`에 아래의 내용을 넣어줍니다.

```
robotstxt:
  useragent: "*"
  allow:
    - /
  sitemap: /sitemap.xml
```



## 7. 참고문헌
---
url : https://msj0319.github.io/2020/02/14/Hexo-Blog-%EA%B5%AC%EA%B8%80-%EC%82%AC%EC%9D%B4%ED%8A%B8-%EB%93%B1%EB%A1%9D-%EB%B0%8F-%EA%B2%80%EC%83%89%EC%97%94%EC%A7%84-%EC%B5%9C%EC%A0%81%ED%99%94-SEO/

url : https://futurecreator.github.io/2016/06/23/search-engine-optimization-hexo-plugins/