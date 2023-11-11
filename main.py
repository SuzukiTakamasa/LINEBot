import os
import re
import csv
from dotenv import load_dotenv
from flask import Flask, request, abort

from payload.payload_generator import PayloadGenerator as PG

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, FlexSendMessage
)

app = Flask(__name__)
load_dotenv()

line_bot_api = LineBotApi(os.environ["CHANNEL_ACCESS_TOKEN"])
handler = WebhookHandler(os.environ["CHANNEL_SECRET"])


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@app.route("/", methods=['GET'])
def healthcheck():
    return 'Healthcheck OK'


def res_data(text: str) -> dict:
    with open('./master/master.csv', 'r') as f:
        data = [row for row in csv.reader(f)]

    res : FlexSendMessage | TextSendMessage | None = None
    have_type_list :list = []
    have_trait_list :list = []
    have_egg_group_list :list = []
    have_alias_list :list = []
        
    for record in data:
        if record[1] == text:
            res = FlexSendMessage(alt_text="[status]", contents=PG.create_status_data(record))
            break
        elif text in (record[3], record[4]) or re.findall(r'^{}\s{}$'.format(record[3], record[4]), text) or re.findall(r'^{}\s{}$'.format(record[4], record[3]), text):
            have_type_list.append(record[1])
        elif text in (record[12], record[13], record[14]):
            have_trait_list.append(record[1])
        elif text in (record[15], record[16]):
            have_egg_group_list.append(record[1])
        elif re.findall(r'^{}\(.+\)$'.format(text), record[1]):
            have_alias_list.append(record[1])

    if len(have_type_list):
        res = FlexSendMessage(alt_text="[type]", contents=PG.create_have_type_list(text, have_type_list))
    elif len(have_trait_list):
        res = FlexSendMessage(alt_text="[trait]", contents=PG.create_have_trait_list(text, have_trait_list))
    elif len(have_egg_group_list):
        res = FlexSendMessage(alt_text="[egg group]", contents=PG.create_have_egg_group_list(text, have_egg_group_list))
    elif len(have_alias_list):
        res = FlexSendMessage(alt_text="[alias]", contents=PG.create_alias_list(have_alias_list))

    if not res:
        res = TextSendMessage(text="マッチするポケモン・タイプ・特性・卵グループが見つかりませんでした。\n※複合タイプで検索したい場合は全角または半角スペースで区切って検索してください。\n(例：ほのお　ひこう)")

    return res


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event: dict):
    res = res_data(event.message.text)
    line_bot_api.reply_message(
        event.reply_token,
        res)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=os.environ["PORT"])