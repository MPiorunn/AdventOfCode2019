lower = 206938
upper = 679128

matching = []
for i in range(lower, upper):
    stringed = str(i)
    tab = ''.join(sorted(stringed))
    inted = int(tab)
    if lower < inted < upper:
        for i in range(0, 10):
            doubled = str(i) + str(i)
            if doubled in tab:
                matching.append(tab)
                break

first_crit = list(set(matching))
first_crit.sort()

with_multiples = []
for crit in first_crit:
    if crit == '555789':
        print crit
    for i in range(0, 10):
        trippled = str(i) * 3
        quaded = str(i) * 4
        fifthed = str(i) * 5
        sixthed = str(i) * 6
        if sixthed in crit:
            with_multiples.append(crit)
            break
        elif fifthed in crit:
            with_multiples.append(crit)
            break
        elif quaded in crit:
            shouldAdd = False
            for j in range(0, 10):
                doubled = str(j) * 2
                if doubled in crit and i != j:
                    shouldAdd = True
                    break
            if not shouldAdd:
                with_multiples.append(crit)
            break
        elif trippled in crit:
            added = False
            for j in range(0, 10):
                tripl = str(j) * 3
                if tripl in crit and i != j:
                    with_multiples.append(crit)
                    added = True
                    break
            if not added:
                shouldAdd = False
                for j in range(0, 10):
                    doubled = str(j) * 2
                    if doubled in crit and i != j:
                        shouldAdd = True
                        break
                if not shouldAdd:
                    with_multiples.append(crit)
            # for j in range(0, 10):
            #     doubled = str(j) * 2
            #     tripl = str(j) * 3
            #     if doubled in crit and tripl in crit and i != j:
            #         shouldAdd = True
            #         break
            # if not shouldAdd:
            #     with_multiples.append(crit)
            break

result = [x for x in first_crit if x not in with_multiples]
print result
print len(result)
