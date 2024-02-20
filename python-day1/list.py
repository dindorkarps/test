 
# array in c 
def function1():
    numbers=[1,2,3,4,5,6,7]
    print(f"type of numbers={type(numbers)}")
    print(f"numbers={numbers}")

    for n in numbers:
        print(f"n={n}")

    cities=["pune", "mumbai", "solapur"]
    print(f"cities={cities} ")
    print(f"type of cities={type(cities)}")

    list=[1,22.3,"pune",True,22,666]
    print(f"list={list}")

#function1()

arr=[1,2,3,4,5,6,7,8,9,10]

print(f"type of arr={type(arr)}")
print(f"arr={arr}")

print(f"length /count of arr={len(arr)}")

arr.append(11)
print(f"arr={arr}")

arr.insert(5,55)
print(f"arr={arr}")

arr.extend([22,33,44])
print(f"arr={arr}")

arr.pop()
print(f"arr={arr}")

arr.pop(5)
print(f"arr={arr}")

print(f"value at 6th location={arr[6]}")
print(f"value at 0th location={arr[0]}")
print(f"value at 11th location={arr[11]}")