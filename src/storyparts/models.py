from enum import Enum

from pydantic import BaseModel


# ----- Scope: StoryPart Types -----


class PartType(Enum):
    """
    The type of segment in a story part
    """

    prologue = "prologue"
    chapter = "chapter"
    epilogue = "epilogue"


class StoryPart(BaseModel):
    """
    The base part class of a story
    """

    min_length: int
    max_length: int
    part_count: int
    part_type: PartType


class Prologue(StoryPart):
    """
    The prologue part of a story
    """

    part_type: PartType = PartType.prologue
    part_count: int = 1


class Chapter(StoryPart):
    """
    The chapter part of a story
    """

    part_type: PartType = PartType.chapter
    part_count: int = 4


class Epilogue(StoryPart):
    """
    The epilogue part of a story
    """

    part_type: PartType = PartType.epilogue
    part_count: int = 2


# ----- End of Scope: StoryPart Models -----


# ----- Scope: StoryPart Agents Configs -----


class StoryPartConfig(BaseModel):
    """
    The parent class for all story part agents
    """

    llm: str
    user_prompt: str
    num_iterations: int = 1
    part: StoryPart
    system_prompt: str | None = None
    title: str
    characters: list[str]  # example "William: He is a blacksmith"
    plot: str
    tone: str
    style: str


# ----- End of Scope: StoryPart Agents Configs -----
