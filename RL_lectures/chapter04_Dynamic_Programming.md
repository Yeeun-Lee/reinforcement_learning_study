# Dynamic Programming(다이나믹 프로그래밍)
### Contents
>[Intro. Steps for Dynamic Programming](#steps-for-dinamic-programming)\
>[1.Policy Iteration](#1.-policy-iteration)
>>[1.1 Policy Evaluation](#1.1-policy-evaluation)\
>>[1.2 Policy Iteration](#1.2-policy-iteration)

> [2. Value Iteration](#2.-value-iteration)\
>>[2.1 Value Iteration](#2.1-value-iteration)\
>>[2.2 Sample Backup](#2.2-sample-backup)


다이나믹 프로그래밍에 들어가기 전에, **Planning**과 **Learning**의 차이를 알고 들어가는 것이 매우 중요합니다.
- **Planning** : 환경의 모형을 알고 문제를 해결함
  - 에이전트는 모형을 가지고 계산을 하고, policy를 조정합니다.
  - a.k.a deliberation, reasoning, intropection, pondering, thought, search
- **Learning** : 환경의 모형은 모르지만 환경과의 상호작용을 통해 문제를 해결함.
  - 에이전트 환경과 상호작용을 하면서 policy를 조정해 나갑니다.

여기서 Dynamic Programming은 Planning에 해당하며, 환경의 모형(보상, state transition matrix, MDP에서 다뤘었죠!!)에 대해 안다는 전제로
문제를 해결합니다. 이 때 문제 해결에는 Bellman Equation을 사용합니다.
> Bellman equation 또한 reward와 state transition matrix 없이는 풀 수 없었습니다.

### Steps for Dynamic Programming
#### running strategy )
현재 opimal하지 않은 어떤 policy에 대해서 value function을 구하고, 현재의 value function을 토대로 더 나은 policy를 구하는 과정을 반복하여
optimal policy를 구하는 것
> 다이나믹 프로그래밍(동적 프로그래밍)은 R.Bellman이 창시한 이론이며, 순차적인 해 탐색 과정을 통해 optimal solution을 구할 수 있다.


<span style= "background-color: #FFFF33"><i>수식은 마크다운에서 표현이 어려워 LaTex문법으로 작성하였습니다.</i></span>

#### 1) prediction
- input : MDP <S, A, P, R, \gamma>, policy \pi or MRP <S, P^\pi, R^\pi, \gamma>
- output : **value function v_\pi**

#### 2) control
- input :  MDP <S, A, P, R, \gamma>
- output : optimal value function v_*, optimal policy \pi_*

## 1. Policy Iteration

---
### 1.1 Policy evaluation
prediction 문제를 푸는 것이다. prediction의 input으로 주어진 policy(\pi)에 대해서 실제 value function을 구하게 되고 여기서
Bellman equation을 사용한다.
> - 현재의 policy(\pi)를 사용해서 true value function을 구할 때는 one step backup을 사용한다.
>- 이전의 Bellman equation과 다른첨은 iteration을 표시하는 k가 붙은 것이다.

<img src = "https://dnddnjs.gitbooks.io/rl/content/1601b1e72a52c39d2fc6447597f0ff3b.png" width = "600">

Bellman equation에서 backup diagram을 사용 했을 때, 계산해서 update를 하는 방식은 차례차례 state 별로 계산하는 방식이었습니다.\
하지만, value function을 update하는 위 다이어그램에서는 **MDP의 모든 state에 대해서 동시에** 한번씩 bellman equation을 계산하여 update를 진행하고,
반복 수를 나타내는 k의 값이 1증가합니다.  

<img src = "https://dnddnjs.gitbooks.io/rl/content/feewa.png" width = "600">

- 에이전트는 상, 하, 좌, 우 네가지의 액션을 취할 수 있습니다. 처음 시작했을 때, random policy로 시작한 에이전트의 모든 state에서 action에 대한 확률은
동일합니다.(1/4 = 0.25)
- 회색이 칠해져 있는 칸을 terminal(끝점) state라 합니다.
- 회색 지점에 도달하는 것을 목표로 하고, 도달하지 못한 경우 time step이 지날 때 마다 -1의 reward
<img src = "https://dnddnjs.gitbooks.io/rl/content/dp4.png">

- k = 0 : 아무것도 일어나지 않은 상태로, 전부 0으로 초기화 됩니다.
- k = 1 : value function update 수식에 값을 대입합니다.(V = 4 * 0.25(-1 + 0) = -1
  - immediate reward : -1, v(0) : 0, num of actions : 4, action들은 전부 동일한 probability 0.25를 가짐)
- k = 2 : (1, 2)state에서, 갈 수 없는 방향이 있음. (V = 1 * 0.25(-1 + 0) + 3 * 0.25(-1+(-1)) = -1.7(rounded))\
이런 식으로 무한 반복 하게 되면 현재 random policy에 대한 true value function을 구할 수 있고, 이를 **policy evaluation**이라 부른다.\

<img src = "https://dnddnjs.gitbooks.io/rl/content/dp5.png">

---
### 1.2 Policy iteration
**policy improvement** : policy에 대한 true value를 얻었을 때 policy를 update해주는 것(점점 optimal policy에 가까워짐.)
  - Greedy improvement: 다음 state 중에서 가장 높은 value function을 가진 state로 가는 것(max값을 취함.)
<img src = "https://dnddnjs.gitbooks.io/rl/content/bd93a4fa73cacc88bc82181ff074766d.png">

**policy iteration** : improvement를 계속 반복하는 과정
<img src = "https://dnddnjs.gitbooks.io/rl/content/6d484ed095cba2cd7a8edf50b7e4e17e.png">
꼭 무한 반복할 필요는 없으며 한번 혹은 세번만에도 optimal policy를 구하기도 한다.

---
## 2. Value Iteration
### 2.1 Value Iteration
앞선 policy iteration과 다른 점은 expectation equation을 사용하는 것이 아닌, **Bellman optimality equation**을 사용한다는 것이다.\
optimal values function들 간의 관계식을 iterative하게 변환해 준다.

- evaluation 단계에서 optimal value만 고려하면 되기 때문에 단 한번만 진행한다.
  - 현재 value function을 계산하고 update할 때 max를 취함으로써 greedy하게 improve하는 효과를 줌
  - 한번의 evaluation + improvement = value iteration
<img src = "https://dnddnjs.gitbooks.io/rl/content/674af1b62041c9bfb73361222264c073.png" width = "600">

### 2.2 Sample Backup
:bulb: **remark**

- DP는 MDP에 대한 정보를 다 가지고 있어야 optimal policy를 구할 수 있다.
- DP는 full-width backup을 사용하고 있어 한번의 backup에도 많은 연산량을 요구한다.
  - 한 번 update할 때 가능한 모든 successor state의 value function을 통해 update하는 방법
- :star: state의 숫자가 늘어날수록 계산량이 계산량이 기하급수적으로 증가하여 MDP가 매우 크거나 MDP에 대해서 다 알지 못할 경우 DP를 적용시킬 수 없다. 

<i>이 때 등장하는 개념이 바로 sample backup이다.</i>

- 모든 가능한 successor state/action을 고려하지 않고, 샘플링을 통해 한 길만 가보고 그 정보를 토대로 value function을 업데이터 함.
- 계산이 효율적일 뿐만 아니라 model-free가 가능함.

:question: **model-free**
DP의 방법대로 optimal 해를 찾으려면 매 iteration마다 reward transition matrix를 알아야 함.
하지만 sample backup의 경우 <S, A, R, S'>을 학습시켜서 나온 reward와 sample transition으로 그 둘을 대체하게 됨.

DP를 sampling을 통해 푸는 것 부터 reinforcement learning 의 시작이 됨
