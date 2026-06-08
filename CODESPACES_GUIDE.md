# 🚀 GitHub Codespaces 部署指南

## 🎯 為什麼選擇 GitHub Codespaces？

- ✅ **完全免費**（60 小時/月）
- ✅ **無需第三方平臺**（直接在 GitHub）
- ✅ **一鍵啟動**
- ✅ **自動公開 URL**
- ✅ **自動安裝依賴**

---

## 🚀 快速開始（3 步）

### Step 1: 訪問你的 GitHub Repository

訪問：https://github.com/HD4ni/gundam-model-advisor

### Step 2: 開啟 Codespaces

1. 點擊綠色的 **< > Code** 按鈕
2. 選擇 **Codespaces** 標籤
3. 點擊 **Create codespace on main**

稍等 1-2 分鐘，Codespaces 會啟動。

### Step 3: 運行應用

Codespaces 打開後，會在終端看到它已經自動安裝依賴了。

在終端執行：

```bash
python app.py
```

應該看到：
```
 * Running on http://0.0.0.0:5000
```

---

## 🌐 獲取公開 URL

### 自動的方式

當你運行 `python app.py` 時，VS Code 會彈出通知：

```
Your application running on port 5000 is available.
```

點擊 **Open in Browser** 或 **Open externally**

### 手動獲取 URL

1. 在 VS Code 底部找到 **Ports** 標籤
2. 找到 Port **5000**
3. 右鍵點擊 → **Copy Forwarded Port URL**
4. 這就是你的公開 URL！

格式類似：
```
https://HD4ni-gundam-model-advisor-xxxxx.github.dev
```

---

## 📝 設置環境變量

Codespaces 會自動使用代碼中的 API Keys（來自 app.py）

但為了安全，最好設置環境變量：

### 方式 1：使用 .env 文件（推薦）

1. 在 Codespaces 終端中創建 `.env` 文件：

```bash
cat > .env << 'EOF'
GOOGLE_API_KEY=AIzaSyAn97md7MDhpj5jT1VhN0DvCOWYXlXDv_g
SERPER_API_KEY=a97ea5beed46036758e7ea95dd41a30dd3b1046a
FLASK_DEBUG=False
PORT=5000
EOF
```

2. 重啟應用：

```bash
python app.py
```

### 方式 2：Codespaces Secrets（適合公開倉庫）

1. 進入 Repository Settings
2. 選擇 **Codespaces** → **Dev container secrets**
3. 添加：
   - `GOOGLE_API_KEY`
   - `SERPER_API_KEY`

---

## 🧪 測試應用

1. 訪問你的公開 URL
2. 試試查詢：「攻擊自由鋼彈」
3. 確保看到推薦商品 + 圖片

---

## ⏱️ 配額說明

**免費額度**：
- 60 小時/月 CPU
- 15 GB 儲存空間
- 適合個人開發和展示

**配額用盡後**：
- 可以刪除 Codespace 重新開啟（免費）
- 或升級到付費方案

---

## 🔄 保持 Codespaces 運行

Codespaces 會在 30 分鐘無活動後自動關閉。

若要保持運行，可以：
1. 偶爾訪問一下公開 URL
2. 或在終端輸入命令保持活動

---

## 💡 常見問題

### Q1: 如何停止 Codespaces？

點擊右上角你的頭像 → **Codespaces** → 看到你的 Codespace → 點擊 **...** → **Stop codespace**

### Q2: 如何編輯代碼？

在 Codespaces 中直接編輯 `app.py` 或其他文件，然後重啟應用。

### Q3: 我的 URL 是公開的嗎？

是的！任何人都可以訪問你的公開 URL。

### Q4: 公開 URL 會過期嗎？

只要 Codespace 還在運行，URL 就有效。Codespace 30 分鐘無活動會自動關閉。

### Q5: 代碼會被看到嗎？

不會。只有 **運行的應用** 可以被訪問。代碼保存在私有的 Codespace 中。

---

## 🎯 工作流

```
1. GitHub → Code → Codespaces → Create codespace
         ↓
2. Codespaces 自動啟動 + 安裝依賴
         ↓
3. 終端執行：python app.py
         ↓
4. Ports 標籤 → 複製公開 URL
         ↓
5. 分享 URL 給朋友使用！
```

---

## ✅ 檢查清單

- [ ] Code 已推送到 GitHub
- [ ] GitHub Repository 已存在
- [ ] 點擊 **< > Code** → **Codespaces** → **Create codespace**
- [ ] 等待 1-2 分鐘啟動
- [ ] 終端執行 `python app.py`
- [ ] 獲取公開 URL
- [ ] 測試應用
- [ ] 分享 URL

---

## 🎉 完成！

你現在有一個完全免費的公開 URL，可以隨時分享給朋友使用！

**公開 URL 範例**：
```
https://HD4ni-gundam-model-advisor-xxxxx.github.dev
```

---

**備註**：
- 免費額度：60 小時/月
- Codespace 30 分鐘無活動自動關閉
- 可隨時重新啟動（不會刪除代碼）

祝你使用愉快！🚀
