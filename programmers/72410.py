# https://programmers.co.kr/learn/courses/30/lessons/72410
# title : 신규 아이디 추천

def solution(new_id):
    answer = ''
    # 1
    new_id = new_id.lower()
    # 2
    if new_id:
        available = {'-', '_', '.'}
        for c in new_id:
            if c.isalnum() or c in available:
                answer += c
        # 3
        while '..' in answer:
            answer = answer.replace('..', '.')
        # 4
        if answer == '.':
            answer = ''
        if answer:
            if answer[0] == '.':
                answer = answer[1:]
            if answer[-1] == '.':
                answer = answer[:-1]
    # 5
    if answer == '':
        answer = 'a'
    # 6
    if len(answer) >= 16:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1]
    # 7
    while len(answer) <= 2:
        answer += answer[-1]

    return answer


if __name__ == '__main__':
    print(solution("...!@BaT#*..y.abcdefghijklm"))
    print(solution("=.="))
    print(solution("123_.def"))
    print(solution("abcdefghijklmn.p"))

"""
3<= len(new_id) <=15
[a-z,0-9,-,_,.]
. 시작, 끝, 연속 불가
1. upper to low case
2. delete other characters
3. .. -> .
4. . 처음 or 끝? 제거
5. empty string -> a
6. len(new_id) >= 16 ? new_id = new_id[:15], last char == . ? delete
7. len(new_id <= 2) repeat new_id[:-1] until len(new_id) == 3
"""
