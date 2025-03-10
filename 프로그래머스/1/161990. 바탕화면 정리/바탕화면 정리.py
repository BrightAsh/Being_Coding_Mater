def solution(wallpaper):
    x_array = []
    y_array = []
    for i, app in enumerate(wallpaper):
        x = app.find('#')
        if x != -1:
            x_array.append(x) 
            x = len(app) - 1 - app[::-1].find('#')
            x_array.append(x) 
            y_array.append(i) 
    print(x_array)
    return [min(y_array),min(x_array), max(y_array)+1, max(x_array)+1]