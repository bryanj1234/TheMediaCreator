import requests
import base64
import brylibopenai as bloai

def save_from_url(url, file_name):
    img_data = requests.get(url).content
    with open(file_name, 'wb') as handler:
        handler.write(img_data)

def get_image_from_text(
        prompt,
        openai_client,
        model="dall-e-3"
):
    return bloai.get_image_from_text(prompt, openai_client, model)

def base64_encode_image(image_path):
  with open(image_path, "rb") as image_file:
    return base64.b64encode(image_file.read()).decode('utf-8')

def get_text_from_images(
        prompt,
        structured_output_class,
        openai_client,
        model="gpt-4o-mini",
        image_urls=None,
        image_file_names=None
):
    if image_urls is None and image_file_names is None:
        raise ValueError("Must set at least one of url or file_name")

    if image_urls is None:
        image_urls = []

    if image_file_names is not None:
        for file_name in image_file_names:
            base64_image = base64_encode_image(file_name)
            image_urls.append(f"data:image/jpeg;base64,{base64_image}")

    return bloai.get_text_from_information(
        prompt,
        structured_output_class,
        openai_client,
        model=model,
        image_urls=image_urls
    )

