# 정렬 알고리즘 시간 복잡도

선택 정렬: 가장 작은 원소를 배열 맨 앞의 원소와 교체
버블 정렬: 그냥 배열의 첫 원소부터 순차적으로 진행
최선: O(n^2)
평균: O(n^2)
최악: O(n^2)

삽입 정렬: 순서대로 삽입하여 다음 값과 비교하여 정렬, 정렬이 되어 있으면 퀵 정렬보다 더 강력하다.
최선: O(n)
평균: O(n^2)
최악: O(n^2)

병합 정렬: 절반씩 계속 나누어 각각 정렬하고 나중에 합친다.
힙 정렬: 완전 이진 트리의 일종으로 우선순위 큐를 위하여 만들어진 자료구조

최선: O(nlogn)
평균: O(nlogn)
최악: O(nlogn)

퀵 정렬: 무작위 pivot을 선정하여 작은 것 큰 것 나눠서 비교한다. 단, 중간값에 가까운 값이 될거라는 보장이 없어서 최악의 경우 n^2 이 될 수 있다.
최선: O(nlogn)
평균: O(nlogn)
최악: O(n^2)
