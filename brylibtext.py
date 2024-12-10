import brylibopenai as bloai

def get_text_from_text(
        prompt,
        structured_output_class,
        openai_client,
        model="gpt-4o-mini"
):
    return bloai.get_text_from_information(
        prompt,
        structured_output_class,
        openai_client,
        model=model
    )