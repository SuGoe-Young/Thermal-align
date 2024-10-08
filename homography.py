# #這個是可以看themal投影到圖像上（確認homo有沒有對齊）
# import cv2
# import os
# import numpy as np

# # Homography 計算函數
# def find_homography():
#     pts_RGB = np.array([[869, 415],[1018, 407],[1025, 577],[877, 587]])
#     pts_Thermal = np.array([[137,100],[371, 94],[377, 367],[143, 371]])
#     h, status = cv2.findHomography(pts_Thermal, pts_RGB)
#     return h

# # 取得 Homography matrix
# h = find_homography()

# # 確保使用絕對路徑或轉為 Windows 相容的路徑格式
# RGB_images = os.listdir(r'.\RGB')
# T_images = os.listdir(r'.\TRM')
# count = 0

# for i in RGB_images:
#     # 讀取照片
#     RGB_frame = cv2.imread(r'.\RGB\\' + i)
#     T_frame = cv2.imread(r'.\TRM\\' + T_images[count])
#     print(f"Processing {i} and {T_images[count]}")
    
#     count += 1
    
#     if RGB_frame is None or T_frame is None:
#         print('No image data')
#         continue
    
#     # 移除縮放操作，使用原始尺寸進行處理
#     im_out = cv2.warpPerspective(T_frame, h, (RGB_frame.shape[1], RGB_frame.shape[0]))
#     im_color_final = cv2.applyColorMap(im_out, cv2.COLORMAP_JET)

#     img_add_final = cv2.addWeighted(RGB_frame, 0.6, im_color_final, 0.4, 0)

#     # 顯示處理後的影像
#     cv2.imshow('RGB', RGB_frame)
#     cv2.imshow('Thermal', T_frame)
#     cv2.imshow('Fusion', img_add_final)
#     cv2.imshow('Thermal Processed', im_color_final) 
#     # 如果要保存處理後的圖片，可以使用 cv2.imwrite
#     cv2.imwrite(f'Processed_RGB_{i}', RGB_frame)
#     cv2.imwrite(f'Processed_Thermal_{T_images[count-1]}', im_out)
#     cv2.imwrite(f'Processed_Fusion_{i}', img_add_final)
    
#     # 按 'q' 鍵退出
#     if cv2.waitKey(0) & 0xFF == ord('q'):
#         break

# cv2.destroyAllWindows()

# import cv2
# import os
# import numpy as np

# # Homography 計算函數
# def find_homography():
#     pts_RGB = np.array([[869, 415],[1018, 407],[1025, 577],[877, 587]])
#     pts_Thermal = np.array([[137,100],[371, 94],[377, 367],[143, 371]])
#     # 確保從 RGB 到 thermal 的映射
#     h, status = cv2.findHomography(pts_RGB, pts_Thermal)
#     return h

# # 取得 Homography matrix
# h = find_homography()

# # 確保使用正確的路徑格式
# RGB_images = os.listdir(r'.\RGB')
# T_images = os.listdir(r'.\TRM')
# count = 0

# for i in RGB_images:
#     # 讀取照片
#     RGB_frame = cv2.imread(r'.\RGB\\' + i)
#     T_frame = cv2.imread(r'.\TRM\\' + T_images[count])
#     print(f"Processing {i} and {T_images[count]}")
    
#     count += 1
    
#     if RGB_frame is None or T_frame is None:
#         print('No image data')
#         continue
    
#     # 使用原始尺寸進行處理，對 RGB_frame 應用 Homography 變換
#     transformed_RGB = cv2.warpPerspective(RGB_frame, h, (T_frame.shape[1], T_frame.shape[0]))

#     cv2.imshow('Transformed RGB', transformed_RGB)
#     cv2.imshow('Thermal', T_frame)
    
#     # 儲存變換後的 RGB 圖像
#     cv2.imwrite(f'Transformed_RGB_{i}', transformed_RGB)
    
#     # 按 'q' 鍵退出
#     if cv2.waitKey(0) & 0xFF == ord('q'):
#         break

# cv2.destroyAllWindows()



# 疊合兩張圖像

import cv2
import numpy as np
# 在此假設 transformed_RGB 和 T_frame 已經是對齊的圖像
# 讀取照片（假設這些圖像已經被讀入）
transformed_RGB = cv2.imread('Transformed_RGB_thermal_camera_20240901-163452.jpg')
thermal_img = cv2.imread('TRM/visible_camera_20240901-163452.jpg')


# 對 thermal 圖像應用色彩映射
thermal_colored = cv2.applyColorMap(thermal_img, cv2.COLORMAP_JET)

# 使用加權融合
alpha = 0.8  # RGB 圖像的權重
beta = 0.2   # Colored thermal 圖像的權重
gamma = 0    
fusion_img = cv2.addWeighted(transformed_RGB, alpha, thermal_colored, beta, gamma)

# 顯示融合後的影像
cv2.imshow('Fusion Image', fusion_img)

# 按任意鍵退出
cv2.waitKey(0)
cv2.destroyAllWindows()