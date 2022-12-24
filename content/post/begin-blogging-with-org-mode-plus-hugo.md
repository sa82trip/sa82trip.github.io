+++
title = "begin blogging with org mode + hugo"
author = ["langEx"]
date = 2021-05-07T16:53:00+09:00
tags = ["blogging", "hugo"]
draft = false
+++

## instruction from official document {#instruction-from-official-document}

1.  Install Hugo
    ```sh
          brew install hugo
          # or
          port install hugo
    ```

    -   brew로 설치했음
    -   설치결과 확인
        ```sh
                  hugo version
        ```

        ```text
        hugo v0.108.0+extended darwin/arm64 BuildDate=unknown
        ```

2.  새로운 사이트 만들기
    ```sh
          hugo new site myblog

          # result
          ❯ tree
          .
          ├── archetypes
          │   └── default.md
          ├── config.toml
          ├── content
          ├── data
          ├── layouts
          ├── static
          └── themes
    ```
3.  테마를 추가하기
    See [themes.gohugo.io](http://themes.gohugo.io) for a list of themes to consider. This quickstart uses the beautiful Ananke theme.
    먼저 테마를 github에서 다운 받고 themes 디렉토리에 추가합니다.
    git submodule을 이용해서 테마의 git repo주소를 연결하고 theme/ananke 디렉토리에 추가합니다.
    그리고 config.toml파일에 테마를 설정합니다.
    ```sh
          echo 'theme = "ananke"' >> config.toml
    ```
    추가한 결과
    ```toml { linenos=true, linenostart=1, hl_lines=["4"] }
              baseURL = "http://example.org/"
              languageCode = "en-us"
              title = "My New Hugo Site"
              theme = "ananke"
    ```
4.  실제로 post 작성해보기
    실제로 수동으로 post용 파일을 만들 수도 있지만 hugo명령어로 하는게 편하고 기본 template도 제공됩니다.
    ```sh
          hugo new posts/my-first-post.md

          #result
          ❯ tree -CdL 2
          .
          ├── archetypes
          ├── content
          │   └── post
          ├── data
          ├── layouts
          ├── resources
          │   └── _gen
          ├── static
          └── themes
          └── ananke

          10 directories
    ```
    tree -L option 줄 때 띄어쓰고 숫자 적어주면 되는데.......
    하여간 만들어진 파일을 열어보면 이렇게 기본적으로 생성된 날짜와 draft인지 아닌지를 구별 해주는 템플릿과 함께 만들어져있습니다.
    ```md
              ---
              title: "My First Post"
              date: 2021-05-07T10:21:00+09:00
              draft: true
              ---
    ```
    draft가 true이면 이 문서는  배포되지 않습니다.

    > Drafts do not get deployed; once you finish a post, update the header of the post to say draft: false. More info [here](https://gohugo.io/getting-started/usage/#draft-future-and-expired-content).
5.  hugo server 시작하기 (local)
    ```sh
          ❯ hugo server -D
          Start building sites …

          | EN
          -------------------+-----
          Pages            | 10
          Paginator pages  |  0
          Non-page files   |  0
          Static files     |  1
          Processed images |  0
          Aliases          |  1
          Sitemaps         |  1
          Cleaned          |  0

          Built in 21 ms
          Watching for changes in /Users/joongil/org-roam/myblog/{archetypes,content,data,layouts,static,themes}
          Watching for config changes in /Users/joongil/org-roam/myblog/config.toml, /Users/joongil/org-roam/myblog/themes/ananke/config.yaml
          Environment: "development"
          Serving pages from memory
          Running in Fast Render Mode. For full rebuilds on change: hugo server --disableFastRender
          Web Server is available at http://localhost:1313/ (bind address 127.0.0.1)
          Press Ctrl+C to stop
    ```
    이제 브라우져를 켜고 <http://localhost:1313에> 들어가면 우리가 만든 블로그가!
    md파일을 수정하고 브라우져를 새로 고치면 바로 적용이 되는걸 알 수 있습니다.
6.  테마를 수정하기(커스터마이징하기)
    config.toml파일 수정하기
    ```toml { linenos=true, linenostart=1, hl_lines=["1"," 4"] }
              baseURL = "http://example.org/" # 도메인이 있다면 여기서 설정
              languageCode = "en-us"
              title = "My New Hugo Site" # 타이틀도 바꿀 수 있습니다.
              theme = "ananke"
    ```

    > Tip: Make the changes to the site configuration or any other file in your site while the Hugo server is running, and you will see the changes in the browser right away, though you may need to clear your cache.

    For theme specific configuration options, see [the theme site](https://github.com/theNewDynamic/gohugo-theme-ananke).
    For further theme customization, see [Customize a Theme](https://gohugo.io/themes/customizing/).
7.  static 페이지들을 빌드하기
    ```shell
          hugo -D
    ```
    output은 ./public에 저장됩니다. (기본값으로)
    (-d/ --destination) flag를 이용하면 저장 디렉터리를 바꿀 수 있습니다.
    publishdir을 config파일에서 설정해도 바꿀 수 있습니다.
8.  netlify에 디플로이
9.  disqus로 comment기능 넣기.
    이때 shortname이라는건 내가 만든 사이트의 \_짧은 이름_을 이야기 하는 거였다.

10. 추가 된 내용 <span class="timestamp-wrapper"><span class="timestamp">&lt;2022-08-10 Wed&gt;</span></span>


## 추가 된 내용 <span class="timestamp-wrapper"><span class="timestamp">[2022-08-10 Wed]</span></span> {#추가-된-내용}


### 1. github에 빌드된 내용으로 바로 올려서 github가 deploy 해주는 것도 가능하다. {#1-dot-github에-빌드된-내용으로-바로-올려서-github가-deploy-해주는-것도-가능하다-dot}

1.  github에 블로그용 리포를 하나 만들고 거기에 로컬에서 빌드된 결과를 푸시한다.
2.  그러면 바로 github가 디플로이를 시작한다.
3.  그리고 확인!
