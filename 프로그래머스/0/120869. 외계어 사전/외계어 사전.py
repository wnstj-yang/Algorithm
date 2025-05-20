def solution(spell, dic):
    spell_dict = {}
    for s in spell:
        spell_dict[s] = 1
    for word in dic:
        check_spell = dict(spell_dict)
        for s in word:
            if s in check_spell and check_spell[s] > 0:
                check_spell[s] -= 1
        if sum(check_spell.values()) == 0:
            return 1
    return 2