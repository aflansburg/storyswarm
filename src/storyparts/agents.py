from pydantic_ai import Agent
from .models import StoryPart, StoryPartConfig
from src.config import AppConfig, get_default_logger

app_config = AppConfig()
log = get_default_logger()


class StoryPartAgent:
    """
    The agent for generating the prologue of a story
    """

    def __init__(
        self,
        *,
        config: StoryPartConfig,
        part: StoryPart,
    ):
        self.config = config

        if self.config.system_prompt:
            log.info("Using system prompt from config.")
            system_prompt = self.config.system_prompt
        else:
            log.info("Using system prompt from defaults.")
            system_prompt = app_config.defaults["agents"][
                self.config.part.part_type.name
            ]["system_prompt"]

        self.agent = Agent(
            model=self.config.llm,
            system_prompt=system_prompt,
        )

        self.part = part

    async def generate_part(self) -> StoryPart:
        """
        Generate a part of the story

        :return: The generated part of the story
        """
        generated_part = None

        for _ in range(self.config.num_iterations):
            prepends = (
                f"This was the previous content that you generated, please make any improvements to it: {generated_part}"
                if generated_part
                else ""
            )
            generated_part = await self.agent.run(
                user_prompt=(
                    f"{prepends}"
                    f"Generate the {self.part.part_type.name} of the story using the following information:"
                    f"Title: {self.config.title}"
                    f"Characters: {self.config.characters}"
                    f"Plot: {self.config.plot}"
                    f"Tone: {self.config.tone}"
                    f"Style: {self.config.style}"
                )
            )

        return generated_part
