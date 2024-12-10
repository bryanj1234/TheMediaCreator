from pydantic import BaseModel

################################################################################
# GenericResponseStructure and prompt creation =================================
################################################################################

class GenericResponseStructure(BaseModel):
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

    added_prompt_explanation: str
    additional_information: str

def generic_prompts_list_to_prompt(prompt_list, context_list=[]):
    context_prompt = ""
    if (len(context_list) > 0):
        context_prompt = "Here is the context you have to start with:\n\n"
        ii = 0
        for context_item in context_list:
            ii += 1
            c_id = "context_item_ " + chr(64 + ii)
            context_prompt += "\t" + c_id + " : " + context_item + "\n"
        context_list += "\n"

    final_prompt = context_prompt
    final_prompt += "\n"
    final_prompt += "I am now going to instruct you to perform one or more tasks. "
    final_prompt += "These tasks are expressed in the following list, where each item begins with a task identifier which has the form prompt_1, prompt_2, prompt_3, etc., followed by a colon ':' character."
    final_prompt += "\n\nHere is the list of tasks:\n\n"

    ii = 0
    for prompt in prompt_list:
        ii +=1
        t_id = "prompt_" + str(ii)
        final_prompt += "\t" + t_id + " : " + prompt + "\n"

    final_prompt += "\n"
    final_prompt += "When you are structuring the output, please populate the fields which start with \"prompt_\" with the corresponding task prompt, and populate the fields which start with \"response_to_prompt_\" with your corresponding response. "
    final_prompt += "If there are additional interesting questions which I did not ask, please add them into the unused \"prompt_\" fields, and add your responses in corresponding \"response_to_prompt_\" fields. "
    final_prompt += "If you choose to populate the \"prompt_\" fields with additional prompts which I didn't send you, then please explain why using the \"added_prompt_explanation\" field. If you did not add any additional prompts, then populate \"added_prompt_explanation\" field with the string \"NO_ADDITIONAL\". "
    final_prompt += "Finally, please evaluate how you did on these tasks, and add your thoughts to the \"additional_information\" field."

    return final_prompt



