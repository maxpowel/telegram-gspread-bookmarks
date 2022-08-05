What is this
============
A telegram bot that just stores everything into a google spreadsheet. I use it when I find an interesting link. Since I use
firefox, chrome and a bunch of browsers on different devices the bookmarks handling is getting complicated. Probably there is
a super mega extension application but I don't know it. This script took me half an hour to build it and I spent hours looking 
for another "good" solution so writing it it's actually saving me time xD.

Prepare your necessary stuff
=============

Create the telegram bot
----------------------
Talk to https://t.me/botfather, send the message `/newbot` and follow the steps (source https://core.telegram.org/bots#6-botfather).
You should end with the api token. Put the api token in the "secret" directory

Gspread access
--------------
https://docs.gspread.org/en/latest/oauth2.html#enable-api-access-for-a-project
* Share you document with the bot email and generate the json credentials
* Create a google spreadsheet and get the id (it is in the url)

How to use it
=============
* Take your Telegram Token
* Json encode the gspread credentials file
* Take your gspread id

Take a look on Dockerfile to see how to run it in your machine

Running it with docker
==============
* docker buildx build -t telegram_gspread_bookmarks --load .
* Create an envfile like this (spread credentials is json encoded)
  ```bash
  TELEGRAM_TOKEN="AAFdas3asdfSDfasdfgSD"
  SPREADSHEET_ID="1jsadfsd_asdjhjgasdhjhjlsfhjlks"
  SPREAD_CREDENTIALS='{"type": "service_account", "project_id": "spreadbot-11111", "private_key_id": "lalalal", "private_key": "-----BEGIN PRIVATE KEY-----\\nlololo\\n-----END PRIVATE KEY-----\\n", "client_email": "spreadbot@spreadbot-45454.iam.gserviceaccount.com", "client_id": "123456", "auth_uri": "https://accounts.google.com/o/oauth2/auth", "token_uri": "https://oauth2.googleapis.com/token", "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs", "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/spreadbot%40spreadbot-123456.iam.gserviceaccount.com"}'
  ```
* docker run --rm --env-file env --name telegram_gspread_bookmarks telegram_gspread_bookmarks

Extra
=====
I also added a systemd service in the systemd directory so you can run it as a service