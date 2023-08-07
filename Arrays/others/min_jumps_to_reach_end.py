# User function Template for python3

# https://practice.geeksforgeeks.org/problems/minimum-number-of-jumps-1587115620/1


class Solution:
    def minJumps(self, arr, n):
        # code here
        if n == 0:
            return -1
        elif arr[0] == 0:
            return -1
        else:
            
            jumps = 1
            steps = arr[0]
            max_reach = arr[0]

            for i in range(1, n-1):
                # decreasing step everytime we iterate
                steps -= 1
                # maximum end we can reach
                max_reach = max(max_reach, arr[i]+i)
                
				# if max reach is smaller than current position then return
                if i >= max_reach:
                    return -1

				# if step == 0 we need to jumps and update step with more available steps
                if steps == 0:
                    jumps += 1
                    steps = max_reach - i
            return jumps


# {
 # Driver Code Starts
# Initial Template for Python 3
if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        n = int(input())
        Arr = [int(x) for x in input().split()]
        ob = Solution()
        ans = ob.minJumps(Arr, n)
        print(ans)
# } Driver Code Ends
