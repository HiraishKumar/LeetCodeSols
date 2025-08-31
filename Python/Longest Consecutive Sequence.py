nums =[9,1,4,7,3,-1,0,5,8,-1,6]
def longestConsecutive( nums: list[int]) -> int:
    Nums=list(map(str,list(sorted(set(nums)))))
    num_index={}
    longest,start=0,0
    for end in range(len(Nums)):
        num=Nums[end]
        num_index[num]=end
        if end!=0 and int(num)-int(Nums[end-1])!=1:
            start=num_index[num]+1
        
        longest=max(longest,(end-start+1))
    return longest

print(longestConsecutive(nums))

    # num_set=set(nums)
    # Nums_fin=sorted(list(num_set))
    # index={}
    # longest,start=0,0
    # for end in range(len(Nums_fin)): 
    #     num=Nums_fin[end]
    #     index[num]=end          
    #     if end!=0 and num-Nums_fin[end-1]!=1:
    #         start=index[num]+1
                
    #     longest=max(longest,(end-start+1))
    # return longest