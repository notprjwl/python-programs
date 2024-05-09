# happiness of length n, 

def maxHappiness(happiness, k):
    happiness.sort(reverse=True)
    total = 0
    for i in range(k):
        maxHappiness = max(happiness[i] - i, 0)
        total += maxHappiness
        print('max_happiness is :', maxHappiness, i)
    return total
        
            
print(maxHappiness(happiness = [1,2,3], k = 2))
    