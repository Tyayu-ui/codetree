def replace_second_chars(s):
    if len(s) < 2:
        return s  # 문자열 길이가 2 미만이면 그대로 반환

    # 앞에서 두 번째 문자와 뒤에서 두 번째 문자 'a'로 변경
    s_list = list(s)
    s_list[1] = 'a'
    s_list[-2] = 'a'

    return "".join(s_list)

# 테스트
s = input().strip()
print(replace_second_chars(s))
