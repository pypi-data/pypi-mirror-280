from typing import Any, Sequence
from asyncflows.actions.utils.prompt_context import TextElement
from asyncflows.models.config.value_declarations import (
    TextDeclaration,
    # ConstDeclaration,
)

from asyncflows.actions.utils.prompt_context import (
    PromptElement,
)


async def render_templates(
    prompt_elements: Sequence[PromptElement], context: dict[str, Any]
) -> list[PromptElement]:
    new_list = []
    for element in prompt_elements:
        if isinstance(element, TextElement):
            element = TextElement(
                role=element.role,
                text=await TextDeclaration(text=element.text).render(context),
            )
        new_list.append(element)
    return new_list
