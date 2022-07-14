import cv2
import numpy as np



class drawingCanvas():
    def __init__(self):
        self.penrange = np.load('penrange.npy') # load HSV range
        self.cap = cv2.VideoCapture("/Users/furkanceran/Desktop/K3.mp4")         #0 means primary camera .
        self.canvas = None                      #initialize blank canvas
        #initial position on pen 
        self.x1,self.y1=0,0
        # val is used to toggle between pen and eraser mode
        self.val=1
        self.w1=0
        self.h1=0
        self.net = cv2.dnn.readNet("SON.weights","yolov3-tiny.cfg") 
        self.classes = []
        

        with open("object.names", "r") as f:        #Eğitim sınıflarımızı yüklüyoruz
            self.classes = [line.strip() for line in f.readlines()]
        self.layer_names = self.net.getLayerNames()           #Eğitim ağımızdan verileri alıyoruz.
        self.output_layers = [self.layer_names[i[0] - 1] for i in self.net.getUnconnectedOutLayers()]
        self.colors = np.random.uniform(0, 255, size=(len(self.classes), 1)) # Sınıfları aldığımız karelere renk verme kodu
        self.area=0
        self.x2=0
        self.y2=0
        self.h2=0
        self.w2=0
        self.draw()   
 
            
    def draw(self):
        
        while True:
            _, self.frame = self.cap.read()       #read new frame
            #self.frame = cv2.flip( self.frame, 1 ) #flip horizontally
            self.frame = cv2.resize(self.frame,(1000,600))

    
            if self.canvas is None:
                self.canvas = np.zeros_like(self.frame) #initialize a black canvas
            
            mask=self.CreateMask()             #createmask
            contours=self.ContourDetect(mask)  #detect Contours
            self.drawLine(contours)            #draw lines
            ret, sct_img = self.cap.read()
        
            height, width, channels = self.frame.shape
            
            # Obje tespiti
            blob = cv2.dnn.blobFromImage(self.frame, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
            
            self.net.setInput(blob)
            outs = self.net.forward(self.output_layers)
            
            # Ekranda bilgi gösterdiğimiz kısım
            class_ids = []
            confidences = []
            boxes = []
            for out in outs:
                for detection in out:
                    scores = detection[5:]
                    class_id = np.argmax(scores)
                    confidence = scores[class_id]
                    if confidence > 0.5:
                        # Obje algılanırsa çalışacak blok
                        center_x = int(detection[0] * width)
                        center_y = int(detection[1] * height)
                        w = int(detection[2] * width)
                        h = int(detection[3] * height)
            
                        # Aldığımız karenin ölçütleri
                        x = int(center_x - w / 2)
                        y = int(center_y - h / 2)
            
                        boxes.append([x, y, w, h])
                        confidences.append(float(confidence))
                        class_ids.append(class_id)
            
            indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)
            self.area=0
            font = cv2.FONT_HERSHEY_PLAIN
            for i in range(len(boxes)):
                if i in indexes:
                    x, y, w, h = boxes[i]
                    label = str(self.classes[class_ids[i]])
                    color = self.colors[0]
                    #cv2.rectangle(self.frame, (x, y), (x + w, y + h), (255,0,255), 2)
                    #cv2.putText(self.frame, label, (x, y + 70), font, 1, (0,255,0), 1)
                    self.x2=x
                    self.y2=y
                    self.h2=h
                    self.w2=w
            self.carpisma()
            cv2.putText(self.frame, "Yolo Koordinatlari = x:"+str(self.x2)+",y:"+str(self.y2) , (0,20), font, 2, (255,255,255), 2)
            cv2.putText(self.frame, "En:"+str(self.w2)+",Boy:"+str(self.h2) , (0,50), font, 2, (255,255,255), 2)
            cv2.putText(self.frame, "Opencv Koordinatlari="+"x:"+str(self.x1)+"y:"+str(self.y1), (0,height-20), font, 2, (255,255,255), 2)
            if self.area>0:
                
                cv2.putText(self.frame, "Kesisim karesi", (self.x1,self.y1), font, 2, (255,0,255), 2)
                if self.x2<self.x1:
                    x=self.x2
                else:
                    x=self.x1
                if self.y2<self.y1:
                    y=self.y2
                else:
                    y=self.y1
                if self.w2<self.w1:
                    w=self.w2
                else:
                    w=self.w1
                cv2.rectangle(self.frame, (x, y), (x + w, y + h), (255,120,255), 2)

            self.display()                     #display results
            k = cv2.waitKey(1) & 0xFF          #wait for keyboard input
            self.takeAction(k)                 #take action based on k value
        
            if k == 27:                        #if esc key is pressed exit
                break   

    def CreateMask(self):
        hsv = cv2.cvtColor(self.frame, cv2.COLOR_BGR2HSV) #convert from BGR to HSV color range
        lower_range = self.penrange[0]                    #load  HSV lower range
        upper_range = self.penrange[1]                    #load  HSV upper range
        mask = cv2.inRange(hsv, lower_range, upper_range) #Create binary mask
        return mask
   
    def ContourDetect(self,mask):
        # Find Contours based on the mask created.
        contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        return contours

    def drawLine(self,contours):
        #if contour area is not none and is greater than 100 draw the line
        if contours and cv2.contourArea(max(contours, key = cv2.contourArea)) > 50:  #100 is required min contour area              
            c = max(contours, key = cv2.contourArea)    
            x2,y2,w,h = cv2.boundingRect(c)
            self.w1=w
            self.h1=h
            if self.x1 == 0 and self.y1 == 0:    #this will we true only for the first time marker is detected
                self.x1,self.y1= x2,y2
            #else:
                # Draw the line on the canvas
                #self.canvas = cv2.line(self.canvas, (self.x1,self.y1),(x2,y2), [255*self.val,0,0], 5)
                #cv2.rectangle(self.frame, (self.x1, self.y1), (self.x1 + w, self.y1 + h), (255,255,0), 2)

            #New point becomes the previous point 
            self.x1,self.y1= x2,y2
            
        else:
            # If there were no contours detected then make x1,y1 = 0 (reset)
            self.x1,self.y1 =0,0   

    def display(self):
        # Merge the canvas and the frame.
        #self.frame = cv2.add(self.frame,self.canvas)    
        cv2.imshow('Robotarm',self.frame)
        #cv2.imshow('canvas',self.canvas)

    def takeAction(self,k):
            # When c is pressed clear the entire canvas
            if k == ord('c'):
                self.canvas = None
            #press e to change between eraser mode and writing mode
            if k==ord('e'):
                self.val= int(not self.val) # toggle val value between 0 and 1 to change marker color.
    def carpisma(self):

        x1 = self.x1
        y1 = self.y1
        width1 = self.w1
        height1 = self.h1

        x2 = self.x2
        y2 = self.y2
        width2 = self.w2
        height2 = self.h2

        endx = max(x1+width1,x2+width2)
        startx = min(x1,x2)
        width = width1+width2-(endx-startx)

        endy = max(y1+height1,y2+height2)
        starty = min(y1,y2)
        height = height1+height2-(endy-starty)

        if width <=0 or height <= 0:
            ratio = 0
            self.area=0
            #print("AREA",self.area)
        else:
            Area = width*height # two box cross  
            Area1 = width1*height1
            Area2 = width2*height2
            ratio = Area*1./(Area1+Area2-Area)
            self.area=Area
            #print("AREA",Area)
if __name__ == '__main__':
    drawingCanvas()
     
cv2.destroyAllWindows()