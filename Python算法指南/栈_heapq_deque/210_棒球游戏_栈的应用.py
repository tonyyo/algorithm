class Solution:
    def calPoints2(self, ops):
        # Time: O(n)
        # Space: O(n)
        history = []
        for op in ops:
            if op == 'C':
                history.pop()
            elif op == 'D':
                history.append(history[-1] * 2)
            elif op == '+':
                history.append(history[-1] + history[-2])
            else:
                history.append(int(op))
        return sum(history)

    def calPoints1(self, ops):
        stack = []
        for x in ops:
            if x == "C":
                stack.pop()
            elif x == "D":
                temp = stack[-1]
                stack.append(temp * 2)
            elif x == "+":
                temp1 = stack[-2]
                temp2 = stack[-1]
                stack.append(temp1 + temp2)
            else:
                stack.append(int(x))
        return sum(stack)

    def calPoints(self, ops):
        stack = []
        for i in range(len(ops)):
            if ops[i] not in ['+', 'D', 'C']:
                stack.append(int(ops[i]))
            elif ops[i] == '+':
                if len(stack) <= 1:  # 防出界
                    return stack[-1]
                stack.append(stack[-1] + stack[-2])
            elif ops[i] == 'D':
                stack.append(stack[-1] * 2)
            else:
                stack.pop()
        return sum(stack)

# 主函数
if __name__ == "__main__":
    ops = ["5", "2", "C", "D", "+"]
    # 创建对象
    solution = Solution()
    print("初始字符串数组是：", ops)
    print("总得分数是：", solution.calPoints(ops))
