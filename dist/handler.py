import json
from urllib.parse import parse_qsl as parse_qs

'''
Your business logic here.

'''

def handle_new_customer_onbording(product_name,gh_user,refunded):
    if not refunded:
        # Call GitHub APIs to on board customer.
        return "🎉🎉🎉 Welcome to the team! 🎉🎉🎉"
    else:
        return "Here's your refund."

def handler(event,context):
    print(json.dumps(event))
    '''
    This event looks similar to:
    {
    ...     "seller_id": "xxx==",
    ...     "product_id": "fdbhJJx4dtlZWjoBK3TIxw==",
    ...     "product_name": "Intro to APIs 101 (Beta)",
    ...     "permalink": "learnapi",
    ...     "product_permalink": "https://gum.co/learnapi",
    ...     "email": "owen@owen.dev",
    ...     "price": "10",
    ...     "gumroad_fee": "0",
    ...     "currency": "usd",
    ...     "quantity": "1",
    ...     "discover_fee_charged": "false",
    ...     "can_contact": "true",
    ...     "referrer": "direct",
    ...     "order_number": "1036205531",
    ...     "sale_id": "i-xxx==",
    ...     "sale_timestamp": "2020-12-31T18:24:07Z",
    ...     "purchaser_id": "1002732354023",
    ...     "offer_code": "owenapidev",
    ...     "test": "true",
    ...     "Github Username": "BoraxTheClean",
    ...     "custom_fields[Github Username]": "BoraxTheClean",
    ...     "ip_country": "United States",
    ...     "is_gift_receiver_purchase": "false",
    ...     "refunded": "false",
    ...     "resource_name": "sale",
    ...     "disputed": "false",
    ...     "dispute_won": "false"
    ... }

    This event was taken from my awesome course: https://gumroad.com/l/learnapi

    '''
    event = dict(parse_qs(event['body']))
    print(json.dumps(event))

    try:
        product_name = event['product_name']
    except:
        return {
            'statusCode': 400,
            'body': 'No product_name in payload.'
        }
    if product_name == 'Intro to APIs 101 (Beta)':
        '''
            Extract additional fields per your requirements.
        '''
        try:
            # This is a custom field on my product.
            # You probably won't have any custom fields or they will be different.
            gh_user = event['Github Username']
        except:
            gh_user = None

        try:
            refunded = event['refunded'].lower()
            refunded = False if refunded == 'false' else True
        except:
            refunded = False
        
        # You can return a custom status code based on whether or not your workflow succeeded.
        # Gumroad will retry 4XX and 5XX status codes 3 times at a 1 hour interval.
        result = handle_github_onboarding(product_name,gh_user,refunded)

        if result:
            return {
                'statusCode': 200
            }
        else:
            return {
                'statusCode': 503
            }
    else:
        return {
            'statusCode': 200
        }
