+++
title = "clojure_programming"
author = ["langEx"]
date = 2021-05-12T10:50:00+09:00
tags = ["clojure", "syntax"]
draft = false
+++

001


## doom emacs clojure mode에서 structure safe하게 coding하기 {#doom-emacs-clojure-mode에서-structure-safe하게-coding하기}

[cleverparens](https://github.com/luxbock/evil-cleverparens)라는 package를 이용하면 된다.

```text
;; in ~/.doom.d/packages.el
(package! evil-cleverparens)

;; in ~/.doom.d/config.el
(add-hook 'lisp-mode-hook #'evil-cleverparens-mode)
```

[위의 코드 출처](https://github.com/hlissner/doom-emacs/issues/3743)


## 실제 코딩 시작 {#실제-코딩-시작}


### Syntax(문법) {#syntax--문법}


#### Forms {#forms}

모든 Clojure code는 Uniform structure로 적혀있다. Clojure는 두 종류를 인식한다

-   Literal representations of data structures (numbers, strings, maps, and vectors)
-   Operations

> We use the term form to refer to valid code. I’ll also sometimes use expression to refer to Clojure forms. But don’t get too hung up on the terminology. Clojure evaluates every form to produce a value. These literal representations are all valid forms

Clojure에서 form을 유요한 코드를 언급하기 위해 쓰고 또 어쩔때는 expression이라고 이야기 하기도 한다. 여기에 너무 매달릴 필요는 없다.

```clojure
"a string"
["a" "vector" "of" "strings"]
(+ 1 2 3)
(str "It was the panda" " in the library" " with a dust")
```

free-floating literals를 code안에서 가질일은 거의 없다.
form은 여는 괄호 연산자 피연산자 닫는 괄호로 이루어진다
comma(쉼표)는 안쓰고 스페이스가 대신한다. 쉼표를 써도 되긴 하지만 컨벤션은 아니다


#### 분기처리 {#분기처리}

if, do, and when

**if** form의 기본 형태

```text
(if boolean-form
    then-form
    optional-else-form)
```

if의 분기처리

```clojure
(if true
  "By Zues's hammer!"
  "By Aquaman's trident!")
```

```text
#+RESULTS:
: By Zues's hammer!
```

---

```clojure
(if false
  "By Zues's hammer!"
  "By Aquaman's trident!")
```

```text
#+RESULTS:
: By Aquaman's trident!
```

\## else 를 omit할 수 있다.

```clojure
(if false "By Odin's Elbow!")
```

```text
#+RESULTS:
;; => nil
```

\## then, else문은 오직 하나의 form만 갖는다는게 다른 언어들과 다른점

-   이걸 우회하기 위해서 _**do**_ 연산자를 이용한다.
    ```clojure
      (if true
          (do (println "Success!")
              "By Zeus's hammer!")
          (do (println "Failure!")
              "By Aquaman's trident!")
          )
    ```

    ```text
        #+RESULTS:
          : Success!
          : "By Zeus's hammer!"
    ```

when은 else를 가지고 있지 않은 if and do를 합친것과 비슷하다.

```clojure
  (when true
  (println "Success!")
  "abra cadabra!")
```

```text
#+RESULTS:
: Success!
: "abra cadabra!"
```

when은 여러가지 form을 수행하고 싶거나 false일 때 nil을 반환하고 싶을 때 사용하면 된다


## nil, true, false, truthiness, equlity, boolean {#nil-true-false-truthiness-equlity-boolean}


### nil true false {#nil-true-false}

| TYPE            | MEANING |
|-----------------|---------|
| false           | false   |
| nil             | false   |
| everything else | true    |

```clojure
(if "bears eat beets"
  "bears beets Battlestar Galactica")
```

```text
#+RESULTS:
: "bears beets Battlestar Galactica"
```

**string** 은 truethy로 여겨진다

---

```clojure
(if nil
  "This won't be the result because nil is falsey"
  "nil is falsey")
```

```text
#+RESULTS:
:  is falsey
```

**nil** 은 falsey로 여겨진다


### equality {#equality}

clojure에선 "="을 "같다"의 의미의 연산자로 사용한다.
딱 이 하나의 연산자만 사용하기 때문에 햇갈릴 일이 없다.

```clojure
(= 1 1)
(= nil nil)
(= 1 2)
```

```text
#+RESULTS:
| true  |
| true  |
| false |
```


### boolean 연산자 "and" or "or" {#boolean-연산자-and-or-or}

이게 약간 햇갈렸는데, 정리를 해보자면
or는 하나만 true면 true이기 때문에 처음 true한 값을 반환하면 되는거고(물론 false가 하나라도 있다면 마지막 값을 반환한다)
and는 다 true여야 true를 반환하기 때문에 하나라도 false가 나오면 그 값을 반환하는 것이다. (아무것도 false가 아니라면 마지막 true한 값을 반환한다.)

```clojure { linenos=true, linenostart=1 }
(or false nil :large_I_mean_venti :why_cant_I_just_say_large)
(or (= 0 1) (= "yes" "no"))
(or nil)
```

1번의 첫번째 true가 반환
2번은 truethy가 없음
3번은 마지막 값 반환

```clojure
(and :free_wifi :hot_coffee)
```

```text
#+RESULTS:
: :hot_coffee
```

마지막 true 값

---

```clojure
(and :feeling_super_cool nil false)
```

```text
;; => nil
```

처음 falsy한 값

---


## 마무리 {#마무리}

-   nil과 false를 빼면 모두 true로 평가된다
-   do는 if와 then을 합친거랑 비슷함
-   and는 처음 falsey를 반환
-   or은 처음 truthy를 반환
-   이제부터 "##"로 기억해야할 것 표시 할 것
