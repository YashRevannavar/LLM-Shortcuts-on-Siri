import logging

from langchain_aws import ChatBedrock
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.prompts import human_prompt, system_prompt


def get_llm_bedrock_ai() -> ChatBedrock:
    return ChatBedrock(
        model_id="anthropic.claude-3-5-sonnet-20240620-v1:0",
        model_kwargs=dict(temperature=0.9),
    )


def llm_daily_response(collected_news_data):
    logging.info("Summarising news articles")
    chat = get_llm_bedrock_ai()
    logging.info("Collecting prompt data")
    messages = [HumanMessage(content=human_prompt, collected_news_data=collected_news_data), SystemMessage(content=system_prompt)]
    try:
        response = chat.invoke(str(messages))
        return response.content
    except Exception as e:
        return f"Due to {str(e)} we could not fetch the news data"
