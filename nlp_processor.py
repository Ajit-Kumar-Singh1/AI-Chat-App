import re
from patterns import patterns

def interpret_input(user_input):
    """
    This function interprets the user's natural language input and determines
    if it should be translated into a SQL query, handled by the Meta-Llama model,
    or provide a predefined system context response.
    """
    for action, data in patterns.items():
        pattern = data['pattern']
        match = re.search(pattern, user_input, re.IGNORECASE)
        if match:
            if 'query_template' in data:
                # Handle SQL query patterns
                sql_query = data['query_template'].format(*match.groups())
                return ('sql', sql_query)
            elif 'response' in data:
                # Handle system context responses
                return ('context', data['response'])
    
    # If no patterns matched, return as a general query for Meta-Llama
    return ('llama', user_input)
