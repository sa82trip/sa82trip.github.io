---
title:  "github.io 블로그 시작하기"
excerpt: "GitHub Blog 서비스인 github.io 블로그 시작하기로 했다."

categories:
  - Blog
tags:
  - Blog
last_modified_at: 2020-08-19 20:44
---
## 처음으로 이용해보는 지킬(Jekyll)
이것은 지킬을 이용해서 적는 처음 블로그 포스트 이다.  
이 글의 제목은 {{ page.title }}이고  
마지막으로 수정된 시간은 {{ page.last_modified_at }}이다.

이렇게 변수를 사용할 수 있다.
여기서 \"\\\"는 없다고 생각하고 봐야함. 
현재 마크다운에서 이스케이프가 안되서 일단 이렇게 적어놓음

```javascript
이런식으로 사용가능하다
 {{page.title}} {{page.last_modified_at}}
```
