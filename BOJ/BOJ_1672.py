# Baekjoon Online Judge - 1672번. DNA 해독


dna_list = {
    'AG': 'C', 'AC': 'A', 'AT': 'G',
    'GA': 'C', 'GC': 'T', 'GT': 'A',
    'CA': 'A', 'CG': 'T', 'CT': 'G',
    'TA': 'G', 'TG': 'A', 'TC': 'G'
}

N = int(input())
sequence = list(input())
f = ''
s = sequence.pop()
# 뒤에서부터 두개씩 끊어서 체크
for _ in range(N - 1):
    f = sequence.pop()
    result = f + s
    if result in dna_list:
        s = dna_list[result]
print(s)
