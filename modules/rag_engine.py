
def split_text(text, chunk_size=500):
    chunks = []

    for i in range(0, len(text), chunk_size):
        chunks.append(text[i:i + chunk_size])

    return chunks


def search_information(question, chunks):

    question = question.lower()

    aliases = {
        "कागदपत्रे": ["documents", "required"],
        "कागदपत्र": ["documents", "required"],
        "पात्रता": ["eligibility"],
        "उत्पन्न": ["income"],
        "अर्ज": ["application", "process"],
        "शिष्यवृत्ती": ["scholarship"],
        "योजना": ["scheme"],
        "रहिवासी": ["resident", "maharashtra"],
        "उपस्थिती": ["attendance"],
        "गुणपत्रक": ["marksheet"],
    }

    keywords = question.split()

    for marathi_word, english_words in aliases.items():
        if marathi_word in question:
            keywords.extend(english_words)

    keywords = [
        word.strip("?,.!:;()[]{}")
        for word in keywords
        if len(word.strip("?,.!:;()[]{}")) > 2
    ]

    results = []

    for chunk in chunks:
        chunk_lower = chunk.lower()

        score = sum(
            1 for word in keywords
            if word in chunk_lower
        )

        if score > 0:
            results.append((score, chunk))

    results.sort(reverse=True, key=lambda x: x[0])

    return [chunk for score, chunk in results[:3]]
