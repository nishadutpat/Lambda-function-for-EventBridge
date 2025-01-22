import logging

LOGGER = logging.getLogger()
LOGGER.setLevel(logging.INFO)

def lambda_handler(event, context):
    LOGGER.info("Event Object from Event Rule")
    LOGGER.info(event)

    headers = {
        "Content-Type": "application/json"
    }
    body = event    
    
    return {
        'statusCode': 200,
        'headers': headers,
        'body': body
    }
