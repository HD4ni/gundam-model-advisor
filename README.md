# 鋼彈老兵模型顧問 | Gundam Old Veteran Model Advisor

🤖 由 Google Gemini AI 驅動的高達模型推薦系統 - 以退役吉翁將軍角色提供專業建議。

## 🚀 快速開始

### 必備環境

- Python 3.11+
- pip（Python 包管理）

### 1. 本地運行

```bash
# 克隆項目
git clone https://github.com/HD4ni/gundam-model-advisor.git
cd gundam-model-advisor

# 創建虛擬環境
python -m venv venv

# 啟動虛擬環境
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

# 安裝依賴
pip install -r requirements.txt

# 設置 API Key（見下面安全配置部分）
# 編輯 .env 文件或設置環境變量

# 運行應用
python app.py

# 訪問 http://localhost:5000
```

### 2. GitHub Codespaces 運行（推薦）

1. 進入此 Repository → **Code** → **Codespaces** → **Create codespace on main**
2. 等待 Codespaces 環境準備完成（會自動安裝依賴）
3. 在 Codespaces 中設置 API Key（見下面安全配置）
4. 終端中運行：
   ```bash
   python app.py
   ```
5. VS Code 會提示 **Forwarded port 5000** → 點擊 **Open in Browser**
6. 應用會在新標簽頁中打開 ✨

---

## 🔐 API Key 安全設置

### ⚠️ 必讀：API Key 從不硬編碼

本項目 **絕不** 在代碼中包含 API Key。所有敏感信息通過環境變量管理。

### 需要的 API Key

1. **Google Gemini API Key** - [Google AI Studio](https://aistudio.google.com/app/apikey)
2. **Serper API Key** - [Serper Dashboard](https://serper.dev/dashboard/)

### 設置方法

#### 方法 A：本地開發（.env 文件）

1. 複製 `.env.example`：
   ```bash
   cp .env.example .env
   ```

2. 編輯 `.env`，填入你的 API Key：
   ```
   GOOGLE_API_KEY=你的Google API Key
   SERPER_API_KEY=你的Serper API Key
   FLASK_DEBUG=False
   PORT=5000
   ```

3. `.env` 已在 `.gitignore` 中，不會被提交到 GitHub

#### 方法 B：GitHub Codespaces（推薦）

1. 進入 Repository → **Settings** → **Codespaces** → **Dev container secrets**
2. 添加兩個 Secrets：
   - Name: `GOOGLE_API_KEY` → Value: 你的 Google API Key
   - Name: `SERPER_API_KEY` → Value: 你的 Serper API Key
3. Codespaces 會自動將 Secrets 注入為環境變量

---

## 📂 項目結構

```
gundam-model-advisor/
├── app.py                      # Flask 後端應用
├── requirements.txt            # Python 依賴
├── .env.example                # 環境變量模板（複製為 .env）
├── .devcontainer/
│   └── devcontainer.json       # Codespaces 自動配置
├── .gitignore                  # 忽略敏感文件（.env, venv, __pycache__）
├── templates/
│   └── index.html              # 前端 UI
├── static/                     # 靜態文件（CSS、JS 等）
├── README.md                   # 此文件
├── SECURITY_API_KEY.md         # 詳細的安全設置指南
└── QUICK_START.md              # 快速部署指南
```

---

## 🎯 功能

✅ **AI 角色扮演**  
- 以退役吉翁將軍角色進行高達模型推薦
- 提供市場分析和產品警告

✅ **產品圖片**  
- 通過 Serper API 搜索 Google Images
- 直接在回應中嵌入產品圖片

✅ **YouTube 搜索鏈接**  
- 提供特定模型的 YouTube 開箱搜索鏈接
- 格式：YouTube 搜索結果頁面

✅ **Markdown 支持**  
- 使用 marked.js 解析 Markdown 回應
- 支持格式化文本、列表、鏈接等

---

## 🛠️ 技術棧

- **後端**：Flask 3.0.0，Gunicorn
- **AI**：Google Gemini 2.5-flash API
- **圖片搜索**：Serper API（Google Images）
- **前端**：HTML/CSS/JavaScript，marked.js
- **環境**：Python 3.11
- **部署**：GitHub Codespaces

---

## 🚢 部署

### GitHub Codespaces（推薦）

✅ **優勢**：
- 免費 60 小時/月
- 無需本地環境配置
- 自動端口轉發為公開 URL
- 自動安裝依賴

**步驟**：
1. 進入 Repository → **Code** → **Codespaces** → **Create codespace on main**
2. 設置環境變量（見上面的安全設置）
3. 運行 `python app.py`
4. 分享公開 URL 給朋友

---

## 📝 環境變量

| 變量名 | 必需 | 說明 |
|------|------|------|
| `GOOGLE_API_KEY` | ✅ | Google Gemini API Key |
| `SERPER_API_KEY` | ✅ | Serper API Key |
| `FLASK_DEBUG` | ⚠️ | 調試模式（生產環境設為 False） |
| `PORT` | ⚠️ | 服務器端口（默認 5000） |

---

## 🔒 安全提示

- 永遠不要在代碼中硬編碼 API Key
- `.env` 文件已在 `.gitignore` 中，不會被提交
- GitHub Secrets 更適合公開倉庫
- 定期檢查 API 使用配額

詳見 [SECURITY_API_KEY.md](SECURITY_API_KEY.md)

---

## 📖 更多文檔

- [SECURITY_API_KEY.md](SECURITY_API_KEY.md) - 詳細的 API Key 安全設置指南
- [QUICK_START.md](QUICK_START.md) - 快速部署指南

---

## 🤝 貢獻

歡迎提出 Issue 和 Pull Request！

---

## 📄 授權

此項目開源供學習和個人使用。

---

**最後更新**：2026 年 6 月 8 日  
**維護者**：HD4ni  
**GitHub**：https://github.com/HD4ni/gundam-model-advisor
