# 🎖️ 鋼彈老兵模型顧問 | Gundam Old Veteran Model Advisor
---

## 🎯 系統核心特色與功能

* **🎭 沉浸式 AI 角色扮演 (System Prompting)**
  AI 將化身為退役吉翁公國將軍。面對聯邦機體時語氣尖銳，面對吉翁同胞則充滿驕傲；給予模型推薦時，強制要求指出商品的「致命缺點或災情」（例如：關節偏軟、補色地獄）。
* **🔍 內建 Google 搜尋接地 (Search Grounding)**
  採用全新 `google-genai` SDK 語法，動態掛載 Google 搜尋工具，確保老兵對最新上市的模型、PB 限定商品的市場現況與定價絕不脫節。
* **📷 動態實體照片檢索 (Serper API)**
  後端利用正則表達式（Regex）攔截 AI 生成的 `[PRODUCT_SEARCH: ...]` 標籤，並透過 Serper API 動態抓取高畫質商品圖，直接以 HTML 卡片形式無縫嵌入對話中。
* **📺 自動化 YouTube 開箱連結**
  針對推薦機體，系統會自動生成專屬的 YouTube 影音開箱檢索按鈕，方便玩家一鍵查閱實體把玩影片。
* **🟢 賽博朋克吉翁風 UI**
  前端採用全螢幕綠光雷達網格背景，搭配吉翁公國紅（Zeon Red）與專屬標誌浮水印，打造硬核的戰術終端機體驗。支援 Markdown 即時渲染（marked.js）。

---

## 🏗️ 系統運作架構

1. **User Input:** 使用者於前端介面輸入機體名稱（如：攻擊自由、沙薩比）。
2. **Flask Backend:** 接收請求，將內容連同老兵的 System Prompt 傳送至 Google Gemini API。
3. **Gemini AI:** 結合 Google Search 獲取最新市場資訊，生成帶有 `[PRODUCT_SEARCH: 產品關鍵字]` 標籤的 Markdown 回應。
4. **Image Fetching:** Flask 後端擷取標籤，發送至 Serper API 獲取產品對應的圖片 URL。
5. **Response Compilation:** 將圖片 URL 轉換為 HTML 圖片網格，合併回原始 Markdown 文本，並回傳給前端。
6. **Frontend Rendering:** 使用 `marked.js` 將 Markdown 渲染為軍事風格的 UI 呈現給使用者。

---

## 🚀 開發環境與本地運行指南(如有需要)

### 1. 必備環境
* Python 3.11 或以上版本
* Git

### 2. 環境建置與啟動
```bash
# 1. 克隆專案到本地
git clone [https://github.com/HD4ni/gundam-model-advisor.git](https://github.com/HD4ni/gundam-model-advisor.git)
cd gundam-model-advisor

# 2. 建立並啟動 Python 虛擬環境
python -m venv venv
source venv/bin/activate  # macOS/Linux
# 或是 venv\Scripts\activate # Windows

# 3. 安裝核心依賴套件
pip install -r requirements.txt

# 4. 設定環境變數
# 請在專案根目錄建立 `.env` 檔案，並填入以下內容：
GOOGLE_API_KEY="你的_Gemini_API_Key"
SERPER_API_KEY="你的_Serper_API_Key"
FLASK_DEBUG=True
PORT=5000

# 5. 啟動伺服器
python app.py