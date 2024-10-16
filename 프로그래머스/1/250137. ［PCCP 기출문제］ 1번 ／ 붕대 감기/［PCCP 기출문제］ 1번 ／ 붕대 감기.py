def solution(bandage, health, attacks):
    answer = 0
    time = 0
    max_time = attacks[-1][0]
    band_time = 0
    max_health = health
    max_band_time, add_health, extra_health = bandage
    while time < max_time:
        time += 1
        if attacks and attacks[0][0] == time:
            at, attack = attacks.pop(0)
            health -= attack
            if health <= 0:
                answer = -1
                break
            band_time = 0
            # print('attack', time, health)
            continue
        band_time += 1
        health += add_health
        if band_time == max_band_time:
            health += extra_health
            band_time = 0
        if health > max_health:
            health = max_health
    #     print('add', time, health)
    # print('finish', time, health)
    if health > 0:
        answer = health
    return answer