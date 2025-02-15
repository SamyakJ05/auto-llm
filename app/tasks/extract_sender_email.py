

def extract_sender_email(input_file: str, output_file: str):
    openai.api_key = os.getenv("AIPROXY_TOKEN")
    
    try:
        with open(input_file, "r", encoding="utf-8") as infile:
            email_text = infile.read()
    except Exception as e:
        raise Exception(f"Error reading {input_file}: {e}")
    
    prompt = (
        "Extract the sender's email address from the following email message. "
        "Return only the email address with no additional text:\n\n"
        f"{email_text}"
    )
    
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful assistant that extracts the sender's email address from an email message."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.0
        )
    except Exception as e:
        raise Exception(f"Error calling OpenAI API: {e}")
    
    sender_email = response.choices[0].message["content"].strip()
    
    try:
        with open(output_file, "w", encoding="utf-8") as outfile:
            outfile.write(sender_email)
    except Exception as e:
        raise Exception(f"Error writing to {output_file}: {e}")