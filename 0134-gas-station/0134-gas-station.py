class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        totalgas=0
        curgas=0
        start=0

        for i in range(len(gas)):
            totalgas+=gas[i]-cost[i]
            curgas+=gas[i]-cost[i]

            if(curgas<0):
                start=i+1
                curgas=0
        if(totalgas >= 0):
            return start
        else:
            return -1
            
        
        