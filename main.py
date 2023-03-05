import os
import re
import csv
from dotenv import load_dotenv
from flask import Flask, request, abort

from payload import PayloadFormat as PF

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, QuickReply, QuickReplyButton, MessageAction
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

def res_data(text) -> dict[str, str | None]:
    with open('./master/master.csv', 'r') as f:
        data = [row for row in csv.reader(f)]

    res = {}
    have_type_list = []
    have_both_types_list = []
    have_trait_list = []
    have_egg_group_list = []
    have_alias_list = []
        
    for record in data:
        if record[1] == text:
            res["text"] = "\n".join((f"【{record[1]}】",
                                   f"図鑑No.{record[0]}",
                                   f"第{record[2]}世代" if re.findall(r'\d', record[2]) else f"{record[2]}",
                                   f"タイプ:{record[3]}/{record[4]}",
                                   f"HP:{record[5]}",
                                   f"攻撃:{record[6]}",
                                   f"防御:{record[7]}",
                                   f"特攻:{record[8]}",
                                   f"特防:{record[9]}",
                                   f"素早さ:{record[10]}",
                                   f"合計:{record[11]}",
                                   f"特性1:{record[12]}",
                                   f"特性2:{record[13]}",
                                   f"夢特性:{record[14]}",
                                   f"卵グループ1:{record[15]}",
                                   f"卵グループ2:{record[16]}"))
            break
        elif text in (record[3], record[4]):
            have_type_list.append(f"{record[1]}")
        elif re.findall(r'^{}\s{}$'.format(record[3], record[4]), text) or re.findall(r'^{}\s{}$'.format(record[4], record[3]), text):
            have_both_types_list.append(record[1])
        elif text in (record[12], record[13], record[14]):
            have_trait_list.append(f"{record[1]}(夢)" if text in record[14] else record[1])
        elif text in (record[15], record[16]):
            have_egg_group_list.append(record[1])
        elif re.findall(r'^{}\(.+\)$'.format(text), record[1]):
            have_alias_list.append(record[1])

    if len(have_type_list):
        res["text"] = f"【「{text}」タイプを持つポケモン】\n"
        res["text"] += "\n".join(have_type_list)
        res["text"] += "\n※複合タイプで検索したい場合は全角または半角スペースで区切って検索してください。\n(例：ほのお　ひこう)"
        if text == "ゴースト":
            res["text"] += "\n※ポケモンの「ゴースト」の種族値は「ゴースト(ポケモン)」で検索してください。"
    elif len(have_both_types_list):
        text = re.sub(r"\s", r"/", text)
        res["text"] = f"【「{text}」タイプのポケモン】\n"
        res["text"] += "\n".join(have_both_types_list)
    elif len(have_trait_list):
        res["text"] = f"【特性：「{text}」を持つポケモン】\n"
        res["text"] += "\n".join(have_trait_list)
    elif len(have_egg_group_list):
        res["text"] = f"【卵グループが「{text}」のポケモン】\n"
        res["text"] += "\n".join(have_egg_group_list)
    elif len(have_alias_list):
        res["text"] = "以下の候補から選択してください。"
        res["quick_reply"] = QuickReply(items=[QuickReplyButton(action=MessageAction(text=aliases, label=aliases)) for aliases in have_alias_list])

    if not len(res):
        res["text"] = "マッチするポケモン・タイプ・特性・卵グループが見つかりませんでした。\n※複合タイプで検索したい場合は全角または半角スペースで区切って検索してください。\n(例：ほのお　ひこう)"

    return res


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    res = res_data(event.message.text)
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(**res))


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=os.environ["PORT"])