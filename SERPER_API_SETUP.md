# 🎯 Serper API 配置指南（超簡單版）

## 為什麼改用 Serper？

你說得對！直接用 Google 搜圖片最直接。

**Serper API 的優點**：
- ✅ 基於 Google Images（就是你要的 Google）
- ✅ 免費申請，100 次搜尋/天
- ✅ 直接返回圖片 URL，系統自動嵌入
- ✅ 無需複雜配置
- ✅ 搜尋精準度最高

---

## 📝 3 步快速設置

### Step 1: 申請 API Key（1 分鐘）

1. 訪問 → https://serper.dev/
2. 點擊 **"Sign Up"** (免費帳戶)
3. 完成驗證
4. 進入 Dashboard → **API Key**
5. 複製你的 Key

### Step 2: 配置代碼

編輯 `app.py` 第 17 行：

```python
SERPER_API_KEY = "your_serper_api_key_here"
```

改成：

```python
SERPER_API_KEY = "abc123def456xyz..."  # 粘貼你的 Key
```

### Step 3: 重啟應用

```bash
# 停止目前的應用（Ctrl+C）
python app.py
```

---

## 🚀 完成！立即測試

訪問 http://localhost:5000，試試：

```
攻擊自由鋼彈
METAL BUILD 攻擊自由
沙薩比
```

系統會自動：
1. AI 生成推薦 + `[PRODUCT_SEARCH: ...]` 標籤
2. 後端調用 Serper API 搜 Google Images
3. 前端直接顯示圖片（**無需跳轉**）

---

## 💡 它是這樣工作的

```
你的查詢「攻擊自由鋼彈」
    ↓
AI 推薦：HG 攻擊自由 [PRODUCT_SEARCH: HG Strike Freedom 攻擊自由]
    ↓
後端呼叫 Serper API：搜尋「HG Strike Freedom 攻擊自由」的 Google Images
    ↓
Serper 返回：[官方圖片 URL, 日本零售商圖片 URL, ...]
    ↓
前端直接顯示：[圖片] [圖片]
```

---

## 📊 免費配額說明

- **免費方案**：100 次搜尋/天
- **1 次查詢 = 2 張圖片 = 2 次搜尋**
- **每天可以服務 50 個查詢** ✅
- 超過配額：自動降級為 Google 搜尋連結

---

## 🆘 常見問題

### 圖片沒有顯示？

**檢查 1**：API Key 是否正確？
```bash
# 編輯 app.py，確認第 17 行的 Key 沒有多餘空格
```

**檢查 2**：Serper 帳戶是否激活？
- 訪問 https://serper.dev/dashboard
- 確認 Credits 顯示為正數

**檢查 3**：網路連線是否正常？

### 搜尋結果仍然不對？

- 你設的 `[PRODUCT_SEARCH: ...]` 搜尋詞會直接傳給 Google Images
- 搜尋詞越具體，結果越準
- 系統已改進提示詞，AI 會自動生成更精確的搜尋詞

### 想增加每日配額？

Serper 付費方案：
- $49/月 → 500,000 次搜尋
- 但免費的 100 次應該夠用了

---

## ✅ 效果對比

| 方案 | 圖片精準度 | 配置難度 | 費用 |
|------|----------|--------|------|
| Unsplash | ⭐⭐ | 簡單 | 免費 |
| Bing | ⭐⭐⭐ | 複雜 | 免費但繁瑣 |
| **Serper** | **⭐⭐⭐⭐⭐** | **最簡單** | **免費** |

---

## 🎓 系統工作流程

1. **前端** → 使用者輸入「攻擊自由鋼彈」
2. **AI (Gemini)** → 分析並推薦模型，生成 `[PRODUCT_SEARCH: ...]` 標籤
3. **後端 (Flask)** → 解析標籤，調用 Serper API
4. **Serper** → 從 Google Images 搜尋並返回 2 個圖片 URL
5. **前端 (HTML)** → 直接在頁面上渲染圖片，支援 Markdown 和 HTML

---

**完成！享受無需跳轉的圖片體驗吧！** 🎉

如有問題，編輯 app.py 第 17 行即可快速更新 API Key。
