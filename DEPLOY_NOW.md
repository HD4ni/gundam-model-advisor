# 🚀 5 分鐘快速部署（Git + GitHub + Zeabur）

## 📋 準備工作

```bash
# 1. 進入項目目錄
cd d:\Code\School\AI人文\final

# 2. 初始化 Git
git init

# 3. 添加並提交所有文件
git add .
git commit -m "鋼彈老兵模型情報系統 v3.3 - 就緒部署"
```

---

## 🌐 上傳到 GitHub

### 在 GitHub 上創建新倉庫

1. 訪問 https://github.com/new
2. 輸入倉庫名：`gundam-model-advisor`
3. 選擇 **Public**
4. **不要** 勾選任何初始化選項
5. 點擊 **Create repository**

### 本地推送到 GitHub

複製 GitHub 頁面上的指令（應類似這樣）：

```bash
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/gundam-model-advisor.git
git push -u origin main
```

> 替換 `YOUR_USERNAME` 為你的 GitHub 用戶名

---

## ☁️ 部署到 Zeabur

### 1. 連接 Zeabur

訪問 https://zeabur.com/：
1. 用 GitHub 登入
2. 點擊 **New Project**
3. 選擇 **Deploy from Git**
4. 選擇 `gundam-model-advisor` 倉庫
5. 選擇 `main` 分支
6. 點擊 **Deploy**

### 2. 設置環境變量

部署開始後，進入 Project Settings：
1. 找到 **Environment Variables**
2. 添加以下變量：

```
GOOGLE_API_KEY = AIzaSyAn97md7MDhpj5jT1VhN0DvCOWYXlXDv_g
SERPER_API_KEY = a97ea5beed46036758e7ea95dd41a30dd3b1046a
```

3. 保存後 Zeabur 會自動重新部署

### 3. 獲取公開 URL

部署完成後，你會得到一個 URL，類似：

```
https://gundam-model-advisor.zeabur.app
```

訪問這個 URL 即可使用你的應用！

---

## ✅ 測試部署

1. 訪問你的公開 URL
2. 試試查詢：「攻擊自由鋼彈」
3. 確保看到推薦商品 + 圖片

---

## 📝 完整文檔

- [DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md) - 詳細部署步驟
- [LOCAL_TESTING.md](LOCAL_TESTING.md) - 本地測試指南
- [SERPER_API_SETUP.md](SERPER_API_SETUP.md) - Serper 配置
- [QUICK_START.md](QUICK_START.md) - 功能快速開始

---

## 🎉 完成！

現在你的應用在雲端運行，可以分享給朋友使用！

---

**部署時間**：約 5-10 分鐘  
**成本**：完全免費（GitHub + Zeabur）
