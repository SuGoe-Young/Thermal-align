# import cv2
# import numpy as np

# # 開啟 RGB 和熱影像攝像頭
# cap_rgb = cv2.VideoCapture(0, cv2.CAP_DSHOW)  
# cap_thermal = cv2.VideoCapture(1, cv2.CAP_DSHOW)


# cap_rgb.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
# cap_rgb.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
# cap_thermal.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
# cap_thermal.set(cv2.CAP_PROP_FRAME_HEIGHT, 512)


# def find_homography():
#     pts_RGB = np.array([(826, 491), (856, 508), (943, 479), (1094, 470), (974, 512), (976, 589), (858, 580)])
#     pts_Thermal = np.array([(60, 241), (103, 265), (247, 218), (492, 209), (293, 275), (295, 393), (110, 387)])
#     h, status = cv2.findHomography(pts_Thermal, pts_RGB)
#     return h


# h = find_homography()

# while True:

#     ret_rgb, frame_rgb = cap_rgb.read()
#     ret_thermal, frame_thermal = cap_thermal.read()


#     if not ret_rgb or not ret_thermal:
#         print("Failed to grab frames")
#         break

#     transformed_thermal = cv2.warpPerspective(frame_thermal, h, (frame_rgb.shape[1], frame_rgb.shape[0]))

#     thermal_colored = cv2.applyColorMap(transformed_thermal, cv2.COLORMAP_JET)


#     alpha = 0.6  
#     beta = 0.4  
#     gamma = 0
#     fusion_img = cv2.addWeighted(frame_rgb, alpha, thermal_colored, beta, gamma)


#     # cv2.imshow('RGB Camera', frame_rgb)
#     # cv2.imshow('Thermal Camera (Colored)', thermal_colored)
#     cv2.imshow('Fusion Image', fusion_img)

  
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break


# cap_rgb.release()
# cap_thermal.release()
# cv2.destroyAllWindows()
import cv2
import numpy as np

# Open RGB and thermal cameras
cap_rgb = cv2.VideoCapture(0, cv2.CAP_DSHOW)  
cap_thermal = cv2.VideoCapture(1, cv2.CAP_DSHOW)

# Set camera properties
cap_rgb.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
cap_rgb.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
cap_thermal.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap_thermal.set(cv2.CAP_PROP_FRAME_HEIGHT, 512)

def find_homography():
    pts_RGB = np.array([(826, 491), (856, 508), (943, 479), (1094, 470), (974, 512), (976, 589), (858, 580)])
    pts_Thermal = np.array([(60, 241), (103, 265), (247, 218), (492, 209), (293, 275), (295, 393), (110, 387)])
    h, status = cv2.findHomography(pts_Thermal, pts_RGB)
    return h

# Get the homography matrix
h = find_homography()

while True:
    ret_rgb, frame_rgb = cap_rgb.read()
    ret_thermal, frame_thermal = cap_thermal.read()

    if not ret_rgb or not ret_thermal:
        print("Failed to grab frames")
        break


    transformed_thermal = cv2.warpPerspective(frame_thermal, h, (frame_rgb.shape[1], frame_rgb.shape[0]))


    thermal_colored = cv2.applyColorMap(transformed_thermal, cv2.COLORMAP_JET)


    mask = cv2.cvtColor(transformed_thermal, cv2.COLOR_BGR2GRAY)
    _, mask = cv2.threshold(mask, 1, 255, cv2.THRESH_BINARY)


    mask_inv = cv2.bitwise_not(mask)

 
    rgb_only = cv2.bitwise_and(frame_rgb, frame_rgb, mask=mask_inv)

    thermal_only = cv2.bitwise_and(thermal_colored, thermal_colored, mask=mask)

    fusion_img = cv2.add(rgb_only, thermal_only)

    cv2.imshow('Fusion Image', fusion_img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap_rgb.release()
cap_thermal.release()
cv2.destroyAllWindows()
