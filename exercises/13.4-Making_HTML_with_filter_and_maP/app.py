all_colors = [
	{"label": 'Red', "sexy": True},
	{"label": 'Pink', "sexy": False},
	{"label": 'Orange', "sexy": True},
	{"label": 'Brown', "sexy": False},
	{"label": 'Pink', "sexy": True},
	{"label": 'Violet', "sexy": True},
	{"label": 'Purple', "sexy": False},
]

#Your code go here:

def filter_colors(color):
    return color["sexy"] == True

def generate_li(list):
    new = ""
    for color in list:
        new += "<li>" + color["label"] + "</li>"
    return new 

colors = list(filter(filter_colors, all_colors))
result = generate_li(colors)

print(result)