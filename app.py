import gradio as gr
from PIL import Image
import pytesseract


pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'

def extract_text(image):
    extracted_text = pytesseract.image_to_string(image, lang='hin+eng+spa+fra+pan')
    return extracted_text

def keyword_search(text, keyword):
    if not keyword:
        return text
    
    words = text.split()
    return [(word, word.lower() == keyword.lower()) for word in words]

def process_image_with_search(image):
    extracted_text = extract_text(image)
    return extracted_text, gr.update(visible=True), gr.update(value="")

def search_keyword(text, keyword):
    highlighted_text = keyword_search(text, keyword)
    return gr.update(value=highlighted_text, visible=True)

def clear_outputs():
    return "", gr.update(value=None, visible=False), gr.update(visible=False), gr.update(value="")

def main():
    theme = gr.themes.Default().set(
        button_primary_background_fill="#FFA500",
        button_primary_background_fill_hover="#FF8C00",
        button_primary_text_color="white",
    )

    with gr.Blocks(theme=theme, css=".highlight { background-color: #FFA500; }") as interface:
        gr.Markdown("# TextVision 🌟")
        gr.Markdown("Upload an image, extract text, and search for keywords.")
        
        with gr.Row():
            with gr.Column(scale=1):
                image_input = gr.Image(type="pil", label="Upload Image")
                with gr.Row():
                    extract_text_button = gr.Button("Extract Text", variant="primary")
                    clear_button = gr.Button("Clear", variant="secondary")
                
                search_keyword_prompt = gr.Checkbox(label="Do you want to search for a keyword?", visible=False)
                
                with gr.Group(visible=False) as search_group:
                    keyword_input = gr.Textbox(label="Enter Keyword")
                    search_button = gr.Button("Search Keyword", variant="primary")
            
            with gr.Column(scale=2):
                extracted_text_output = gr.Textbox(label="Extracted Text", interactive=False, lines=10)
                keyword_highlighted_output = gr.HighlightedText(label="Highlighted Text", visible=False)

        extract_text_button.click(
            process_image_with_search,
            inputs=image_input,
            outputs=[extracted_text_output, search_keyword_prompt, search_group],
        )

        search_keyword_prompt.change(
            lambda val: [gr.update(visible=val), gr.update(visible=val), gr.update(visible=val)],
            inputs=search_keyword_prompt,
            outputs=[keyword_input, search_button, search_group],
        )

        clear_button.click(
            clear_outputs,
            outputs=[extracted_text_output, keyword_highlighted_output, search_group],
        )

        search_button.click(
            search_keyword,
            inputs=[extracted_text_output, keyword_input],
            outputs=keyword_highlighted_output,
        )

    interface.launch()

if __name__ == "__main__":
    main()
