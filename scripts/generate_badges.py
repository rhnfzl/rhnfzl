"""
Generate shields.io badge markdown for GitHub profile README.

Usage:
    python scripts/generate_badges.py > /tmp/tech_stack_badges.md

All badges use for-the-badge style. Tools without Simple Icons entries
get custom base64-encoded SVG logos.
"""

import base64


def b64(svg: str) -> str:
    return base64.b64encode(svg.encode()).decode()


def badge(label: str, color: str, logo_type: str, logo_val: str, logo_color: str = "white") -> str:
    """Generate a shields.io badge img tag.

    Args:
        label: Badge text (use -- for hyphens, %20 for spaces)
        color: Hex color without #
        logo_type: "si" for Simple Icons slug, "b64" for custom SVG
        logo_val: Simple Icons slug or raw SVG string
        logo_color: Logo color override (only for Simple Icons)
    """
    label_enc = label.replace("-", "--").replace(" ", "%20")
    url = f"https://img.shields.io/badge/{label_enc}-{color}?style=for-the-badge"
    if logo_type == "si":
        url += f"&logo={logo_val}&logoColor={logo_color}"
    elif logo_type == "b64":
        encoded = b64(logo_val)
        url += f"&logo=data:image/svg%2bxml;base64,{encoded}"
    return f'  <img src="{url}" alt="{label}"/>'


# Custom SVG icons for tools without Simple Icons entries
# All icons are white fill, 24x24 viewBox
CUSTOM_SVGS = {
    # OpenAI - hexagonal knot logo
    "openai": '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="white"><path d="M22.282 9.821a5.985 5.985 0 0 0-.516-4.91 6.046 6.046 0 0 0-6.51-2.9A6.065 6.065 0 0 0 4.981 4.18a5.985 5.985 0 0 0-3.998 2.9 6.046 6.046 0 0 0 .743 7.097 5.98 5.98 0 0 0 .51 4.911 6.051 6.051 0 0 0 6.515 2.9A5.985 5.985 0 0 0 13.26 24a6.056 6.056 0 0 0 5.772-4.206 5.99 5.99 0 0 0 3.997-2.9 6.056 6.056 0 0 0-.747-7.073zM13.26 22.43a4.476 4.476 0 0 1-2.876-1.04l.141-.081 4.779-2.758a.795.795 0 0 0 .392-.681v-6.737l2.02 1.168a.071.071 0 0 1 .038.052v5.583a4.504 4.504 0 0 1-4.494 4.494zM3.6 18.304a4.47 4.47 0 0 1-.535-3.014l.142.085 4.783 2.759a.771.771 0 0 0 .78 0l5.843-3.369v2.332a.08.08 0 0 1-.033.062L9.74 19.95a4.5 4.5 0 0 1-6.14-1.646zM2.34 7.896a4.485 4.485 0 0 1 2.366-1.973V11.6a.766.766 0 0 0 .388.676l5.815 3.355-2.02 1.168a.076.076 0 0 1-.071 0l-4.83-2.786A4.504 4.504 0 0 1 2.34 7.872zm16.597 3.855l-5.833-3.387L15.119 7.2a.076.076 0 0 1 .071 0l4.83 2.791a4.494 4.494 0 0 1-.676 8.105v-5.678a.79.79 0 0 0-.407-.667zm2.01-3.023l-.141-.085-4.774-2.782a.776.776 0 0 0-.785 0L9.409 9.23V6.897a.066.066 0 0 1 .028-.061l4.83-2.787a4.5 4.5 0 0 1 6.68 4.66zm-12.64 4.135l-2.02-1.164a.08.08 0 0 1-.038-.057V6.075a4.5 4.5 0 0 1 7.375-3.453l-.142.08L8.704 5.46a.795.795 0 0 0-.393.681zm1.097-2.365l2.602-1.5 2.607 1.5v2.999l-2.597 1.5-2.607-1.5z"/></svg>',

    # Sentence-Transformers - molecular graph (based on sbert.net logo)
    "sbert": '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="white"><circle cx="12" cy="4" r="2"/><circle cx="18" cy="7" r="2"/><circle cx="18" cy="14" r="2"/><circle cx="12" cy="17" r="2"/><circle cx="6" cy="14" r="2"/><circle cx="6" cy="7" r="2"/><line x1="12" y1="4" x2="18" y2="7" stroke="white" stroke-width="1.5"/><line x1="18" y1="7" x2="18" y2="14" stroke="white" stroke-width="1.5"/><line x1="18" y1="14" x2="12" y2="17" stroke="white" stroke-width="1.5"/><line x1="12" y1="17" x2="6" y2="14" stroke="white" stroke-width="1.5"/><line x1="6" y1="14" x2="6" y2="7" stroke="white" stroke-width="1.5"/><line x1="6" y1="7" x2="12" y2="4" stroke="white" stroke-width="1.5"/></svg>',

    # DeepSpeed - lightning bolt (speed)
    "deepspeed": '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="white"><path d="M13 0L3 14h7v10l10-14h-7z"/></svg>',

    # ChromaDB - overlapping circles (color/chroma)
    "chromadb": '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="white"><circle cx="8" cy="9" r="5.5" opacity="0.7"/><circle cx="16" cy="9" r="5.5" opacity="0.5"/><circle cx="12" cy="15" r="5.5" opacity="0.6"/></svg>',

    # LanceDB - downward arrow/lance
    "lancedb": '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="white"><path d="M19 2l-14 14h5v6h4v-6h5z"/></svg>',

    # Qdrant - star/point (vector search)
    "qdrant": '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="white"><path d="M12 0l3 9h9l-7.5 5.5L19.5 24 12 18l-7.5 6 3-9.5L0 9h9z"/></svg>',

    # LlamaIndex - llama silhouette
    "llamaindex": '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="white"><path d="M17 3c-1.5 0-3 1-4 2.5C11.5 4 10.5 3 9 3 6 3 4 6 4 9c0 2 .8 3.5 2 5v6c0 1.1.9 2 2 2h8c1.1 0 2-.9 2-2v-6c1.2-1.5 2-3 2-5 0-3-2-6-3-6zm-7 5a1 1 0 1 1 0 2 1 1 0 0 1 0-2zm4 0a1 1 0 1 1 0 2 1 1 0 0 1 0-2z"/></svg>',

    # Instructor - info circle (structured output)
    "instructor": '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="white"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm1 15h-2v-6h2v6zm0-8h-2V7h2v2z"/></svg>',

    # NLTK - text lines (NLP)
    "nltk": '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="white"><path d="M3 4h18v2H3zm0 4h14v2H3zm0 4h18v2H3zm0 4h10v2H3zm0 4h14v2H3z"/></svg>',

    # Langfuse - monitoring sparkline
    "langfuse": '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="white"><path d="M3 20h18v1H3zm0-3l4-5 3 3 5-7 5 6v2H3z"/></svg>',

    # SageMaker - lightbulb with ML spark
    "sagemaker": '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="white"><path d="M12 2a7 7 0 0 0-7 7c0 2.38 1.19 4.47 3 5.74V17a2 2 0 0 0 2 2h4a2 2 0 0 0 2-2v-2.26c1.81-1.27 3-3.36 3-5.74a7 7 0 0 0-7-7zm-1 9H8l4-5v4h3l-4 5V11zM9 20v1a1 1 0 0 0 1 1h4a1 1 0 0 0 1-1v-1H9z"/></svg>',

    # IBM - simplified horizontal stripes
    "ibm": '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="white"><path d="M0 3h8v2H0zm10 0h4v2h-4zm6 0h8v2h-8zM0 7h4v2h4V7h2v2h4V7h2v2h4V7h4v2h-4v2h4v2h-8v-2h-2v2H6v-2H4v2H0v-2h4V9H0zm0 12h8v2H0zm10 0h4v2h-4zm6 0h8v2h-8z"/></svg>',

    # AWS - cloud icon
    "aws": '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="white"><path d="M18.75 11.35a4.32 4.32 0 0 0 .15-1.14c0-2.57-2.1-4.65-4.7-4.65-2.08 0-3.86 1.34-4.48 3.2a3.58 3.58 0 0 0-1.54-.35c-1.97 0-3.56 1.55-3.56 3.47 0 .24.03.47.07.7A3.77 3.77 0 0 0 1 16.2c0 2.1 1.73 3.8 3.87 3.8h12.26c1.77 0 3.2-1.4 3.2-3.14 0-1.52-1.1-2.78-2.58-3.08z"/></svg>',
}


def generate_tech_stack() -> str:
    lines = []

    # Core ML & AI
    lines.append('<p align="center">')
    lines.append('  <strong>Core ML & AI</strong><br/><br/>')
    lines.append(badge("Python", "3776AB", "si", "python"))
    lines.append(badge("PyTorch", "EE4C2C", "si", "pytorch"))
    lines.append(badge("TensorFlow", "FF6F00", "si", "tensorflow"))
    lines.append(badge("NumPy", "013243", "si", "numpy"))
    lines.append(badge("Pandas", "150458", "si", "pandas"))
    lines.append(badge("scikit-learn", "F7931E", "si", "scikit-learn"))
    lines.append(badge("HuggingFace", "FFD21E", "si", "huggingface", "black"))
    lines.append(badge("ONNX", "005CED", "si", "onnx"))
    lines.append(badge("spaCy", "09A3D5", "si", "spacy"))
    lines.append(badge("Sentence-Transformers", "FF6F00", "b64", CUSTOM_SVGS["sbert"]))
    lines.append(badge("DeepSpeed", "0078D4", "b64", CUSTOM_SVGS["deepspeed"]))
    lines.append('</p>')
    lines.append('')

    # LLM & NLP
    lines.append('<p align="center">')
    lines.append('  <strong>LLM & NLP</strong><br/><br/>')
    lines.append(badge("OpenAI", "412991", "b64", CUSTOM_SVGS["openai"]))
    lines.append(badge("Anthropic", "191919", "si", "anthropic"))
    lines.append(badge("LangChain", "1C3C3C", "si", "langchain"))
    lines.append(badge("FAISS", "0467DF", "si", "meta"))
    lines.append(badge("ChromaDB", "FF6446", "b64", CUSTOM_SVGS["chromadb"]))
    lines.append(badge("LanceDB", "4B0082", "b64", CUSTOM_SVGS["lancedb"]))
    lines.append(badge("Qdrant", "DC382D", "b64", CUSTOM_SVGS["qdrant"]))
    lines.append(badge("Pydantic AI", "E92063", "si", "pydantic"))
    lines.append(badge("LlamaIndex", "6F42C1", "b64", CUSTOM_SVGS["llamaindex"]))
    lines.append(badge("CrewAI", "FF4B4B", "si", "crewai"))
    lines.append(badge("Instructor", "191919", "b64", CUSTOM_SVGS["instructor"]))
    lines.append(badge("NLTK", "154F5B", "b64", CUSTOM_SVGS["nltk"]))
    lines.append('</p>')
    lines.append('')

    # Infrastructure & DevOps
    lines.append('<p align="center">')
    lines.append('  <strong>Infrastructure & DevOps</strong><br/><br/>')
    lines.append(badge("AWS", "232F3E", "b64", CUSTOM_SVGS["aws"]))
    lines.append(badge("Docker", "2496ED", "si", "docker"))
    lines.append(badge("FastAPI", "009688", "si", "fastapi"))
    lines.append(badge("Linux", "FCC624", "si", "linux", "black"))
    lines.append(badge("Redis", "DC382D", "si", "redis"))
    lines.append(badge("PostgreSQL", "4169E1", "si", "postgresql"))
    lines.append(badge("MySQL", "4479A1", "si", "mysql"))
    lines.append(badge("Cassandra", "1287B1", "si", "apachecassandra"))
    lines.append(badge("Git", "F05032", "si", "git"))
    lines.append(badge("GitHub Actions", "2088FF", "si", "githubactions"))
    lines.append(badge("DB2", "054ADA", "b64", CUSTOM_SVGS["ibm"]))
    lines.append(badge("Celery", "37814A", "si", "celery"))
    lines.append(badge("Kubernetes", "326CE5", "si", "kubernetes"))
    lines.append(badge("Gunicorn", "499848", "si", "gunicorn"))
    lines.append('</p>')
    lines.append('')

    # Tools & Platforms
    lines.append('<p align="center">')
    lines.append('  <strong>Tools & Platforms</strong><br/><br/>')
    lines.append(badge("Streamlit", "FF4B4B", "si", "streamlit"))
    lines.append(badge("SageMaker", "FF9900", "b64", CUSTOM_SVGS["sagemaker"]))
    lines.append(badge("MLflow", "0194E2", "si", "mlflow"))
    lines.append(badge("W&B", "FFBE00", "si", "weightsandbiases", "black"))
    lines.append(badge("Langfuse", "000000", "b64", CUSTOM_SVGS["langfuse"]))
    lines.append(badge("Plotly", "3F4F75", "si", "plotly"))
    lines.append(badge("Pydantic", "E92063", "si", "pydantic"))
    lines.append(badge("Ruff", "D7FF64", "si", "ruff", "black"))
    lines.append('</p>')

    return '\n'.join(lines)


if __name__ == "__main__":
    print(generate_tech_stack())
