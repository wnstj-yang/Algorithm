def solution(cacheSize, cities):
    answer = 0
    cache = []
    # 캐시 사이즈가 0인경우 예외처리
    if cacheSize == 0:
        return len(cities) * 5

    for city in cities:
        city = city.lower()
        if city in cache:
            answer += 1
            # 캐시에 있다면 최근에 사용한 것이므로 제거를 하고 다시 추가
            cache.remove(city)
            cache.append(city)
        else:
            # 만약 캐시 사이즈만큼 차있지 않다면 넣어줌
            # 캐시 사이즈만큼 쌓이게 되면 하나 빼고 넣어준다
            if len(cache) < cacheSize:
                cache.append(city)
            else:
                cache.pop(0)
                cache.append(city)
            answer += 5
    return answer
