import json
from py3cw.request import Py3CW

#TODO: Replace the print statements with real logging. 
#TODO: Error handling, there is none at the moment.
#TODO: Hook in telegram API and send message whenever deal is adjusted. 

#Configuration settings
with open('config.json') as json_settings_file:
    config = json.load(json_settings_file)

apiKey = config['apiSettings'].get('apiKey')
apiSecret = config['apiSettings'].get('apiSecret')
bots = config['bots']

p3cw = Py3CW(key=apiKey,secret=apiSecret,request_options={
        'request_timeout': 10,
        'nr_of_retries': 1,
        'retry_status_codes': [502]
    }
)

#AdjustTIP: 
# Adjusted the take profit % of a deal to a new value. 
#   dealID: integer, the 3c deal id. 
# returns
#   deal, 3c deal object. 
def AdjustTP(dealId, tpAmt):
    error, data = p3cw.request(
        entity='deals',
        action='update_deal', 
        action_id=str(dealId),
        payload={
            "deal_id":dealId,
            "take_profit":tpAmt
        }
    )
    return data

#GetBotDeals: 
# Fetches a list of active bot deals from 3commmas. 
#   botId: integer, the 3c bot id. 
# returns: 
#   dict, a list of active 3c deals. 
def GetBotDeals(botId):
    print ("Gettting deals for bot: %s"%botId)
    error, data = p3cw.request(
        entity='deals',
        action='', 
        payload={
            "scope":"active",
            "bot_id":botId
        }
    )
    return data

#LookUpTpAmt
# Gets the expected take profit amount from the configuration data for the 
# current safty order
#   soTPAmounts : a list of softey order take profit amounts.
#   soCount: the current saftey order amount. 
def LookUpTpAmt(soTPAmts, soCount):
    tpAmt = soTPAmts.get(str(soCount))
    return tpAmt


#The main script logic starts here. 
#1. loop through the list of bots as defined in the config file. 
for bot in bots: 
    #2. Get active deals for the bot from the API. 
    deals = GetBotDeals(bot['botID'])
    soTPAmts = bot['soTPAmts']

    #3. Loop through the deals and adjust take profit as needed. 
    for deal in deals: 
        dealId = deal['id']
        dealSOCount = int(deal['completed_safety_orders_count'])
        dealTPAmt = float(deal['take_profit'])
        tpAmt = LookUpTpAmt(soTPAmts, dealSOCount)

        if dealSOCount >= 1 and dealTPAmt != tpAmt:
            #We need to adjust the take profit amount since values don't match. 
            print("Adjust deal %s from %s to %s"%(dealId, dealTPAmt, tpAmt))
            AdjustTP(dealId, tpAmt)
        else:
            print("Nothing todo for deal %s, take profit amounts match"%dealId)
