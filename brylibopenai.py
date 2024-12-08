from openai import OpenAI

################################################################################
# Get a client that can use API ================================================
################################################################################

def get_open_ai_client(api_key, org_id):
    return OpenAI(api_key=api_key, organization=org_id)


