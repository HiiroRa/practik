d = int(input())
month = int(input())
year = int (input())
if month > 2:
    m = month - 2
else:
    m = 10+month
c = year // 100
y = year % 100
dayweek = (d + ((13*m - 1) // 5) + y + (y // 4 + c//4 - 2*c + 777)) % 7
print (dayweek)
