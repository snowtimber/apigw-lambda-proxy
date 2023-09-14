import json

def lambda_handler(event, context):
    # Log the incoming event (for demonstration purposes)
    print("Received event:", json.dumps(event))

    # Your custom logic can go here if needed.

    # Return the event as the response
    response = {
        "statusCode": 200,
        "body": json.dumps(event)
    }

    return response