# 🚀 部署到雲端完整指南

## 階段二：部署到 Zeabur

本指南將幫助你將鋼彈老兵情報系統部署到雲端，獲得一個公開可訪問的 URL。

---

## 📋 前置需求

確保已安裝：
- Git（下載：https://git-scm.com/）
- GitHub 帳戶（註冊：https://github.com/）
- Zeabur 帳戶（註冊：https://zeabur.com/）

---

## 🔧 Step 1: 初始化 Git Repository

在本地項目目錄中初始化 Git：

```bash
# 進入項目目錄
cd d:\Code\School\AI人文\final

# 初始化 Git repository
git init

# 添加所有文件
git add .

# 首次提交
git commit -m "初始提交：鋼彈老兵模型情報系統 v3.3"
```

### 檢查狀態
```bash
git status
```

應該顯示：`On branch master nothing to commit, working tree clean`

---

## 🌐 Step 2: 創建 GitHub Repository

### 2.1 在 GitHub 上創建新倉庫

1. 訪問 https://github.com/new
2. 填寫信息：
   - **Repository name**：`gundam-model-advisor`（或自訂）
   - **Description**：`鋼彈老兵模型情報終端 - Zeabur 雲端版`
   - **Public** 或 **Private**（推薦 Public 便於展示）
3. **Do not** 勾選「Initialize this repository with...」
4. 點擊 **Create repository**

### 2.2 連接本地 Git 到 GitHub

複製頁面上的指令（應如下所示），在本地終端執行：

```bash
git branch -M main

git remote add origin https://github.com/你的用戶名/gundam-model-advisor.git

git push -u origin main
```

替換 `你的用戶名` 為你的 GitHub 用戶名。

### 檢查是否成功
訪問 `https://github.com/你的用戶名/gundam-model-advisor`，應該看到你的代碼已上傳。

---

## 🚀 Step 3: 部署到 Zeabur

### 3.1 連接 GitHub 到 Zeabur

1. 訪問 https://zeabur.com/
2. 使用 GitHub 帳戶登入
3. 點擊 **New Project** → **Deploy from Git**
4. **Select Repository**：選擇 `gundam-model-advisor`
5. **Select Branch**：選擇 `main`
6. 點擊 **Deploy**

### 3.2 配置環境變量

Zeabur 部署後，需要設置 API Keys：

1. 進入 Project Dashboard
2. 找到你的 Flask 應用（通常名稱為 `app` 或 `web`）
3. 進入 **Settings** → **Environment Variables**
4. 添加以下環境變量：

```
GOOGLE_API_KEY = AIzaSyAn97md7MDhpj5jT1VhN0DvCOWYXlXDv_g
SERPER_API_KEY = a97ea5beed46036758e7ea95dd41a30dd3b1046a
FLASK_DEBUG = False
```

> **安全提示**：不要在代碼中硬編碼 API Key。環境變量方式更安全。

### 3.3 重新部署

修改環境變量後，Zeabur 會自動重新部署。等待部署完成（通常 2-5 分鐘）。

---

## 🔗 Step 4: 獲取公開 URL

部署完成後，你會看到一個公開 URL，格式如：

```
https://gundam-model-advisor.zeabur.app
```

或

```
https://gundam-model-advisor-[隨機碼].zeabur.app
```

### 驗證應用

訪問這個 URL，檢查應用是否正常運行。

---

## 📝 部署文件說明

我已為你準備了以下部署文件：

| 文件 | 用途 |
|------|------|
| `requirements.txt` | Python 依賴列表 |
| `Procfile` | 應用啟動命令 |
| `runtime.txt` | Python 版本指定 |
| `zeabur.json` | Zeabur 配置（可選） |
| `.gitignore` | Git 忽略規則 |

---

## 🛠️ 常見問題

### Q1: 部署失敗，顯示 "Module not found"？

**A**: 確保 `requirements.txt` 包含所有依賴：
```bash
pip freeze > requirements.txt
```

### Q2: 應用啟動但無法訪問？

**A**: 檢查 Zeabur Dashboard 的日誌：
1. 進入項目
2. 查看 **Logs** 標籤
3. 查找錯誤信息

### Q3: API 回應超時或出錯？

**A**: 檢查環境變量是否正確設置：
```bash
# 本地測試
echo $GOOGLE_API_KEY
echo $SERPER_API_KEY
```

### Q4: 想修改代碼後重新部署？

**A**: 只需推送到 GitHub，Zeabur 會自動檢測並重新部署：
```bash
git add .
git commit -m "修復：改進搜尋詞精準度"
git push
```

### Q5: 如何使用自訂域名？

**A**: 在 Zeabur Dashboard 的 **Settings** 中：
1. 進入 **Custom Domain**
2. 添加你的域名
3. 按照指示配置 DNS

---

## ✅ 檢查清單

部署前確保已完成：

- [ ] Git 已初始化和配置
- [ ] GitHub Repository 已創建
- [ ] 代碼已推送到 GitHub
- [ ] GitHub 帳戶已連接 Zeabur
- [ ] Zeabur Project 已創建
- [ ] 環境變量已設置（GOOGLE_API_KEY, SERPER_API_KEY）
- [ ] 部署完成，應用正常運行
- [ ] 獲得公開 URL

---

## 🎉 完成！

現在你的鋼彈老兵模型情報系統已在雲端運行，可以獲得一個公開 URL！

### 分享你的應用

將你的公開 URL 分享給朋友：
```
https://gundam-model-advisor-xxx.zeabur.app
```

---

## 📚 下一步

1. **監控應用** → 定期查看 Zeabur 日誌確保穩定
2. **增加功能** → 在本地修改後推送更新
3. **優化性能** → 根據使用情況調整配置
4. **備份數據** → 重要數據妥善備份

---

## 🆘 需要幫助？

- **Zeabur 文檔**：https://docs.zeabur.com/
- **Git 教學**：https://git-scm.com/book/
- **Flask 部署**：https://flask.palletsprojects.com/deployment/

---

**部署日期**：2026 年 6 月 8 日  
**狀態**：✅ 部署就緒
