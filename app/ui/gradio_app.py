import gradio as gr
import requests
import os

API_URL = os.environ.get("API_URL", "http://flask-api:5000")

def book_ticket(name, event):
    return requests.post(f"{API_URL}/book", json={"name": name, "event": event}).json()

def view_ticket(ticket_id):
    return requests.get(f"{API_URL}/view/{ticket_id}").json()

def cancel_ticket(ticket_id):
    return requests.delete(f"{API_URL}/cancel/{ticket_id}").json()

with gr.Blocks() as demo:
    gr.Markdown("## 🎟️ Ticket Booking System")

    with gr.Tab("Book Ticket"):
        name_input = gr.Textbox(label="Name")
        event_input = gr.Textbox(label="Event")
        book_btn = gr.Button("Book")
        book_output = gr.JSON()
        book_btn.click(book_ticket, [name_input, event_input], book_output)

    with gr.Tab("View Ticket"):
        view_input = gr.Textbox(label="Ticket ID")
        view_btn = gr.Button("View")
        view_output = gr.JSON()
        view_btn.click(view_ticket, view_input, view_output)

    with gr.Tab("Cancel Ticket"):
        cancel_input = gr.Textbox(label="Ticket ID")
        cancel_btn = gr.Button("Cancel")
        cancel_output = gr.JSON()
        cancel_btn.click(cancel_ticket, cancel_input, cancel_output)

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860)
