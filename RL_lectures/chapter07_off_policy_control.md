# Off Policy Control

Control이 현재의 policy 위에서 이루어 지는 것 
> 현재 policy로 움직이면서 그 policy를 평가한다.
> - exploration의 한계 존재

## off policy
움직이는 policy와 학습하는 policy를 분리시킨 것.

하나의 policy(mu)를 따르면서 여러개의 policy들을(pi_1, pi_2 ~ pi_{t-1})학습할 수 있다.
> - 이전의 policy들을 재활용하여 학습한다.
> - 다른 agent나 사람을 관찰하고 그로부터 학습한다.
>- 탐험을 계속 하면서도 optimal한 policy를 학습하게 된다(Q-Learning)

## Importance sampling
통계학에서 효율적으로 기댓값을 추정하기 위해 고안된 개념이다.
> 쉽게 말해, p(x)라는 분포에 대해 추정하고 있을 때 샘플을 생성하기 어려울 때, 비교적 샘플 생성이 용이한 분포 q(x)에서 샘플을 생성하여 p의 기댓값을 계산하는 기법.

**강화학습에의 적용**
기존에 random하게 찍어보고 추정하는 과정을 monte-carlo로서 monte carlo estimation이라고 부른다.\
이 때, importance sampling의 개념을 차용하여, 중요한 부분을 위주로 탐색을 하면 더 빠르고 효율적으로 값을 추정할 수 있다는 아이디어.

### Off Policy MC vs TD

**Monte Carlo** : episode가 끝나야 계산할 수 있음.\
에피소드가 끝나고 나서 return을 계산하게 되면, 각 step마다 받은 reward들은 당시의 action policy인 mu를 따라서 한 것이기 때문에 스텝마다 pi/mu를 해주어야 한다.(importance sampling)\
(그리 좋은 아이디어가 아님)

**TD** : importance sampling을 1-step만 진행하면 된다.\
TD의 경우 업데이트에 이전 스텝, 혹은 주위 하나의 스텝을 기준으로 업데이트를 진행하기 때문에, importance sampling을 통해 비
슷하게 만들어 준다고 할 때 하나의 스텝에 대해서만 비슷하게 policy를 얻으면 된다.

> importance sampling을 하면 variance가 explode되는 경향이 있는데, 이 때 TD가 MC에 비해 현저히 낮은 variance를 가진다.

## Q-Learning
앞선 importance sampling은 variance explode문제가 있었다. Off-Policy Learning에서 가장 좋은 알고리즘은 Q-Learning이다.

TD에서 업데이트를 진행할 때, behavior policy와 다른 policy(alternatice)를 사용하게 되면 importance sampling이 필요하지 않다.\
여기서는 action-value funtion을 이용한다.

> **[예시]**
> 항상 가던 음식점만 가는게 아니라 가끔 새로운 곳을 시도해 본다.\
이 때 중요한 것은 epsilon greedy 알고리즘을 사용한다는 것이다.

- Behavior policy(mu) : epsilon greedy
- target policy(alternative) : greedy

epsilon greedy의 경우 탐험 부족 문제는 해결했지만 수렴 속도가 느리다는 단점이 있었다. 이를 해결하기 위해 epsilon을 시간에 따라 decay시키는 방법과 Q-learning을 사용하는 방식이 나타났다.
> 최대로 진행할 수 있는 step을 정할 때, 가끔 random(확률적)하게 선택을 하게 된다.\
> 가보지 않을 곳을 탐험 하면서 새로운 좋은 경로를 찾을 수 있게끔 
