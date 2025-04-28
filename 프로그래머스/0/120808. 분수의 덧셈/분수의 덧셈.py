def solution(numer1, denom1, numer2, denom2):
    top = numer1 * denom2 + numer2 * denom1
    bottom = denom1 * denom2
    a, b = top, bottom
    if a < b:
        a, b = b, a
    while b > 0:
        a, b = b, a % b
    return [top // a, bottom // a]