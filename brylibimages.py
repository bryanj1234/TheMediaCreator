import brylibopenai as bloai
import requests
import base64
import json

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
        answer_struct_func = bloai.get_default_question_answer_structure

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

    tool_calls = response.choices[0].message.tool_calls

    ret_vals = []
    for tool_call in tool_calls:
        func_args = json.loads(tool_call.function.arguments)
        ret_vals.append({"func_name":tool_call.function.name, "func_args":func_args})

    return ret_vals
