# 1. If Statements

is_female = True

if is_female:
    print("You are a female")
else:
    print("You are not a female")

# or keyword - one condition has to be true
is_male = True
is_tall = False

if is_male or is_tall:
    print("You are a male or tall or both")
else:
    print("You are neither male nor tall")

# and keyword - both conditions have to be true
is_child = True
is_short = False

if is_child and is_short:
    print("You are a short child")
else:
    print("You are either not a child or not short or both")

# else if(elif) keyword
is_man = True
is_tall = False

if is_man and is_tall:
    print("You are a tall man")
elif is_man and not(is_tall):
    print("You are short man")
elif not(is_man) and is_tall:
    print("You are not a man but are tall")
else:
    print("You are neither a man nor tall")

# If Statements & Comparisons
def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

print(max_num(3, 21, 7))

# >= Greater than or equal to
# <= Less than or equal to
# == Equal to
# != Not equal to

