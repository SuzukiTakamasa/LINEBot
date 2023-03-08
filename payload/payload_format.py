from payload.payload_content import PayloadContent as PC

class PayloadFormat:
    status_format = {
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "vertical",
    "spacing": "md",
    "contents": [
      {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "text",
            "text": "", #name
            "weight": "bold",
            "size": "xl",
            "align": "start",
            "contents": []
          },
          {
            "type": "image",
            "url": "", #dot_image_url
            "align": "end",
            "size": "xxs"
          }
        ]
      },
      {
        "type": "box",
        "layout": "vertical",
        "spacing": "sm",
        "contents": []
      }
    ]
  }
    }

    type_format = {
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "vertical",
    "spacing": "md",
    "action": {
      "type": "uri",
      "label": "Action",
      "uri": ""
    },
    "contents": [
      {
        "type": "text",
        "text": "", #title: type
        "weight": "bold",
        "size": "md",
        "contents": []
      },
      {
        "type": "box",
        "layout": "vertical",
        "spacing": "sm",
        "contents": []
      }
    ]
  }
}

    trait_format = {
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "vertical",
    "spacing": "md",
    "action": {
      "type": "uri",
      "label": "Action",
      "uri": ""
    },
    "contents": [
      {
        "type": "text",
        "text": "", #title: trait
        "weight": "bold",
        "size": "md",
        "contents": []
      },
      {
        "type": "box",
        "layout": "vertical",
        "spacing": "sm",
        "contents": []
      }
    ]
  }
}

    egg_group_format = {
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "vertical",
    "spacing": "md",
    "action": {
      "type": "uri",
      "label": "Action",
      "uri": ""
    },
    "contents": [
      {
        "type": "text",
        "text": "", #title: egg_group
        "weight": "bold",
        "size": "md",
        "contents": []
      },
      {
        "type": "box",
        "layout": "vertical",
        "spacing": "sm",
        "contents": []
      }
    ]
  }
}

    aliasz_format = {
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "vertical",
    "spacing": "md",
    "action": {
      "type": "uri",
      "label": "Action",
      "uri": ""
    },
    "contents": [
      {
        "type": "text",
        "text": "以下の候補から選択してください",
        "weight": "bold",
        "size": "md",
        "contents": []
      },
      {
        "type": "box",
        "layout": "vertical",
        "spacing": "sm",
        "contents": []
      }
    ]
  }
}

    not_matched = {
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "vertical",
    "spacing": "md",
    "action": {
      "type": "uri",
      "label": "Action",
      "uri": ""
    },
    "contents": [
      {
        "type": "text",
        "text": "※マッチするポケモン・タイプ・特性",
        "contents": []
      },
      {
        "type": "text",
        "text": "卵グループが見つかりませんでした。",
        "contents": []
      }
    ]
  }
}

    @classmethod
    def create_status_data(self, record) -> dict:
        self.status_format["body"]["contents"][0]["contents"][0]["text"] += record[1]
        self.status_format["body"]["contents"][0]["contents"][1]["url"] += record[18]

        for item, value in zip(range(0, 14), range(3, 17)):
            each_item = PC.status_body_items
            each_item["contents"][0]["text"] = PC.ITEM_NAME[item]
            each_item["contents"][1]["text"] = record[value]

            self.status_format["body"]["contents"][1]["contents"].append(each_item)
        
        PC.status_body_button_label["text"] = PC.BUTTON_LABEL[0]
        self.status_format["body"]["contents"][1]["contents"].append(PC.status_body_button_label)

        PC.status_body_button["label"] = f"{record[3]}タイプで検索" if record[4] == "-" else f"{record[3]}/{record[4]}タイプで検索"
        PC.status_body_button["text"] = f"{record[3]}" if record[4] == "-" else f"{record[3]} {record[4]}"
        self.status_format["body"]["contents"][1]["contents"].append(PC.status_body_button)

        PC.status_body_button_label["text"] = PC.BUTTON_LABEL[1]
        self.status_format["body"]["contents"][1]["contents"].append(PC.status_body_button_label)

        PC.status_body_button["label"] = f"「{record[12]}」で検索"
        PC.status_body_button["text"] = f"{record[12]}"
        self.status_format["body"]["contents"][1]["contents"].append(PC.status_body_button)

        if record[13] != "-":
            PC.status_body_button["label"] = f"「{record[13]}」で検索"
            PC.status_body_button["text"] = f"{record[13]}"
            self.status_format["body"]["contents"][1]["contents"].append(PC.status_body_button)
        
        if record[14] != "-":
            PC.status_body_button["label"] = f"「{record[14]}」で検索"
            PC.status_body_button["text"] = f"{record[14]}"
            self.status_format["body"]["contents"][1]["contents"].append(PC.status_body_button)
        
        PC.status_body_button_label["text"] = PC.BUTTON_LABEL[2]
        self.status_format["body"]["contents"][1]["contents"].append(PC.status_body_button_label)

        PC.status_body_button["label"] = f"「{record[15]}」で検索"
        PC.status_body_button["text"] = f"{record[15]}"
        self.status_format["body"]["contents"][1]["contents"].append(PC.status_body_button)

        if record[16] != "-":
            PC.status_body_button["label"] = f"「{record[16]}」で検索"
            PC.status_body_button["text"] = f"{record[16]}"
            self.status_format["body"]["contents"][1]["contents"].append(PC.status_body_button)
        
        return self.status_format

