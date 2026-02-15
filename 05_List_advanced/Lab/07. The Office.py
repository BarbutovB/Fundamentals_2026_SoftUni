happiness_list = input().split()
factor = int(input())

improved_happiness = []
for h in happiness_list:
    improved_happiness.append(int(h) * factor)

total_sum = 0
for h in improved_happiness:
    total_sum = total_sum + h

average = total_sum / len(improved_happiness)

happy_count = 0
for h in improved_happiness:
    if h >= average:
        happy_count = happy_count + 1

total_count = len(improved_happiness)
if happy_count >= total_count / 2:
    print(f"Score: {happy_count}/{total_count}. Employees are happy!")
else:
    print(f"Score: {happy_count}/{total_count}. Employees are not happy!")
