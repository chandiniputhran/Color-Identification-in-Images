import pandas as pd
import cv2


img_path = 'pic1.jpg'
csv_path = 'colors.csv'

index = ['color', 'colorname', 'hex', 'R', 'G', 'B']
df = pd.read_csv(csv_path,names=index,header=None)

img = cv2.imread(img_path)
img = cv2.resize(img, (800, 600))

clicked = False
r = g = b = xpos = ypos = 0

def get_color_name(R, G, B):
    minimum = 1000;
    for i in range(len(df)):
        d=

def draw_function(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        global clicked, r, g, b, xpos, ypos
        xpos = x
        ypos=y
        b, g, r = img[y, x]
        b = int(b)
        g = int(g)
        r = int(r)
        
cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_function)

print(clicked,r,g,b,xpos,ypos)
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllwindows()




