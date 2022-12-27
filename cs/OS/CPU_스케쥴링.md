# Starvation

---

### 하나의 프로세스가 스케줄링 전략상 문제로 인해 계속해서 CPU가 할당되지 못하는 상황

# Preemptive Scheduling

---

- **Non-preemptive(비선점형) 스케줄링**

CPU에서 돌고있는 Job을 다 끝날 때 까지 기다려 줘야하는 스케줄링 전략(중간에 못 뺐는 거)

- **Preemptive(선점형) 스케줄링**

중간에 개입해서 진행중인 Job을 끊고 다른 Job을 할당 하는 것이 가능한 스케줄링 전략(중간에 뺐을 수 있는 거)

# Scheduling 알고리즘의 목표들

---

- No starvation
- 프로세스들이 공정하게 CPU에 할당 되기
- 모든 CPU가 적당하게 동작중인 상태로 진행

**Scheduling 알고리즘의 목적에 따라 적절하게 Scheduling전략을 짜면 된다**

# Scheduling 특징

---

## Want to Maximize

- CPU utilization (Cpu 놀지마!)
- Throughput   (완료된 task/시간) 4/10  <  3/5

## Want to Minimize

- Response Time: 처음 task가 준비된 시점 부터  CPU에 할당 되기까지 기다리는 시간
- Waiting Time : 대기하는 시간 (Response Time + 중간에 Preemptive되면서 기다리는 시간)
- Turnaround Time  : Task 처음 준비 될때 부터 끝날 때 까지

# FCFS(First-Come, First-Served)

---

**도착한 순서대로 CPU에 할당하라!(선입선출)**

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/0629fb6a-9620-431f-82c7-2453941d4e42/__2021-06-29_175922.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/0629fb6a-9620-431f-82c7-2453941d4e42/__2021-06-29_175922.png)

- Non-preemptive
- 장점 : 순서만 기다리면 조만간 CPU에 할당 될거니까(No Starvation)
- 단점 : Convoy effect (수송수단 ex)경운기)

          ( 만약 작은 task가 큰 task 뒤에 있으면 오래 기다려야 한다- response time 길어진다)

          ex) 마트를 갔는데 난 과자 하나 살건데 앞에 카트 끌고 온 사람 기다려야 하는경우

# SJF/SRTF

---

## SJF(Shortest Job First)

**프로세스를 보고 제일 조금 걸리는 애들을 먼저 CPU할당**

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/776cdf1f-048b-422b-8b5e-993091ff3a17/__2021-06-29_180128.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/776cdf1f-048b-422b-8b5e-993091ff3a17/__2021-06-29_180128.png)

- Non-Preemptive
- Priority scheduling
- 장점

    Convoy effect 해결

- 단점

    1. Can Starvation 

    2. 시간(future CPU burst time) 얼마나 걸릴지 예측이 불가능하다.

       단지 이전의 CPU burst Time으로 추측할 뿐

## SRTF (Shortest Remaining Time First)

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/492e8481-5021-4c13-8da4-c1d3525ad958/__2021-06-29_180259.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/492e8481-5021-4c13-8da4-c1d3525ad958/__2021-06-29_180259.png)

**새로운 Job이 왔을 때 남아있는 실행시간을 보고 더 짧은애 있으면 그 프로세스한테 주자!**

- A preemptive version of SJF

# Priority Scheduling

---

**job들마다 우선순위를 갖는 스케줄링 방법**

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/6682c006-07aa-4bd1-a2d0-767dd6c1e54f/__2021-06-29_180535.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/6682c006-07aa-4bd1-a2d0-767dd6c1e54f/__2021-06-29_180535.png)

SJF는 CPU burst time을 기준으로 priority를 만든 스케줄링 전략 이므로 Priority scheduling

## Problem

- **Can Starvation**

    Solution 

    -  Aging (너무 오래 할당 안됐으면 우선순위 높여주자) 경로우대! 

    -  Priority boosting (starvation 염려 되는 상황에 우선순위 쭈욱 높여준다)

- **Priority inversion**

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/e7c776c5-4926-45e0-a9bd-3807ed294f6f/__2021-06-29_152808.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/e7c776c5-4926-45e0-a9bd-3807ed294f6f/__2021-06-29_152808.png)

# RR (Round robin)

---

**Concurrent하게 진행하자!**

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/4f625335-e31e-4ff0-82dd-2c0fb3f6b8b3/__2021-06-29_180624.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/4f625335-e31e-4ff0-82dd-2c0fb3f6b8b3/__2021-06-29_180624.png)

- 각 Job에 time slice(time quantum)가 주어진다.

    그 time slice만큼만 진행하고 다른 job으로 넘어간다

- preemptive
- no starvation
- response time이 짧아짐

### time slice간격을 어떻게 할것인가?

IF Too Short : context switch overhead

IF Too Long : response time 길어짐(like FCFS)

**일반적으로 10~100ms**