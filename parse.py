import google.generativeai as genai

# Set up Gemini API
genai.configure(api_key="AIzaSyBm2qB_qmaKTiINv7S4eot-f70vkucy6qU")
model = genai.GenerativeModel("gemini-1.5-pro")

def parse_with_gemini(dom_chunks, parse_description):
    template = (
        "You are tasked with extracting specific information from the following text content:\n\n"
        "{dom_content}\n\n"
        "Instructions:\n"
        "1. **Extract Information:** Only extract the data that directly matches the description: {parse_description}.\n"
        "2. **No Extra Content:** Do not include explanations or extra text.\n"
        "3. **Empty Response:** If no match is found, return an empty string ('').\n"
        "4. **Direct Data Only:** Provide only the requested information, nothing else."
    )

    parsed_results = []

    for i, chunk in enumerate(dom_chunks, start=1):
        prompt = template.format(dom_content=chunk, parse_description=parse_description)

        try:
            response = model.generate_content(prompt)
            print(f"Parsed batch: {i} of {len(dom_chunks)}")
            parsed_results.append(response.text.strip() if response.text else '')

        except Exception as e:
            print(f"Error: {e}")
            parsed_results.append('')

    return "\n".join(parsed_results)

# Example Usage
dom_chunks = ["This is an example text containing a phone number: +1-234-567-8901."]
parse_description = "Extract the phone number from the text."

result = parse_with_gemini(dom_chunks, parse_description)
print("Extracted Data:", result)
