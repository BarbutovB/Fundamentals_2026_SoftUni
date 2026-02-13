def loading_bar(n):
    if n == 100:
        return "100% Complete!\n[##########]"
    
    percent_count = n // 10
    dots_count = 10 - percent_count
    bar = f"{n}% [{'%' * percent_count}{'.' * dots_count}]"
    return f"{bar}\nStill loading..."

percentage = int(input())
print(loading_bar(percentage))
