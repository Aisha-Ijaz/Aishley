from agents import Agent, Runner, OpenAIChatCompletionsModel, AsyncOpenAI, RunConfig

import os
from dotenv import load_dotenv

load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")

client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"  
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=client
)

config = RunConfig(
    model=model,
    model_provider=client,
    tracing_disabled=True
)

agent = Agent(
    name="Aishley",
    instructions="You are an expert chef who helps users with recipes. Your job is to provide easy, delicious, and simple recipes in Roman Urdu."
)

result = Runner.run_sync(
    agent,
    input="Please tell me how to make tea step by step.",
    run_config = config
)


print(result.final_output)