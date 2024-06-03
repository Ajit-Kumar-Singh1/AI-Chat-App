import db_connect
import llama_api
import nlp_processor

def main():
    api_key = "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"
    
    print("Welcome to the chat application! Type 'exit' or 'quit' to end the chat.")
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() in ['exit', 'quit']:
            break
        
        action, query_or_prompt = nlp_processor.interpret_input(user_input)
        
        if action == 'sql':
            # Execute the SQL query
            try:
                db_response = db_connect.query_db(query_or_prompt)
                if db_response:
                    print("Database Response:")
                    for row in db_response:
                        print(row)
                else:
                    print("No results found for the query.")
            except Exception as e:
                print(f"Database query failed: {e}")
        elif action == 'context':
            print(f"Response: {query_or_prompt}")
        else:
            # Send the input to Meta-Llama
            try:
                llama_response = llama_api.query_huggingface_inference(api_key, query_or_prompt)
                print(f"Llama: {llama_response}")
            except Exception as e:
                print(f"Meta-Llama query failed: {e}")

if __name__ == "__main__":
    main()
