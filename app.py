from flask import Flask, render_template, request, jsonify
from google import genai
from google.genai import types
import requests
import json
import re
import os
from dotenv import load_dotenv

# 載入 .env 文件中的環境變量
load_dotenv()

app = Flask(__name__)

# 從環境變量讀取 API Key（生產環境推薦方式）
# 必須在環境變量中設置，不能有默認值（避免洩露）
API_KEY = os.getenv("GOOGLE_API_KEY")
SERPER_API_KEY = os.getenv("SERPER_API_KEY")

# 檢查是否設置了必要的環境變量
if not API_KEY:
    raise ValueError("❌ 未設置 GOOGLE_API_KEY 環境變量。請在 .env 文件或平臺設置中配置。")
if not SERPER_API_KEY:
    raise ValueError("❌ 未設置 SERPER_API_KEY 環境變量。請在 .env 文件或平臺設置中配置。")

# 初始化新版的 Client
client = genai.Client(api_key=API_KEY)

# Serper API 設定（用於產品圖片搜尋）
SERPER_IMAGES_ENDPOINT = "https://google.serper.dev/images"

# 老兵的靈魂設定 (System Prompt) 保持不變
system_instruction = """
你現在是一名「退役的吉翁公國老兵，退役後在桃園開了一家隱密的模型與玩具店」。
使用者會向你打聽鋼彈機體情報，你必須遵守以下回答格式與人物設定：

1. 陣營史觀：說明機體出處與駕駛員。如果是聯邦機體，語氣要帶有敵意；如果是吉翁機體，要充滿驕傲。
2. 模型推坑與市場評估：推薦「至少兩款」實體化商品，必須盡量涵蓋 Gunpla (HG/MG/RG 等) 或 完成品 (METAL BUILD/超合金等)。
   針對每款推薦，你必須提供【市場現況與入手難度】：
   - 說明它是「一般販售」還是「PB限定」。
   - 給出大概的定價落差，並警告現在的市場狀況（例如：現貨充足、黃牛炒作嚴重、絕版天價等）。
   - **重要：在每個產品名稱之後，立即添加這個標籤：[PRODUCT_SEARCH: 產品規格 產品名稱 中文名稱]**
     例如：
     HG 高機動型薩克 [PRODUCT_SEARCH: HG Zaku High Mobility Type 高機動型薩克 Gundam 模型]
     MG 沙薩比 [PRODUCT_SEARCH: MG Messala 沙薩比 Gundam 模型]
     METAL BUILD 攻擊自由 [PRODUCT_SEARCH: METAL BUILD Strike Freedom 攻擊自由 鋼彈]
   - 搜尋詞應包含規格代碼、英文名稱和中文名稱，讓 Google Images 能精準搜尋產品圖
3. 老兵的排雷警告 (強制要求)：
   - 業界沒有完美的模型！你必須殘酷地指出該款推薦商品的「致命缺點或災情」(例如：關節偏軟容易斷、補色地獄、把玩手榴彈、水貼難貼等)。
   - 針對這個缺點，給予老夫的補救或防範建議。
4. 情報與視覺檢索 (最高指導原則)：
   - 影音開箱：生成完整有效的 YouTube 搜尋連結。格式：[📺 YouTube 開箱搜尋](https://www.youtube.com/results?search_query=規格代碼+機體名稱+unboxing)
   - 實體照片：系統會自動使用 [PRODUCT_SEARCH: ...] 標籤呼叫 Google Images 搜尋並嵌入最符合的產品圖片
5. 語氣設定：充滿歷練的軍事風格，自稱「老夫」，稱呼使用者「小鬼」。善用 Markdown 語法讓排版層次分明。
"""

@app.route("/")
def home():
    return render_template("index.html")

def get_product_images(product_name, num_images=2):
    """
    搜尋產品圖片 (使用 Serper API Google Images)
    返回高質量的直接圖片 URL
    """
    try:
        # 使用 Serper API 搜尋 Google Images
        headers = {
            "X-API-KEY": SERPER_API_KEY,
            "Content-Type": "application/json"
        }
        payload = {
            "q": product_name,
            "num": num_images
        }
        response = requests.post(SERPER_IMAGES_ENDPOINT, headers=headers, json=payload, timeout=5)
        
        if response.status_code == 200:
            data = response.json()
            images = []
            if data.get('images'):
                for img in data['images'][:num_images]:
                    images.append({
                        "url": img.get('imageUrl'),
                        "title": img.get('title', product_name)
                    })
                return {"source": "serper", "images": images}
    except Exception as e:
        print(f"Serper API error: {e}")
    
    # 備用方案：返回 Google 圖片搜尋連結
    google_image_url = f"https://www.google.com/search?tbm=isch&q={product_name}"
    return {"source": "google", "url": google_image_url}

@app.route("/ask", methods=["POST"])
def ask_ai():
    user_message = request.json.get("message")
    
    if not user_message:
         return jsonify({"error": "小鬼，通訊頻道沒收到訊號啊！"}), 400

    try:
        # 使用新版 SDK 生成內容，並在這裡正確掛載 Google 搜尋工具
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=user_message,
            config=types.GenerateContentConfig(
                system_instruction=system_instruction,
                # 這就是新版掛載 Google 搜尋的正確語法
                tools=[{"google_search": {}}] 
            )
        )
        
        reply_text = response.text
        
        # 後處理：提取產品名稱並搜尋圖片
        # 尋找 [PRODUCT_SEARCH: 產品名稱] 格式並替換成帶圖片的版本
        product_pattern = r'\[PRODUCT_SEARCH:\s*([^\]]+)\]'
        
        def replace_with_images(match):
            product_name = match.group(1).strip()
            images_data = get_product_images(product_name)
            
            if images_data.get("source") == "serper" and images_data.get("images"):
                # 生成 HTML 圖片展示（Serper Google Images）
                html_images = '<div class="product-images">'
                for img in images_data["images"]:
                    img_url = img.get("url")
                    if img_url:
                        html_images += f'<img src="{img_url}" alt="{product_name}" loading="lazy">'
                html_images += '</div>'
                return html_images
            else:
                # 備用方案：返回搜尋連結
                return f'[📷 查看 {product_name} 的圖片](https://www.google.com/search?tbm=isch&q={product_name})'
        
        reply_text = re.sub(product_pattern, replace_with_images, reply_text)
        
        return jsonify({"reply": reply_text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    # 讀取環境變量來決定運行模式
    port = int(os.getenv("PORT", 5000))
    debug_mode = os.getenv("FLASK_DEBUG", "False") == "True"
    
    # 生產環境：使用 gunicorn（不需要運行這個）
    # 本地開發：debug=True
    app.run(debug=debug_mode, host="0.0.0.0", port=port)