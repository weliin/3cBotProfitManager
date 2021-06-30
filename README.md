# 3cBotProfitManager
Adjusts bots' take profit percentage based on the number of safety orders taken for a 3commas DCA bot or bots which is a strategy used by [BLOCK PARTY TRADING](https://www.blockpartytrading.com/)

# DISCLAIMER
This script should be used at your own risk, I will not be responsible for any errors encountered while using the script. You should read and understand what the script is doing before using the script.  Use of the script means that you understand this warning and agree that you are using the script at your own risk.

# Requirements
* Python version 3.9, tested on 3.9.5
* py3cw Python module which is available at the [Project Homepage](https://github.com/bogdanteodoru/py3cw) or installed via pip `pip install py3cw`.
* 3commas.io API Key with BotsRead, BotsWrite, and AccountsRead permissions. 

# Configuration
Configuration is done in the config.json file.  You will nee the 3commas.io API key and API Key secret. You should check to make sure the JSON is well formed by using a JSON Validator like [JSON Lint](https://jsonlint.com/)

The example config file edits the settings for 3 bots. You get the bot id from 3commas website or using Bot Manager.  If you want to script to mange more or less bots simply remove a the JSON object from the JSON array.

* Replace YOUR_3COMMAS_API_KEY with your 3 commas API key from their website. 
* Replace YOUR_3COMMAS_API_SECRET_KEY with your 3 commas API secret key from their website. 
* Replace the bot id 9999999 in the config file with your Bot Id. 
* Edit the take profit amounts for each safety order step.  If you don't need a step, delete it, if you need another step, add it.  Just make sure your JSON is well formed and validated. 

```json
  {
    "apiSettings":{
      "apiKey":"YOUR_3COMMAS_API_KEY", 
      "apiSecret": "YOUR_3COMMAS_API_SECRET_KEY"
    },
    "bots":[
      {
        "botID":9999999,
        "soTPAmts":{
            "1":0.75,
            "2":1.00,
            "3":1.50,
            "4":2.00,
            "5":3.00,
            "6":4.00, 
            "7":5.00
        }
      }, 
      {
        "botID":9999999,
        "soTPAmts":{
          "1":0.75,
            "2":1.00,
            "3":1.50,
            "4":2.00,
            "5":3.00,
            "6":4.00
        }
      },
      {
        "botID":9999999, 
        "soTPAmts":{
            "1":0.65,
            "2":0.75,
            "3":1.5,
            "4":3.0,
            "5":3.0
        }
      }
    ]
  }
```

# Executing
Running the script is rather straightforward `python 3cBotProfitManager.py` (Mac or Linux) or `py 3cBotProfitManager.py` (Windows).  You can then use a scheduled task or cron job to excecute the script periodically. I personally run it every 10 minutes.  

# Questions or Problems
If you run into any issues, please create an issue on this repository and I will do what I can to help out.
