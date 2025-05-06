# storyswarm backend

This is a simple [FastAPI](https://fastapi.tiangolo.com/) backend that leverages [Pydantic AI](https://ai.pydantic.dev/) to write a story, part by part, with special purpose agents.

Very much a work in process (for fun).

Currently, only the Prologue agent is implemented.

There is no auth for this API yet.

For most LLMs, providing your API key in an `env.local` file is sufficient enough.
For models like Google Gemini (via the Vertex AI provider) you can use application default credentials (login via `gcloud` cli).

Hoping to build a simple frontend for this as well in the near future.

## Getting started
1. Clone the repo
2. `uv venv`
3. `source .venv/bin/activate`
4. `uv python install`
5. `uv python sync`
6. `uv run app.py` (or use the included `launch.json` if debugging in vscode)
7. Profit 💰

## Making a call to generate a story

### Example JSON payload to generate a Prologue
```json
{
	"llm": "openai:gpt-4o-mini",
	"user_prompt": "Write a prologue about a mystical land that was accidentally devastated by alien visitors. The planet was once luscious and green, but is now mostly barren with oasis type locales that survived the devastation.",
	"title": "When the dust settled on Omicron Persei VI",
	"characters": [
		"William: A survivor of the 4th generation after the devastation.",
		"ID10T: A witty robot with a hilarious name, left behind by the precursor."
	],
	"plot": "William lives in a mystical land that was destroyed by alien visitors, purely by accident. Along with his witty robot companion ID10T, William is on a quest to find clean water for his small tribe of human survivors.",
	"tone": "mystical and magical, yet sci-fi, with humor, but not too much. Not too dry, not too wet.",
	"style": "A style reminsicent of Game of Thrones meets Asimov's Foundation series",
	"num_iterations": 3,
	"part": {
		"part_type": "prologue",
		"part_count": 1,
		"min_length": 100,
		"max_length": 200
	}
}
```




