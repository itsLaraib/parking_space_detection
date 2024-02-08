import cv2 as cv
import pickle


width,height=107,48

try:
    with open('CarPark','rb') as f:
        posList=pickle.load(f)
except:
    posList=[]    

def mouseClick(events,x,y,flags,params):
    if events == cv.EVENT_LBUTTONDOWN:
        posList.append((x,y))
    elif events ==cv.EVENT_RBUTTONDOWN:
        for i,pos in enumerate(posList):
            print(x,y)
            if pos[0]<x<pos[0]+width and pos[1]<y<pos[1]+height:
                posList.pop(i)

    with open('CarPark','wb') as f:
        pickle.dump(posList,f)

while True:
    img=cv.imread('carParkImg.png')
    # print(posList)
    for pos in posList:
        x,y=pos
        cv.rectangle(img,(x,y),(x+width,y+height),(255,0,255),3)

    cv.imshow('Image',img)    
    cv.setMouseCallback("Image",mouseClick)
    if cv.waitKey(10) & 0xFF==ord('d'):
        break

cv.destroyAllWindows()


