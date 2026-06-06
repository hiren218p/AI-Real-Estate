import streamlit as st

from agents.company_research_agent import research_company
from agents.analysis_agent import analyze_company
from agents.recommendation_agent import recommend_ai_solutions
from agents.pitch_agent import generate_pitch
from agents.property_agent import recommend_property
from agents.chatbot_agent import chat_response
from utils.pdf_generator import create_pdf

from database.history_db import (
    create_database,
    save_report,
    get_reports
)


# Page Setup

st.set_page_config(
    page_title="AI Real Estate Advisor",
    page_icon="🏠",
    layout="wide"
)


# Create Database

create_database()



# ---------------- SIDEBAR ----------------

st.sidebar.title("🏠 AI Real Estate")


menu = st.sidebar.selectbox(
    "Select Feature",
    [
        "Company Analysis",
        "Property Search",
        "AI Chatbot",
        "History",
        "About Project"
    ]
)



# ---------------- COMPANY ANALYSIS ----------------


if menu == "Company Analysis":


    st.title("🏢 Company Analysis")


    company = st.text_input(
        "Enter Real Estate Company Name"
    )


    if st.button("Generate Report"):


        if company:


            company_data = research_company(company)


            analysis = analyze_company(company_data)


            solutions = recommend_ai_solutions()


            pitch = generate_pitch(company)



            st.header("🏢 Company Overview")


            st.write(
                company_data.get(
                    "overview",
                    "No data available"
                )
            )



            st.subheader("📍 Location")


            st.write(
                company_data.get(
                    "location",
                    "Unknown"
                )
            )



            st.subheader("🏠 Projects")


            projects = company_data.get(
                "projects",
                []
            )


            for p in projects:

                st.write(
                    "✓",
                    p
                )



            st.header("⚠️ Business Challenges")


            for c in analysis["challenges"]:

                st.write(
                    "•",
                    c
                )



            st.header("🤖 AI Recommendations")


            for s in solutions:

                st.success(s)



            st.header("📄 CEO Pitch")


            st.text(pitch)



            # Save History

            save_report(
                company,
                company_data["overview"],
                pitch
            )



            # PDF

            pdf = create_pdf(
                company,
                company_data["overview"],
                analysis["challenges"],
                solutions,
                pitch
            )


            with open(pdf,"rb") as file:


                st.download_button(
                    label="⬇ Download PDF Report",
                    data=file,
                    file_name="AI_Report.pdf",
                    mime="application/pdf"
                )



        else:

            st.warning(
                "Enter company name"
            )





# ---------------- PROPERTY SEARCH ----------------


elif menu == "Property Search":


    st.title("🏠 Property Recommendation")


    location = st.text_input(
        "Enter Location"
    )


    budget = st.number_input(
        "Budget",
        min_value=1000000,
        value=5000000
    )



    if st.button("Search Property"):


        result = recommend_property(
            location,
            budget
        )


        if result:


            for p in result:


                st.info(
f"""
🏠 Property: {p['name']}

📍 Location:
{p['location']}

🏢 Type:
{p['type']}

💰 Price:
₹{p['price']}
"""
                )


        else:

            st.warning(
                "No property found"
            )





# ---------------- CHATBOT ----------------


elif menu == "AI Chatbot":


    st.title(
        "🤖 Real Estate AI Chatbot"
    )


    question = st.text_input(
        "Ask your question"
    )


    if question:


        answer = chat_response(
            question
        )


        st.success(answer)





# ---------------- HISTORY ----------------


elif menu == "History":


    st.title("📂 Report History")


    reports = get_reports()


    if reports:


        for r in reports:


            st.subheader(
                r[1]
            )


            st.write(
                r[2]
            )


            st.divider()


    else:

        st.info(
            "No history available"
        )





# ---------------- ABOUT ----------------


elif menu == "About Project":


    st.title(
        "🏠 About AI Real Estate Advisor"
    )


    st.write(
"""
AI based real estate analysis system.

Features:

✅ Company Research Agent  
✅ Property Recommendation  
✅ AI Chatbot  
✅ PDF Report Generator  
✅ Report History Database  


Technology:

🐍 Python  
🎈 Streamlit  
🤖 AI Agents  
🗄 SQLite  
📄 ReportLab
"""
    )