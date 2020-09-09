# Value Function Approximation
지금까지는 action value function을 table로 만들어서 푸는 tabular Method들을 살펴 보았다. 하지만 이 경우 테이블이 점점 커지게 되면 table이 점점 커져,\
 메모리 문제 뿐만 아니라 학습 시간 문제도 발생하게 된다.
 
 따라서 연속적으로 action과 state가 발생하는 real world에 적용할 수 없다(generalization problem)
 
 ## Parameterizing value funtion
 table로 작성되었던 value function을 w라는 parameter를 가진 함수로 변형시켜 준다. 앞으로의 학습은 이 파라미터 w를 조정하면서 이루어 진다.
 
 업데이트 및 approximation에는 여러 방법이 있는데, 현재 살펴 볼 수 있는 것은 linear combinations of features, NN 방식이 있다.  
 
 ## Stochastic Gradient Descent(SGD, 확률적 경사하강법)
 목표 : 원하는 대상(target)과 자신의 error을 최소화 하는 것.\
 이 때, update에 대해서 방향을 알아야 하는데, 이 때 함수의 미분(gradient) 개념을 사용한다. gradient는 경사이기 때문에 양의 값이면 위로 올라가는 방향이므로
  -를 곱하여 사용한다.
  
  (수식 부분은 필기로 진행하였습니다.)
  
  수식을 살펴보면 분모에 2가 곱해져 있는 것을 볼 수가 있는데, 이 경우 뒷 부분에 나오는 함수를 미분하는 과정에서 수식을 간소화 하기 위해 곱해진 것이다.
  
  ### Gradient Descent on RL
  여기서 파라미터 w를 사용한 error 함수인 J(w)를 정의하는데, 이 때에는 v(s)와 추정된 값인 hat(v)(s,w)의 error를 사용한다.

example) MSE
여기서 1/2를 곱한 이유를 뚜렷하게 볼 수 있다. squared sum을 진행하면서 제곱이 이루어지는데, 이 수식을 미분하면서 나오는 2라는 상수를 1/2로 곱해주면서 식을 간소화해준다.

- gradient descent finds local minimum
> 한꺼번에 업데이트

- stochastic gradient descent samples the gradient
> DP에서 강화학습으로 넘어갈 때처럼 expectation을 없애고 sampling으로 대체\
> (단순히 expectation이 사라진 형태)

## Learning with Function Approximator
- policy evalutation : parameter(w)의 update
- polucy improvement : update된 action value function에 epsilon-greedy action을 취하면서 improve

## Batch Methods
SGD처럼 차근차근 gradient를 따라서 parameter를 update하는 것이 아니라, 경험한 training data에 대한 경험을 전부 모아 한꺼번에 update하는 것.

- 한꺼번에 하면 최적의 value function을 얻기 어렵기 때문에 이 중간 정도 되는 mini-batch방식을 사용하기도 한다.

### Experience Replay
replay memory를 만들어 경험들을 time-step마다 끊어서 저장하고, 모아 둔 transition들을 여기서부터 mini-batch 사이즈 만큼 꺼내서 update를 진행한다.

>- sample efficient
>- step-by-step update -> 데이터 간 correlation으로 인해 학습이 잘 안되는 문제도 해
