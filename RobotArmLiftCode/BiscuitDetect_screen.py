import cv2          #Open-cv Kütüphanesi: Bu kütüphane ile resim üzerinde işleme kare içine alma  resme yazı ekleme gibi bir çok
                    #görüntü işleme uygulamaları yapılabilir.
import numpy as np #Pythonda resim gibi matrissel işlemleri yapmak için kullanılan kütüphane


import mss #ekran fotosu almamızı sağlayan kütüphane
import mss.tools 

net = cv2.dnn.readNet("SON.weights","yolov3-tiny.cfg") # Eğittiğimiz ağı yüklüyoruz
classes = []
with open("object.names", "r") as f:        #Eğitim sınıflarımızı yüklüyoruz
    classes = [line.strip() for line in f.readlines()]
layer_names = net.getLayerNames()           #Eğitim ağımızdan verileri alıyoruz.
output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]
colors = np.random.uniform(0, 255, size=(len(classes), 1)) # Sınıfları aldığımız karelere renk verme kodu

while True:
    with mss.mss() as sct:

            # Ekran resmini anlık alıcağımız bölge
            monitor = {"top": 44, "left": 0, "width": 800, "height": 600}
                
                
             
            sct_img = sct.grab(monitor)
                
            
            
    cookie=[]
    screen =  np.array(sct_img)
    img = cv2.cvtColor(screen, cv2.COLOR_BGR2RGB)           # Aldığımız resimler ters renklerde çıkıcaktır bunu düzeltmek için
    img = np.flip(img[:, :, :3], 2)                             #rgb ye çevirip flip ederek matrisini düzenliyoruz
    img = cv2.resize(img, None, fx=0.4, fy=0.4)             #resmi bozmadan yeniden boyutlandırıyoruz.
    height, width, channels = img.shape
    
    # Obje tespiti
    blob = cv2.dnn.blobFromImage(img, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
    
    net.setInput(blob)
    outs = net.forward(output_layers)
    
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

    font = cv2.FONT_HERSHEY_PLAIN
    for i in range(len(boxes)):
        if i in indexes:
            x, y, w, h = boxes[i]
            label = str(classes[class_ids[i]])
            color = colors[0]
            cv2.rectangle(img, (x, y), (x + w, y + h), (255,0,0), 2)
            cv2.putText(img, label, (x, y + 70), font, 1, (0,255,0), 1)
            cookie.append(label)
    if len(boxes)>=1:          #Eğer bisküvi algılanırsa;
        cv2.putText(img, "Number of Biscuits="+str(len(boxes)), (0, 50), font, 1, (255,255,255), 1)
        round_c=0
        rectangle_c=0
        cocoa_c=0
        normal_c=0
        
    cv2.imshow("Biscuit Counter", img)
    if cv2.waitKey(25) & 0xFF == ord('q'): #Eğer q ya basarsanız yada çarpı tuşuna, pencereyi kapatmaya yarayan önemli bir kod
        cv2.destroyAllWindows()
        break
cv2.destroyAllWindows()