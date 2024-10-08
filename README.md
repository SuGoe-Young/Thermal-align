# Thermal-align
# 熱影像校準與融合專案

## 介紹
這是一個專門用來處理 RGB 相機跟熱影像相機影像校準的專案。使用 OpenCV 來計算兩個相機影像的同質性變換 (Homography)，讓熱影像可以準確對應到 RGB 影像上，並透過OpenCV來顯示熱影像在 RGB 圖像上的效果。
![image](https://github.com/user-attachments/assets/78bf2642-fe44-47b2-b893-7ca1e0c703bc)


## 功能
- **手動選取控制點 find_pts.py**：透過手動選取控制點來計算同質性變換。
- **影像融合 homography.py/realtime_homography.py**：將熱影像轉換為 JET 色彩表並疊加到 RGB 圖像上。

## 安裝方式
1. 使用 Windows OS，並且確保相機與熱影像攝影機完整安裝在基座上且系統可識別此兩台裝置。
2. 先確保你的環境有安裝 Python >= 3.7(推薦使用Anaconda)。
   ```bash
   pip install opencv-python numpy
3. Clone 此專案到你的本地環境：
   ```bash
   git clone https://github.com/SuGoe-Young/Thermal-align.git

## 使用說明
### find_pts
  ```bash
  cd find_pts
  python find_pts
  ```
1.輸入 2 使用相機進行即時拍攝，直至尋找到理想畫面。(建議尋找有明確稜角的畫面)。<br>
2.按c進行截圖，該圖片即為用作尋照對應點的圖像。<br>
3.從RGB影像開始標點。(建議5 ~ 10個點)<br>
4.按照相同的對應點(要按照順序)在熱影像上進行標點。(建議5 ~ 10個點)<br>
5.操作完畢後按下Enter，對應點結果顯示在終端機，如圖:<br>

![image](https://github.com/user-attachments/assets/d8bc9a17-31d8-4543-848e-c1c2bb5858c8)<br>
*上方為RGB下方為Thermal。

### realtime_homography_xxx2xxx.py

1.紀錄find_pts的對應點，上方為RGB下方為Thermal。<br>
2.在該片段中貼上，如圖: (圖示的點與上圖不符，僅供參考)<br>
![image](https://github.com/user-attachments/assets/0064b2bc-71e2-4725-add4-87c9cc80092e)<br>
3.運行程式。<br>
  ```bash
  cd .. # go to  root
  python realtime_homography_xxx2xxx.py
```
## 注意事項
- 相機與熱影像相機跟電腦連接有時會有問題，可以先使用read_camera進行調試。
- 校正後的圖像受對應點的影響甚大，故需仔細標點。
