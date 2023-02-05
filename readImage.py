import cv2
img=cv2.imread("butterfly.jpg")
cv2.putText(img,"RICK ASTLEY IS ALEY'S DAD!!",(20,220),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=1,color=(0,0,255))
grey=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
cv2.imshow("ALEY SMELLS!!!!",grey)
print(img)
cv2.waitKey(0)