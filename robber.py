nums = [2,7,9,3,1,9]

def rob(nums_list):
    robbed = 0
   
    robbed_list1 = []
    robbed_list2 = []
    for num in nums_list[::2]:
      robbed += num
      robbed_list1.insert(robbed)

    for num in nums_list[1::2]:
      robbed += num
      robbed_list2.insert(robbed)
    
    robbed = max(robbed_list1, robbed_list2)
    print(robbed_list1)
    print(robbed_list2)
    
    return robbed
        

amount_robbed = rob(nums)
print(amount_robbed)