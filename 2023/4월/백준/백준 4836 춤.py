while True:
    try:
        dances = input().split()
        is_normal = False
        for i in range(len(dances)):
            if dances[i] == 'dip':
                if i != 0:
                    if dances[i-1] == 'jiggle':
                        is_normal = True
                        continue
                if i > 1:
                    if dances[i-2] == 'jiggle':
                        is_normal = True
                        continue

        dances[-1] = 'clap'
        dances[-2] = 'stomp'
        dances[-3] = 'clap'

        for i in range(len(dances)-1):
            if dances[i] == 'twirl':
                if dances[i+1] != 'hop':
                    is_normal = False
                    break


        if dances[0] != 'jiggle':
            is_normal = False

        if dances.count('dip') == 0:




    except:
        break