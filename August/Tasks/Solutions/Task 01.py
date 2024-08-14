#East - აღმოსავლეთი
#North - ჩრდილოეთი
#South - სამხრეთი
#West - დასავლეთი

def how_long_does_it_take(directions):
    if len(directions) != 10:
        return False
    north_south = 0
    east_west = 0
    for something in directions:
        if something == 'n':
            north_south += 1
        elif something == 's':
            north_south -= 1
        elif something == 'e':
            east_west += 1
        elif something == 'w':
            east_west -= 1
    return north_south == 0 and east_west == 0



    
print(how_long_does_it_take(['w','e','w','e','w','e','w','e','w','e','w','e'])) #False
print(how_long_does_it_take(['n','s','n','s','n','s','n','s','n','s'])) #True
print(how_long_does_it_take(['n','n','n','s','n','s','n','s','n','s'])) #False
print(how_long_does_it_take(['e', 'e', 'w', 'n', 'n', 's', 'e', 'w', 'n', 's'])) #False 
print(how_long_does_it_take(['e', 'w', 'e', 'w', 'n', 's', 'n', 's', 'e', 'w'])) #True