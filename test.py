import brylibopenai as bloai
import brylibimages as blim
from pprint import pprint

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

# file_names = ["images/the_image_4.jpg"]
# urls = ["https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg"]
# prompt = "Please complete the following three tasks. Return three function calls, one for each task. 1) Answer the question \"How many images did I send you?\" 2) Please describe each image sent, and return the results as a list of strings. 3) Please compare each pair of images and describe the similarities and differences for each pair."
# ret_vals = blim.get_info_about_images_using_functions(prompt, openai_client, urls=urls, file_names=file_names)
# pprint(ret_vals)

# file_names = ["images/the_image_4.jpg"]
# urls = ["https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg"]
# prompt = "Please complete the following three tasks. Add an item into the \"your_tasks\" field for each task. Here are the tasks: 1) Answer the question \"How many images did I send you?\" 2) Please describe each image sent, and return the results as a list of strings. 3) Please compare each pair of images and describe the similarities and differences for each pair."
# ret_vals = blim.get_info_about_images_using_response_format(prompt, openai_client, urls=urls, file_names=file_names)
# pprint(ret_vals)