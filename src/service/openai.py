import openai

extra_promt = """
Ты являешься телеграмм ботом, помогающий людям получить ответы про хакатон
Ты должен отвечать вопросы, касающийся хакатона про Latoken и давать информацию
про эту компанию и хакатон, который устраивают чтобы нанять кадры. Следуя
этим правилам ответь на этот вопрос ниже
{}

"""

async def get_completetions(promt: str) -> str:
    client = openai.AsyncOpenAI(api_key=openai.api_key)
    result = await client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": extra_promt.format(promt),
            }
        ],
        model="gpt-4",
        max_tokens=256, 
        temperature=0.1
    )
    return result.choices[0].message.content
