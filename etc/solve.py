import math

TOTAL_QUESTIONS = 60
Solve_answer = 40
Correct_answer = 23

print("풀이률은" + str((Solve_answer / TOTAL_QUESTIONS) * 100) + '%입니다.')
print("정답률은" + str((math.floor((Correct_answer / Solve_answer) * 100)) * 100 / 100) + '%입니다.')