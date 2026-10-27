### Hi, I'm Rehan

I'm an AI/ML research engineer in the Netherlands. I build NLP and LLM systems that turn messy, multilingual text into something a production system can match on and trust. I've been building software and data systems for 8+ years, the last 5 in machine learning and LLMs.

Lately I've been working on a tool-calling agent with an MCP server, and on the scripted conversations and A/B tests that decide whether a change ships. For fun, I'm writing an LLM from scratch and learning some Rust.

I did my MSc in Computer Science and Engineering (Data Science) at TU Eindhoven.

### Some things I've built at work

- An agentic AI assistant with a public MCP server, live in production.
- A domain-adapted embedding model that serves about 12M calls a month.
- Dutch BERT and RoBERTa models, adapted to our text with continued pretraining. Six of our classifiers run on top of them.
- An in-house LLM parser that turns documents into structured data. It beat the commercial parsers we tested, so it replaced them.
- A classifier for multilingual job titles that first finds candidates, then re-ranks them with a fine-tuned cross-encoder. The re-ranking lifted top-1 from 47% to 65% over retrieval alone.

### How I work

- I decide what "good enough" means before I test. Then I compare against what we run today, on data the model hasn't seen.
- I let the model work out what someone is asking for. Anything that has to be right, like records, permissions and business rules, stays in code.
- I don't reach for an LLM by default. A small BERT-style model, or one distilled from an LLM's answers, is often fast and cheap enough to do the job.
- I automate anything I've done twice.
- I build every day with coding agents like Claude Code, Codex, Cursor and Pi, and I review what they write.

### Open source

- [reddit-stash](https://github.com/rhnfzl/reddit-stash) backs up the Reddit posts and comments you saved, posted or upvoted, as markdown, to your disk, Dropbox or S3. It runs on GitHub Actions or Docker.
- [SqueakyCleanText](https://github.com/rhnfzl/SqueakyCleanText) is a Python library on PyPI. It cleans text and strips personal data before the text reaches a model.
- [reddit-stash-insights](https://github.com/rhnfzl/reddit-stash-insights) lets you search and ask questions of that saved Reddit archive. It mixes keyword and embedding search, runs on a local model and has an MCP server for Claude Code.
- [agent-usage-tracker](https://github.com/rhnfzl/agent-usage-tracker) reads the logs that Claude Code, Codex, Cursor and Pi already write, and turns them into usage records you host yourself. It needs no proxy and no API key, so it works with a plain subscription.
- [human-html](https://github.com/rhnfzl/human-html) is an agent skill that makes coding agents write plans and reviews as one self-contained HTML page instead of long Markdown, and checks the page before handing it over.

### Writing

<!-- WRITING:START -->
- [Belief State: a memory of what is true, not just the conversation history](https://rhnfzl.com/writing/belief-state) (Jul 2026)
<!-- WRITING:END -->

Tools I use most: Python, PyTorch, Hugging Face, sentence-transformers, FAISS, FastAPI, AWS, MLflow, MCP and vLLM.

Outside work: chai, runs, lifts and boulders, and podcasts at a speed that worries people.

I'm open to research engineering roles in NLP, retrieval and ranking, LLM systems, agents and evaluation. Happy to talk.

[rhnfzl.com](https://rhnfzl.com) · [LinkedIn](https://linkedin.com/in/rhnfzl) · [Hugging Face](https://huggingface.co/rhnfzl) · [X](https://x.com/rhnfzl) · [hey@rhnfzl.com](mailto:hey@rhnfzl.com)
