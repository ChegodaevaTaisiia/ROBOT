import numpy as np
import cv2
  
webcam = cv2.VideoCapture(0)
  
while(1):
    _, imageFrame = webcam.read()
  
   
    hsvFrame = cv2.cvtColor(imageFrame, cv2.COLOR_BGR2HSV)
  
   
    oranje_lower = np.array((0, 66, 255), np.uint8)
    oranje_upper = np.array((90, 235, 255), np.uint8)
    oranje_mask = cv2.inRange(hsvFrame, oranje_lower, oranje_upper)
    
   
    red_lower = np.array([136, 87, 111], np.uint8)
    red_upper = np.array([180, 255, 255], np.uint8)
    red_mask = cv2.inRange(hsvFrame, red_lower, red_upper)
    
    green_lower = np.array([25, 52, 72], np.uint8)
    green_upper = np.array([102, 255, 255], np.uint8)
    green_mask = cv2.inRange(hsvFrame, green_lower, green_upper)
  
    
    blue_lower = np.array([92, 9, 30], np.uint8)
    blue_upper = np.array([119, 6, 72], np.uint8)
    blue_mask = cv2.inRange(hsvFrame, blue_lower, blue_upper)
      
    
    kernal = np.ones((5, 5), "uint8")
    
    
    res_oranje = cv2.bitwise_and(imageFrame, imageFrame, 
                              mask = oranje_mask)
   
    res_red = cv2.bitwise_and(imageFrame, imageFrame, 
                              mask = red_mask)
      
   
    res_green = cv2.bitwise_and(imageFrame, imageFrame,
                                mask = green_mask)
      
   
    res_blue = cv2.bitwise_and(imageFrame, imageFrame,
                               mask = blue_mask)
    
 
    contours, hierarchy = cv2.findContours(oranje_mask,
                                           cv2.RETR_TREE,
                                           cv2.CHAIN_APPROX_SIMPLE)
      
    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if(area > 300):
            x, y, w, h = cv2.boundingRect(contour)
            imageFrame = cv2.rectangle(imageFrame, (x, y), 
                                       (x + w, y + h), 
                                       (165, 0, 255), 2)
              
            cv2.putText(imageFrame, "oranje Colour", (x, y),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.0,
                        (30, 154, 227))    
   
   
    contours, hierarchy = cv2.findContours(red_mask,
                                           cv2.RETR_TREE,
                                           cv2.CHAIN_APPROX_SIMPLE)
      
    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if(area > 300):
            x, y, w, h = cv2.boundingRect(contour)
            imageFrame = cv2.rectangle(imageFrame, (x, y), 
                                       (x + w, y + h), 
                                       (0, 0, 255), 2)
              
            cv2.putText(imageFrame, "Red Colour", (x, y),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.0,
                        (0, 0, 255))    
  
   
    contours, hierarchy = cv2.findContours(green_mask,
                                           cv2.RETR_TREE,
                                           cv2.CHAIN_APPROX_SIMPLE)
      
    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if(area > 300):
            x, y, w, h = cv2.boundingRect(contour)
            imageFrame = cv2.rectangle(imageFrame, (x, y), 
                                       (x + w, y + h),
                                       (0, 255, 0), 2)
              
            cv2.putText(imageFrame, "Green Colour", (x, y),
                        cv2.FONT_HERSHEY_SIMPLEX, 
                        1.0, (0, 255, 0))
  
   
    contours, hierarchy = cv2.findContours(blue_mask,
                                           cv2.RETR_TREE,
                                           cv2.CHAIN_APPROX_SIMPLE)
    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if(area > 300):
            x, y, w, h = cv2.boundingRect(contour)
            imageFrame = cv2.rectangle(imageFrame, (x, y),
                                       (x + w, y + h),
                                       (255, 0, 0), 2)
              
            cv2.putText(imageFrame, "Purple Colour", (x, y),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        1.0, (255, 0, 0))
              
  
    cv2.imshow("Color Detection", imageFrame)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        cap.release()
        cv2.destroyAllWindows()
        break