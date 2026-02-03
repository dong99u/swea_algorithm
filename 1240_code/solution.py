import sys
sys.stdin = open('input.txt')

CODE_LENGTH = 56

t = int(input())

matching_code = {
    '0001101': 0,
    '0011001': 1,
    '0010011': 2,
    '0111101': 3,
    '0100011': 4,
    '0110001': 5,
    '0101111': 6,
    '0111011': 7,
    '0110111': 8,
    '0001011': 9
}

for tc in range(1, t + 1):
    n, m = map(int, input().split())

    # 암호화된 코드들을 받음.
    lst: list = [
        input()
        for _ in range(n)
    ]

    code: str = ''
    for row in lst:
        # 코드의 한 줄에 1이 존재하지 않으면 패스
        # 코드에 한 줄에 1이 존재하면 해독하고자 하는 코드가 있는 것임.
        if '1' not in row:
            continue

        # 각 숫자의 매칭되는 비트 코드는 모두 1로 끝나므로 거꾸로 찾기.
        last_1_index = row.rfind('1')

        # 해독하고자 하는 코드 가져오기.
        code = row[last_1_index - CODE_LENGTH + 1: last_1_index + 1]
        break

    odd_sum = 0
    even_sum = 0
    for idx, start_idx in enumerate(range(0, CODE_LENGTH, 7)):
        c = code[start_idx:start_idx + 7]

        if idx % 2 == 0: # 홀수일때
            odd_sum += matching_code[c]
        else:
            even_sum += matching_code[c]

    answer = 0

    if (odd_sum * 3 + even_sum) % 10 == 0:
        answer = odd_sum + even_sum

    print(f'#{tc} {answer if answer else 0}')