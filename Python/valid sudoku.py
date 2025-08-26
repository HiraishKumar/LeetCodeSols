import numpy as np



board=[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

    
def ValidSudoku(board):    
    # arr=np.array(board)
    # lst=[]
    # for rows in range(9):
    #     lst.append([coloumn for coloumn in arr[rows] if coloumn.isdigit()])
    # tst=np.transpose(arr)   
    # lst2=[]
    # for k in range(9):
    #     lst2.append([coloumn for coloumn in tst[k] if coloumn.isdigit()])
        
       
    # if len(list(filter(lambda x:len(x)==len(set(x)),lst)))!=len(lst): 
    #     return False
    # if len(list(filter(lambda x:len(x)==len(set(x)),lst2))) != len(lst2) :
    #     return False

    # for rows in np.array_split(arr, 3, axis=1):
    #     for coloumn in np.array_split(rows,3):
    #         flattened_list = list(chain.from_iterable(coloumn))
    #         test=[num for num in flattened_list if num.isdigit()]
    #         if len(set(test))!=len(test):
    #             return False      
    
    # else: 
    #     return True
    index = []
    for rows in range(9):
        for coloumn in range(9):
            element = board[rows][coloumn]
            if element != '.':
                index+=((rows, element), (element, coloumn), (rows // 3, coloumn // 3, element))
    return len(index) == len(set(index)) 
    # return index
    

print(np.array(ValidSudoku(board)))