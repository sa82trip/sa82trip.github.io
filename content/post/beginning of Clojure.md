+++
title = "beginning of Clojure"
author = ["langEx"]
date = 2021-05-10T10:37:00+09:00
draft = false
+++

## Clojure란? {#clojure란}

Rich Hickey가 만든 Lisp의 방언격의 함수형 프로그래밍 언어.

<!--more-->

나중에 햇갈리지 않기 위해 기억할 것은 Clojure라 하면 언어 그 자체와 compiler(clojure.jar)를 말한다는 것.
Clojure는 hosted language이다.(JVM의 실행되는 것도, Clojure의 핵심 기능도(threding, GC))


### 기억해야하는 컨셉 {#기억해야하는-컨셉}

-   자바프로그램인 clojure.jar 가 clojure 소스를 읽고 Java bytecode로 만든다.
-   만들어진 Java bytecode는 clojure.jar가 돌아가고 있는 JVM process에서 돌아가게 된다.


## Clojure 시작하기 {#clojure-시작하기}

주로 사용되고 있는 [Leiningen](http://leiningen.org/)을 사용하여 프로젝트를 만들수도 있고 빌드를 할 수도 있다.

> Leiningen and Clojure require Java. OpenJDK version 8 is recommended at this time.
> _from Leiningen official website_


### macOS에선 Homebrew로 간단히 설치가능 {#macos에선-homebrew로-간단히-설치가능}

```sh
brew install leiningen
```


### 설치결과 확인 {#설치결과-확인}

```sh
lein -version
```

```text
Leiningen 2.9.4 on Java 11.0.7 OpenJDK 64-Bit Server VM
```


### 새로운 Clojure Project만들어 보기 {#새로운-clojure-project만들어-보기}

<a id="code-snippet--create-new-project"></a>
```sh
lein new app first-clojure-app
```

```text
❯ tree
.
├── CHANGELOG.md
├── LICENSE
├── README.md
├── doc
│   └── intro.md
├── project.clj
├── resources
├── src
│   └── first_clojure_app
│       └── core.clj
└── test
    └── first_clojure_app
        └── core_test.clj

6 directories, 7 files
```

-   project.clj : 프로젝트에 대한 설정을 가지고 있는 파일. 무슨 dependency들을 가지고 있는지, 언제 실행 되어야 하는지, 어떤 함수가 가장 먼저 실행되는지 등의 정보를 가지고 있음
-   core.clj : clojure 코드를 적을 곳


### 실제로 실행해보기 with core.clj {#실제로-실행해보기-with-core-dot-clj}

<a id="code-snippet--core-file"></a>
```clojure { linenos=true, linenostart=1 }
;;/first-clojure-app/src/first_clojure_app:
(ns first-clojure-app.core
  (:gen-class))

(defn -main
  "I don't do a whole lot ... yet."
  [& args]
  (println "Hello, Clojure!!!"))
```

-   2번 라인에서 name space를 명명하는데, 메모리에 올라가있는 단위라고 생각하지만 좀 더 공부를 해봐야 제대로 알듯하다.
-   실행해보려면 커맨드라인에서 입력
    ```sh
      lein run
    ```

    ```text
      Hello, Clojure!!
    ```
-   -main 함수가 실행 된 것


### build 해보기 {#build-해보기}

-   commandline에서 명령어 실행
    <a id="code-snippet--build-project"></a>
    ```sh
       lein uberjar
    ```

    ```text
       //결과
       Compiling first-clojure-app.core
       Created /Users/xxx/org/first-clojure-app/target/uberjar/first-clojure-app-0.1.0-SNAPSHOT.jar
       Created /Users/xxx/org/first-clojure-app/target/uberjar/first-clojure-app-0.1.0-SNAPSHOT-standalone.jar
    ```

-   java로 실행해보기
    <a id="code-snippet--excute-jar"></a>
    ```sh
       java -jar first-clojure-app/target/uberjar/first-clojure-app-0.1.0-SNAPSHOT-standalone.jar
    ```

    ```text
       Hello  Clojure!!
    ```


### 짧게 정리 {#짧게-정리}

```sh
#create project
lein new app first-clojure-app

#created core file
;;/first-clojure-app/src/first_clojure_app:
(ns first-clojure-app.core
  (:gen-class))

(defn -main
  "I don't do a whole lot ... yet."
  [& args]
  (println "Hello, Clojure!!!"))

#build project
   lein uberjar

#excute_jar
   java -jar first-clojure-app/target/uberjar/first-clojure-app-0.1.0-SNAPSHOT-standalone.jar
```


### 마무리 {#마무리}

다음 포스팅은 REPL을 이용하는 Clojure 코딩에 대하여.
