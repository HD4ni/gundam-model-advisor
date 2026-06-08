# 本地測試指南

## 在部署前的本地測試

確保應用在本地正常運行後再部署到雲端。

---

## 🔧 環境設置

### Step 1: 複製 .env 文件

```bash
# Windows PowerShell
copy .env.example .env

# Linux/Mac
cp .env.example .env
```

### Step 2: 編輯 .env 文件

打開 `.env`，填入你的 API Keys：

```ini
GOOGLE_API_KEY = AIzaSyAn97md7MDhpj5jT1VhN0DvCOWYXlXDv_g
SERPER_API_KEY = a97ea5beed46036758e7ea95dd41a30dd3b1046a
FLASK_DEBUG = True
```

### Step 3: 安裝依賴

```bash
# 激活虛擬環境
# Windows
.\venv\Scripts\activate

# Linux/Mac
source venv/bin/activate

# 安裝依賴
pip install -r requirements.txt
```

---

## 🚀 運行應用

```bash
python app.py
```

應該看到：
```
 * Serving Flask app 'app'
 * Running on http://0.0.0.0:5000
```

### 訪問應用

打開瀏覽器，訪問：
```
http://localhost:5000
```

---

## 🧪 測試功能

### 測試案例 1：基本查詢
```
輸入：攻擊自由鋼彈
預期：收到吉翁老兵的回應 + 推薦商品 + 圖片
```

### 測試案例 2：複雜查詢
```
輸入：METAL BUILD 攻擊自由
預期：更精確的推薦 + 高清圖片
```

### 測試案例 3：不同陣營機體
```
輸入：沙薩比
預期：吉翁機體，充滿驕傲的語氣
```

---

## 🐛 常見問題

### 問題 1：缺少 requests 模塊

```
ModuleNotFoundError: No module named 'requests'
```

**解決**：
```bash
pip install requests
```

### 問題 2：缺少 google 模塊

```
ModuleNotFoundError: No module named 'google'
```

**解決**：
```bash
pip install google-generativeai
```

### 問題 3：缺少 dotenv 模塊

```
ModuleNotFoundError: No module named 'dotenv'
```

**解決**：
```bash
pip install python-dotenv
```

### 問題 4：API Key 無效

```
Error: Invalid API key provided
```

**檢查**：
- 確保 .env 文件中的 Key 正確複製
- 沒有多餘空格
- Key 仍然有效（未被吊銷）

### 問題 5：圖片搜尋失敗

```
Serper API error: ...
```

**檢查**：
- SERPER_API_KEY 是否設置正確
- Serper 配額是否超出（100 次/天）

---

## 📝 測試檢查清單

- [ ] 應用成功啟動
- [ ] 前端頁面可正常顯示
- [ ] 可以輸入查詢
- [ ] AI 返回合理的回應
- [ ] YouTube 連結有效
- [ ] 圖片正確顯示（或備用搜尋連結）
- [ ] 無 JavaScript 錯誤
- [ ] 無 Python 錯誤日誌

---

## ✅ 準備就緒

如果所有測試都通過，你可以開始部署流程：

```bash
git add .
git commit -m "通過本地測試，準備部署"
git push
```

然後按照 [DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md) 的步驟進行部署。

---

**備註**：.env 文件包含敏感信息，已在 .gitignore 中排除，不會被推送到 GitHub。
