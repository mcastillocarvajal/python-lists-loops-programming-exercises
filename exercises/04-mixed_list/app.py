mix = [42, True, "towel", [2,1], 'hello', 34.4, {"name": "juan"}]

# Your code below:

def func(arr):
    for i in range(len(arr)):
        print(type(arr[i]))

func(mix)
