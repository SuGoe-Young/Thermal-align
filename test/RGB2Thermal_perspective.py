import cv2
import os
import numpy as np

# Homography 計算函數
def find_homography():
    pts_RGB = np.array([[869, 415], [1018, 407], [1025, 577], [877, 587]])
    pts_Thermal = np.array([[137, 100], [371, 94], [377, 367], [143, 371]])
    # 確保從 RGB 到 thermal 的映射
    h, status = cv2.findHomography(pts_RGB, pts_Thermal)
    return h

# 取得 Homography matrix
h = find_homography()

# 確保使用正確的路徑格式
RGB_images = os.listdir(r'..\RGB')
T_images = os.listdir(r'..\TRM')

# 檢查兩個目錄中的圖像數量是否相同
if len(RGB_images) != len(T_images):
    print("RGB 和 Thermal 目錄中的圖像數量不一致，請檢查資料夾內容")
    exit(1)

for i, rgb_image in enumerate(RGB_images):
    # 讀取照片
    RGB_frame = cv2.imread(os.path.join(r'..\RGB', rgb_image))
    T_frame = cv2.imread(os.path.join(r'..\TRM', T_images[i]))
    print(f"Processing {rgb_image} and {T_images[i]}")
    
    if RGB_frame is None or T_frame is None:
        print('No image data')
        continue
    
    # 使用原始尺寸進行處理，對 RGB_frame 應用 Homography 變換
    transformed_RGB = cv2.warpPerspective(RGB_frame, h, (T_frame.shape[1], T_frame.shape[0]))

    cv2.imshow('Transformed RGB', transformed_RGB)
    cv2.imshow('Thermal', T_frame)
    
    # 儲存變換後的 RGB 圖像
    output_filename = f'Transformed_RGB_{os.path.splitext(rgb_image)[0]}.jpg'
    cv2.imwrite(output_filename, transformed_RGB)
    print(f"Saved {output_filename}")

    # 按 'q' 鍵退出
    if cv2.waitKey(0) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
