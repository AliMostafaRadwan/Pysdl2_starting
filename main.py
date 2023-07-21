import cv2
import sdl2
import sdl2.ext
import numpy

windowSize = (640,480)

#initialize the camera
cap = cv2.VideoCapture(1)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, windowSize[0])
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, windowSize[1])
#grab and show a first frame from the camera
_,image = cap.read()
# cv2.imshow('cv2',image)
# cv2.waitKey(0)

#initialize sdl2
sdl2.ext.init()
window = sdl2.ext.Window("sdl2", size=windowSize)
window.show()
windowSurf = sdl2.SDL_GetWindowSurface(window.window)
windowArray = sdl2.ext.pixels3d(windowSurf.contents)

while True: #keep reading to have a live feed from the cam
    _,image = cap.read()
    image = numpy.insert(image,3,255,axis=2) #add alpha
    image = numpy.rot90(image) #rotate dims
    numpy.copyto(windowArray, image)
    window.refresh()
