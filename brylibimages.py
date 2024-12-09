import requests
import base64
import json
import brylibprompt as blp

def save_from_url(url, file_name):
    img_data = requests.get(url).content
    with open(file_name, 'wb') as handler:
        handler.write(img_data)

def get_image_from_prompt(prompt, openai_client, model="dall-e-3"):
    response = openai_client.images.generate(prompt=prompt, model=model)
    image = response.data[0]
    return {
        "url":image.url,
        "b64_json": image.b64_json,
        "revised_prompt": image.revised_prompt,
    }

def base64_encode_image(image_path):
  with open(image_path, "rb") as image_file:
    return base64.b64encode(image_file.read()).decode('utf-8')

def get_info_about_images(
        prompt,
        openai_client,
        urls=None,
        file_names=None,
        model="gpt-4o-mini",
        answer_struct_func=None
):
    if urls is None and file_names is None:
        raise ValueError("Must set at least one of url or file_name")

    if urls is None:
        urls = []

    if file_names is not None:
        for file_name in file_names:
            base64_image = base64_encode_image(file_name)
            urls.append(f"data:image/jpeg;base64,{base64_image}")

    user_content = [{"type": "text", "text": prompt}]
    for url in urls:
        img_info = {
            "type": "image_url",
            "image_url": {
                "url": url,
            },
        }
        user_content.append(img_info)

    if answer_struct_func is None:
        # Return JSON.
        # Presumably you found some other way to control the response,
        # maybe by using a well-structured prompt.
        response = openai_client.chat.completions.create(
            model=model,
            messages=[
                {
                    "role": "user",
                    "content": user_content,
                }
            ],
            response_format= {
                "type": "json_object",
            },
            max_tokens=300,
        )
        return json.loads(response.choices[0].message.content)
    else:
        # You are using answer_struct_func to control the response.
        tools = [
            {
                "type": "function",
                "function": answer_struct_func(),
            }
        ]
        response = openai_client.chat.completions.create(
            model=model,
            messages=[
                {
                    "role": "user",
                    "content": user_content,
                }
            ],
            tools=tools,
            max_tokens=300,
        )

        ret_vals = blp.extract_and_reassemble_fragmented_func_results(response.choices[0].message.tool_calls)
        return ret_vals
