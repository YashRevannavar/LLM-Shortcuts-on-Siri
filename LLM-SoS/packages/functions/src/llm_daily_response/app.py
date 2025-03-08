


def handler(event, context):
    try:
        import logging
        from news_loader import collect_top_headline_content
        from llm_service import llm_daily_response
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        from constants import NEWS_URL

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
