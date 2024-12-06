import math

TOTAL_QUESTIONS = 40
Solve_answer = 17
Correct_answer = 8

print("풀이률은" + str((Solve_answer / TOTAL_QUESTIONS) * 100) + '%입니다.')
print("정답률은" + str((math.floor((Correct_answer / Solve_answer) * 100)) * 100 / 100) + '%입니다.')
