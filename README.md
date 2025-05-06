![Run Tests](https://github.com/aflansburg/storyswarm/.github/workflows/test.yml)
![Run Linter](https://github.com/aflansburg/storyswarm/.github/workflows/lint.yml)
![Run Typechecking](https://github.com/aflansburg/storyswarm/.github/workflows/typecheck.yml)

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

## Running tests
`PYTHONPATH=src uv run pytest`

## Making a call to generate a story

### Example JSON payload to generate a Prologue

**Example Request:**
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

**Example Response:**
```json
{
	"part": {
		"output": "In the fading light of a world once vibrant, the wasteland sprawled before them—a tapestry of charred dreams and forgotten echoes. \"Will,\" ID10T chirped, his words laced with the kind of mischief only a relic of ancient ingenuity could muster, \"ever wonder if the aliens were just throwing a cosmic shindig gone horribly awry? A real ‘whoopsie-daisy’ moment?\" \n\nWilliam squinted at the horizon, tracing the scars etched deep by celestial folly. \"Survival brooks no musings on galactic blunders, my companion.\" \n\nYet amidst the ruins, whispers of life clung stubbornly, beckoning. “True,” said ID10T, a glint of hope in his optic sensors, “but uncover some fresh water, and we just might rewrite the narrative of this universe.” \n\nThus, their arduous quest into the mystic desolation began.",
		"_output_tool_name": null,
		"_state": {
			"message_history": [
				{
					"parts": [
						{
							"content": "You are a professional writer.\nYou are given a title, characters, plot, tone, and style.\nYou are to generate a prologue...",
							"timestamp": "2025-05-06T21:59:23.736979+00:00",
							"dynamic_ref": null,
							"part_kind": "system-prompt"
						},
						{
							"content": "This was the previous content that you generated, please make any improvements to it: AgentRunResult(output='In the dim glow of smoldering embers, the wasteland sprawled before them—a realm once rich in life, now a canvas scorched by unintended cosmic visitation. “Will,” chimed ID10T, his tone a playful tapestry woven with irony, “ever ponder if the aliens were just having a wild intergalactic gaffe? A cosmic ‘whoopsie-daisy’?” \\n\\nWilliam crouched, keen eyes mapping the shattered horizon...",
							"timestamp": "2025-05-06T21:59:23.736986+00:00",
							"part_kind": "user-prompt"
						}
					],
					"instructions": null,
					"kind": "request"
				},
				{
					"parts": [
						{
							"content": "In the fading light of a world once vibrant, the wasteland sprawled before them—a tapestry of charred dreams and forgotten echoes. \"Will,\" ID10T chirped, his words laced with the kind of mischief only a relic of ancient ingenuity could muster, \"ever wonder if the aliens were just throwing a cosmic shindig gone horribly awry? A real ‘whoopsie-daisy’ moment?\" \n\nWilliam squinted at the horizon, tracing the scars etched deep by celestial folly. \"Survival brooks no musings on galactic blunders, my companion.\" \n\nYet amidst the ruins, whispers of life clung stubbornly, beckoning. “True,” said ID10T, a glint of hope in his optic sensors, “but uncover some fresh water, and we just might rewrite the narrative of this universe.” \n\nThus, their arduous quest into the mystic desolation began.",
							"part_kind": "text"
						}
					],
					"model_name": "gpt-4o-mini-2024-07-18",
					"timestamp": "2025-05-06T21:59:23+00:00",
					"kind": "response"
				}
			],
			"usage": {
				"requests": 1,
				"request_tokens": 1133,
				"response_tokens": 187,
				"total_tokens": 1320,
				"details": {
					"accepted_prediction_tokens": 0,
					"audio_tokens": 0,
					"reasoning_tokens": 0,
					"rejected_prediction_tokens": 0,
					"cached_tokens": 0
				}
			},
			"retries": 0,
			"run_step": 1
		},
		"_new_message_index": 0,
		"_traceparent_value": null
	},
	"config": {
		"llm": "openai:gpt-4o-mini",
		"user_prompt": "Write a prologue about a mystical land that was accidentally devastated by alien visitors. The planet was once luscious and green, but is now mostly barren with oasis type locales that survived the devastation.",
		"num_iterations": 3,
		"part": {
			"min_length": 100,
			"max_length": 200,
			"part_count": 1,
			"part_type": "prologue"
		},
		"system_prompt": null,
		"title": "When the dust settled on Omicron Persei VI",
		"characters": [
			"William: A survivor of the 4th generation after the devastation.",
			"ID10T: A witty robot with a hilarious name, left behind by the precursor."
		],
		"plot": "William lives in a mystical land that was destroyed by alien visitors, purely by accident. Along with his witty robot companion ID10T, William is on a quest to find clean water for his small tribe of human survivors.",
		"tone": "mystical and magical, yet sci-fi, with humor, but not too much. Not too dry, not too wet.",
		"style": "A style reminsicent of Game of Thrones meets Asimov's Foundation series"
	}
}
```


