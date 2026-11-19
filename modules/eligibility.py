
def check_eligibility(
    category,
    income,
    resident,
    course,
    attendance
):
    results = []

    if category != "VJNT":
        results.append("❌ Applicant VJNT category मध्ये नाही.")
    else:
        results.append("✅ VJNT Category योग्य आहे.")

    if not resident:
        results.append("❌ Maharashtra resident असणे आवश्यक आहे.")
    else:
        results.append("✅ Maharashtra residency योग्य आहे.")

    if income > 250000:
        results.append("❌ Annual family income ₹2.5 lakh पेक्षा जास्त आहे.")
    else:
        results.append("✅ Income criteria पूर्ण आहे.")

    if not course:
        results.append("❌ Government-approved post-matric course आवश्यक आहे.")
    else:
        results.append("✅ Course criteria पूर्ण आहे.")

    if attendance < 75:
        results.append("❌ Attendance 75% पेक्षा कमी आहे.")
    else:
        results.append("✅ Attendance criteria पूर्ण आहे.")

    return results


# PM-KISAN ELIGIBILITY CHECKER

def check_pm_kisan_eligibility(
    farmer_family,
    land_records,
    aadhaar,
    bank_details
):
    results = []

    if farmer_family:
        results.append("✅ Farmer family condition reported as fulfilled.")
    else:
        results.append("❌ Eligible landholding farmer family असणे आवश्यक आहे.")

    if land_records:
        results.append("✅ Land ownership records available.")
    else:
        results.append("❌ Land ownership records आवश्यक आहेत.")

    if aadhaar:
        results.append("✅ Aadhaar details available.")
    else:
        results.append("❌ Aadhaar details आवश्यक आहेत.")

    if bank_details:
        results.append("✅ Bank account details available.")
    else:
        results.append("❌ Bank account details आवश्यक आहेत.")

    results.append(
        "⚠️ Final eligibility depends on official PM-KISAN "
        "rules, exclusions and government record verification."
    )

    return results
