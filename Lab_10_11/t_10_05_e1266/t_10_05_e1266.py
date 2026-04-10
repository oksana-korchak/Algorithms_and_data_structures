import sys

def max_score(weight, score, num):
    global maxScore, N, n, tracks

    if weight == N or num >= n:
        if score > maxScore:
            maxScore = score
        return

    if maxScore == N:
        return

    # Беремо трек
    if weight + tracks[num] <= N:
        max_score(weight + tracks[num], score + tracks[num], num + 1)

    # Не беремо трек
    max_score(weight, score, num + 1)


if __name__ == '__main__':

    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue

        data = [int(x) for x in line.split()]

        N = data[0]       # тривалість касети
        n = data[1]       # кількість треків
        tracks = data[2:] # тривалості треків

        maxScore = 0
        max_score(0, 0, 0)

        print(f"sum:{maxScore}")