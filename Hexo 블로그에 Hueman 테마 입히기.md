---
title: Hexo 블로그에 Hueman 테마 입히기
date: 2023-11-14 22:08
authors: Hardy
categories: Blog
tags:
  - "#Hexo"
  - "#Blog"
  - "#Hueman"
---

## 1. 개요
---
이번 글에서는 Hexo 블로그에 `Hueman` 테마를 입히는 방법에 대해 알려드리겠습니다.
Hexo 블로그 테마로 `Icarus`나 `NexT` 등 인기 있는 테마가 있지만 사용해본 결과 `Hueman` 테마가 가장 맘에 들었습니다.
`Icarus`의 경우 `Next`나 `Hueman` 테마와 다른 방법을 사용하니 `Docs`를 보면서 진행하시면 됩니다.

## 2. Hueman 테마 입히기
---
먼저 블로그 폴더로 이동한 다음, 아래의 명령어를 입력합니다.

```
$ git clone https://github.com/ppoffice/hexo-theme-hueman.git themes/hueman
```

`git clone`으로 테마를 가져오는 것입니다.

그리고 아래의 명령어를 입력합니다.

```
$ npm install -S hexo-generator-json-content
```

Hexo 블로그에 `JSON` 형식의 콘텐츠를 생성하는 플러그인을 설치합니다.

그리고 `themes/hueman`에 들어가보면 `_config.yml.example` 파일이 있습니다.
이 파일을 바꿔줘야 합니다.

```
$ cp _config.yml.example _config.yml
```

`cp`는 copy를 의미하고 복사해서 `_config.yml` 파일을 만든다는 의미입니다.

그리고 복사한 파일이 아닌 Hexo에 있는 `_config.yml` 파일로 들어가서 테마를 `Hueman`으로 바꿔줍니다.

```
theme: hueman
```

그 다음 배포하면 됩니다.

```
$ hexo g
$ hexo d
```

![[231115-1.png]]

보다시피 완성된 것을 볼 수 있습니다.

## 3. 작가, 카테고리, 태그 생성
---
게시물에 들어갈 작가, 카테고리, 태그를 만들기 위해 `index.md` 파일을 생성해야 합니다.

작가 : `source/author/index.md`

```
---
title: Authors
layout: "authors"
---
```

카테고리 : `source/categories/index.md`

```
---
title: Categories
layout: "categories"
---
```

태그 : `source/tags/index.md`

```
---
title: Tags
layout: "tags"
---
```

## 4. 참고문헌
---
url : https://github.com/ppoffice/hexo-theme-hueman/wiki