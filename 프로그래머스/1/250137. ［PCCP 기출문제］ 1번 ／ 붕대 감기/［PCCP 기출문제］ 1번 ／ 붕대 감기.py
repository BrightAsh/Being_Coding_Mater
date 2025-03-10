def solution(bandage, health, attacks):
    tmp = 0
    hp = health
    sec_array = [attacks[i][0] for i in range(len(attacks))]

    for i,sec in enumerate(sec_array):
        if (sec - tmp - 1)//bandage[0] != 0:
            hp = hp + (sec - tmp - 1) * bandage[1] + ((sec - tmp - 1)//bandage[0]) * bandage[2]
        else:
            hp = hp + (sec - tmp - 1) * bandage[1]
        tmp = sec
        if hp > health:
            hp = health
        hp = hp - attacks[i][1]
        if hp <= 0:
            hp = -1
            break;
    return hp
