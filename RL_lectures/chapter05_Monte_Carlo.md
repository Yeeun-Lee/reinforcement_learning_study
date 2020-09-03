# Monte Carlo Learning


## 1. Monte Carlo Prediction
:bulb: model free prediction
현재의 policy를 바탕으로 움직이면서 sampling을 통해 value function을 update하는 것.(만약 policy update까지 이루어 지면 model free control이라 한다)
### Contents
> 

#### sampling을 통해 학습하는 model free 방법
1) Monte-Carlo : episode마다 updaate
2) Temporal Difference : time step마다 update

### 1.1 Monte Carlo
episode를 끝까지 가본 후에 받은 reward들로 각 state의 value function들을 거꾸로 계산해 본다. 따라서 MC(Monte Carlo)는 끝나지 않는 
episode에서는 사용할 수 없다.
> 순간 순간 받았던 reward들을 시간 순서대로 discount시켜서 sample return을 구할 수 있다.

<img src="https://dnddnjs.gitbooks.io/rl/content/MC1.png">

### 1.2 First visit MC vs Every visit MC
multiple episode를 진행할 경우 한 episode마다 얻었던 return을 MC에서는 단순 평균으로 사용한다.
- 어떤 state에 대해 return을 계산 해 두었는데, 다른 episode에서도 그 state를 지나서 새로운 return을 얻는다
- 두 값의 평균을 취해준다.
- 반복을 거치면서 return들이 쌓일 수록 평균 값은 **true value function**에 가까워진다.

[First visit] : 처음 방문한 state만 인정함, 두 번째 그 state 방문에 대해서는 return을 계산하지 않음.\
[Every visit] : 방문할 때마다 따로 따로 return 계산

:red_circle: 두 방식 모두 무한대로 가면 true value function으로 수렴한다.
<img src="https://dnddnjs.gitbooks.io/rl/content/MC2.png">

### 1.3 Incremental Mean
MC에서 사용하는 평균은 기존에 흔히 사용하는 총합/갯수 가 아니라 하나 하나 더해야면서 평균을 구해야 하기 때문에 Incremental mean의 식을 사용한다.
<img src="https://dnddnjs.gitbooks.io/rl/content/MC3.png">

이를 First visit MC에 적용합니다.

<img src="https://dnddnjs.gitbooks.io/rl/content/MC4.png">

- 분수에서 분모에 위치한 N(St)점점 무한대로 가게 됩니다. 이때, 이 값을 알파로 고정시켜 놓게 되면 효과적으로 평균을 취할 수 있습니다.
  - 맨 처음 정보들에 대해서 가중치를 덜 주는 형태.


**Why**:question:
강화학습은 stationary problem이 아니라서 매 episode마다 새로운 policy를 사용한다(non-stationary). 

### 1.5 Backup Diagram

MC의 backup과정
<img src="https://dnddnjs.gitbooks.io/rl/content/MC5.png">

- MC는 sampling을 통해 학습하는 model-free 방식 --> 하나의 가지로 terminal state까지 이어짐.
- episode마다 update를 진행하여, state에서 어떠한 action을 하느냐에 따라 전혀 다른 experience가 된다(무작위성) --> 높은 variance
- variance가 높은 대신, random인 만큼 bias는 낮은 편

---
## 2. Monte Carlo Control

### 2.1 Monte Carlo Policy Iteration
DP의 Policy Iteration에서 evaluation부분을 Monte-Carlo방식으로 바꾸어준다.

### 2.2 Monte Carlo Control
Monte-Carlo Policy Iteration의 문제점
- value function
- Exploration
- Policy Iteration

(1) Value Function\
현재는 MC로써 Policy를 evaluation할 때 value function을 사용하는데, 이는 improve(greeedy)에서 문제가 발생하게 됨.
- MC는 model-free이지만, value function을 사용하여 policy improvememt를 진행하려면 MDP의 model을 알아야 한다.
- 따라서 value function 대신에 action value function을 이용하면 문제 없이 model-free가 된다.

<img src="https://dnddnjs.gitbooks.io/rl/content/MC10.png">

(2) Exploration\


