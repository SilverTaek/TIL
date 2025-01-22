# 조건
monthly_investment_year1_2 = 1_000_000  # 대출 상환 중 매달 투자 금액 (2년)
monthly_investment_year3 = 2_000_000  # 대출 상환 후 매달 투자 금액 (1년)
annual_return_rate = 0.08  # 연평균 수익률 (8%)
monthly_return_rate = annual_return_rate / 12  # 월 수익률
months_year1_2 = 24  # 대출 상환 기간 (2년)
months_year3 = 12  # 대출 상환 후 기간 (1년)

# 1. ISA 투자 (대출 상환 중 2년간 투자)
future_value_year1_2 = sum([
    monthly_investment_year1_2 * (1 + monthly_return_rate) ** (months_year1_2 - n)
    for n in range(months_year1_2)
])

# 2. ISA 추가 투자 (대출 상환 완료 후 1년간 투자)
future_value_year3 = sum([
    monthly_investment_year3 * (1 + monthly_return_rate) ** (months_year3 - n)
    for n in range(months_year3)
])

# 3. 2년간 투자분에 대한 3년째 복리 계산 (추가 1년간 성장)
future_value_year1_2_at_end = future_value_year1_2 * (1 + monthly_return_rate) ** months_year3

# 총 미래 자산 계산
total_future_value = future_value_year1_2_at_end + future_value_year3

# 총 투자 금액
total_investment = (monthly_investment_year1_2 * months_year1_2) + (monthly_investment_year3 * months_year3)

total_future_value, total_investment, total_future_value - total_investment
