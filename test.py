import brylibopenai as bloai
import brylibimages as blim
import brylibtext as blt
import brylibpromptandstructure as blpands
from pprint import pprint

OPENAI_api_key = open(r"C:\Users\Bryan\Documents\_API_KEYS\TheMediaCreator 2024").read().strip()
OPENAI_org_id = open(r"C:\Users\Bryan\Documents\_API_KEYS\OpenAI_Org_ID").read().strip()

# gets OPENAI_API_KEY from your environment variables
openai_client = bloai.get_open_ai_client(OPENAI_api_key, OPENAI_org_id)

# Get image from text ==========================================================

# initial_prompt = "impressionist image of a cat looking out a window."
# image = blim.get_image_from_text(initial_prompt, openai_client)
# url = image["url"]
# #b64_json = image["b64_json"]
# #revised_prompt = image["revised_prompt"]
# file_name = "images/the_image_5.jpg"
# blim.save_from_url(url, file_name)

# Get text from image ==========================================================

# file_names = ["images/the_image_4.jpg", "images/the_image_5.jpg"]
# # urls = ["https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg"]
# urls = None
# prompts_list = [
#     "How many images did I send you?",
#     #"Please describe each image sent, and return the results as a list of strings.",
#     # "Please compare each pair of images and describe the similarities and differences for each pair.",
#     # "What is a good way to combine these images?",
#     # "Can you make a story based on these two images?",
#     # "How would you imagine the temperature of these images?"
# ]
# structured_output_class = blpands.GenericResponseStructure
# prompt = blpands.generic_prompts_list_to_prompt(prompts_list)
# print("====================================================================================")
# print(prompt)
# print("====================================================================================")
# ret_vals = blim.get_text_from_images(prompt, structured_output_class, openai_client, image_urls=urls, image_file_names=file_names)
# print("====================================================================================")
# pprint(ret_vals)
# print("====================================================================================")

# Get text from text ===========================================================

context_list = [
    "There is cat sitting on a windowsill, looking intently out the window. It is deeply engaged with what's going on outside.",
    "The cat is white."
]

prompts_list = [
    "What color is the cat?",
    "Please come up with three or four plausible reasons that cat would be so focused on what's happening outside."
]

structured_output_class = blpands.GenericResponseStructure
prompt = blpands.generic_prompts_list_to_prompt(prompts_list, context_list)
print("====================================================================================")
print(prompt)
print("====================================================================================")
ret_vals = blt.get_text_from_text(prompt, structured_output_class, openai_client)
print("====================================================================================")
pprint(ret_vals)
print("====================================================================================")


