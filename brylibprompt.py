import json
from pydantic import BaseModel

################################################################################
# Structured Output Formatting =================================================
################################################################################

class GenericQuestionResponseStructure(BaseModel):
    prompt_1: str
    prompt_2: str
    prompt_3: str
    prompt_4: str
    prompt_5: str
    prompt_6: str
    prompt_7: str
    prompt_8: str
    prompt_9: str
    response_to_prompt_1: str
    response_to_prompt_2: str
    response_to_prompt_3: str
    response_to_prompt_4: str
    response_to_prompt_5: str
    response_to_prompt_6: str
    response_to_prompt_7: str
    response_to_prompt_8: str
    response_to_prompt_9: str
    additional_information: str

################################################################################
# Function to create structured prompts ========================================
################################################################################

def create_generic_prompt_from_prompt_list(prompt_list):
    final_prompt = "I am going to instruct you to perform one or more tasks. "
    final_prompt += "These tasks are expressed in the following list, where each item begins with a task identifier which has the form prompt_1, prompt_2, prompt_3, etc., followed by a colon ':' character."
    final_prompt += "\n\nHere is the list of tasks:\n\n"

    ii = 0
    for prompt in prompt_list:
        t_id = "prompt_" + str(ii)
        final_prompt += "\t" + t_id + " : " + prompt + "\n"

    final_prompt += "\n"
    final_prompt += "When you are structuring the output, please populate the fields which start with \"prompt_\" with the corresponding task prompt, and populate the fields which start with \"response_to_prompt_\" with your corresponding response. IF there is any additioal information you'd like to include, please put it in the \"additional_information\" field."

    return final_prompt



################################################################################
# Function signature definitions for controlling responses =====================
################################################################################

def generate_function_signature(arg_props, required_props, func_name="anonymous_function"):
    func_sig = {
        "name": func_name,
        "parameters": {
            "type": "object",
            "properties": arg_props,
            "additionalProperties": False,
            "required": required_props
        }
    }

    the_lambda = lambda:func_sig

    return the_lambda

