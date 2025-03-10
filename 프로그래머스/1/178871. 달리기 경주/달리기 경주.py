def solution(players, callings):
    position = {player: i for i, player in enumerate(players)}
    for name in callings:
        index = position[name]
        
        players[index] = players[index-1]
        players[index-1] = name
        
        position[players[index]] = index
        position[players[index-1]] = index - 1
        
    
    return players
