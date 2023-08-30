import gradio as gr

from naamkaran.generate import generate_names


def gen_names(start_letter, end_letter, how_many,
              max_length, gender, temperature):
    """
    Generates names for the given inputs.
    """
    names = generate_names(start_letter, end_letter, int(how_many), int(max_length), gender, temperature)
    return ", ".join(names)


iface = gr.Interface(
    fn=gen_names,
    inputs=[gr.components.Text(value="A", label="Starting letter"),
            gr.components.Text(value="e", label="Ending letter"),
            gr.components.Number(value=5, label="How many to generate"),
            gr.components.Number(value=5, label="Max length of the name"),
            gr.components.Radio(["M", "F"], label="Gender", value="F"),
            gr.components.Slider(0.1, 1, step=0.1, label='Temperature', value=0.5)],
    outputs="text",
    title="Naamkaran",
    description="Generate names for the given dataframe.",
    article="Naamkaran is a library to generate random names.",
    allow_flagging="never",
    examples=[
        ["a", "n", 1, 5, "M", 0.5],
        ["a", "n", 1, 5, "F", 0.5],
    ]
)

if __name__ == "__main__":
    iface.launch()
