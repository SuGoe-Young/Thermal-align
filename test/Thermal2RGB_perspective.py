import cv2
import os
import numpy as np

# Homography 計算函數
def find_homography():
    pts_RGB = np.array([[869, 415],[1018, 407],[1025, 577],[877, 587]])
    pts_Thermal = np.array([[137,100],[371, 94],[377, 367],[143, 371]])
    h, status = cv2.findHomography(pts_Thermal, pts_RGB)
    return h

# 取得 Homography matrix
h = find_homography()

# 確保使用絕對路徑或轉為 Windows 相容的路徑格式
RGB_images = os.listdir(r'..\RGB')
T_images = os.listdir(r'..\TRM')
count = 0

for i in RGB_images:
    # 讀取照片
    RGB_frame = cv2.imread(r'..\RGB' + i)
    T_frame = cv2.imread(r'..\TRM' + T_images[count])
    print(f"Processing {i} and {T_images[count]}")
    
    count += 1
    
    if RGB_frame is None or T_frame is None:
        print('No image data')
        continue
    
    # 移除縮放操作，使用原始尺寸進行處理
    im_out = cv2.warpPerspective(T_frame, h, (RGB_frame.shape[1], RGB_frame.shape[0]))
    im_color_final = cv2.applyColorMap(im_out, cv2.COLORMAP_JET)

    img_add_final = cv2.addWeighted(RGB_frame, 0.6, im_color_final, 0.4, 0)

    # 顯示處理後的影像
    cv2.imshow('RGB', RGB_frame)
    cv2.imshow('Thermal', T_frame)
    cv2.imshow('Fusion', img_add_final)
    cv2.imshow('Thermal Processed', im_color_final) 
    # 如果要保存處理後的圖片，可以使用 cv2.imwrite
    cv2.imwrite(f'Processed_RGB_{i}', RGB_frame)
    cv2.imwrite(f'Processed_Thermal_{T_images[count-1]}', im_out)
    cv2.imwrite(f'Processed_Fusion_{i}', img_add_final)
    
    # 按 'q' 鍵退出
    if cv2.waitKey(0) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
