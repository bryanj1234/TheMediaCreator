import json

################################################################################
# Function to create structured prompts ========================================
################################################################################

def create_json_prompt_from_prompt_list(prompt_list):
    prompt_dict = {}
    response_dict = {}
    ii = 0
    for prompt in prompt_list:
        ii += 1
        q_num = "Q" + str(ii)
        prompt_dict[q_num] = prompt
        response_dict[q_num] = "PUT_YOUR_ANSWER_HERE"

    message_dict = {"prompts":prompt_dict, "responses":response_dict}

    message_dict_jsonified = json.dumps(message_dict, indent=4)

    final_prompt = "The following JSON object named \"message_dict_jsonified\" has two properties: 'prompts' and 'responses', both of which hold a JSON object. PLease iterate through the properties (Q1, Q2, etc...) of the 'prompts' object. For each prompt in the the 'prompts' object, place your response in the corresponding key of the 'responses' object. Return the modified \"message_dict_jsonified\" object to me."
    final_prompt += "\n\n"
    final_prompt += "message_dict_jsonified = " + message_dict_jsonified

    return final_prompt

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

