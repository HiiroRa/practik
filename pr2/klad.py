stepresult = 0
rosaresult = 'север'
x1 = 0
y1 = 0
x = int(input())
y = int (input())
naprav = input ()
while naprav != 'стоп' :
    if x == x1 and y == y1:
            if naprav == 'вперед':
                stepresult == stepresult
                step = int (input())
            elif naprav == 'направо' or naprav == 'налево' or naprav == 'разворот':
                rosaresult == rosaresult
            elif naprav == 'стоп':
                break
            naprav = input()
    else:
        stepresult += 1
        if naprav == 'вперед':
            step = int (input())
            if rosaresult == 'север':
                y1 += step
            elif rosaresult == 'восток':
                x1 += step
            elif rosaresult == 'юг':
                y1 -= step
            elif rosaresult == 'запад':
                x1 -= step
        elif naprav == 'направо':
            if rosaresult == 'север':
                rosaresult = 'восток'
            elif rosaresult == 'восток':
                rosaresult = 'юг'
            elif rosaresult == 'юг':
                rosaresult = 'запад'
            elif rosaresult == 'запад':
                rosaresult = 'север'
        elif naprav == 'налево':
            if rosaresult == 'север':
                rosaresult = 'запад'
            elif rosaresult == 'восток':
                rosaresult = 'север'
            elif rosaresult == 'юг':
                rosaresult = 'восток'
            elif rosaresult == 'запад':
                rosaresult = 'юг'
        elif naprav == 'разворот':
            if rosaresult == 'север':
                rosaresult = 'юг'
            elif rosaresult == 'восток':
                rosaresult = 'запад'
            elif rosaresult == 'юг':
                rosaresult = 'север'
            elif rosaresult == 'запад':
                rosaresult = 'восток'
        naprav = input()
print (stepresult)
print (rosaresult)
