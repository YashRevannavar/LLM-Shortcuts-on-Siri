import logging

from langchain_aws import ChatBedrock
from langchain_core.messages import HumanMessage


def get_llm_bedrock_ai() -> ChatBedrock:
    return ChatBedrock(
        model_id="anthropic.claude-3-5-sonnet-20240620-v1:0",
        model_kwargs=dict(temperature=0.9),
    )


def llm_daily_response(collected_news_data):
    logging.info("Summarising news articles")
    chat = get_llm_bedrock_ai()
    system_prompt = f"""
        You are a personal ai News reporter that helps me summarise news articles every day,
        My name is Yash and I want to stay connected to the news but I am busy so help me understand top news.
        You will provide me with a list of the news articles below, Please report me this news in a human-like manner.
        {collected_news_data}

        Make sure it is going to be in an audio format so make it sound like a human and do not format it textually.
        Always greet me with "Hello Yash" and say "Goodbye have a good day" at the end.
        """
    messages = [HumanMessage(content=system_prompt)]
    try:
        response = chat.invoke(messages)
        return response.content
    except Exception as e:
        return f"Due to {str(e)} we could not fetch the news data"
