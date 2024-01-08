---
title: Hexo 블로그 만드는 방법
date: 2023-11-14 21:25
authors: Hardy
categories: Blog
tags:
  - "#Hexo"
  - "#Blog"
toc: "true"
---

## 1. 개요
---
Github를 이용하여 Github pages를 만들어 블로그로 사용할 수 있습니다.
일반적으로 Jekyll 블로그와, Hexo 블로그, Hugo 블로그를 만들어서 사용하는데요.
예전에 Jekyll 블로그를 만들어서 사용하였으나 페이지 로딩 시간 등 단점을 듣고 Hexo 블로그를 만들기로 했습니다. 그럼 Hexo 블로그를 만드는 방법을 알아보겠습니다.



## 2. 필수 설치 및 가입
---
먼저 블로그를 만들기 위해 필요한 정보를 알아보겠습니다.

첫 번째는 당연히 Github에 가입을 해야합니다.
가입하는 방법은 어렵지 않으니 따로 설명하지 않겠습니다.
링크 : https://github.com/

두 번째는 node.js를 설치해야 합니다.
링크를 따라 설치하는 방법이 있고 `nvm`을 이용해 설치하는 방법이 있습니다.
이왕이면 LTS가 적혀있는 버전을 설치하시길 바랍니다.
링크 : https://nodejs.org/en

세  번째는 Git을 설치해야 합니다.
링크 : https://git-scm.com/

마지막으로 Hexo를 설치하면 됩니다.

```
$ npm install -g hexo-cli
```

정적 웹사이트 생성기를 설치하기 위한 명령어입니다.
다만, `npm`의 경우 `Node Package Manager`의 약자로 `Node.js`를 설치해야만 사용하실 수 있습니다.



## 3. 블로그 생성
---
버전용, 배포용 등 관리하는 것은 따로 다루지 않겠습니다.

먼저 터미널에서 원하는 위치에 아래의 명령어를 작성하시면 됩니다.

```
$ mkdir 폴더명
$ cd 폴더
```

`mkdir`은 `directory`를 생성한다는 의미고, `cd`는 `change directory`를 의미합니다. 폴더에 들어간다고 보시면 됩니다.

그 다음 아래의 명령어를 작성합니다.

```
$ hexo init blog
$ cd blog
```

`hexo init blog`는 블로그를 새로 생성하기 위해 초기화하는 것입니다. `blog`는 원하는 이름으로 작성하시면 됩니다.

```
$ npm install
$ npm install hexo-server --save
$ npm install hexo-deployer-git --save
```

`npm install` 명령어로 블로그에 필요한 node.js 패키지를 설치합니다.
그 다음, `npm install hexo-server --save` 명령어로 Hexo 로컬 서버를 실행시키기 위한 패키지인 `hexo-server`를 설치합니다.
마지막으로 `npm install hexo-deployer-git --save` 명령어로 Hexo로 생성한 정적 웹사이트를 배포하기 위한 Git 배포 플러그인을 설치합니다.



## 4. 블로그 정보 넣기
---
위의 내용을 전부 하셨다면 폴더에 Hexo 블로그 관련 파일들이 설치되었습니다.
그 중 `_config.yml` 파일이 기본적인 블로그 정보를 설정할 수 있습니다. 이 파일에 들어갑니다.

`_config.yml` 파일을 열어보면 아래의 내용이 있습니다. 제가 실제로 입력한 내용입니다.

```
title: DS Guru
description: 'Data Scientist'
author: Hardy
language: en
```

그 외 `subtitle` 등 필요하시면 넣어주시면 됩니다.

다음으로 `url`을 넣어주겠습니다.

```
url: https://dsguru.github.io/
```

마지막으로 배포에 관한 내용을 입력해주겠습니다.

```
deploy:
  type: git
  repo: https://github.com/dsguru/dsguru.github.io
  branch: main
```

제가 위에 넣지 않은 내용인데 본인 계정에서 `유저이름.github.io` 이름이 된  `repository`를 생성해야 합니다.
그 다음 위의 내용을 넣으면 됩니다.

## 5. 배포
---
```
hexo generate
hexo deploy
```

`hexo generate` 명령어는 정적 페이지를 생성하는 명령어입니다. `hexo g` 명령어도 같은 의미입니다.
그 다음, `hexo deploy` 명령어로 배포하면 됩니다. `hexo d` 로 작성하셔도 됩니다.

하지만, 배포하기 전에 확인하고 싶은 마음이 들 수 있습니다.

```
hexo server
```

`hexo server` 또는 `hexo s` 명령어를 입력하여 로컬 서버를 연 다음 확인한 후에 배포하셔도 됩니다.

![[231114-1.png]]

배포한 뒤에 본인의 블로그 `url`에 들어가보면 생성되어있는 것을 볼 수 있습니다.
시간은 3~5분 정도 걸리니 기다리시면 됩니다.



## 6. 참고문헌
---
아래의 블로그에서 참고하였습니다.
url: https://dschloe.github.io/settings/hexo_blog/

다음 글에서는 인기 있는 테마 중 하나인 `Hueman` 테마를 입히는 방법에 대해 작성하겠습니다.