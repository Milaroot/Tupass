from itertools import combinations, permutations


KEYWORDS_ARR = []
COMBINATIONS_ARR = []
OPT_ARR = []    

#open file here
with open("keyword.txt", "r") as key_file:             
    
    for text in key_file: 
        text = text.strip()
        KEYWORDS_ARR.append(text)
    
#upper here
tmp = []
for con in KEYWORDS_ARR:
    if con.isalpha():
        all_upp = con.upper()
        first_upp = con.capitalize()
        tmp.extend([first_upp, all_upp])
KEYWORDS_ARR.extend(tmp)

     
#combinations here
for rnd in range(1, len(KEYWORDS_ARR) + 1):
    tmp = combinations(KEYWORDS_ARR, rnd)
    COMBINATIONS_ARR.extend(tmp)


#permutations here
for com in COMBINATIONS_ARR: 
    OPT_ARR.extend(permutations(com, len(com)))


#output here
with open("result.txt", "w") as ofile:
    for opt in OPT_ARR:
        opt = "".join(list(opt))
        ofile.write(opt + "\n")
    
