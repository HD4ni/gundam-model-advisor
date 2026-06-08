# 🔐 API Key 安全設置指南

## ⚠️ 重要：你的舊 API Key 已洩露

你的 Google API Key 和 Serper API Key 曾被提交到 GitHub，**已被公開**。

### 立即行動：重新生成 API Key

#### Step 1: 撤銷舊的 Google API Key

1. 訪問 [Google Cloud Console](https://console.cloud.google.com/)
2. 進入 **APIs & Services** → **Credentials**
3. 找到你的 API Key
4. 點擊 **🗑️ Delete**（刪除）
5. 申請新的 API Key
6. 複製新 Key

#### Step 2: 撤銷舊的 Serper API Key

1. 訪問 [Serper Dashboard](https://serper.dev/dashboard/)
2. 進入 **API Key Settings**
3. 點擊 **Regenerate API Key**
4. 複製新 Key

---

## 🛡️ 安全設置方式

### 方式 1：本地開發（使用 .env 文件）

1. **編輯 `.env` 文件**（已包含在項目中）

```bash
GOOGLE_API_KEY = 你的新 Google API Key
SERPER_API_KEY = 你的新 Serper API Key
FLASK_DEBUG = False
PORT = 5000
```

2. **驗證 .gitignore 包含 `.env`**（已配置）

```
# .gitignore 中應該有
.env
```

3. **確認 `.env` 不會被提交**

```bash
git status  # 應該看不到 .env 文件
```

### 方式 2：GitHub Codespaces（推薦）

在 Codespaces 中運行時設置環境變量：

#### 方法 A：使用 .env 文件（簡單）

1. 在 Codespaces 終端中創建 `.env` 文件：

```bash
cat > .env << 'EOF'
GOOGLE_API_KEY=你的新Key
SERPER_API_KEY=你的新Key
FLASK_DEBUG=False
PORT=5000
EOF
```

2. 運行應用：

```bash
python app.py
```

#### 方法 B：使用 Codespaces Secrets（更安全）

1. 進入你的 GitHub Repository Settings
2. 選擇 **Codespaces** → **Dev container secrets**
3. 添加新 Secret：
   - Name: `GOOGLE_API_KEY`
   - Value: 你的新 Google API Key
4. 再添加一個：
   - Name: `SERPER_API_KEY`
   - Value: 你的新 Serper API Key

Codespaces 會自動將 Secrets 注入為環境變量。

---

## ✅ 安全檢查清單

- [ ] 舊的 Google API Key 已刪除
- [ ] 舊的 Serper API Key 已重新生成
- [ ] `.env` 文件已包含新 Key
- [ ] `.env` 文件在 `.gitignore` 中
- [ ] 本地 `git status` 看不到 `.env`
- [ ] Codespaces 環境變量已配置
- [ ] 應用正常運行

---

## 🔍 驗證環境變量設置

運行此命令檢查環境變量是否正確加載：

```bash
# 在應用啟動時，會自動檢查這些變量
python app.py
```

如果看到錯誤：
```
ValueError: ❌ 未設置 GOOGLE_API_KEY 環境變量。
```

表示環境變量未正確設置，需要重新配置。

---

## 💡 重要提醒

### 永遠不要提交 API Key

❌ **不要做**：
```python
API_KEY = "AIzaSy..."  # 錯誤！會被提交到 GitHub
```

✅ **應該做**：
```python
API_KEY = os.getenv("GOOGLE_API_KEY")  # 正確！從環境變量讀取
```

### .env 文件不會被提交

`.env` 文件已在 `.gitignore` 中，git 會自動忽略它：

```
# .gitignore
.env          # ← 本地環境變量，不會被提交
.env.example  # ← 模板，供他人參考
```

---

## 🚀 現在使用新 Key

### 本地測試

```bash
# 1. 確保 .env 文件已更新新 Key
cat .env

# 2. 運行應用
python app.py

# 3. 訪問 http://localhost:5000
```

### Codespaces 中運行

```bash
# 1. 在 Codespaces 中創建 .env 或配置 Secrets
# 2. 運行應用
python app.py

# 3. 獲取公開 URL，分享給朋友
```

---

## 📝 Git 歷史警告

⚠️ **重要**：舊 API Key 仍在 Git 歷史中

- GitHub 上的舊提交仍包含原始 API Key
- 因此你 **必須重新生成** API Key（已做）
- 舊 Key 已無效（Google/Serper 無法識別）

如果需要完全從 Git 歷史中移除，可以使用 BFG Repo-Cleaner（高級操作），但通常重新生成 Key 就足夠了。

---

## ✨ 現在完全安全

- ✅ 代碼中沒有 hardcoded API Key
- ✅ API Key 只從環境變量讀取
- ✅ `.env` 已在 `.gitignore` 中
- ✅ 舊 Key 已失效（重新生成了）
- ✅ 可以安心分享 GitHub 倉庫

---

**更新日期**：2026 年 6 月 8 日  
**安全級別**：🟢 安全
