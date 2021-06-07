# https://programmers.co.kr/learn/courses/30/lessons/60057
# 문자열 압축
# 2020 KAKAO BLIND RECRUITMENT


def solution(s):
    answer = len(s)
    for slide in range(1, len(s) // 2 + 1):
        tmp = len(s)
        i = 0
        while i < len(s):
            cnt = 1
            while s[i:i + slide] == s[i + slide:i + slide * 2]:
                cnt += 1
                i += slide
            if cnt > 1:
                tmp -= (cnt - 1) * slide
                tmp += len(str(cnt))
            else:
                i += slide
        answer = min(answer, tmp)
    return answer


if __name__ == '__main__':
    print(solution("a"))
    print(solution("aabbaccc"))
    print(solution("ababcdcdababcdcd"))
    print(solution("abcabcdede"))
    print(solution("abcabcabcabcdededededede"))
    print(solution("xababcdcdababcdcd"))
    print(solution("xxxxxxxxxxyyy"))
    print(solution("bbaabaaaab"))
    print(solution("zzzbbabbabba"))
"""
1 <=len(s) <=1000
s= ['a-z']
"""
