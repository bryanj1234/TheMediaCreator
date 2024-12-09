import brylibopenai as bloai
import brylibimages as blim
import brylibprompt as blp
import json

OPENAI_api_key = open(r"C:\Users\Bryan\Documents\_API_KEYS\TheMediaCreator 2024").read().strip()
OPENAI_org_id = open(r"C:\Users\Bryan\Documents\_API_KEYS\OpenAI_Org_ID").read().strip()

# gets OPENAI_API_KEY from your environment variables
openai_client = bloai.get_open_ai_client(OPENAI_api_key, OPENAI_org_id)

# Get image from text ==========================================================

# initial_prompt = "black and white image of a leopard jumping on an antelope on the Serengeti ."
# image = blim.get_image_from_prompt(initial_prompt, openai_client)
# url = image["url"]
# #b64_json = image["b64_json"]
# #revised_prompt = image["revised_prompt"]
# file_name = "images/the_image_4.jpg"
# blim.save_from_url(url, file_name)

# Get text from image ==========================================================

file_names = ["images/the_image_4.jpg"]
urls = ["https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg"]
# prompt_list = [
#     "How many images did I send you?",
#     "Please describe each image sent, and return the results as a list of strings.",
#     "Please compare each pair of images and describe the similarities and differences for each pair."
# ]
prompt_list = [
    "What is a good way to combine these images?",
    "Can you make a story based on these two images?",
    "How would you imagine the temperature of these images?"
]
prompt, answer_struct_func = blp.create_function_and_prompt_from_prompt_list(prompt_list)
ret_vals = blim.get_info_about_images(prompt, openai_client, answer_struct_func=answer_struct_func, urls=urls, file_names=file_names)
print(ret_vals)

# Get text from text ===========================================================



