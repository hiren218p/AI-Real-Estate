from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet


def create_pdf(
    company,
    overview,
    challenges,
    solutions,
    pitch
):

    file_name = "AI_Real_Estate_Report.pdf"


    doc = SimpleDocTemplate(
        file_name
    )


    styles = getSampleStyleSheet()


    content = []


    content.append(
        Paragraph(
            "AI Real Estate Advisor Report",
            styles["Title"]
        )
    )


    content.append(
        Spacer(1, 20)
    )


    content.append(
        Paragraph(
            f"Company Name: {company}",
            styles["Normal"]
        )
    )


    content.append(
        Paragraph(
            overview,
            styles["Normal"]
        )
    )



    content.append(
        Paragraph(
            "Business Challenges",
            styles["Heading2"]
        )
    )


    for item in challenges:

        content.append(
            Paragraph(
                "• " + item,
                styles["Normal"]
            )
        )



    content.append(
        Paragraph(
            "AI Recommendations",
            styles["Heading2"]
        )
    )


    for item in solutions:

        content.append(
            Paragraph(
                "• " + item,
                styles["Normal"]
            )
        )



    content.append(
        Paragraph(
            "CEO Pitch",
            styles["Heading2"]
        )
    )


    content.append(
        Paragraph(
            pitch.replace("\n","<br/>"),
            styles["Normal"]
        )
    )


    doc.build(
        content
    )


    return file_name