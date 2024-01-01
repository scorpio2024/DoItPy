a = int(input("숫자a를 입력하세요: "))
b = int(input("숫자b를 입력하세요: "))


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def div(a, b):
    return a / b


def mul(a, b):
    return a * b


result_add = add(a, b)
result_sub = sub(a, b)
result_div = div(a, b)
result_mul = mul(a, b)

print(f"{a},{b}의 합은 {result_add}입니다.")
print(f"{a},{b}의 차은 {result_sub}입니다.")
print(f"{a},{b}의 나누기은 {result_div}입니다.")
print(f"{a},{b}의 곱은 {result_mul}입니다.")
