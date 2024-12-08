import brylibopenai as bloai
import brylibimages as blim

OPENAI_api_key = open(r"C:\Users\Bryan\Documents\_API_KEYS\TheMediaCreator 2024").read().strip()
OPENAI_org_id = open(r"C:\Users\Bryan\Documents\_API_KEYS\OpenAI_Org_ID").read().strip()

# gets OPENAI_API_KEY from your environment variables
openai_client = bloai.get_open_ai_client(OPENAI_api_key, OPENAI_org_id)

initial_prompt = "black and white image of a leopard jumping on an antelope on the Serengeti ."

image = blim.get_image_from_prompt(initial_prompt, openai_client)

url = image["url"]
#b64_json = image["b64_json"]
#revised_prompt = image["revised_prompt"]

file_name = "images/the_image_4.jpg"
blim.save_from_url(url, file_name)

