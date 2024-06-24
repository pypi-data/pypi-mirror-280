import pytest

from asyncflows_classify.actions.classify import Classify, Inputs, Outputs
from asyncflows.models.config.model import ModelConfig


@pytest.mark.parametrize(
    "inputs, expected_outputs",
    [
        (
            Inputs(
                data="This is a test",
                labels=["test", "prod"],
            ),
            Outputs(classification="test"),
        ),
        (
            Inputs(
                data="I'm so happy to see you",
                labels=["positive", "negative"],
            ),
            Outputs(classification="positive"),
        ),
        (
            Inputs(
                data="I'm so happy to see you",
                labels=["positive", "negative"],
                additional_instructions="The statement in the data is a lie. The word happy has a negative connotation",
            ),
            Outputs(classification="negative"),
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
    action = Classify(log=log, temp_dir=temp_dir)
    outputs = await action.run(inputs)
    assert outputs == expected_outputs
