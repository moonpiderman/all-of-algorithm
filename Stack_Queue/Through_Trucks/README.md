# No.42583

## Quiz

> - 트럭 여러 대가 강을 가로지르는 일 차선 다리를 정해진 순으로 건너려 합니다. 모든 트럭이 다리를 건너려면 최소 몇 초가 걸리는지 알아내야 합니다. 트럭은 1초에 1만큼 움직이며, 다리 길이는 bridge_length이고 다리는 무게 weight까지 견딥니다.
> - ※ 트럭이 다리에 완전히 오르지 않은 경우, 이 트럭의 무게는 고려하지 않습니다.
> - 예를 들어, 길이가 2이고 10kg 무게를 견디는 다리가 있습니다. 무게가 [7, 4, 5, 6]kg인 트럭이 순서대로 최단 시간 안에 다리를 건너려면 다음과 같이 건너야 합니다.

| 경과시간 | 다리를 지난 트럭 | 다리를 건너는 트럭 | 대기트럭     |
| :------- | :--------------- | :----------------- | :----------- |
| 0        | []               | []                 | [7, 4, 5, 8] |
| 1~2      | []               | [7]                | [4, 5, 6]    |
| 3        | [7]              | [4]                | [5, 6]       |
| 4        | [7]              | [4, 5]             | [6]          |
| 5        | [7, 4]           | [5]                | [6]          |
| 6~7      | [7, 4, 5]        | [6]                | []           |
| 8        | [7, 4, 5, 6]     | []                 | []           |

## Solution

1. 최종 시간을 체크해줄 변수를 생성한다.
2. 다리의 길이만큼의 새로운 리스트를 생성한다.
3. 리스트의 값이 존재할 때까지 반복문을 사용해준다.
4. 시간은 어차피 흐르므로 반복문이 돌 때마다 1을 더한다.
5. 리스트의 맨 앞은 어차피 빠져나갈 녀석이기 때문에 pop(0)으로 먼저 제거한다.
6. truck_weights에 pop과 append를 사용해서 queue리스트에 이어붙여줄 것이기 때문에 존재 여부에 따라 가정문을 사용한다.
7. truck_weights[0]을 쓰는 이유는 대기 트럭들에서 첫번째를 빼내기 위함이다.