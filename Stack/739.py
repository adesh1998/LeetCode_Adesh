class Solution:
    def dailyTemperatures(temperatures):
        stack=[]
        result=[0]*len(temperatures)
        for i,t in enumerate(temperatures):
            while stack and t>stack[-1][0]:
                stackTemp,stackIndex=stack.pop()
                result[stackIndex]=(i-stackIndex)
            stack.append([t,i])
        return result
    temp=[73,74,75,71,69,72,76,73]

    print(dailyTemperatures(temp))

