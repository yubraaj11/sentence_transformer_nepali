import gradio as gr
from sentence_transformers import SentenceTransformer
import numpy as np

# Download from the 🤗 Hub
model = SentenceTransformer("syubraj/sentence_similarity_nepali_v2")

def calculate_similarity(sentence1, sentence2):
    # Encode the sentences
    embeddings = model.encode([sentence1, sentence2])
    
    # Calculate cosine similarity
    similarity = np.dot(embeddings[0], embeddings[1]) / (np.linalg.norm(embeddings[0]) * np.linalg.norm(embeddings[1]))
    
    return f"Similarity score: {similarity:.4f}"

# Define example inputs
examples = [
    ["रातो, डबल डेकर बस।", "रातो डबल डेकर बस।"],
    ["दुई कालो कुकुर हिउँमा हिंड्दै।", "तीन सेतो बिरालो घाँसमा बसिरहेको।"],
    ["आज मौसम सफा र घाम लागेको छ।", "आकाश निलो र घाम चम्किलो छ।"],
]

# Create Gradio interface
iface = gr.Interface(
    fn=calculate_similarity,
    inputs=[
        gr.Textbox(label="Enter the first sentence:"),
        gr.Textbox(label="Enter the sentence to compare:")
    ],
    outputs=gr.Textbox(label="Result"),
    title="Nepali Sentence Similarity Calculator",
    description="Compare the similarity between two Nepali sentences using the syubraj/sentence_similarity_nepali_v2 model.",
    examples=examples
)

# Launch the interface
iface.launch()