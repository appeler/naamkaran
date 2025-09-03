import gradio as gr

from naamkaran.generate import generate_names


def gen_names(start_letter, end_letter, how_many, max_length, gender, temperature):
    """
    Generates names for the given inputs.
    """
    if len(end_letter) > 1:
        end_letter = end_letter[0]
    if len(start_letter) > 1:
        start_letter = start_letter[0]
    if len(start_letter) < 1:
        start_letter = "a"
    if len(end_letter) < 1:
        end_letter = None
    if int(max_length) < 1:
        max_length = 5
    if int(how_many) < 1:
        how_many = 1

    names = generate_names(
        start_letter, end_letter, int(how_many), int(max_length), gender, temperature
    )
    return ", ".join(names)


iface = gr.Interface(
    fn=gen_names,
    inputs=[
        gr.components.Text(value="A", label="Starting letter (default: 'A')"),
        gr.components.Text(value="e", label="Ending letter (default: None)"),
        gr.components.Number(value=5, label="How many to generate (default: 1)"),
        gr.components.Number(value=5, label="Max length of the name (default: 5)"),
        gr.components.Radio(["M", "F"], label="Gender", value="F"),
        gr.components.Slider(0.1, 1, step=0.1, label="Temperature", value=0.5),
    ],
    outputs=gr.components.Textbox(lines=10, label="Names"),
    title="Naamkaran",
    description="Generate names for the given below inputs",
    article="Naamkaran is a library to generate random names.",
    flagging_mode="never",
    examples=[
        ["a", "n", 1, 5, "M", 0.5],
        ["a", "n", 1, 5, "F", 0.5],
    ],
)

if __name__ == "__main__":
    iface.launch()
