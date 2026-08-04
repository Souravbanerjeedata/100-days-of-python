import colorgram
colors = colorgram.extract('image.jpg', 30)

random_color_list = []

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    random_color_list.append(new_color)

print(random_color_list)