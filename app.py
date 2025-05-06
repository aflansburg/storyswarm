import os
from fastapi import FastAPI, Request, HTTPException
from pydantic_ai.models import KnownModelName
from typing import get_args

from dotenv import load_dotenv

if os.path.exists(".env.local"):
    load_dotenv(dotenv_path=".env.local")

from src.config import AppConfig, get_default_logger
from src.storyparts import Prologue, Chapter, Epilogue
from src.storyparts.agents import StoryPartAgent
from src.storyparts.models import StoryPartConfig

log = get_default_logger()

app_config = AppConfig()

app = FastAPI()

log.debug(
    "\n======== App Config ======== \n"
    f"{'\n'.join([f'{k}: {v}' for k, v in app_config.__dict__.items()])}"
    "\n======== End of App Config ======== "
)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/models/list")
async def list_models():
    all_models = [
        model
        for model in list(get_args(KnownModelName.__value__))
        if "test" not in model
    ]
    return {"all_models": all_models}


@app.post("/part/generate")
async def _generate_part(request: Request):
    """
    Generate a part of the story

    Args:
        request: The request object

    Returns:
        The generated part of the story
    """
    try:
        data = await request.json()
        part_definition = data["part"]

        match part_definition["part_type"]:
            case "prologue":
                part = Prologue(**part_definition)
            case "chapter":
                return {"message": "Chapter generation not implemented yet"}
                # part = Chapter(**part_definition)
            case "epilogue":
                return {"message": "Epilogue generation not implemented yet"}
                # part = Epilogue(**part_definition)
        part_config = StoryPartConfig(**data)
        part_agent = StoryPartAgent(config=part_config, part=part)
        part = await part_agent.generate_part()
        return {"part": part, "config": part_config}
    except Exception as e:
        log.error(f"Error generating part: {e}")
        raise HTTPException(status_code=500, detail=str(e))
