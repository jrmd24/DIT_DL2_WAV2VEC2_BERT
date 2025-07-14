import gradio as gr

import audiospeechsentimentanalysis_jrmdiouf as assaj


def find_sentiment(input):
    return assaj.get_audio_sentiment(input)


with gr.Blocks() as demo:
    gr.Markdown(
        "<h1 style='text-align: center;'>CUSTOM MODEL BASED ON WAV2VEC2 AND BERT BASE TO ANALYZE SPEECH SENTIMENT</h1>"
    )

    gr.Interface(
        fn=find_sentiment,
        inputs=[gr.Audio(type="filepath")],
        outputs=["text"],
        live=False,
    )

    gr.Markdown(
        "<h2 style='text-align: center;'>Speech sentiment analysis model loss during training and eval time</h2>"
    )

    with gr.Row():
        gr.Image(value="wandb_chart_train.png", label="Training Loss", width=300)
        gr.Image(value="wandb_chart_eval.png", label="Pipeline eval Loss", width=300)

    gr.Markdown(
        "<h2 style='text-align: center;'>Confusion matrix obtained from model evaluation on VoxCeleb dataset</h2>"
    )

    with gr.Row():
        gr.Image(
            value="SpeechSentimentModelConfusionMatrix.png",
            label="Confusion Matrix from model evaluation",
        )

    with gr.Row():
        gr.Markdown(
            "<h3><span style='text-decoration:underline;'>Pipeline Accuracy</span> : <span style='font-style:italic;'>0.758</span></h3>"
        )


demo.launch(share=True)
