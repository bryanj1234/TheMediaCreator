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

    final_prompt = "The following JSON object named \"message_dict_jsonified\" has two properties: 'prompts' and 'responses', both of which hold a JSON object. Please iterate through the properties (Q1, Q2, etc...) of the 'prompts' object. For each prompt in the the 'prompts' object, place your response in the corresponding key of the 'responses' object. Return the modified \"message_dict_jsonified\" object to me."
    final_prompt += "\n\n"
    final_prompt += "message_dict_jsonified = " + message_dict_jsonified

    return final_prompt

def create_function_and_prompt_from_prompt_list(prompt_list):
    final_prompt = "I am going to instruct you to perform one or more tasks. "
    final_prompt += "These tasks are expressed in the following list, where each item begins with a task identifier which has the form P_1, P_2, P_3, etc., followed by a colon ':' character."
    final_prompt += "\n\nHere is the list of tasks:\n\n"

    ii = 0
    for prompt in prompt_list:
        t_id = "T_" + str(ii)
        final_prompt += "\t" + t_id + " : " + prompt

    final_prompt += "\n"
    final_prompt += "You will use your \"function calling\" ability to structure the output. "
    final_prompt += "When you are preparing the function invocation, please create an argument for each task. "
    final_prompt += "In the output, populate the fields which start with \"T_\" with the corresponding task prompt, and populate the fields which start with \"R_\" with your corresponding response."

    arg_props = {}
    required_props = []

    # Metadata
    # arg_props["initial_prompt"] = {"type": "string"}
    # required_props.append("initial_prompt")

    ii = 0
    for _ in prompt_list:
        ii += 1
        t_id = "T_" + str(ii)
        r_id = "R_" + str(ii)
        arg_props[t_id] = {"type": "string"}
        arg_props[r_id] = {"type": "string"}
        required_props.append(t_id)
        required_props.append(r_id)

    func_sig = generate_function_signature(arg_props, required_props, func_name="anonymous_function")

    return final_prompt, func_sig

def extract_and_reassemble_fragmented_func_results(tool_calls):
    ret_vals = {}
    for tool_call in tool_calls:
        func_args = json.loads(tool_call.function.arguments)
        for the_aarg in func_args:
            ret_vals[the_aarg] = func_args[the_aarg]

    return ret_vals


################################################################################
# Function signature definitions for controlling responses =====================
################################################################################

def generate_function_signature(arg_props, required_props, func_name="anonymous_function"):
    func_sig = {
        "name": func_name,
        "parameters": {
            "type": "object",
            "properties": arg_props,
            "required": required_props
        }
    }

    the_lambda = lambda:func_sig

    return the_lambda

