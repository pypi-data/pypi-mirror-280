from typing import Optional
from asyncflows import Action, BaseModel, DefaultModelInputs
from asyncflows.actions.utils.prompt_context import TextElement
from asyncflows.models.config.model import OptionalModelConfig
from asyncflows.utils.async_utils import (
    iterator_to_coro,
)


from asyncflows.actions.prompt import Prompt, Inputs as PromptInputs

from asyncflows_classify.utils import render_templates

# adapted from PrefectHQ/marvin@95e2936:src/marvin/ai/prompts/text_prompts.py

prompt = [
    TextElement(
        role="system",
        text="""
# Expert Entity Extractor

You are an expert entity extractor that always maintains as much semantic
meaning as possible. You use inference or deduction whenever necessary to
supply missing or omitted data. Examine the provided data, text, or
information and generate a list of any entities or objects that match the
requested format.

Respond ONLY with a comma-separated list of entities
""",
    ),
    TextElement(
        role="user",
        text="""
## Data to extract

{{ data }}

{% if instructions -%} 
## Additional instructions

{{ instructions }} 
{% endif %}

## Response format

- When providing integers, do not write out any decimals at all
- Use deduction where appropriate e.g. "3 dollars fifty cents" is a single
  value [3.5] not two values [3, 50] unless the user specifically asks for
  each part.
  
Respond ONLY with a comma-separated list of entities
""",
    ),
]


class Inputs(DefaultModelInputs):
    data: str
    additional_instructions: str | None = None
    model: Optional[OptionalModelConfig] = None


class Outputs(BaseModel):
    entities: list[str] | None


class Extract(Action[Inputs, Outputs]):
    name = "extract"

    async def run(self, inputs: Inputs) -> Outputs:
        rendered_prompt = await render_templates(
            prompt,
            {
                "data": inputs.data,
                "instructions": inputs.additional_instructions,
            },
        )
        prompt_inputs = PromptInputs(
            prompt=rendered_prompt,
            model=inputs.model,
        )
        prompt_inputs._default_model = inputs._default_model

        prompt_action = Prompt(log=self.log, temp_dir=self.temp_dir)

        prompt_outputs = await iterator_to_coro(prompt_action.run(prompt_inputs))
        if prompt_outputs is None:
            self.log.error("Error invoking prompt; no outputs received")
            return Outputs(entities=None)
        text_result = prompt_outputs.result

        # extract a list of comma-separated strings from the result
        entities = [entity.strip() for entity in text_result.split(",")]

        return Outputs(entities=entities)
