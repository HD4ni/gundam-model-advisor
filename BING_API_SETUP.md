# 🔧 Bing Image Search API 配置指南

## 問題修正

你之前上傳的圖片（METAL BUILD 攻擊自由）搜尋結果不對 ❌

**原因**：Unsplash API 主要收錄攝影和藝術作品，**不適合搜尋鋼彈模型產品圖**

**解決**：改用 **Bing Image Search API** ✅
- 🎯 專門最佳化產品圖搜尋
- 📦 涵蓋官方商品型錄、零售商網站等
- 🌐 全球數十億張圖片庫

---

## ⚡ 快速設置（3 分鐘）

### Step 1: 申請 Bing Search API

1. 訪問 [Azure Marketplace](https://portal.azure.com/)
2. 搜尋 **"Bing Search"**
3. 選擇 **"Bing Image Search API"**
4. 點擊 **"Subscribe"** (免費方案)
5. 申請完成後進入 **"Resource Keys"**
6. 複製 **"Key 1"**

### Step 2: 配置 API Key

編輯 `app.py`，找到第 17 行：

```python
BING_SEARCH_KEY = "your_bing_api_key_here"  # ← 改成你複製的 Key
```

替換成：

```python
BING_SEARCH_KEY = "abc123def456ghi789xyz..."  # 粘貼你的 Key
```

### Step 3: 重啟應用

```bash
# 停止目前運行的應用（Ctrl+C）
# 然後重啟

python app.py
```

---

## 🧪 測試效果

重啟後試試提問：

```
攻擊自由鋼彈
METAL BUILD 攻擊自由
MG 沙薩比
```

### 新的搜尋行為

現在系統會根據你的推薦：

```
HG 攻擊自由鋼彈 [PRODUCT_SEARCH: HG 攻擊自由 Strike Freedom Gundam]
↓ 自動搜尋
✅ 直接顯示 Bandai 官方產品圖
✅ 顯示日本零售商的實拍照
✅ 用戶無需跳轉
```

---

## 📊 效果對比

| 方案 | 圖片質量 | 搜尋速度 | 費用 |
|------|--------|--------|------|
| Unsplash | ⭐⭐ (藝術為主) | 快 | 免費 |
| **Bing** | ⭐⭐⭐⭐⭐ (產品專用) | 中等 | 免費 (前 1000次/月) |
| Google | ⭐⭐⭐⭐ | 中等 | 需付費 |

---

## 🎓 搜尋詞最佳化

系統已改進提示詞，現在會生成這樣的標籤：

❌ 舊：`[PRODUCT_SEARCH: 攻擊自由]` 
→ 搜尋結果混雜，可能是同人圖、動畫截圖

✅ 新：`[PRODUCT_SEARCH: METAL BUILD 攻擊自由 Strike Freedom Gundam]`
→ Bing 會精準找到官方產品型錄

---

## 🆘 故障排除

### 圖片還是不對？

**可能原因 1**：API Key 無效
```bash
# 檢查 Key 是否正確複製
# 確認是 Bing Image Search（不是 Bing Web Search）
```

**可能原因 2**：搜尋詞仍不夠具體
- 模型會自動改進搜尋詞格式
- 下一次對話應該會更準確

### API 超過配額？

- Bing 免費方案：**1,000 請求/月**
- 超過後自動降級到 Google 圖片搜尋連結
- 下月恢復

### 想用其他圖片源？

編輯 `get_product_images()` 函數，改成：
- **Pixabay API** - 免費，無需信用卡
- **Pexels API** - 免費，高質量
- **Flickr API** - 社群圖片
- 本地圖片庫 - 完全自主控制

---

## 💡 高級用法

### 自訂搜尋參數

編輯 `app.py` 第 65-71 行的 `params` 設置：

```python
params = {
    "q": product_name,           # 搜尋詞
    "count": 3,                  # 圖片數量
    "imageType": "Photo",        # 只要照片（去除繪圖）
    "aspect": "Wide",            # 只要橫幅（適合展示）
    "safeSearch": "Moderate"     # 安全篩選
}
```

---

## 📝 系統提示詞改進

新版提示詞已要求 AI 生成更精確的搜尋標籤：

✅ **包含規格代碼**：HG / MG / RG / HGUC / METAL BUILD  
✅ **包含中英文名稱**：正式中文名 + 英文名  
✅ **適合 Bing 搜尋**：結合實體商品關鍵詞  

例如，AI 現在會產生：

```
1. METAL BUILD 攻擊自由鋼彈 [PRODUCT_SEARCH: METAL BUILD 攻擊自由 Strike Freedom Gundam]
   市場現況：Bandai 限量版本，定價約 NT$3,500...

2. MG 攻擊自由鋼彈 [PRODUCT_SEARCH: MG 攻擊自由 Strike Freedom Gundam]
   市場現況：一般販售，定價約 NT$2,800...
```

---

**更新日期**：2026 年 6 月 8 日  
**版本**：v3.2 (Bing Image Search Integration)
