epsilon = 0.0000001 # 분모가 0이 되는 현상 방지하기 위해 epsilon 사용

def perceptron(x1, x2):
    w1, w2, b = 1.0, 1.0, -1.5
    sum = x1 * w1 + x2 * w2 + b #x는 입력값, w는 가중치, b는 편향
    if sum > epsilon :
        return 1 # sum이 0보다 크면 1반환
    else :
        return 0 # sum이 0이거나 음수면 0반환

 # 퍼셉트론이 AND 소자처럼 동작하게 됨.
print(perceptron(0, 0)) # 0반환
print(perceptron(1, 0)) # 0반환
print(perceptron(0, 1)) # 0반환
print(perceptron(1, 1)) # 1반환

