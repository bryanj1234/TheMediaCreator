from openai import OpenAI
import requests
import base64


def save_from_url(url, file_name):
    img_data = requests.get(url).content
    with open(file_name, 'wb') as handler:
        handler.write(img_data)

def get_image_from_prompt(prompt, openai_client, model="dall-e-3"):
    response = openai_client.images.generate(prompt=prompt, model=model)
    # Looks like
    # ImagesResponse(
    #     created=1733620007,
    #     data=[
    #         Image(
    #             b64_json=None,
    #             revised_prompt="A South Asian eleph....",
    #             url='https://oaidalleapiprodscus.blob.core.win...'
    #         )
    #     ]
    # )
    image = response.data[0]
    return {
        "url":image.url,
        "b64_json": image.b64_json,
        "revised_prompt": image.revised_prompt,
    }

def base64_encode_image(image_path):
  with open(image_path, "rb") as image_file:
    return base64.b64encode(image_file.read()).decode('utf-8')

def get_text_from_image(openai_client, url=None, file_name=None, model="dall-e-3"):
    if (url is None and file_name is None) or (url is not None and file_name is not None):
        raise ValueError("Must set exactly one of url or file_name")

    if file_name is not None:
        base64_image = base64_encode_image(file_name)
        url = f"data:image/jpeg;base64,{base64_image}"
        
    response = openai_client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": "What’s in this image?"},
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": url,
                        },
                    },
                ],
            }
        ],
        max_tokens=300,
    )

    print(response.choices[0])