import json


def solution(table, languages, preference):
    scores = list()
    rank = len(table[0].split())
    for row in table:
        row.split()[0]
        score = 0
        for i, l in enumerate(languages):
            if l in row:
                score += preference[i] * (rank - row.split().index(l))
        scores.append(score)
    candidates = [table[i].split()[0] for i in range(len(scores)) if scores[i] == max(scores)]
    return sorted(candidates)[0]


def test():
    print(solution(
        json.loads(
            '["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"]'),
        ["PYTHON", "C++", "SQL"], [7, 5, 5]))
    print(solution(json.loads(
        '["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++","HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP","GAME C++ C# JAVASCRIPT C JAVA"]'),
        ["JAVA", "JAVASCRIPT"], [7, 5]))


if __name__ == '__main__':
    test()
