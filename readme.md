# Generative AI Based Product Content Automation

AI-powered marketing content generation system that creates complete social media marketing assets from a single product image.

The system analyzes the uploaded product image using Vision AI models and automatically generates:

* Product Title
* Product Description
* Product Features
* SEO Keywords
* Hashtags
* Social Media Caption
* Promotional Banner Concept/Image

---

# 🚀 Features

✅ Upload Product Image
✅ AI-based Image Understanding
✅ Automatic Marketing Content Generation
✅ SEO-Friendly Content
✅ Social Media Ready Captions
✅ Banner Prompt Generation
✅ FastAPI Backend
✅ React Frontend
✅ Hugging Face Image Generation Support
✅ Groq/OpenAI LLM Integration

---

# 🛠️ Tech Stack

## Frontend

* HTML
* CSS
* JAVASCRIPT

## Backend

* FastAPI
* Python

## AI Models & APIs

* Groq LLM
* OpenAI Vision / LLaMA Vision
* Hugging Face Inference API

## Other Libraries

* Pillow
* python-dotenv
* uvicorn

---

# ⚙️ Installation

## 1️⃣ Clone Repository

```bash
git clone <your-repository-url>
cd project
```

---

# 🔧 Backend Setup

## Create Virtual Environment

### Mac/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file inside `backend/`

```env
GROQ_API_KEY=your_groq_api_key
HF_TOKEN=your_huggingface_token
```

---

# ▶️ Run Backend

```bash
uvicorn main:App_w --reload
```

Backend runs on:

```bash
http://127.0.0.1:8000
```


# 📸 Workflow

1. User uploads a product image
2. Vision AI analyzes the image
3. LLM generates:

   * Product title
   * Description
   * Features
   * SEO keywords
   * Hashtags
   * Social media caption
4. Hugging Face model generates:

   * Promotional banner/image
5. Results displayed on UI

---

# 🧠 AI Prompt Flow

## Vision Analysis Prompt

```text
Analyze the uploaded product image and identify:
- Product type
- Product category
- Color
- Usage
- Target audience
- Branding style
```

---

## Marketing Content Prompt

```text
Generate:
1. Product Title
2. Product Description
3. Product Features
4. SEO Keywords
5. Social Media Caption
6. Hashtags
7. Promotional Banner Concept
```

---

# 📡 API Endpoint

## Upload Product Image

```http
POST /generate-content
```

### Request

```form-data
image: file
```

### Response

```json
{
  "title": "Premium Wireless Headphones",
  "description": "Experience immersive sound quality...",
  "features": [
    "Noise Cancellation",
    "Bluetooth 5.3",
    "40 Hour Battery"
  ],
  "seo_keywords": [
    "wireless headphones",
    "bluetooth headset"
  ],
  "hashtags": [
    "#tech",
    "#gadgets"
  ],
  "caption": "Upgrade your music experience 🎧",
  "banner_image": "/generated/banner.png"
}
```

---

# 🖼️ Promotional Banner Generation

The system automatically creates a marketing banner prompt such as:

```text
Create a modern eCommerce promotional banner for premium wireless headphones with neon lighting, dark background, stylish typography, and professional product placement.
```

This prompt is sent to Hugging Face image generation models.

---

# 📷 Sample Output

## Generated Content

* Product Title
* Product Description
* Features
* SEO Keywords
* Captions
* Hashtags

## Generated Banner

AI-generated promotional social media banner.

---

# 🔥 Future Improvements

* Multi-language content generation
* Video advertisement generation
* Instagram Reel script generation
* AI voice-over generation
* Shopify integration
* Amazon listing optimization
* Scheduled social media posting
* Brand tone customization

---

# 🎯 Use Cases

* eCommerce Stores
* Shopify Sellers
* Amazon Sellers
* Digital Marketing Agencies
* Social Media Managers
* Product Advertisers

---

# 🧪 Example Products

* Fashion
* Electronics
* Cosmetics
* Food Products
* Shoes
* Accessories
* Furniture

---

# 👨‍💻 Author

Developed as part of an AI-powered Generative Marketing Automation project.

---

# 📄 License

MIT License

---

# ⭐ Conclusion

This project automates product marketing using Generative AI by transforming a single product image into complete social media-ready marketing content and promotional assets.
