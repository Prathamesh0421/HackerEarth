test_cases = int(input())
 
for i in range(test_cases):
    
    green_balloon_cost,blue_balloon_cost = map(int,input().split())
    participants = int(input())
    total_cost = 0
    for num in range(participants):
        ans1,ans2 = map(int,input().split())
        
        if i%2 == 0:
            total_cost = total_cost + ans1*green_balloon_cost + ans2*blue_balloon_cost
        else:
            total_cost = total_cost + ans1*blue_balloon_cost + ans2*green_balloon_cost
 
 
    print(total_cost)
