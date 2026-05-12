from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import base64
import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

app = FastAPI()

# Enable CORS so your frontend can talk to the backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

client = Groq(api_key= api_key)


@app.post("/generate-marketing")
async def process_image(file: UploadFile = File(...)):
    try:
        # 1. Read and Encode Image
        contents = await file.read()
        base64_image = base64.b64encode(contents).decode('utf-8')

        # 2. Call Groq (Using your specific model)
        completion = client.chat.completions.create(
            model="meta-llama/llama-4-scout-17b-16e-instruct",
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": (
                                "Act as an expert Social Media Marketer. Analyze this product image and generate:\n"
                                "1. Product Title: Catchy & SEO optimized.\n"
                                "2. Product Description: A 3-sentence persuasive pitch.\n"
                                "3. Key Features: 4 bullet points focusing on benefits.\n"
                                "4. SEO Keywords: 10 relevant keywords.\n"
                                "5. Hashtags: 5 trending tags.\n"
                                "6. Social Media Caption: Engaging post with emojis and a Call to Action.\n"
                                "7. Promotional Banner Concept: Describe the visual layout for a sales banner."
                            )
                        },
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/jpeg;base64,{base64_image}",
                            },
                        },
                    ],
                }
            ],
            temperature=0.7,  # Higher temperature for better creative writing
        )

        return {"result": completion.choices[0].message.content}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))