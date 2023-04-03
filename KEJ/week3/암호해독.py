def solution(cipher, code):
    return ''.join(v for i, v in enumerate(cipher) if (i+1) % code == 0)
