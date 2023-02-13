import os
import re
import csv
from dotenv import load_dotenv
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
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

def res_data(text):
    with open('./master/master.csv', 'r') as f:
        data = [row for row in csv.reader(f)]

    res = ""
    have_trait_list = []
    have_alias_list = []
        
    for record in data:
        if record[1] == text:
            res += f"【{record[1]}】\n"
            res += f"図鑑No.{record[0]}\n"
            res += f"第{record[2]}世代\n" if re.findall(r'\d', record[2]) else "ヒスイ\n"
            res += f"タイプ:{record[3]}/{record[4]}\n" if len(record[4]) else f"タイプ:{record[3]}/-\n"
            res += f"HP:{record[5]}\n"
            res += f"攻撃:{record[6]}\n"
            res += f"防御:{record[7]}\n"
            res += f"特攻:{record[8]}\n"
            res += f"特防:{record[9]}\n"
            res += f"素早さ:{record[10]}\n"
            res += f"合計:{record[11]}\n"
            res += f"特性1:{record[12]}\n" if len(record[12]) else f"特性1:-\n"
            res += f"特性2:{record[13]}\n" if len(record[13]) else f"特性2:-\n"
            res += f"夢特性:{record[14]}" if len(record[14]) else f"夢特性:-"
            break
        elif text in (record[12], record[13], record[14]):
            have_trait = f"{record[1]}(夢)" if text in record[14] else record[1]
            have_trait_list.append(have_trait)
            res = f"【特性：「{text}」を持つポケモン】\n"
            for have_traits in have_trait_list:
                res += have_traits if have_traits == have_trait_list[len(have_trait_list)-1] else f"{have_traits}\n"
        elif record[1].startswith(text):
            have_alias_list.append(record[1])
            res = "以下のワードで検索してください\n"
            for have_aliases in have_alias_list:
                res += have_aliases if have_aliases == have_alias_list[len(have_alias_list)-1] else f"{have_aliases}\n"

    if not len(res):
        res = "マッチするポケモン・特性が見つかりませんでした。\n(現在第5世代までのポケモンのみサポートしています。)"

    return res


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    res = res_data(event.message.text)
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=res))


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=os.environ["PORT"])