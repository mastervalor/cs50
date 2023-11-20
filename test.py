

start = int(input("start: "))
end = int(input("end: "))

years = 0

while start < end:
    start +=  start/12
    print(start)
    years += 1
    
    
print(f"{years} years")