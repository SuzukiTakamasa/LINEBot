import re

class PayloadGenerator:
    @classmethod
    def create_status_data(cls, record: list) -> dict:
        status =  {
          "type": "bubble",
          "body": {
            "type": "box",
            "layout": "vertical",
            "spacing": "md",
            "contents": [
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": record[1],
                    "weight": "bold",
                    "size": "lg",
                    "align": "start",
                    "contents": []
                  },
                  {
                    "type": "image",
                    "url": record[18] if record[18] else "https://via.placeholder.com/150x150.png?text=No+Image",
                    "align": "start",
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
                        "text": f"第{record[2]}世代" if record[2].isdigit() else f"{record[2]}",
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
              }
            ]
          }
        }

        if record[13] != "-":
            status["body"]["contents"].insert(6, {
            "type": "button",
            "action": {
            "type": "message",
            "label": f"「{record[13]}」で検索",
            "text": record[13]
            },
            "color": "#1D2B6BFF",
            "height": "sm",
            "style": "primary"
        })
            
        if record[14] != "-":
            status["body"]["contents"].insert(6 if record[13] == "-" else 7, {
            "type": "button",
            "action": {
            "type": "message",
            "label": f"「{record[14]}」で検索",
            "text": record[14]
            },
            "color": "#1D2B6BFF",
            "height": "sm",
            "style": "primary"
        })

        if record[16] != "-":
            status["body"]["contents"].append({
            "type": "button",
            "action": {
            "type": "message",
            "label": f"「{record[16]}」で検索",
            "text": record[16]
            },
            "color": "#1D2B6BFF",
            "height": "sm",
            "style": "primary"
        })

        return status

    
    @classmethod
    def create_have_type_list(cls, text: str, have_type_list: list) -> dict:
       carousel_columns = []
       for i in range(0, len(have_type_list), 50):
           carousel_columns.append(have_type_list[i:i+50])
           
       types = {
          "type": "carousel",
          "contents": [{
          "type": "bubble",
          "body": {
            "type": "box",
            "layout": "vertical",
            "spacing": "md",
            "contents": [
              {
                "type": "text",
                "text": f"「{text}」タイプのポケモン" if not re.findall(r'^.+\s.+$', text) else "{}タイプのポケモン".format(re.sub(r'\s', '/', text)),
                "weight": "bold",
                "size": "md",
                "contents": []
              },
              {
                "type": "box",
                "layout": "vertical",
                "spacing": "md",
                "contents": [
                      {
                    "type": "button",
                    "action": {
                      "type": "message",
                      "label": name,
                      "text": name
                    },
                    "color": "#1D2B6BFF",
                    "margin": "sm",
                    "height": "sm",
                    "style": "primary",
                    "gravity": "top"
                  } for name in column
                ]
              }
            ]
          }
        } for column in carousel_columns
      ]
    }
       
       return types

    
    @classmethod
    def create_have_trait_list(cls, text: str, have_trait_list: list) -> dict:
        carousel_columns = []
        for i in range(0, len(have_trait_list), 50):
            carousel_columns.append(have_trait_list[i:i+50])

        traits = {
          "type": "carousel",
          "contents": [{
          "type": "bubble",
          "body": {
            "type": "box",
            "layout": "vertical",
            "spacing": "md",
            "contents": [
              {
                "type": "text",
                "text": f"「{text}」を持つポケモン",
                "weight": "bold",
                "size": "md",
                "contents": []
              },
              {
                "type": "box",
                "layout": "vertical",
                "spacing": "md",
                "contents": [
                    {
                    "type": "button",
                    "action": {
                      "type": "message",
                      "label": name,
                      "text": name
                    },
                    "color": "#1D2B6BFF",
                    "margin": "sm",
                    "height": "sm",
                    "style": "primary",
                    "gravity": "top"
                  } for name in column
                ]
              }
            ]
          }
        } for column in carousel_columns
      ]
    }
        
        return traits
    
    @classmethod
    def create_have_egg_group_list(cls, text: str, have_egg_group_list: list) -> dict:
        carousel_columns = []
        for i in range(0, len(have_egg_group_list), 50):
            carousel_columns.append(have_egg_group_list[i:i+50])

        egg_groups = {
          "type": "carousel",
          "contents": [{
          "type": "bubble",
          "body": {
            "type": "box",
            "layout": "vertical",
            "spacing": "md",
            "contents": [
              {
                "type": "text",
                "text": f"「{text}」のポケモン",
                "weight": "bold",
                "size": "md",
                "contents": []
              },
              {
                "type": "box",
                "layout": "vertical",
                "spacing": "md",
                "contents": [
                  {
                    "type": "button",
                    "action": {
                      "type": "message",
                      "label": name,
                      "text": name
                    },
                    "color": "#1D2B6BFF",
                    "margin": "sm",
                    "height": "sm",
                    "style": "primary",
                    "gravity": "top"
                  } for name in column
                ]
              }
            ]
          }
        } for column in carousel_columns
      ]
    }
        
        return egg_groups
         
    
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