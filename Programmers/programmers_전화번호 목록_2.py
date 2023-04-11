def solution(phone_book):
    hash_map = {}
    for num in phone_book:
        hash_map[num] = 1
    for phone_number in phone_book:
        num = ''
        for n in phone_number:
            num += n
            if num in hash_map and num != phone_number:
                return False
    return True