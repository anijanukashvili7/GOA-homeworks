# 1
def litres(time):
    return int(time * 0.5)


# 2
def paperwork(n, m):
    if n < 0 or m < 0:
        return 0
    return n * m


# 3
def grow(numbers_list):
    result = 1
    
    for number in numbers_list:
        result = result * number
    
    return result

# 4
def fake_bin(x):
    result = ''
    
    for char in x:
        if int(char) < 5:
            result = result + "0"
        else:
            result = result + "1"
    
    return result

# 5

def count_by(x, n):
    
    return [i * x for i in range(1,n+1)]

# 6

def to_jaden_case(string):

    for letter in string:
        if letter == "?'" :
            letter[+1].lowercase()
        else:
            return string.title()
    return string

# 7

def remove_smallest(numbers):
    if not numbers:
        return []
    
    smallest_index = numbers.index(min(numbers))
    return numbers[:smallest_index] + numbers[smallest_index + 1:]






































































