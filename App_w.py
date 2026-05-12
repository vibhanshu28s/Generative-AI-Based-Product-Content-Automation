from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import re
import base64
import os
from huggingface_hub import InferenceClient
from groq import Groq
from dotenv import load_dotenv
from huggingface_hub import login


load_dotenv()

hf_key = os.getenv("hf")

login(hf_key)



groq_api_key = os.getenv("GROQ_API_KEY")
hf_api_key = os.getenv("HF_TOKEN")

# Initialize Clients
groq_client = Groq(api_key=groq_api_key)
hf_client = InferenceClient(
    provider="hf-inference",
    api_key=hf_api_key,
)

# =========================================
# FASTAPI APP
# =========================================
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount static files to serve the generated image
app.mount("/static", StaticFiles(directory="."), name="static")

@app.post("/generate-marketing")
async def process_image(file: UploadFile = File(...)):
    try:
        # READ UPLOADED IMAGE
        contents = await file.read()
        base64_image = base64.b64encode(contents).decode("utf-8")

        # STEP 1 → GENERATE MARKETING CONTENT VIA GROQ
        completion = groq_client.chat.completions.create(
            model="meta-llama/llama-4-scout-17b-16e-instruct",
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": (
                                "Act as an expert Social Media Marketer. Analyze this product image and generate for indian market don't give price:\n"
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
            temperature=0.1,  # Higher temperature for better creative writing
        )
        marketing_result = completion.choices[0].message.content
        # print("marketing_result")
        # print(marketing_result)

        # =========================================
        # PRODUCT DESCRIPTION
        # =========================================

        product_title = ""

        title_match = re.search(
            r"Product Title[:\-\s]*([\s\S]*?)(?=2\.|Product Description)",
            marketing_result,
            re.IGNORECASE
        )

        if title_match:
            product_title = title_match.group(1).strip()

        # print("PRODUCT TITLE:")
        # print(product_title)

        # =========================================
        # BANNER CONCEPT
        # =========================================

        banner_concept = ""

        banner_match = re.search(
            r"Promotional Banner Concept[:\-\s]*([\s\S]*)",
            marketing_result,
            re.IGNORECASE
        )

        if banner_match:
            banner_concept = banner_match.group(1).strip()
        #
        # print("BANNER CONCEPT:")
        # print(banner_concept)

        image_gen =  product_title + banner_concept
        # print("image_gen:")
        # print(image_gen)

        # STEP 2 → GENERATE IMAGE USING INFERENCE CLIENT
        # This replaces the previous requests.post logic
        image = hf_client.text_to_image(
            image_gen,
            # model="black-forest-labs/FLUX.1-schnell",
            model="black-forest-labs/FLUX.1-schnell",
        )

        # SAVE THE PIL IMAGE OBJECT
        image_path = "generated_banner.png"
        image.save(image_path)

        # STEP 3 → RETURN RESPONSE
        return {
            "marketing_content": marketing_result,
            "banner_url": "http://127.0.0.1:8000/static/generated_banner.png"
        }

    except Exception as e:
        # Catching and returning the specific error for debugging
        raise HTTPException(status_code=500, detail=str(e))