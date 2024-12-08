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

file_names = ["images/the_image_4.jpg"]
urls = ["https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg"]

# answer_struct_func = bloai.get_default_question_answer_structure
# prompt = "Please preform the following three tasks, but respond as if it were only one task. 1) Tell me how many images I sent you. 2) Please describe each image sent, and return the results as a list of strings. 3) Please compare each pair of images and describe the similarities and differences for each pair.\n\nPopulate both the 'my_prompt' and 'your_answer' properties of the function argument."
# ret_vals = blim.get_info_about_images(prompt, openai_client, answer_struct_func=answer_struct_func, urls=urls, file_names=file_names)
# print(ret_vals[0]["func_args"]["my_prompts"])
# print(ret_vals[0]["func_args"]["your_answers"])

# answer_struct_func = bloai.get_multipart_question_answer_structure
# prompt = "Please complete the following three tasks, but respond as if they were one single task. Populate array inside the \"your_tasks\" field with an entry for each of the following tasks, setting value at \"my_prompt\" to the task you are assigned, and setting value at \"your_answer\" with your response for that task.\n\n Here are the tasks:\n\n1) Answer the question \"How many images did I send you?\" 2) Please describe each image sent, and return the results as a list of strings. 3) Please compare each pair of images and describe the similarities and differences for each pair."
# ret_vals = blim.get_info_about_images(prompt, openai_client, answer_struct_func=answer_struct_func, urls=urls, file_names=file_names)
# ai_tasks = ret_vals[0]["func_args"]["your_tasks"]
# for task in ai_tasks:
#     print(task["my_prompt"])
#     print(task["your_answer"])
