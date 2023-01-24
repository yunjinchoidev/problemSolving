def solution(survey, choices):
    answer = ''
    re = {'R':0, 'T':0, 'C':0, 'F':0,
         'J':0, 'M':0, 'A':0, 'N':0}

    for i in range(len(choices)):
        if choices[i] <= 3:
            re[list(survey[i])[0]] += 4-choices[i]
        elif choices[i] == 4:
            continue
        else:
            re[list(survey[i])[1]] += choices[i] -4
    print(re)
    answer+= 'R' if re['R'] >= re['T'] else 'T'
    answer+= 'C' if re['C'] >= re['F'] else 'F'
    answer+= 'J' if re['J'] >= re['M'] else 'M'
    answer+= 'A' if re['A'] >= re['N'] else 'N'


    return answer