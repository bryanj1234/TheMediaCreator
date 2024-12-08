from openai import OpenAI

def get_open_ai_client(api_key, org_id):
    return OpenAI(api_key=api_key, organization=org_id)