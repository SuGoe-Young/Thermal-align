import cv2
import numpy as np

cap_rgb = cv2.VideoCapture(0, cv2.CAP_DSHOW)  
cap_thermal = cv2.VideoCapture(1, cv2.CAP_DSHOW) 
cap_rgb.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
cap_rgb.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
cap_thermal.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap_thermal.set(cv2.CAP_PROP_FRAME_HEIGHT, 512)
# Homography 計算函數
def find_homography():
    pts_RGB = np.array([(854, 503), (934, 461), (982, 455), (1079, 428), (974, 489), (986, 565), (866, 574)])
    pts_Thermal = np.array([(102, 252), (237, 185), (311, 178), (473, 139), (293, 233), (316, 354), (123, 368)])
    # pts_RGB = np.array([[869, 415], [1018, 407], [1025, 577], [877, 587]])
    # pts_Thermal = np.array([[137, 100], [371, 94], [377, 367], [143, 371]])
    h, status = cv2.findHomography(pts_RGB, pts_Thermal)
    return h


h = find_homography()

while True:
    
    ret_rgb, frame_rgb = cap_rgb.read()
    ret_thermal, frame_thermal = cap_thermal.read()

    if not ret_rgb or not ret_thermal:
        print("Failed to grab frames")
        break

    
    transformed_rgb = cv2.warpPerspective(frame_rgb, h, (frame_thermal.shape[1], frame_thermal.shape[0]))

  
    thermal_colored = cv2.applyColorMap(frame_thermal, cv2.COLORMAP_JET)

   
    alpha = 0.8  
    beta = 0.2  
    gamma = 0
    fusion_img = cv2.addWeighted(transformed_rgb, alpha, thermal_colored, beta, gamma)

 
    cv2.imshow('Original RGB', frame_rgb)
    cv2.imshow('Original Thermal', thermal_colored)
    cv2.imshow('Fusion Image', fusion_img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap_rgb.release()
cap_thermal.release()
cv2.destroyAllWindows()
