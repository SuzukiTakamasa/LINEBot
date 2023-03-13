

class PayloadGenerator:
    @classmethod
    def spacer(cls):
        return {"type": "spacer", "size": "xs"}

    @classmethod
    def create_status_data(cls, record: list) -> dict:
        return {
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
            "text": record[1],
            "weight": "bold",
            "size": "xl",
            "align": "start",
            "contents": []
          },
          {
            "type": "image",
            "url": record[18],
            "align": "end",
            "size": "xxs"
          }
        ]
      },
      {
        "type": "box",
        "layout": "vertical",
        "spacing": "sm",
        "contents": [
          {
            "type": "box",
            "layout": "baseline",
            "contents": [
              {
                "type": "text",
                "text": f"図鑑No.{record[0]}",
                "weight": "bold",
                "margin": "sm",
                "contents": []
              }
            ]
          },
          {
            "type": "box",
            "layout": "baseline",
            "contents": [
              {
                "type": "text",
                "text": f"第{record[2]}世代",
                "weight": "bold",
                "flex": 0,
                "margin": "sm",
                "contents": []
              }
            ]
          },
          {
            "type": "box",
            "layout": "baseline",
            "contents": [
              {
                "type": "text",
                "text": "タイプ",
                "weight": "bold",
                "align": "start",
                "contents": []
              },
              {
                "type": "text",
                "text": f"{record[3]}/{record[4]}",
                "align": "end",
                "contents": []
              }
            ]
          },
          {
            "type": "box",
            "layout": "baseline",
            "contents": [
              {
                "type": "text",
                "text": "HP",
                "weight": "bold",
                "contents": []
              },
              {
                "type": "text",
                "text": record[5],
                "align": "end",
                "contents": []
              }
            ]
          },
          {
            "type": "box",
            "layout": "baseline",
            "contents": [
              {
                "type": "text",
                "text": "攻撃",
                "weight": "bold",
                "contents": []
              },
              {
                "type": "text",
                "text": record[6],
                "align": "end",
                "contents": []
              }
            ]
          },
          {
            "type": "box",
            "layout": "baseline",
            "contents": [
              {
                "type": "text",
                "text": "防御",
                "weight": "bold",
                "contents": []
              },
              {
                "type": "text",
                "text": record[7],
                "align": "end",
                "contents": []
              }
            ]
          },
          {
            "type": "box",
            "layout": "baseline",
            "contents": [
              {
                "type": "text",
                "text": "特攻",
                "weight": "bold",
                "contents": []
              },
              {
                "type": "text",
                "text": record[8],
                "align": "end",
                "contents": []
              }
            ]
          },
          {
            "type": "box",
            "layout": "baseline",
            "contents": [
              {
                "type": "text",
                "text": "特防",
                "weight": "bold",
                "contents": []
              },
              {
                "type": "text",
                "text": record[9],
                "align": "end",
                "contents": []
              }
            ]
          },
          {
            "type": "box",
            "layout": "baseline",
            "contents": [
              {
                "type": "text",
                "text": "素早さ",
                "weight": "bold",
                "contents": []
              },
              {
                "type": "text",
                "text": record[10],
                "align": "end",
                "contents": []
              }
            ]
          },
          {
            "type": "box",
            "layout": "baseline",
            "contents": [
              {
                "type": "text",
                "text": "合計",
                "weight": "bold",
                "contents": []
              },
              {
                "type": "text",
                "text": record[11],
                "align": "end",
                "contents": []
              }
            ]
          },
          {
            "type": "box",
            "layout": "baseline",
            "contents": [
              {
                "type": "text",
                "text": "特性1",
                "weight": "bold",
                "contents": []
              },
              {
                "type": "text",
                "text": record[12],
                "align": "end",
                "contents": []
              }
            ]
          },
          {
            "type": "box",
            "layout": "baseline",
            "contents": [
              {
                "type": "text",
                "text": "特性2",
                "weight": "bold",
                "contents": []
              },
              {
                "type": "text",
                "text": record[13],
                "align": "end",
                "contents": []
              }
            ]
          },
          {
            "type": "box",
            "layout": "baseline",
            "contents": [
              {
                "type": "text",
                "text": "夢特性",
                "weight": "bold",
                "contents": []
              },
              {
                "type": "text",
                "text": record[14],
                "align": "end",
                "contents": []
              }
            ]
          },
          {
            "type": "box",
            "layout": "baseline",
            "contents": [
              {
                "type": "text",
                "text": "卵グループ1",
                "weight": "bold",
                "contents": []
              },
              {
                "type": "text",
                "text": record[15],
                "align": "end",
                "contents": []
              }
            ]
          },
          {
            "type": "box",
            "layout": "baseline",
            "contents": [
              {
                "type": "text",
                "text": "卵グループ2",
                "weight": "bold",
                "contents": []
              },
              {
                "type": "text",
                "text": record[16],
                "align": "end",
                "contents": []
              }
            ]
          }
        ]
      },
      {
        "type": "text",
        "text": "同じタイプを持つポケモンを検索",
        "margin": "lg",
        "contents": []
      },
      {
        "type": "button",
        "action": {
          "type": "message",
          "label": f"「{record[3]}」タイプを検索" if record[4] == "-" else f"「{record[3]}/{record[4]}」タイプを検索",
          "text": record[3] if record[4] == "-" else f"{record[3]} {record[4]}"
        },
        "color": "#1D2B6BFF",
        "height": "sm",
        "style": "primary"
      },
      {
        "type": "text",
        "text": "同じ特性を持つポケモンを検索",
        "margin": "lg",
        "contents": []
      },
      {
        "type": "button",
        "action": {
          "type": "message",
          "label": f"「{record[12]}」で検索",
          "text": record[12]
        },
        "color": "#1D2B6BFF",
        "height": "sm",
        "style": "primary"
      },
      {
        "type": "button",
        "action": {
          "type": "message",
          "label": f"「{record[13]}」で検索",
          "text": record[13]
        },
        "color": "#1D2B6BFF",
        "height": "sm",
        "style": "primary"
      } if record[13] != "-" else cls.spacer(),
      {
        "type": "text",
        "text": "同じ卵グループを持つポケモンを検索",
        "margin": "lg",
        "contents": []
      },
      {
        "type": "button",
        "action": {
          "type": "message",
          "label": f"「{record[15]}」で検索",
          "text": record[15]
        },
        "color": "#1D2B6BFF",
        "height": "sm",
        "style": "primary"
      },
      {
        "type": "button",
        "action": {
          "type": "message",
          "label": f"「{record[16]}」で検索",
          "text": record[16]
        },
        "color": "#1D2B6BFF",
        "height": "sm",
        "style": "primary"
      } if record[16] != "-" else cls.spacer()
    ]
  }
}

    
    @classmethod
    def create_have_type_list(cls, text: str, have_type_dict: dict) -> dict:
       return {
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "vertical",
    "spacing": "md",
    "contents": [
      {
        "type": "text",
        "text": f"「{text}」タイプを持つポケモン",
        "weight": "bold",
        "size": "md",
        "contents": []
      },
      {
        "type": "box",
        "layout": "vertical",
        "spacing": "sm",
        "contents": [
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "image",
                "url": v,
                "align": "start",
                "size": "xxs"
              },
              {
                "type": "text",
                "text": k,
                "weight": "bold",
                "size": "lg",
                "align": "end",
                "margin": "sm",
                "contents": []
              }
            ]
          } for k, v in have_type_dict.items()
        ]
      }
    ]
  }
}

    
    @classmethod
    def create_have_trait_list(cls, text: str, have_trait_dict: dict) -> dict:
        return {
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "vertical",
    "spacing": "md",
    "contents": [
      {
        "type": "text",
        "text": f"特性「{text}」を持つポケモン",
        "weight": "bold",
        "size": "md",
        "contents": []
      },
      {
        "type": "box",
        "layout": "vertical",
        "spacing": "sm",
        "contents": [
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "image",
                "url": v,
                "align": "start",
                "size": "xxs"
              },
              {
                "type": "text",
                "text": k,
                "weight": "bold",
                "size": "lg",
                "align": "end",
                "margin": "sm",
                "contents": []
              }
            ]
          } for k, v in have_trait_dict.items()
        ]
      }
    ]
  }
}
    
    @classmethod
    def create_have_egg_group_list(cls, text: str, have_egg_group_dict: dict) -> dict:
        return {
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "vertical",
    "spacing": "md",
    "contents": [
      {
        "type": "text",
        "text": f"卵グループ「{text}」のポケモン",
        "weight": "bold",
        "size": "md",
        "contents": []
      },
      {
        "type": "box",
        "layout": "vertical",
        "spacing": "sm",
        "contents": [
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "image",
                "url": v,
                "align": "start",
                "size": "xxs"
              },
              {
                "type": "text",
                "text": k,
                "weight": "bold",
                "size": "lg",
                "align": "end",
                "margin": "sm",
                "contents": []
              }
            ]
          } for k, v in have_egg_group_dict.items()
        ]
      }
    ]
  }
}
    
    @classmethod
    def create_alias_list(cls, have_alias_list: list) -> dict:
        return {
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "vertical",
    "spacing": "md",
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
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": alias,
              "text": alias
            },
            "color": "#1D2B6BFF",
            "height": "sm",
            "style": "primary"
          } for alias in have_alias_list
        ]
      }
    ]
  }
}