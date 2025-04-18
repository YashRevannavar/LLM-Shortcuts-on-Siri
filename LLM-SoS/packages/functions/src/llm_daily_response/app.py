


def handler(event, context):
    try:
        import logging
        from news_loader import collect_top_headline_content
        from llm_service import llm_daily_response
        from dotenv import load_dotenv
        import os

        load_dotenv()
        NEWS_URL = os.getenv("NEWS_URL")
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)

        collected_news_data = collect_top_headline_content(NEWS_URL)
        response = llm_daily_response(collected_news_data)
        return {
            "statusCode": 200,
            "body": str(response)
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "body": f"Due to {str(e)} we could not fetch the news data"
        }
