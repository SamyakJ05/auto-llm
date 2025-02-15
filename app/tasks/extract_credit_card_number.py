def extract_text_from_image(image_path: str) -> str:
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image)
    return text

def clean_credit_card_number(raw_text: str) -> str:
    digits = re.sub(r'\D', '', raw_text)
    
    if 13 <= len(digits) <= 19:
        return digits
    return None

def refine_credit_card_number_with_llm(extracted_text: str) -> str:
    if not OPENAI_API_KEY:
        raise ValueError("AIPROXY_TOKEN not set.")

    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role": "system", "content": "Extract the credit card number from the given text. Return only the numeric credit card number with no spaces or extra characters."},
                  {"role": "user", "content": extracted_text}],
    )

    return response["choices"][0]["message"]["content"].strip()

def process_credit_card_image(input_image: str, output_file: str):
    extracted_text = extract_text_from_image(input_image)
    credit_card_number = clean_credit_card_number(extracted_text)

    if not credit_card_number:
        credit_card_number = refine_credit_card_number_with_llm(extracted_text)

    if credit_card_number:
        with open(output_file, "w") as f:
            f.write(credit_card_number)
        print(f"Credit card number saved to {output_file}")
    else:
        print("Failed to extract a valid credit card number.")