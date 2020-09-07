# Temporal Difference(TD)

MC(Monte-Carlo)와 DP(Dynamic-Programming)의 특성을 결합한 형태
> idea : model-free 방식에서 꼭 episode가 끝나지 않더라고 time step마다 학습할 수 있지 않을까

- MC : model-free
- DP : time step learning

> TD는 현재의 value funtion을 계산하는 데에 이전에 지나온 주변의 state들의 value function을 이용한다.
> -Bellman Equation : 여기서도 벨만 방정식을 이용하는데, 이를 벨만 방적식이 Bootstraping한다고 한다.
>- 현재 상태에서 어떻게든 한다.

## 1. TD(0)

- 타겟 Gt를 incremental mean으로 사용하고, 타겟과 현재 value function의 차이를 TD error라 한다.
<자세한 내용은 이추 추가함>

장점 : final outcome을 모르더라도 학습할 수 있으며, 매 step마다 학습할 수 있다.

## 2. Bias/Variance Trade-Off

- bias가 높다 : 중앙으로부터 전체적으로 많이 벗어남.(TD)
- variance가 높다 : 전체적으로 많이 퍼져있다.(MC)
> 이 둘은 trade-off관계에 있다.

## 3. Sarsa(TD-control)
model-free control이 되기 위해 action-value function을 이용함.(Q-function으로 변경)


이 때, 입실론 그리디 알고리즘을 사용한다.
#### Epsilon greedy algorithm
기존 greedy algorithm을 사용했을 때, local optimum에 빠지게 될 경우 exploration이 부족하다는 단점이 있었다.
- 이를 보완하기 위해 일정한 확률로 랜덤하게 이전에 최선의 결과를 냈던 state로 움직인다.(epsilon : hyperparameter, 0~1)
