'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    count = 0
    #base case
    if len(word) == 0 or len(word) < 2:
        return count
    elif word[0:2] =='th': 
        count +=1
        return count_th(word[1:]) +1
    else:
        return count_th(word[1:])

print(count_th('t'))
print(count_th('thisthisthis'))

  

    