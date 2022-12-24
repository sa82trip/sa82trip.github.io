+++
title = "What I learned while bloggin with hugo with org"
author = ["langEx"]
date = 2021-05-07T23:30:00+09:00
tags = ["hugo", "blogging", "knowhow"]
draft = false
+++

블로그를 쓰면서 알게 된 것들 이것저것

<!--more-->


## <span class="underline">_This post not will be sorted or indexed by any order._</span> {#9560de}


## Variable {#variable}

[Variables](https://gohugo.io/variables/) : static site에서 많은 variables을 사용할 수 있다.

사용 가능한 variables 리스트 (공식 홈페이지에 자세한 설명 있음)

<style>
.zebra-striping tbody tr:nth-child(odd) {
background: #aaaa;
  }
.zebra-striping th {
  border-bottom: solid;
  background: purple;
}
</style>

<div class="ox-hugo-table zebra-striping sane-table">

| name                  | namae                   |
|-----------------------|-------------------------|
| Site Variables        | Shortcode Variables     |
| Page Variables        | Pages Methods           |
| Taxonomy Variables    | File Variables          |
| Menu Entry Properties | Hugo-specific Variables |
| Git Info Variables    | Sitemap Variables       |

</div>


## table customize 하기 {#table-customize-하기}

1.  config파일에 마크다운관련 설정을 넣어준다
    ```toml { linenos=true, linenostart=1, hl_lines=["6-8"] }
       [markup]
           [markup.tableOfContents]
               endLevel = 3
               ordered = false
               startLevel = 1
           [markup.goldmark]
               [markup.goldmark.renderer]
               unsafe= true
    ```
2.  org file에서 css를 만들고 그 css를 내가 만든 테이블에 적용한다.
    ```text
       #+begin_export html
       <style>
       .zebra-striping tbody tr:nth-child(odd) {
       background: #eee;
       }
       .zebra-striping th {
       border-bottom: solid;
       }
       </style>
       #+end_export

       #+attr_html: :class zebra-striping sane-table
       | name                  | namae                   |
       |-----------------------+-------------------------|
       | Site Variables        | Shortcode Variables     |
       | Page Variables        | Pages Methods           |
       | Taxonomy Variables    | File Variables          |
       | Menu Entry Properties | Hugo-specific Variables |
       | Git Info Variables    | Sitemap Variables       |
    ```
3.  customized vs normal table
    -   **customized**

        <div class="ox-hugo-table zebra-striping sane-table">

        | name                  | namae                   |
        |-----------------------|-------------------------|
        | Site Variables        | Shortcode Variables     |
        | Page Variables        | Pages Methods           |
        | Taxonomy Variables    | File Variables          |
        | Menu Entry Properties | Hugo-specific Variables |
        | Git Info Variables    | Sitemap Variables       |

        </div>

    -   **normal**

        | name                  | namae                   |
        |-----------------------|-------------------------|
        | Site Variables        | Shortcode Variables     |
        | Page Variables        | Pages Methods           |
        | Taxonomy Variables    | File Variables          |
        | Menu Entry Properties | Hugo-specific Variables |
        | Git Info Variables    | Sitemap Variables       |


## summary를 내가 원하는대로 정하기 {#summary를-내가-원하는대로-정하기}

원하는 위치에 아래의 코드를 넣어준다

```text
#+hugo: more
```


## git submodule에 대해서 {#git-submodule에-대해서}

submodule을 등록했다면, 그리고 submodule에 변화가 필요한 상황이라면 그리고 부모 모듈에도 변화가 필요한 상황이라면 처음 커밋 푸쉬되야 되는 대상은 submodule이다. 왜냐하면 그 값을 부모가 참조하면서 커밋이 되어야 하니깐.
