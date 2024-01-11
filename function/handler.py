def main(event, context):
    message = 'Hello World from the Kyma Function '+context['function-name']+' running on '+context['runtime']+ '!';
    print(message)
    return message
