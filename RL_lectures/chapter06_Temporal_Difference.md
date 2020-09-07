# Temporal Difference(TD)

MC(Monte-Carlo)와 DP(Dynamic-Programming)의 특성을 결합한 형태
> idea : model-free 방식에서 꼭 episode가 끝나지 않더라고 time step마다 학습할 수 있지 않을까

- MC : model-free
- DP : time step learning

> TD는 현재의 value funtion을 계산하는 데에 이전에 지나온 주변의 state들의 value function을 이용한다.
> -Bellman Equation : 여기서도 벨만 방정식을 이용하는데, 이를 벨만 방적식이 Bootstraping한다고 한다.
>- 현재 상태에서 어떻게든 한다.

## 1. TD(0)

incremental mean
$ R_{t+1} + \gamma V(S_{t+1}) $
