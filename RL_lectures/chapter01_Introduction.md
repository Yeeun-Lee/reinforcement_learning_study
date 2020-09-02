## Chapter 1 - Reinforcement Learning Introduction

강화학습은 주어진 환경(environment)에서 최대한의 보상(reward)을 받을 수 있는 에이전트(agent)를 학습하는 것을 의미합니다.

- 환경 : 에이전트가 움직이는 공간
- 에이전트 : 환경에 포함되며, 움직임(action)을 통해 상태를 변경 시킨다.
- 보상 : 상태에 따라 주어지는 각 단계의 반환값

강화학습은 최근 들어 머신러닝 영역에서 가장 주목받고 있으며, 행위 심리학의 영향을 받았다.

### Trial and Error(스키너의 상자 실험 - 강화이론)
![](https://mblogthumb-phinf.pstatic.net/MjAxNzAzMjBfMTAw/MDAxNDkwMDE5NDYzMjgy.-OAl7ifW-lAvVJjzu2cOHhkLHAdFNZKe1F05v32ubbcg.WvHcQi5YybBC4FI1b03JwTRmX2fprF7Zcvkg0DUcvzAg.JPEG.guten1234/%EC%8A%A4%ED%82%A4%EB%84%88%EC%83%81%EC%9E%90.jpg?type=w2)
>1. 배고픈 쥐를 상자에 넣는다(스키너 상자, 레버를 건드리면 먹이가 나온다.
>2. 쥐가 상자안을 돌아다니다가 우연히 레버를 건드린다.
>3. 먹이가 나온다.
>4. 2, 3을 반복한다.(처음 쥐는 먹이가 나올 수 있는 방법을 모르는 상태)
>5. 반복을 통해 레버를 내리면 먹이가 나온다는 사실을 인지하게 된다.(강화)
>**결과** : 쥐는 배가 고플 때 레버를 내리게 된다(보상)

![](http://www.incompleteideas.net/book/ebook/figtmp7.png)
