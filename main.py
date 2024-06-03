import signal
import sys
from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
import db_connect
import llama_api
import nlp_processor

app = FastAPI()

api_key = "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"

def generate_html_table(data):
    """Generate HTML table from a list of tuples."""
    if not data:
        return "<p>No results found.</p>"

    table = "<div class='table-responsive'><table class='table table-striped'>"
    headers = [desc[0] for desc in data[0].cursor_description]
    table += "<thead><tr>" + "".join(f"<th>{header}</th>" for header in headers) + "</tr></thead>"
    table += "<tbody>"
    for row in data:
        table += "<tr>" + "".join(f"<td>{cell}</td>" for cell in row) + "</tr>"
    table += "</tbody></table></div>"
    
    return table

@app.get("/", response_class=HTMLResponse)
async def get_form():
    return """
    <!DOCTYPE html>
    <html>
        <head>
            <title>Chat Application</title>
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet">
            <style>
                body { padding: 20px; }
                .chat-container { max-width: 800px; margin: auto; }
                .card { margin-bottom: 10px; }
                .response { white-space: pre-wrap; }
            </style>
        </head>
        <body>
            <div class="container chat-container">
                <h1>Chat with CMDB Tracker database</h1>
                <form id="chat-form" action="/" method="post">
                    <div class="mb-3">
                        <label for="user_input" class="form-label">You:</label>
                        <input type="text" id="user_input" name="user_input" class="form-control" required>
                    </div>
                    <button type="submit" class="btn btn-primary">Send</button>
                </form>
                <div id="chat-response" class="mt-4"></div>
            </div>
            <script>
                document.getElementById("chat-form").onsubmit = async (event) => {
                    event.preventDefault();
                    const userInput = document.getElementById("user_input").value;
                    const responseContainer = document.getElementById("chat-response");

                    const response = await fetch("/", {
                        method: "POST",
                        body: new FormData(event.target)
                    });

                    const text = await response.text();
                    responseContainer.innerHTML = `
                        <div class="card">
                            <div class="card-body">
                                <h5 class="card-title">You:</h5>
                                <p class="card-text">${userInput}</p>
                            </div>
                        </div>
                        <div class="card">
                            <div class="card-body">
                                <h5 class="card-title">Response:</h5>
                                <div class="card-text response">${text}</div>
                            </div>
                        </div>
                    `;
                    document.getElementById("user_input").value = "";
                };
            </script>
        </body>
    </html>
    """

@app.post("/", response_class=HTMLResponse)
async def handle_form(user_input: str = Form(...)):
    action, query_or_prompt = nlp_processor.interpret_input(user_input)
    
    response = ""
    
    if action == 'sql':
        try:
            db_response = db_connect.query_db(query_or_prompt)
            description = f"<p>The following results were retrieved for your query: <code>{query_or_prompt}</code></p>"
            response = description + generate_html_table(db_response)
        except Exception as e:
            response = f"<p>Database query failed: {e}</p>"
    elif action == 'context':
        response = f"<p>{query_or_prompt}</p>"
    else:
        try:
            llama_response = llama_api.query_huggingface_inference(api_key, query_or_prompt)
            description = f"<p>The Meta-Llama model responded to your input: <code>{user_input}</code></p>"
            response = description + f"<p>Llama: {llama_response}</p>"
        except Exception as e:
            response = f"<p>Meta-Llama query failed due to an error. Please try again later.</p><p>Error: {e}</p>"
    
    return response

if __name__ == "__main__":
    import uvicorn
    from multiprocessing import Process

    def run_server():
        uvicorn.run(app, host="0.0.0.0", port=8000)

    server_process = Process(target=run_server)
    server_process.start()

    def signal_handler(sig, frame):
        print('Stopping server...')
        server_process.terminate()
        server_process.join()
        sys.exit(0)

    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)

    signal.pause()
