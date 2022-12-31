###Extracting rbg values from a picture
import colorgram

rgb_colors = []
colors = colorgram.extract('Day_18\project\download.jpg',30)
for color in colors:
    r=color.rgb.r
    g=color.rgb.g
    b=color.rgb.b
    new_color = (r,g,b)
    rgb_colors.append(new_color)

print(rgb_colors)