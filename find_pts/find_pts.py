import cv2
import numpy as np

# Store control points
pts_RGB = []
pts_Thermal = []

# Define mouse callback functions
def select_points_rgb(event, x, y, flags, param):
    # print('Select points on RGB image...')
    if event == cv2.EVENT_LBUTTONDOWN:
        pts_RGB.append((x, y))
        cv2.circle(RGB_frame, (x, y), 5, (0, 255, 0), -1)
        print(pts_RGB)
        cv2.imshow("RGB", RGB_frame)

def select_points_thermal(event, x, y, flags, param):
    # print('Select points on Thermal image...')
    if event == cv2.EVENT_LBUTTONDOWN:
        pts_Thermal.append((x, y))
        cv2.circle(T_frame, (x, y), 5, (0, 0, 255), -1)
        print(pts_Thermal)
        cv2.imshow("Thermal", T_frame)

# Choose mode
print("Select mode: 1 - Load images from path, 2 - Use camera")
mode = int(input("Enter mode (1 or 2): "))

if mode == 1:
    RGB_frame = cv2.imread(r'C:\Users\young\viewsec\Thermal\RGB\thermal_camera_20240901-163452.jpg')
    T_frame = cv2.imread(r'C:\Users\young\viewsec\Thermal\TRM\visible_camera_20240901-163452.jpg')
elif mode == 2:
    cap_rgb = cv2.VideoCapture(0, cv2.CAP_DSHOW)  
    cap_thermal = cv2.VideoCapture(1, cv2.CAP_DSHOW) 
    cap_rgb.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
    cap_rgb.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
    cap_thermal.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap_thermal.set(cv2.CAP_PROP_FRAME_HEIGHT, 512)
    while True:
        ret_rgb, frame_rgb = cap_rgb.read()
        ret_thermal, frame_thermal = cap_thermal.read()

        if not ret_rgb or not ret_thermal:
            print("Failed to read frames, please check camera connections")
            break

        cv2.imshow('RGB Camera', frame_rgb)
        cv2.imshow('Thermal Camera', frame_thermal)

        key = cv2.waitKey(1) & 0xFF

        if key == ord('c'):
            RGB_frame = frame_rgb.copy()
            T_frame = frame_thermal.copy()
            cv2.imwrite('captured_rgb.jpg', RGB_frame)
            cv2.imwrite('captured_thermal.jpg', T_frame)
            print("Screenshot saved")
            break
        elif key == ord('q'):
            print("Exiting camera mode")
            cap_rgb.release()
            cap_thermal.release()
            cv2.destroyAllWindows()
            exit(0)

    cap_rgb.release()
    cap_thermal.release()
    cv2.destroyAllWindows()
else:
    print("Invalid selection, please enter 1 or 2")
    exit(0)

cv2.imshow("RGB", RGB_frame)
cv2.imshow("Thermal", T_frame)

print('Select points on RGB image...')
cv2.setMouseCallback("RGB", select_points_rgb)
print('Select points on Thermal image...')
cv2.setMouseCallback("Thermal", select_points_thermal)

cv2.waitKey(0)
cv2.destroyAllWindows()

if len(pts_RGB) != len(pts_Thermal):
    print("Number of points do not match, please select again")
else:
    print("Control points selection complete")
