### ๐งโ๐ป [๊ฑฐ๋ฆฌ๋๊ธฐ ํ์ธํ๊ธฐ](https://programmers.co.kr/learn/courses/30/lessons/81302)

> - ๊ฐ๋ฐ์๋ฅผ ํฌ๋งํ๋ ์ฃ ๋ฅด๋๊ฐ ์นด์นด์ค์ ๋ฉด์ ์ ๋ณด๋ฌ ์์ต๋๋ค.
> - ์ฝ๋ก๋ ๋ฐ์ด๋ฌ์ค ๊ฐ์ผ ์๋ฐฉ์ ์ํด ์์์๋ค์ ๊ฑฐ๋ฆฌ๋ฅผ ๋ฌ์ ๋๊ธฐ๋ฅผ ํด์ผํ๋๋ฐ ๊ฐ๋ฐ ์ง๊ตฐ ๋ฉด์ ์ธ ๋งํผ ์๋์ ๊ฐ์ ๊ท์น์ผ๋ก ๋๊ธฐ์ค์ ๊ฑฐ๋ฆฌ๋ฅผ ๋๊ณ  ์๋๋ก ์๋ดํ๊ณ  ์์ต๋๋ค.
> > - ๋๊ธฐ์ค์ 5๊ฐ์ด๋ฉฐ, ๊ฐ ๋๊ธฐ์ค์ 5x5 ํฌ๊ธฐ์๋๋ค.
> > - ๊ฑฐ๋ฆฌ๋๊ธฐ๋ฅผ ์ํ์ฌ ์์์๋ค ๋ผ๋ฆฌ๋ ๋งจํดํผ ๊ฑฐ๋ฆฌ1๊ฐ 2 ์ดํ๋ก ์์ง ๋ง์ ์ฃผ์ธ์.
> > - ๋จ ์์์๊ฐ ์์์๋ ์๋ฆฌ ์ฌ์ด๊ฐ ํํฐ์์ผ๋ก ๋งํ ์์ ๊ฒฝ์ฐ์๋ ํ์ฉํฉ๋๋ค.
> 
> ์๋ฅผ ๋ค์ด,
![initial](https://user-images.githubusercontent.com/70942197/125180819-ad185b80-e239-11eb-913b-a11229ae6c3f.png)
> 5๊ฐ์ ๋๊ธฐ์ค์ ๋ณธ ์ฃ ๋ฅด๋๋ ๊ฐ ๋๊ธฐ์ค์์ ์์์๋ค์ด ๊ฑฐ๋ฆฌ๋๊ธฐ๋ฅผ ์ ๊ธฐํค๊ณ  ์๋์ง ์๊ณ  ์ถ์ด์ก์ต๋๋ค. ์๋ฆฌ์ ์์์๋ ์์์๋ค์ ์ ๋ณด์ ๋๊ธฐ์ค ๊ตฌ์กฐ๋ฅผ ๋๊ธฐ์ค๋ณ๋ก ๋ด์ 2์ฐจ์ ๋ฌธ์์ด ๋ฐฐ์ด places๊ฐ ๋งค๊ฐ๋ณ์๋ก ์ฃผ์ด์ง๋๋ค. ๊ฐ ๋๊ธฐ์ค๋ณ๋ก ๊ฑฐ๋ฆฌ๋๊ธฐ๋ฅผ ์งํค๊ณ  ์์ผ๋ฉด 1์, ํ ๋ช์ด๋ผ๋ ์งํค์ง ์๊ณ  ์์ผ๋ฉด 0์ ๋ฐฐ์ด์ ๋ด์ return ํ๋๋ก solution ํจ์๋ฅผ ์์ฑํด ์ฃผ์ธ์.

> ์ ํ ์ฌํญ
>
> - places์ ํ ๊ธธ์ด(๋๊ธฐ์ค ๊ฐ์) = 5
> > - places์ ๊ฐ ํ์ ํ๋์ ๋๊ธฐ์ค ๊ตฌ์กฐ๋ฅผ ๋ํ๋๋๋ค.
> - places์ ์ด ๊ธธ์ด(๋๊ธฐ์ค ์ธ๋ก ๊ธธ์ด) = 5
> - places์ ์์๋ P,O,X๋ก ์ด๋ฃจ์ด์ง ๋ฌธ์์ด์๋๋ค.
> > - places ์์์ ๊ธธ์ด(๋๊ธฐ์ค ๊ฐ๋ก ๊ธธ์ด) = 5
> > - P๋ ์์์๊ฐ ์์์๋ ์๋ฆฌ๋ฅผ ์๋ฏธํฉ๋๋ค.
> > - O๋ ๋น ํ์ด๋ธ์ ์๋ฏธํฉ๋๋ค.
> > - X๋ ํํฐ์์ ์๋ฏธํฉ๋๋ค.
> - ์๋ ฅ์ผ๋ก ์ฃผ์ด์ง๋ 5๊ฐ ๋๊ธฐ์ค์ ํฌ๊ธฐ๋ ๋ชจ๋ 5x5 ์๋๋ค.
> - return ๊ฐ ํ์
> > - 1์ฐจ์ ์ ์ ๋ฐฐ์ด์ 5๊ฐ์ ์์๋ฅผ ๋ด์์ return ํฉ๋๋ค.
> > - places์ ๋ด๊ฒจ ์๋ 5๊ฐ ๋๊ธฐ์ค์ ์์๋๋ก, ๊ฑฐ๋ฆฌ๋๊ธฐ ์ค์ ์ฌ๋ถ๋ฅผ ์ฐจ๋ก๋๋ก ๋ฐฐ์ด์ ๋ด์ต๋๋ค.
> > - ๊ฐ ๋๊ธฐ์ค ๋ณ๋ก ๋ชจ๋  ์์์๊ฐ ๊ฑฐ๋ฆฌ๋๊ธฐ๋ฅผ ์งํค๊ณ  ์์ผ๋ฉด 1์, ํ ๋ช์ด๋ผ๋ ์งํค์ง ์๊ณ  ์์ผ๋ฉด 0์ ๋ด์ต๋๋ค.

> ์์ถ๋ ฅ ์์ 
> 
> |places|result|
> |:---|:---|
> |[["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]|[1, 0, 1, 1, 1]|
