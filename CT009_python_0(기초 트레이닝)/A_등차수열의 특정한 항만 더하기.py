def solution(a, d, included):
    return sum(a + i * d for i, f in enumerate(included) if f)