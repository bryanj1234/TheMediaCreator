from openai import OpenAI

################################################################################
# Get a client that can use API ================================================
################################################################################

def get_open_ai_client(api_key, org_id):
    return OpenAI(api_key=api_key, organization=org_id)


################################################################################
# Function signature definitions for controlling responses =====================
################################################################################

def get_default_question_answer_structure():
    return {
        "name": "default_question_answer_structure",
        "parameters": {
            "type": "object",
            "properties": {
                "my_prompts": {
                    "type": "array",
                    "items": {
                        "type": "string"
                    },
                },
                "your_answers": {
                    "type": "array",
                    "items": {
                        "type": "string"
                    },
                }
            },
            "required": ["my_prompts", "your_answers"]
        }
    }

def get_multipart_question_answer_structure():
    return {
        "name": "get_multipart_question_answer_structure",
        "parameters": {
            "type": "object",
            "properties": {
                "your_tasks": {
                    "type": "array",
                    "items": {
                        "my_prompt": {
                            "type": "string"
                        },
                        "your_answer": {
                            "type": "string"
                        },
                    }
                }
            },
            "required": ["your_tasks", "my_prompt", "your_answer"]
        }
    }