from openai import OpenAI
import requests


def save_from_url(url, file_name):
    img_data = requests.get(url).content
    with open(file_name, 'wb') as handler:
        handler.write(img_data)

def get_image_from_prompt(openai_client, prompt, model="dall-e-3"):
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

