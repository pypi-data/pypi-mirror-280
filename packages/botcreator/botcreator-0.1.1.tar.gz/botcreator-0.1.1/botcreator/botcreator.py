import random
import re

def botresponse(prompt, filename):
    exact_matches = []
    condition_matches = []

    with open(filename, 'r') as f:
        lines = f.readlines()

        for line in lines:
            if '/' not in line:
                continue
            index = line.rfind('/')
            prompt_part = line[:index].strip()
            response_part = line[index+1:].strip()
            responses = response_part.split('#')
            
            if '#' not in prompt_part and '&' not in prompt_part:
                exact_matches.append((prompt_part, responses))
            else:
                prompt_conditions = prompt_part.split('#')
                condition_matches.append((prompt_conditions, responses))
    
    for exact_prompt, responses in exact_matches:
        if exact_prompt == prompt:
            return random.choice(responses)
    
    for prompt_conditions, responses in condition_matches:
        for condition in prompt_conditions:
            sub_conditions = condition.split('&')
            if all(sub_condition.strip() in prompt for sub_condition in sub_conditions):
                return random.choice(responses)
    
    for exact_prompt, responses in exact_matches:
        if exact_prompt in prompt:
            return random.choice(responses)
        
    # Check for * (startswith) and ** (endswith) conditions
    for exact_prompt, responses in exact_matches:
        if exact_prompt.startswith('*'):
            if prompt.startswith(exact_prompt[1:]):
                return random.choice(responses)
        elif exact_prompt.startswith('**'):
            if prompt.endswith(exact_prompt[2:]):
                return random.choice(responses)
        elif exact_prompt.startswith('regex(') and exact_prompt.endswith(')'):
            regex_pattern = exact_prompt[len('regex('):-1]
            if re.match(regex_pattern, prompt):
                return random.choice(responses)
    
    for prompt_conditions, responses in condition_matches:
        for condition in prompt_conditions:
            if condition.startswith('*'):
                if prompt.startswith(condition[1:]):
                    return random.choice(responses)
            elif condition.startswith('**'):
                if prompt.endswith(condition[2:]):
                    return random.choice(responses)
            elif condition.startswith('regex(') and condition.endswith(')'):
                regex_pattern = condition[len('regex('):-1]
                if re.match(regex_pattern, prompt):
                    return random.choice(responses)
    
    return None