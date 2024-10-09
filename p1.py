# Get destination and number of trolleys
N, M = map(int, input().split())

# Make list for dynamic programming (saving the number of ways to board a trolley)
trolleys_Dp = {}
  
''' Get trolleys and create trolley list '''
def getTrolleys(trolleys):
  for i in range(M):
    (origin, destination) = map(int, input().split())
    trolleys.append((origin,destination))
  return trolleys 

''' We want to count in how many ways i can board a trolley '''
def countBoardTrolleys(trolleys_Dp, trolleys, final_trolleys):
  for i in range(len(trolleys)):
    origin = trolleys[i][0]
    destination = trolleys[i][1]
    # if trolley is at origin, add 1 to number of ways to board it
    if origin == 0:
      trolleys_Dp[i] = [destination,origin,1]
    else:
      trolleys_Dp[i] = [destination,origin,0]
    # if trolley is at destination, add number of ways to board it to final answer
    if len(trolleys_Dp) > 1:
      j = i
      new_sum = 0
      while destination == trolleys_Dp[j-1][0] and j > 0:
        j -= 1
      while trolleys_Dp[j-1][0] >= origin:
        new_sum = (trolleys_Dp[j-1][2] + trolleys_Dp[i][2])%(10**9+9)
        trolleys_Dp[i] = [destination,origin,new_sum]
        if j == 1:
          break
        j -= 1
    
    if trolleys[i][1] == N:
      final_trolleys = (trolleys_Dp[i][2] + final_trolleys)%(10**9+9)
  return final_trolleys
    
trolleys = getTrolleys([])
# Sort list by destination
trolleys.sort(key=lambda tup: tup[1])
ans = countBoardTrolleys(trolleys_Dp, trolleys, 0)
print(ans)