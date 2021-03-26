# 정렬

import json


def solution(arr, q):
    parents = set()
    arr = json.loads(arr)
    for a in arr:
        parents.add(int(a.split()[2]))
    leaves = [a for a in arr if int(a.split()[0]) not in parents]
    idxs = [a.split()[1] for a in leaves]
    has_answer = False
    answers = list()
    for leaf in leaves:
        if q in leaf:
            has_answer = True
            # print(q, leaf)
            ans = leaf.split()[1]
            sib = leaf
            while True:
                p = int(sib.split()[2]) - 1
                if p > -1:
                    ans = arr[p].split()[1] + '/' + ans
                    sib = arr[p]
                    # print(ans)
                else:
                    break
            answers.append(ans)
    if not has_answer:
        print(f"Your search for {q} didn't return any results")
    else:
        print(sorted(answers, key=lambda a: (
            -1 if a.split('/')[-1] == q else 1,
            -a.split('/')[-1].count(q),
            [a.split('/')[-1].replace(q, ' ' * len(q), i).index(q) for i in range(a.split('/')[-1].count(q))],
            idxs.index(a.split('/')[-1]),
        )))
        test = list()
        print(answers)
        for a in answers:
            test.append(
                [a.split('/')[-1].replace(q, ' ' * len(q), i).index(q) for i in range(a.split('/')[-1].count(q))])
        print(test)
        print(sorted(test))


def test():
    print('aaaa'.index('aa'))
    solution(
        '["1 BROWN 0", "2 CONY 0", "3 DOLL 1", "4 DOLL 2", "5 LARGE-BROWN 3", "6 SMALL-BROWN 3", "7 BLACK-CONY 4", "8 BROWN-CONY 4"]',
        "BROWN")
    solution(
        '["1 BROWN 0", "2 CONY 0", "3 DOLL 1", "4 DOLL 2", "5 LARGE-BROWN 3", "6 SMALL-BROWN 3", "7 BLACK-CONY 4", "8 BROWN-CONY 4"]',
        "SALLY")
    solution(
        '["1 ROOTA 0", "2 AA 1", "3 ZZZ 1", "4 AABAA 1", "5 AAAAA 1", "6 AAAA 1", "7 BAAAAAAA 1", "8 BBAA 1", "9 CAA 1", "10 ROOTB 0", "11 AA 10"]',
        "AA")
    ans1 = ["CONY/DOLL/BROWN-CONY", "BROWN/DOLL/LARGE-BROWN", "BROWN/DOLL/SMALL-BROWN"]
    ans2 = ["Your search for (SALLY) didn't return any results"]
    ans3 = ["ROOTA/AA", "ROOTB/AA", "ROOTA/BAAAAAAA", "ROOTA/AAAAA", "ROOTA/AAAA", "ROOTA/AABAA", "ROOTA/CAA",
            "ROOTA/BBAA"]


if __name__ == '__main__':
    test()
