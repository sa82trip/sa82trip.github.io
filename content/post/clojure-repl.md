+++
title = "clojure-repl"
author = ["langEx"]
date = 2021-05-10T20:08:00+09:00
draft = false
+++

## how to use repl {#how-to-use-repl}


### lein을 이용하는 방법 {#lein을-이용하는-방법}

repl을 이용하는 방법은 간단하다. 프로젝트의 core.clj파일이 있는 디렉토리로 이동하여 commandLine에 lein repl 이라고 입력하면 된다.

```sh
lein repl
```

```sh
❯ lein repl
nREPL server started on port 62671 on host 127.0.0.1 - nrepl://127.0.0.1:62671
REPL-y 0.4.4, nREPL 0.7.0
Clojure 1.10.1
OpenJDK 64-Bit Server VM 11.0.7+10
    Docs: (doc function-name-here)
          (find-doc "part-of-name-here")
  Source: (source function-name-here)
 Javadoc: (javadoc java-object-or-class-here)
    Exit: Control+D or (exit) or (quit)
 Results: Stored in vars *1, *2, *3, an exception in *e

first-clojure-app.core=>
```

-   아래와 같이 나오면 성공이다.

    first-clojure-app.core=&gt;


### cider를 이용하는 방법 {#cider를-이용하는-방법}

cider는 emacs에서 clojure interactive programming을 할 수 있게 도와주는 개발환경이다.
emacs에서 core.clj파일을 열고 M-x clojure/open repl을 선택하면 된다
repl이 연결되면 현재의 버퍼밑에 미니 버퍼에 repl이 활성화 된다

```sh
nREPL server started on port 61488 on host localhost - nrepl://localhost:61488
;; Connected to nREPL server - nrepl://localhost:61488
;; CIDER 1.1.0snapshot, nREPL 0.8.3
;; Clojure 1.10.1, Java 11.0.7
;;     Docs: (doc function-name)
;;           (find-doc part-of-name)
;;   Source: (source function-name)
;;  Javadoc: (javadoc java-object-or-class)
;;     Exit: <C-c C-q>
;;  Results: Stored in vars *1, *2, *3, an exception in *e;
;;  Startup: /usr/local/bin/lein update-in :dependencies conj \[nrepl/nrepl\ \"0.8.3\"\] -- update-in :plugins conj \[refactor-nrepl/refactor-nrepl\ \"2.5.1\"\] -- update-in :plugins conj \[cider/cider-nrepl\ \"0.25.9\"\] -- repl :headless :host localhost
```

cider에서 repl을 활성화 하니 자동완성이나 괄호를 맞춰주는 기능등이 바로 작동해서 이 방식으로 repl을 이용하는 편이 더 좋을 것 같다.(doom emacs라서 세팅이 많은 부분 미리 되어있음)
