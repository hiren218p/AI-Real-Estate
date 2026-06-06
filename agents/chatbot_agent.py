import os
from dotenv import load_dotenv
import google.generativeai as genai


load_dotenv()


api_key = os.getenv("GOOGLE_API_KEY")


model = None


if api_key:

    genai.configure(
        api_key=api_key
    )

    model = genai.GenerativeModel(
        "gemini-2.0-flash"
    )



def offline_response(question):

    question = question.lower()


    if "investment" in question:

        return """
🏠 Best Property Investment Strategy:

1. Choose a location with future growth
2. Check transport and infrastructure
3. Analyze rental demand
4. Compare property prices
5. Verify documents before buying

Long term investment usually gives better returns.
"""


    elif "price" in question:

        return """
💰 Property price depends on:

• Location
• Property size
• Construction quality
• Amenities
• Market demand
"""


    elif "location" in question:

        return """
📍 Good real estate locations have:

✓ Good connectivity
✓ Schools and hospitals nearby
✓ Business areas
✓ Future development plans
"""


    elif "buy" in question:

        return """
Before buying property:

✓ Check legal documents
✓ Compare market rates
✓ Visit property
✓ Check builder reputation
"""


    else:

        return """
I am your AI Real Estate Advisor 🤖

I can help you with:

🏠 Property search
💰 Investment advice
📍 Location analysis
📊 Market guidance
"""




def chat_response(question):

    try:


        if model:


            response = model.generate_content(
                f"""
You are an AI Real Estate Advisor.

Answer this question:

{question}

Give practical real estate advice.
"""
            )


            return response.text



        else:

            return offline_response(question)



    except Exception:

        return offline_response(question)