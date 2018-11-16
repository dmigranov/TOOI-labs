import time
from datetime import datetime

#1
t = int(input())
while t > 0:
    time.sleep(t)
    print(t, "seconds passed")
    t = int(input())

print("negative value; the cycle is stopped")

#2
t_start = time.time()

sum = 0
for i in range(1000000):
    sum += i

print("Time passed:", time.time() - t_start)


#3
d = input("Введите дату своего рождения (ДД.ММ.ГГГГ): ")
t = datetime.strptime(d, '%d.%m.%Y')
days = datetime.today()
print("Разница:", (days-t).days, "дней")
