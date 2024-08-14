def does_tezela_like_the_array(array):
    if len(array) == 0:
        return True
    
    for something in array:
        if type(something) == int:
            continue
        elif type(something) == float:
            if something % 1 == 0:
                continue
            else:
                return False
        else:
            return False
    return True
    



print(does_tezela_like_the_array([])) #True
print(does_tezela_like_the_array([1, 2, 3, 4])) #True
print(does_tezela_like_the_array([1.0, 2.0, 3.0])) #True
print(does_tezela_like_the_array([1.0, 2.0, 3.0001])) #False
print(does_tezela_like_the_array(["-1"])) #False