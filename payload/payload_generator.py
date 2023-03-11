import re
from payload.payload_format import PayloadFormat as PF

class PayloadGenerator:
    @classmethod
    def create_status_data(self, record: list) -> dict:
        #Pokemon name and dot image URL 
        PF.status_format["body"]["contents"][0]["contents"][0]["text"] += record[1]
        PF.status_format["body"]["contents"][0]["contents"][1]["url"] += record[18]

        #Number and Generation
        PF.status_body_items["contents"][0]["text"] = record[0]
        PF.status_body_items["contents"][0]["text"] = record[2] if re.findall(r'\d', record[2]) else f"{record[2]}"
        PF.status_format["body"]["contents"][1]["contents"].append(PF.status_body_items)

        #Each status item
        for item, value in zip(range(0, 13), range(3, 16)):
            PF.status_body_items["contents"][0]["text"] = PF.ITEM_NAME[item]
            PF.status_body_items_value["text"] = record[value]
            PF.status_format["body"]["contents"][1]["contents"].append(PF.status_body_items)
        
        #Search related pokemon button by "type"
        PF.status_body_button_label["text"] = PF.BUTTON_LABEL[0]
        PF.status_format["body"]["contents"][1]["contents"].append(PF.status_body_button_label)

        PF.status_body_button["label"] = f"{record[3]}タイプで検索" if record[4] == "-" else f"{record[3]}/{record[4]}タイプで検索"
        PF.status_body_button["text"] = f"{record[3]}" if record[4] == "-" else f"{record[3]} {record[4]}"
        PF.status_format["body"]["contents"][1]["contents"].append(PF.status_body_button)

        #Search related pokemon button by "trait"
        PF.status_body_button_label["text"] = PF.BUTTON_LABEL[1]
        PF.status_format["body"]["contents"][1]["contents"].append(PF.status_body_button_label)

        PF.status_body_button["label"] = f"「{record[12]}」で検索"
        PF.status_body_button["text"] = f"{record[12]}"
        PF.status_format["body"]["contents"][1]["contents"].append(PF.status_body_button)

        if record[13] != "-":
            PF.status_body_button["label"] = f"「{record[13]}」で検索"
            PF.status_body_button["text"] = f"{record[13]}"
            PF.status_format["body"]["contents"][1]["contents"].append(PF.status_body_button)
        
        if record[14] != "-":
            PF.status_body_button["label"] = f"「{record[14]}」で検索"
            PF.status_body_button["text"] = f"{record[14]}"
            PF.status_format["body"]["contents"][1]["contents"].append(PF.status_body_button)
        
         #Search related pokemon button by "egg group"
        PF.status_body_button_label["text"] = PF.BUTTON_LABEL[2]
        PF.status_format["body"]["contents"][1]["contents"].append(PF.status_body_button_label)

        PF.status_body_button["label"] = f"「{record[15]}」で検索"
        PF.status_body_button["text"] = f"{record[15]}"
        PF.status_format["body"]["contents"][1]["contents"].append(PF.status_body_button)

        if record[16] != "-":
            PF.status_body_button["label"] = f"「{record[16]}」で検索"
            PF.status_body_button["text"] = f"{record[16]}"
            PF.status_format["body"]["contents"][1]["contents"].append(PF.status_body_button)
        
        return PF.status_format
    
    @classmethod
    def create_have_type_list(self, text: str, have_type_dict: dict) -> dict:
        #Set a title
        PF.type_format["body"]["contents"][0]["text"] = f"「{text}」タイプを持つポケモン"

        #Set contents
        for k, v in have_type_dict.items():
            PF.type_body["contents"][0]["url"] = v
            PF.type_body["contents"][1]["text"] = k
            PF.type_format["body"]["contents"][1]["contents"].append(PF.type_body)

        return PF.type_format
    
    @classmethod
    def create_have_both_types_list(self, text: str, have_both_types_dict: dict) -> dict:
        #Replace blank to slash
        text = re.sub(r"\s", r"/", text)

        #Set a title
        PF.type_format["body"]["contents"][0]["text"] = f"「{text}」タイプを持つポケモン"

        #Set contents
        for k, v in have_both_types_dict.items():
            PF.type_body["contents"][0]["url"] = v
            PF.type_body["contents"][1]["text"] = k
            PF.type_format["body"]["contents"][1]["contents"].append(PF.type_body)
            
        return PF.type_format
    
    @classmethod
    def create_have_trait_list(self, text: str, have_trait_dict: dict) -> dict:
        #Set a title
        PF.trait_format["body"]["contents"][0]["text"] = f"「特性{text}」を持つポケモン"

        #Set contents
        for k, v in have_trait_dict.items():
            PF.trait_body["contents"][0]["url"] = v
            PF.trait_body["contents"][1]["text"] = k
            PF.trait_format["body"]["contents"][1]["contents"].append(PF.trait_body)

        return PF.trait_format
    
    @classmethod
    def create_have_egg_group_list(self, text: str, have_egg_group_dict: dict) -> dict:
        #Set a title
        PF.egg_group_format["body"]["contents"][0]["text"] = f"「卵グループが{text}」のポケモン"

        #Set contents
        for k, v in have_egg_group_dict.items():
            PF.egg_group_body["contents"][0]["url"] = v
            PF.egg_group_body["contents"][1]["text"] = k
            PF.egg_group_format["body"]["contents"][1]["contents"].append(PF.egg_group_body)

        return PF.egg_group_format
    
    @classmethod
    def create_alias_list(self, have_alias_list: list) -> dict:
        #Set contents
        for i in have_alias_list:
            PF.alias_body["action"]["label"] = PF.alias_body["action"]["text"] = i
            PF.alias_format.append(PF.alias_body)

        return PF.alias_format