# score = [5, 4, 3, 2, 1] 
score = [10, 3, 8, 9, 4]

# temp = 0
# result = str(score)
# def relative_ranks(score):
#     while score:
#         maxItem = max(score)
#         if temp < maxItem:
#             result.replace(str(maxItem), 'Gold Medal')
        

    
# print(relative_ranks(score))

def relative_ranks(scores):
    sorted_scores = sorted(scores, reverse = True) # sorting
    medals = ["Gold Medal", "Silver Medal", "Bronze Medal"] # medals array
    
    rank_dict = {sorted_scores[i] : medals[i] for i in range(len(sorted_scores))} # key value pair for the first 3 ranks 
    rank_dict.update({sorted_scores[i] : str(i+1) for i in range(len(medals), len(sorted_scores))})  # for the next ranks after 3
    
    return [rank_dict[score] for score in scores]   #returning the value for the respective score in the list


scores = [1]
print(relative_ranks(scores))
    
    