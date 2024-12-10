from openai import OpenAI

################################################################################
# Get a client that can use API ================================================
################################################################################

def get_open_ai_client(api_key, org_id):
    return OpenAI(api_key=api_key, organization=org_id)


def get_image_from_text(prompt, openai_client, model="dall-e-3"):
    response = openai_client.images.generate(prompt=prompt, model=model)
    image = response.data[0]
    return {
        "url":image.url,
        "b64_json": image.b64_json,
        "revised_prompt": image.revised_prompt,
    }


def get_text_from_information(
        prompt,
        structured_output_class,
        openai_client,
        model="gpt-4o-mini",
        image_urls=None
):
    if structured_output_class is None:
        raise ValueError("Must set structured_output_class")

    if image_urls is None:
        image_urls = []

    user_content = [{"type": "text", "text": prompt}]

    for url in image_urls:
        img_info = {
            "type": "image_url",
            "image_url": {
                "url": url,
            },
        }
        user_content.append(img_info)

    completion = openai_client.beta.chat.completions.parse(
        model=model,
        messages=[
            {"role": "user",
             "content": user_content},
        ],
        response_format=structured_output_class,
    )
    ret_vals = completion.choices[0].message.parsed

    return ret_vals