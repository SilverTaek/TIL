from collections import deque

prices = [1, 2, 3, 2, 3]


# i 가 0번 인덱스부터 탐색하면서 j가 i보다 하나 큰값만큼 비교해서 i보다 크거나 같으면 +1 씩 카운팅해준다.
# 만약에 j가 i보다 아예 크면 +1만하고 break한다. 
# def get_price_not_fall_periods(prices):
#     # 이 부분을 채워주세요!
#     answer = [0] * len(prices)
#     for i in range(0, len(prices)):
#         cnt = 0
#         for j in range(i+1, len(prices)):
#             if prices[i] <= prices[j]:
#                 cnt+=1
#             else:
#                 cnt+= 1
#                 break
#         answer[i] = cnt
        
#     return answer
    
def get_price_not_fall_periods(prices):
    result = []
    prices = deque(prices)

    while prices:
        cnt = 0
        current_price = prices.popleft()
        for next_price in prices:
            if current_price <= next_price:
                cnt +=1
            else:
                cnt +=1
                break
        result.append(cnt)

    return result


print(get_price_not_fall_periods(prices))

print("정답 = [4, 3, 1, 1, 0] / 현재 풀이 값 = ", get_price_not_fall_periods(prices))
print("정답 = [6, 2, 1, 3, 2, 1, 0] / 현재 풀이 값 = ", get_price_not_fall_periods([3, 9, 9, 3, 5, 7, 2]))
print("정답 = [6, 1, 4, 3, 1, 1, 0] / 현재 풀이 값 = ", get_price_not_fall_periods([1, 5, 3, 6, 7, 6, 5]))