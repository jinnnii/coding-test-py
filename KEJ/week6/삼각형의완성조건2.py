def solution(sides):
    answer1 = [i for i in range(abs(sides[0]-sides[1])+1, max(sides))]
    answer2 = [i for i in range(max(sides), sum(sides))]
    return len(answer1+answer2)