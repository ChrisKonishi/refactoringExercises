import time

def generate_pair_wise():
    ori = {'SP', 'RJ', 'MG', 'ES', 'BA'}
    dst = {
        "AC", "AL", "AP", "AM", "BA", "CE", "ES", "GO", "MA", "MT", "MS", 'MG',
        'PA', "PB", "PR", "PE", "PI", "RJ", "RN", "RS", "RO", "RR", "SC", "SP",
        "SE", "TO"
    }
    cat = {'A', 'B', 'C', 'D', 'E'}
 
    ori_dst = []
    ori_cat = []
    dst_cat = []
 
    for o in ori:
        for d in dst:
            if o != d:
                ori_dst.append((o,d))
            for c in cat:
                ori_cat.append((o,c))
                dst_cat.append((d,c))
 
    test = []
 
    for o in ori:
        for d in dst:   
            for c in cat:
                if  ((o, d) not in list(map(lambda x: (x[0], x[1]), test))) and ((o, c) not in list(map(lambda x: (x[0], x[2]), test))) and ((d, c) not in list(map(lambda x: (x[1], x[2]), test))) and o !=d:
                    test.append((o,d,c))
 
    print(test)
    print(len(test))

generate_pair_wise()