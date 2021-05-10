### 🧑‍💻 문제 No. 42746

> 한자리 숫자가 적힌 종이 조각이 흩어져있습니다.
> 흩어진 종이 조각을 붙여 소수를 몇 개 만들 수 있는지 알아내려 합니다.
> 각 종이 조각에 적힌 숫자가 적힌 문자열 numbers가 주어졌을 때, 종이 조각으로 만들 수 있는 소수가 몇 개인지 return 하도록 solution 함수를 완성해주세요.

> 제한 사항
>
> - numbers는 길이 1 이상 7 이하인 문자열입니다.
> - numbers는 0~9까지 숫자만으로 이루어져 있습니다.
> - "013"은 0, 1, 3 숫자가 적힌 종이 조각이 흩어져있다는 의미입니다.

| numbers | return |
| :------ | :----- |
| "17"    | 3      |
| "011"   | 2      |

> 입출력 예 설명
>
> > - 예제 #1
> >   [1, 7]으로는 소수 [7, 17, 71]를 만들 수 있습니다.
> > - 예제 #2
> >   [0, 1, 1]으로는 소수 [11, 101]를 만들 수 있습니다.
> > - 11과 011은 같은 수로 취급합니다.

### 🧑‍💻 Solution

> 1. 소수를 만들어줄 함수를 생성한다.
> 2. 입력받은 numbers를 하나씩 쪼개준다.
> 3. 순열을 만들어서 total 리스트에 나열해준다.
> 4. 2차원 리스트를 이어붙여주고 모두 int형으로 변환 후 중복을 제거한다.
> 5. 소수를 판별하여 소수가 맞으면 answer를 count한다.