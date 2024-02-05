import gradio as gr
import google.generativeai as genai

# Configure the Google Generative AI API key
genai.configure(api_key='AIzaSyCpwqVPdsR4QCfp6AvR7dozl0lMpri6hSI')  # Replace with your API key

# List available models and select the first one that supports text generation
models = [m for m in genai.list_models() if 'generateText' in m.supported_generation_methods]
model = models[0].name if models else None

# Initialize search history list
search_history = []

# Define the code generation function
def generate_code(prompt):
    result = genai.generate_text(model=model, prompt=prompt, temperature=0.8, max_output_tokens=200).result if model else "No suitable models found."
    
    # Add the current search to history
    search_history.append((prompt, result))
    
    return result

# Create the Gradio interface with custom style and HTML block
with gr.Blocks(css=".gradio-container {background-color: white;}") as demo:
    # Custom HTML block
    gr.HTML("<h1 style='color: purple;'>Code Generation Assistant</h1>")
    
    # Gradio Textbox for user input
    prompt = gr.Textbox(placeholder="Enter your prompt", label="Prompt")
    
    # Gradio Textbox for displaying generated code
    output = gr.Textbox(label="Generated Code")
    
    # Gradio Button for triggering code generation
    generate_btn = gr.Button("Generate Code")
    generate_btn.click(generate_code, inputs=prompt, outputs=output, api_name="generate_code")
    

    
# Launch the Gradio interface
demo.launch()
