#stack
#이것이 코딩테스트다 5.


#python에서 stack 이용 시 별도의 라이브러리 없이 append/pop으로 stack과 동일하게 동작
stack = []
stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()

print(stack)
print(stack[::-1])