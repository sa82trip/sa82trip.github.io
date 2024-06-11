---
title: draw diagram with mermaid
date: 2024-06-12 06:00:00 +0800
categories: [Tools]
tags: [howto]
mermaid: true
pin: true
---
## Flow chart example
```mermaid
flowchart LR
   a --> b & c--> d
 ```

## Sequence diagram example
```mermaid
sequenceDiagram
    user->>site: login
    site-->>user: take user to main page of website
    user->>site: logout
    site-->>user: take user to login page
```

 node의 형태와 edge의 형태를 바꿀 수 있고 공식문서를 참고

 기본적인 사용법은 이곳에 추가 예정

 참조 : [공식문서](https://mermaid.js.org/intro/);