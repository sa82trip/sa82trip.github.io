+++
title = "org_babel"
author = ["langEx"]
date = 2021-05-10T16:40:00+09:00
tags = ["emacs", "org"]
draft = false
+++

## org mode에서 여러 언어의 source code를 다룰 수 있다 {#org-mode에서-여러-언어의-source-code를-다룰-수-있다}

(이로 인해서 literate programming이 가능해진다)

-   clojure를 org파일에서 사용하려면 org-babel-clojure-backend를 'cider로 설정해준다
-   org에서 **_clojure_** 사용해보기
    1.  기본적인 연산
        ```clojure
               (+ 1 4)
        ```

        ```text
        5
        ```

    2.  Clojure vector
        ```clojure
             [1 2 3 4]
        ```

        <div class="no">

        [1 2 3 4]

        </div>

    3.  Clojure map
        ```clojure
               (def small-map {:a 2 :b 4 :c 8})
               (:b small-map)
        ```

        <div class="results">

        | #'user/small-map |
        |------------------|
        | 4                |

        </div>

-   typescript 사용해보기
    ```typescript
      const name_with_type:string = "powerful machine"

      console.log(name_with_type)
    ```

    ```text
        #+RESULTS:
          : powerful machine
    ```
-   python에서 사용해보기

    -   (header args에 :results output을 주어서 script모드로 해야 print 가능)

    <!--listend-->

    ```python
      name_in_python = "bold snake"
      print(name_in_python)
    ```

    ```text
        #+RESULTS:
          : bold snake
    ```


## 서로 다른 언어끼리 variable을 넘겨줄 수 있다. {#서로-다른-언어끼리-variable을-넘겨줄-수-있다-dot}


### <span class="org-todo done DONE">DONE</span> 이 부분 정리 {#이-부분-정리}

아직 정리 더 해야함


#### header argumnet로 전달하기 {#header-argumnet로-전달하기}

[참조 공식 사이트](https://orgmode.org/manual/Environment-of-a-Code-Block.html#Environment-of-a-Code-Block)

```text
:var NAME=ASSIGN
```

header가 있는 컬럼 1줄짜리 테이블을 선언

```text
#+name: less-cols
| a |
|---|
| b |
| c |
```

org에서 선언한 테이블이 html에선 이렇게 보인다

<a id="table--less-cols"></a>

| a |
|---|
| b |
| c |

python으로 테이블을 받아서 처리해보기

```text { linenos=true, linenostart=1 }
#+begin_src python :var tab=less-cols :colnames nil
return[[val + '*' for val in row] for row in tab]
#+end_src

#+RESULTS:
| a  |
|----|
| b* |
| c* |
```


#### source code의 결과를 내보내어 사용하기 {#source-code의-결과를-내보내어-사용하기}
