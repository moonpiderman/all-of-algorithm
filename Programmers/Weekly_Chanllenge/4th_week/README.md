### ๐งโ๐ป [์ง์๊ตฐ ์ถ์ฒํ๊ธฐ](https://programmers.co.kr/learn/courses/30/lessons/84325)

> - ๊ฐ๋ฐ์๊ฐ ์ฌ์ฉํ๋ ์ธ์ด์ ์ธ์ด ์ ํธ๋๋ฅผ ์๋ ฅํ๋ฉด ๊ทธ์ ๋ง๋ ์ง์๊ตฐ์ ์ถ์ฒํด์ฃผ๋ ์๊ณ ๋ฆฌ์ฆ์ ๊ฐ๋ฐํ๋ ค๊ณ  ํฉ๋๋ค.
> - ์๋ ํ๋ 5๊ฐ ์ง์๊ตฐ ๋ณ๋ก ๋ง์ด ์ฌ์ฉํ๋ 5๊ฐ ์ธ์ด์ ์ง์๊ตฐ ์ธ์ด ์ ์๋ฅผ ๋ถ์ฌํ ํ์๋๋ค.
> 
> |์ ์|SI|CONTENTS|HARDWARE|PORTAL|GAME|
> |:---|:---|:---|:---|:---|:---|
> |5|JAVA|JAVASCRIPT|C|JAVA|C++|
> |4|JAVASCRIPT|JAVA|C++|JAVASCRIPT|C#|
> |3|SQL|PYTHON|PYTHON|PYTHON|JAVASCRIPT|
> |2|PYTHON|SQL|JAVA|KOTLIN|C|
> |1|C#|C++|JAVASCRIPT|PHP|JAVA|
> 
> - ์๋ฅผ ๋ค๋ฉด, SQL์ SI ์ง์๊ตฐ ์ธ์ด ์ ์๋ 3์ ์ด์ง๋ง CONTENTS ์ง์๊ตฐ ์ธ์ด ์ ์๋ 2์ ์๋๋ค. SQL์ HARDWARE, PORTAL, GAME ์ง์๊ตฐ ์ธ์ด ์ ์๋ 0์ ์๋๋ค.
> - ์ง์๊ตฐ ์ธ์ด ์ ์๋ฅผ ์ ๋ฆฌํ ๋ฌธ์์ด ๋ฐฐ์ด table, ๊ฐ๋ฐ์๊ฐ ์ฌ์ฉํ๋ ์ธ์ด๋ฅผ ๋ด์ ๋ฌธ์์ด ๋ฐฐ์ด languages, ์ธ์ด ์ ํธ๋๋ฅผ ๋ด์ ์ ์ ๋ฐฐ์ด preference๊ฐ ๋งค๊ฐ๋ณ์๋ก ์ฃผ์ด์ง๋๋ค. ๊ฐ๋ฐ์๊ฐ ์ฌ์ฉํ๋ ์ธ์ด์ ์ธ์ด ์ ํธ๋ x ์ง์๊ตฐ ์ธ์ด ์ ์์ ์ดํฉ์ด ๊ฐ์ฅ ๋์ ์ง์๊ตฐ์ return ํ๋๋ก solution ํจ์๋ฅผ ์์ฑํด์ฃผ์ธ์. ์ดํฉ์ด ๊ฐ์ ์ง์๊ตฐ์ด ์ฌ๋ฌ ๊ฐ์ผ ๊ฒฝ์ฐ, ์ด๋ฆ์ด ์ฌ์  ์์ผ๋ก ๊ฐ์ฅ ๋น ๋ฅธ ์ง์๊ตฐ์ return ํด์ฃผ์ธ์.

> - ์ ํ ์ฌํญ
> 
> - table์ ๊ธธ์ด = 5
> > - table์ ์์๋ "์ง์๊ตฐ 5์ ์ธ์ด 4์ ์ธ์ด 3์ ์ธ์ด 2์ ์ธ์ด 1์ ์ธ์ด"ํ์์ ๋ฌธ์์ด์๋๋ค. ์ง์๊ตฐ, 5์ ์ธ์ด, 4์ธ์ด, 3์ ์ธ์ด, 2์ ์ธ์ด, 1์ ์ธ์ด๋ ํ๋์ ๊ณต๋ฐฑ์ผ๋ก ๊ตฌ๋ถ๋์ด ์์ต๋๋ค.
> > - table์ ๋ชจ๋  ํ์คํธ์ผ์ด์ค์์ ๋์ผํฉ๋๋ค.
> - 1 โค languages์ ๊ธธ์ด โค 9
> > - languages์ ์์๋ "JAVA", "JAVASCRIPT", "C", "C++" ,"C#" , "SQL", "PYTHON", "KOTLIN", "PHP" ์ค ํ ๊ฐ ์ด์์ผ๋ก ์ด๋ฃจ์ด์ ธ ์์ต๋๋ค.
> > - languages์ ์์๋ ์ค๋ณต๋์ง ์์ต๋๋ค.
> - preference์ ๊ธธ์ด = languages์ ๊ธธ์ด
> > - 1 โค preference์ ์์ โค 10
> - preference์ i๋ฒ์งธ ์์๋ languages์ i๋ฒ์งธ ์์์ ์ธ์ด ์ ํธ๋์๋๋ค.
> - return ํ  ๋ฌธ์์ด์ "SI", "CONTENTS", "HARDWARE", "PORTAL", "GAME" ์ค ํ๋์๋๋ค.

> ์์ถ๋ ฅ ์์ 
> 
> |table|languages|preference|result|
> |:---|:---|:---|:---|
> |["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"]|["PYTHON", "C++", "SQL"]|[7, 5, 5]|"HARDWARE"|
> |["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"]|["JAVA", "JAVASCRIPT"]|[7, 5]|"PORTAL"|
