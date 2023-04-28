def solution(spell, dic):
    for i in dic:
        for j in spell:
            if j not in i:
                break
        else:
            return 1
    else:
        return 2
    
def _solution(spell, dic):
    spell = set(spell)
    for s in dic:
        if not spell-set(s):
            return 1
    return 2