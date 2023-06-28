from itertools import combinations, permutations

#This function can add keywords that are in all uppercase and with the first letter capitalized.
def upper_keywords(KEYWORDS_ARR: list) -> list:
    tmp_arr = []
    for con in KEYWORDS_ARR:
        if con.isalpha():
            all_upp = con.upper()
            first_upp = con.capitalize()
            tmp_arr.extend([first_upp, all_upp])
    KEYWORDS_ARR.extend(tmp_arr)
    return KEYWORDS_ARR



#This function will generate all possible combinations of keywords.
def combinations_keywords(KEYWORDS_ARR: list) -> list:
    combinations_arr = []
    for rnd in range(1, len(KEYWORDS_ARR) + 1):
        tmp = combinations(KEYWORDS_ARR, rnd)
        combinations_arr.extend(tmp)
    return combinations_arr



#This function will generate all possible permutations of keywords. 
def permutations_keywords(combinations_arr: list) -> list:
    opt_arr = []
    for com in combinations_arr: 
        opt_arr.extend(permutations(com, len(com)))
    return opt_arr
