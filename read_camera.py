import cv2
import time

cap_visible = cv2.VideoCapture(0, cv2.CAP_DSHOW)
# cap_thermal = cv2.VideoCapture(2, )
cap_thermal = cv2.VideoCapture(1, cv2.CAP_DSHOW)
cap_visible.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
cap_visible.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
cap_thermal.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap_thermal.set(cv2.CAP_PROP_FRAME_HEIGHT, 512)

print('rgb size : (', cap_visible.get(cv2.CAP_PROP_FRAME_WIDTH), cap_visible.get(cv2.CAP_PROP_FRAME_HEIGHT), cap_visible.get(cv2.CAP_PROP_FPS), ')')
print('thermal size : (', cap_thermal.get(cv2.CAP_PROP_FRAME_WIDTH), cap_thermal.get(cv2.CAP_PROP_FRAME_HEIGHT), cap_thermal.get(cv2.CAP_PROP_FPS), ')')

while True:
    ret_visible, frame_visible = cap_visible.read()
    ret_thermal, frame_thermal = cap_thermal.read()

    if ret_visible:
        cv2.imshow('Visible Camera', frame_visible)
        pass
    if ret_thermal:
        cv2.imshow('Thermal Camera', frame_thermal)

    key = cv2.waitKey(1) & 0xFF

    if key == ord('r'):
        timestamp = time.strftime("%Y%m%d-%H%M%S")
        if ret_visible:
            cv2.imwrite(f'visible_camera_{timestamp}.jpg', frame_visible)
            print(f'Saved visible_camera_{timestamp}.jpg')
        if ret_thermal:
            cv2.imwrite(f'thermal_camera_{timestamp}.jpg', frame_thermal)
            print(f'Saved thermal_camera_{timestamp}.jpg')

    if key == ord('q'):
        break

cap_visible.release()
cap_thermal.release()
cv2.destroyAllWindows()
# import cv2

# # 嘗試打開相機 (索引0 或 1)
# cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)  # 嘗試 MSMF 後端或 DSHOW

# if not cap.isOpened():
#     print("Cannot open the camera.")
# else:
#     # 設置相機的格式或分辨率
#     cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
#     cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    
#     while True:
#         ret, frame = cap.read()
#         if not ret:
#             print("Failed to grab frame.")
#             break
        
#         cv2.imshow('Thermal Camera - JL-H512-271E', frame)
        
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break

# cap.release()
# cv2.destroyAllWindows()
