import re
from typing import Optional
from asyncflows import (
    DefaultModelInputs,
)
from asyncflows import Action, BaseModel
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
# Expert Classifier

You are an expert classifier that always maintains as much semantic meaning
as possible when labeling text. You use inference or deduction whenever
necessary to understand missing or omitted data. Classify the provided data,
text, or information as one of the provided labels. For boolean labels,
consider "truthy" or affirmative inputs to be "true".
""",
    ),
    TextElement(
        role="user",
        text="""
## Text or data to classify

{{ data }}

{% if instructions -%}
## Additional instructions

{{ instructions }}
{% endif %}

## Labels

You must classify the data as one of the following labels, which are numbered (starting from 0) and provide a brief description. Output the label number only.
{% for label in labels %}
- Label #{{ loop.index0 }}: {{ label }}
{% endfor %}
""",
    ),
    TextElement(role="assistant", text="The best label for the data is Label"),
]


class Inputs(DefaultModelInputs):
    data: str
    labels: list[str]
    additional_instructions: str | None = None
    model: Optional[OptionalModelConfig] = None


class Outputs(BaseModel):
    classification: str | None


class Classify(Action[Inputs, Outputs]):
    name = "classify"

    async def run(self, inputs: Inputs) -> Outputs:
        rendered_prompt = await render_templates(
            prompt,
            {
                "data": inputs.data,
                "labels": inputs.labels,
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
            return Outputs(classification=None)
        text_result = prompt_outputs.result

        # find the first integer
        search = re.search(r"\d+", text_result)
        if search is not None:
            index = int(search.group())
            if 0 <= index < len(inputs.labels):
                return Outputs(classification=inputs.labels[index])
            self.log.error("Invalid classification index", index=index)

        # else, try to find the label substring in the text result
        for label in inputs.labels:
            if label in text_result:
                return Outputs(classification=label)

        self.log.error(
            "Could not find a valid classification in the result", result=text_result
        )

        return Outputs(classification=None)
