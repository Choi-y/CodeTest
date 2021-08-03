# The candy war (https://www.acmicpc.net/problem/9037) 풀이 (7/3)

# 알고리즘 유치원 선생님인 영희는 간식시간이 되자 아이들에게 사탕을 나누어 주려고 하였다.
# 하지만 욕심 많고 제멋대로인 유치원 아이들은 차례대로 받으라는 선생님의 말을 무시한 채 마구잡이로 사탕을 집어 갔고 많은 사탕을 집어 간 아이가 있는가 하면 사탕을 거의 차지하지 못하고 우는 아이도 있었다.
# 말로 타일러도 아이들이 말을 듣지 않자 영희는 한 가지 놀이를 제안했다. 일단 모든 아이들이 원으로 둘러 앉는다. 그리고 모든 아이들은 동시에 자기가 가지고 있는 사탕의 절반을 오른쪽 아이에게 준다.
# 만약 이 결과 홀수개의 사탕을 가지게 된 아이가 있을 경우 선생님이 한 개를 보충해 짝수로 만들어 주기로 했다.
# 흥미로워 보이는 이 놀이에 아이들은 참여 했고 이 과정을 몇 번 거치자 자연스럽게 모든 아이들이 같은 수의 사탕을 가지게 되어 소란은 종료되었다.
# 자기가 가진 사탕의 반을 옆에 오른쪽에 앉은 아이에게 주는 과정과 선생님이 사탕을 보충해 주는 과정을 묶어서 1 순환이라고 할 때 몇 번의 순환을 거치면 모든 아이들이 같은 수의 사탕을 가지게 되는지 계산 해보자.
# 단, 처음부터 홀수개의 사탕을 가지고 있으면 선생님이 짝수로 보충을 먼저 해주며 이 경우 순환수에 들어가지 않는다. 선생님은 충분한 수의 사탕을 갖고 있다고 가정하자.


# 테스트 케이스 T
T = int(input())
sol = list()

for i in range(T):
    N = int(input())
    C = list(map(int, input().split()))

    solution = -1

    while(1):
        # 짝수 맞춰 주는 과정
        for j in range(N):
            if C[j] % 2 == 1:
                C[j] += 1

        solution += 1
        if C.count(C[0]) == N:
            break

        # 옆으로 주는 과정
        tmp = list()
        for j in range(N):
            tmp.append(C[j]//2)
            C[j] -= tmp[j]

        C[0] = C[0] + tmp[N-1]
        for j in range(N-1):
            C[j+1] += tmp[j]

    sol.append(solution)

for i in range(T):
    print(sol[i])