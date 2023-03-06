

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