import brylibopenai as bloai
import brylibimages as blim

OPENAI_api_key = open(r"C:\Users\Bryan\Documents\_API_KEYS\TheMediaCreator 2024").read().strip()
OPENAI_org_id = open(r"C:\Users\Bryan\Documents\_API_KEYS\OpenAI_Org_ID").read().strip()

# gets OPENAI_API_KEY from your environment variables
openai_client = bloai.get_open_ai_client(OPENAI_api_key, OPENAI_org_id)

initial_prompt = "A impressionist image of an astronaut lounging in a tropical resort floating in space. The astronaut, of Nordic descent, is comfortably settled in a floaty chair with a drink in lap, wearing the helmet but the rest of the spacesuit is off. The resort has palm trees growing in an terraformed environment, a cool pool filled with shimmering water, and spherical villas floating around. The blackness of space, dusted with stars, is presenting a stark contrast with the vibrant colors of the resort."

image = blim.get_image_from_prompt(openai_client, initial_prompt)

print("HERE");

url = image["url"]
b64_json = image["b64_json"]
revised_prompt = image["revised_prompt"]

print(b64_json)
print(revised_prompt)

file_name = "the_image_2.jpg"
blim.save_from_url(url, file_name)

