import json

def lambda_handler(event, context):
    # Log the incoming event (for demonstration purposes)
    print("Received event:", json.dumps(event))

    # Your custom logic can go here if needed.

    # Add a custom message to the response
    custom_message = "This is a custom message from your Lambda function."

    # Return the event along with the custom message as the response
    response = {
        "statusCode": 200,
        "body": json.dumps({
            "message": custom_message,
            "event": event
        })
    }

    return response