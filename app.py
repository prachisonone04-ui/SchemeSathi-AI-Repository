import os
import streamlit as st

st.set_page_config(
    page_title="SchemeSathi AI",
    page_icon="🏛️",
    layout="wide",
    initial_sidebar_state="expanded"
)


st.markdown("""
<style>

/* SchemeSathi Main Title */
.stApp h1 {
    color: #FFFFFF !important;
}

/* SchemeSathi Subtitle */
.stApp h2,
.stApp h3 {
    color: #FFFFFF !important;
}

/* All Banner Text */
.stApp p {
    color: #FFFFFF !important;
}

/* Status Text */
.stApp span {
    color: #FFFFFF !important;
}

</style>
""", unsafe_allow_html=True)

from groq import Groq

from config import GROQ_API_KEY
from modules.eligibility import (
    check_eligibility,
    check_pm_kisan_eligibility
)
from modules.translator import get_language_instruction
from modules.ai_agent import build_prompt
from modules.document_loader import load_scheme_document
from modules.rag_engine import split_text, search_information


# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="SchemeSathi AI",
    page_icon="🏛️",
    layout="wide"
)


# --------------------------------------------------
# GROQ AI CLIENT
# --------------------------------------------------

client = Groq(api_key=GROQ_API_KEY)


# --------------------------------------------------
# SCHEME DETAILS
# --------------------------------------------------

SCHEME_DETAILS = {
    "vjnt_scholarship": {
        "name": "VJNT Post-Matric Scholarship",
        "url": "https://www.myscheme.gov.in/schemes/pmsvs-maharashtra",
        "portal": "https://mahadbt.maharashtra.gov.in/"
    },

    "pm_kisan": {
        "name": "PM-KISAN Samman Nidhi",
        "url": "https://pmkisan.gov.in/",
        "portal": "https://pmkisan.gov.in/"
    }
}


# --------------------------------------------------
# LOAD MULTIPLE SCHEME DOCUMENTS
# --------------------------------------------------

@st.cache_data
def load_data():

    schemes = {}

    folder = "data/schemes"

    if not os.path.isdir(folder):
        raise FileNotFoundError(
            "data/schemes folder not found."
        )

    for filename in os.listdir(folder):

        if filename.lower().endswith(".txt"):

            file_path = os.path.join(folder, filename)

            text = load_scheme_document(file_path)

            scheme_id = os.path.splitext(filename)[0]

            schemes[scheme_id] = {
                "text": text,
                "chunks": split_text(text),
                "filename": filename
            }

    return schemes


try:

    schemes = load_data()

    document_loaded = len(schemes) > 0

    document_error = ""

except Exception as e:

    schemes = {}

    document_loaded = False

    document_error = str(e)


# --------------------------------------------------
# HEADER
# --------------------------------------------------

st.title("🏛️ SchemeSathi AI")

st.markdown("""
<div style="
    background: linear-gradient(120deg, #123B70, #2875C7);
    padding: 30px;
    border-radius: 15px;
    text-align: center;
    margin-bottom: 25px;
">
    <h1 style="color:white; margin:0;">
        🏛️ SchemeSathi AI
    </h1>
    <p style="color:#EAF2FB; font-size:18px; margin-top:10px;">
        Government Schemes Made Simple, For Everyone.
    </p>
    <p style="color:white; font-size:16px;">
        सरकारी योजनांची माहिती आता सोप्या भाषेत!
    </p>
</div>
""", unsafe_allow_html=True)


st.subheader(
    "Government Schemes Made Simple, For Everyone."
)

st.write(
    "सरकारी योजनांची माहिती आता सोप्या भाषेत!"
)

st.divider()


# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------


# SIDEBAR DESIGN

st.sidebar.markdown("""
<div style="
    background-color: #123B70;
    padding: 18px;
    border-radius: 12px;
    text-align: center;
">
    <h2 style="color: white; margin: 0;">
        🏛️ SchemeSathi
    </h2>
    <p style="color: #EAF2FB; margin: 5px 0 0 0;">
        AI Government Assistant
    </p>
</div>
""", unsafe_allow_html=True)

st.sidebar.markdown("### 📌 Navigation")

menu = st.sidebar.selectbox(
    "Choose Feature",
    [
        "Home",
        "Multiple Government Schemes",
        "Eligibility Checker",
        "Multilingual Assistant",
        "Application Process Guide"
    ]
)

if document_loaded:

    st.sidebar.success(
        f"{len(schemes)} Government Schemes Loaded"
    )

else:

    st.sidebar.error(
        "Scheme Documents Not Loaded"
    )

    st.sidebar.caption(document_error)


# --------------------------------------------------
# HOME PAGE
# --------------------------------------------------

if menu == "Home":

    st.header("Welcome to SchemeSathi AI")

    st.write(
        "Understand government schemes in your own language."
    )

    st.markdown("""
    ### ✨ What can SchemeSathi AI do?

    - 🎓 Scholarship Eligibility Checker
    - 🏛️ Multiple Government Schemes
    - 🤖 AI-powered Scheme Assistant
    - 🌐 Marathi, Hindi and English Support
    - 📄 Required Documents Information
    - 📝 Application Process Guidance
    - 🔍 Relevant Information Retrieval
    - 📚 Source References
    """)

    st.info(
        "Select a feature from the sidebar to get started."
    )

    st.subheader("🌐 Official Government Portals")

    st.markdown(
        "[myScheme Portal](https://www.myscheme.gov.in/)"
    )

    st.markdown(
        "[MahaDBT Portal](https://mahadbt.maharashtra.gov.in/)"
    )

    st.markdown(
        "[PM-KISAN Portal](https://pmkisan.gov.in/)"
    )

    st.markdown(
        "[National Scholarship Portal](https://scholarships.gov.in/)"
    )


# --------------------------------------------------
# MULTIPLE GOVERNMENT SCHEMES
# --------------------------------------------------


st.header("🏛️ Multiple Government Schemes")

if not document_loaded:

        st.error("No scheme documents are available.")

else:

        st.write(
            "Explore the government schemes available in SchemeSathi AI."
        )

        for scheme_id, data in schemes.items():

            details = SCHEME_DETAILS.get(
                scheme_id,
                {
                    "name": scheme_id.replace("_", " ").title(),
                    "url": "",
                    "portal": ""
                }
            )

            with st.expander(details["name"]):

                st.write(data["text"])

                if details["url"]:
                    st.markdown(
                        f"[Official Scheme Source]({details['url']})"
                    )


# --------------------------------------------------
# APPLICATION PROCESS GUIDE
# --------------------------------------------------

if menu == "Application Process Guide":

        st.header("📝 Application Process Guide")

scheme = st.selectbox(
        "Choose Government Scheme",
        [
            "VJNT Post-Matric Scholarship",
            "PM-KISAN Samman Nidhi"
        ]
    )

if scheme == "VJNT Post-Matric Scholarship":

        st.subheader("🎓 VJNT Scholarship Application Steps")

        steps = [
            "Visit MahaDBT portal.",
            "Login or register.",
            "Select VJNT Post-Matric Scholarship.",
            "Fill the application form.",
            "Upload required documents.",
            "Submit the application.",
            "Save the application reference number."
        ]

        for i, step in enumerate(steps, 1):
            st.write(f"**Step {i}:** {step}")

        st.markdown(
            "[Open MahaDBT Portal](https://mahadbt.maharashtra.gov.in/)"
        )

else:

        st.subheader("🌾 PM-KISAN Application Steps")

        steps = [
            "Visit the official PM-KISAN portal.",
            "Complete Farmer Registration.",
            "Enter Aadhaar and bank details.",
            "Submit the required information.",
            "Check application status on the portal."
        ]

        for i, step in enumerate(steps, 1):
            st.write(f"**Step {i}:** {step}")

        st.markdown(
            "[Open PM-KISAN Portal](https://pmkisan.gov.in/)"
        )


# --------------------------------------------------
# ELIGIBILITY CHECKER
# --------------------------------------------------

if menu == "Eligibility Checker":

    st.header("🎓 Government Scheme Eligibility Checker")

scheme_type = st.radio(
        "Choose Scheme",
        ["VJNT Scholarship", "PM-KISAN"]
    )

st.warning(
        "This is a basic guidance tool, not an official "
        "government eligibility decision."
    )

    # VJNT SCHOLARSHIP

if scheme_type == "VJNT Scholarship":

        st.subheader("🎓 VJNT Scholarship")

        category = st.selectbox(
            "Select Your Category",
            ["General", "SC", "ST", "OBC", "SBC", "VJNT"]
        )

        income = st.number_input(
            "Annual Family Income (₹)",
            min_value=0,
            value=150000
        )

        resident = st.checkbox(
            "I am a resident of Maharashtra"
        )

        course = st.checkbox(
            "I am enrolled in an approved post-matric course"
        )

        attendance = st.slider(
            "Attendance Percentage",
            0, 100, 75
        )

        if st.button("Check Eligibility", type="primary"):

            results = check_eligibility(
                category,
                income,
                resident,
                course,
                attendance
            )

            st.subheader("📋 Eligibility Results")

            for result in results:
                st.write(result)

            st.markdown(
                "[Open MahaDBT Portal](https://mahadbt.maharashtra.gov.in/)"
            )

    # PM-KISAN

else:

        st.subheader("🌾 PM-KISAN Eligibility")

        farmer_family = st.checkbox(
            "I belong to an eligible landholding farmer family"
        )

        land_records = st.checkbox(
            "I have land ownership records"
        )

        aadhaar = st.checkbox(
            "I have Aadhaar details"
        )

        bank_details = st.checkbox(
            "I have bank account details"
        )

        if st.button("Check PM-KISAN Eligibility", type="primary"):

            results = check_pm_kisan_eligibility(
                farmer_family,
                land_records,
                aadhaar,
                bank_details
            )

            st.subheader("📋 Eligibility Results")

            for result in results:
                st.write(result)

            st.markdown(
                "[Open PM-KISAN Portal](https://pmkisan.gov.in/)"
            )



# --------------------------------------------------
# MULTILINGUAL AI ASSISTANT
# --------------------------------------------------

if menu == "Multilingual Assistant":

        st.header("🤖 Ask SchemeSathi AI")

st.write(
        "Ask questions about government schemes "
        "in your preferred language."
    )

if not document_loaded:

        st.error(
            "Please add TXT scheme documents inside data/schemes."
        )

else:

        scheme_options = {
            scheme_id: SCHEME_DETAILS.get(
                scheme_id,
                {
                    "name": scheme_id.replace("_", " ").title()
                }
            )["name"]
            for scheme_id in schemes
        }

        selected_scheme = st.selectbox(
            "Choose Government Scheme",
            options=list(scheme_options.keys()),
            format_func=lambda x: scheme_options[x]
        )

        language = st.selectbox(
            "Choose Your Language",
            ["मराठी", "हिंदी", "English"]
        )

        question = st.text_area(
            "Ask Your Question",
            placeholder=(
                "Example: VJNT शिष्यवृत्तीसाठी "
                "कोणती कागदपत्रे आवश्यक आहेत?"
            ),
            height=100
        )

        if st.button("Get Answer", type="primary"):

            if not question.strip():

                st.warning("Please enter your question.")

            else:

                try:

                    selected_data = schemes[selected_scheme]

                    scheme_text = selected_data["text"]

                    chunks = selected_data["chunks"]

                    # RETRIEVE RELEVANT INFORMATION

                    relevant_chunks = search_information(
                        question,
                        chunks
                    )

                    if relevant_chunks:

                        context = "\n\n".join(
                            relevant_chunks
                        )

                        retrieval_method = (
                            "Keyword-based retrieval"
                        )

                    else:

                        context = scheme_text

                        retrieval_method = (
                            "Full document fallback"
                        )

                    # LANGUAGE INSTRUCTION

                    language_instruction = (
                        get_language_instruction(language)
                    )

                    # BUILD PROMPT

                    prompt = build_prompt(
                        question,
                        context,
                        language_instruction
                    )

                    # AI RESPONSE

                    with st.spinner(
                        "SchemeSathi AI is finding your answer..."
                    ):

                        response = client.chat.completions.create(

                            model="openai/gpt-oss-20b",

                            messages=[
                                {
                                    "role": "system",
                                    "content": """
You are SchemeSathi AI, a reliable government scheme information assistant.

STRICT RULES:

1. Answer only using the selected scheme document.
2. Never invent government rules, benefits, amounts,
   eligibility criteria, documents or deadlines.
3. Keep the official scheme name accurate.
4. Answer in the language selected by the user.
5. Use simple and clear language.
6. If information is missing, clearly say it is not
   available in the provided document.
7. Do not add unsupported statements.
8. Do not add missing-information disclaimers when
   the requested information is already available.
9. Organize answers with headings or numbered lists.
10. Do not claim that demo results are official decisions.
"""
                                },
                                {
                                    "role": "user",
                                    "content": prompt
                                }
                            ],

                            temperature=0.1,

                            max_tokens=1200
                        )

                    answer = response.choices[0].message.content

                    # DISPLAY ANSWER

                    st.subheader("📌 Answer")

                    st.markdown(answer)

                    st.divider()

                    # INFORMATION SOURCES

                    st.subheader("📚 Information Sources")

                    st.success(
                        f"Source: {selected_data['filename']}"
                    )

                    st.caption(
                        f"Retrieval method: {retrieval_method}"
                    )

                    with st.expander(
                        "🔍 View Retrieved Information"
                    ):

                        st.write(context)

                    # OFFICIAL SOURCES

                    details = SCHEME_DETAILS.get(
                        selected_scheme,
                        {}
                    )

                    st.subheader(
                        "🌐 Official Government Portals"
                    )

                    if details.get("url"):

                        st.markdown(
                            f"[Official Scheme Source]({details['url']})"
                        )

                    if details.get("portal"):

                        st.markdown(
                            f"[Application Portal]({details['portal']})"
                        )

                    st.caption(
                        "Verify the latest scheme rules "
                        "on official government portals before applying."
                    )

                except Exception as e:

                    st.error(
                        f"AI Error: {e}"
                    )



# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.divider()

st.caption(
    "🏛️ SchemeSathi AI | Making Government Schemes "
    "Easy to Understand"
)
