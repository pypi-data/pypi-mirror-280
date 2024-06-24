import pytest

from asyncflows_classify.actions.extract import Extract, Inputs, Outputs
from asyncflows.models.config.model import ModelConfig


@pytest.mark.parametrize(
    "inputs, expected_outputs",
    [
        (
            Inputs(
                data="I like apples and oranges",
            ),
            Outputs(entities=["apples", "oranges"]),
        ),
        (
            Inputs(
                data="I'm so happy to see you",
                additional_instructions="Extract emotions",
            ),
            Outputs(entities=["happiness"]),
        ),
        (
            Inputs(
                data="I feel a whirlwind of emotions: anger, sadness, and happiness. Anyway, do you want to go to the park or to the beach?",
                additional_instructions="Extract locations",
            ),
            Outputs(entities=["park", "beach"]),
        ),
    ],
)
@pytest.mark.slow
@pytest.mark.allow_skip
@pytest.mark.asyncio
async def test_classify(log, temp_dir, inputs, expected_outputs):
    inputs._default_model = ModelConfig(
        model="ollama/llama3",
    )
    action = Extract(log=log, temp_dir=temp_dir)
    outputs = await action.run(inputs)
    assert outputs == expected_outputs
