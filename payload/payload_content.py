

class PayloadContent:
    ITEM_NAME = ("タイプ", "HP", "攻撃", "防御", "特攻", "特防", "素早さ", "合計",
                 "特性1", "特性2", "夢特性", "卵グループ1", "卵グループ2")
    BUTTON_LABEL = ("同じタイプを持つポケモンを検索", "同じ特性を持つポケモンを検索", "同じ卵グループを持つポケモンを検索")

    status_body_items = {
            "type": "box",
            "layout": "baseline",
            "contents": [
              {
                "type": "text",
                "text": "", #ITEM_NAME
                "weight": "bold",
                "margin": "sm",
                "contents": []
              }
            ]
          }
    
    status_body_items_value = {
        "type": "text",
        "text": "", #value
        "align": "end",
        "contents": []
        }
    
    status_body_button_label = {
        "type": "text",
        "text": "", #BUTTON_LABEL
        "margin": "lg",
        "contents": []
    }

    status_body_button = {
        "type": "button",
        "action": {
          "type": "message",
          "label": "", #button label
          "text": "" #submit text
        },
        "color": "#1D2B6BFF",
        "height": "sm",
        "style": "primary"
    }

    type_body = {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "image",
                "url": "", #dot_image_url
                "align": "start",
                "size": "xxs"
              },
              {
                "type": "text",
                "text": "", #name
                "weight": "bold",
                "size": "lg",
                "align": "end",
                "margin": "sm",
                "contents": []
              }
            ]
          }
    
    trait_body = {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "image",
                "url": "", #dot_image_url
                "align": "start",
                "size": "xxs"
              },
              {
                "type": "text",
                "text": "", #name
                "weight": "bold",
                "size": "lg",
                "align": "end",
                "margin": "sm",
                "contents": []
              }
            ]
          }
    
    egg_group_body = {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "image",
                "url": "", #odt_iamge_url
                "align": "start",
                "size": "xxs"
              },
              {
                "type": "text",
                "text": "", #name
                "weight": "bold",
                "size": "lg",
                "align": "end",
                "margin": "sm",
                "contents": []
              }
            ]
          }
    
    alias_body = {
            "type": "button",
            "action": {
              "type": "message",
              "label": "", #name
              "text": "" #name
            },
            "color": "#1D2B6BFF",
            "height": "sm",
            "style": "primary"
          }