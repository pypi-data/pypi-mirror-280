import copy

base_template = {
    "type": "message",
    "attachments": [
        {
            "contentType": "application/vnd.microsoft.card.adaptive",
            "content": {
                "type": "AdaptiveCard",
                "body": [
                    {  # heading
                        "type": "TextBlock",
                        "size": "Large",
                        "weight": "Bolder",
                        "text": "{<>}",
                        "wrap": True
                    },
                    {
                        "type": "TextBlock",
                        "text": "Triggered by <at>User</at>",
                        "wrap": True,
                        "height": "stretch",
                        "horizontalAlignment": "Left",
                        "size": "Medium"
                    },
                    {
                        "type": "TextBlock",
                        "size": "Small",
                        "weight": "Bolder",
                        "text": "",
                        "wrap": True
                    },
                    {
                        "type": "ColumnSet",
                        "columns": [
                            {
                                "type": "Column",
                                "width": "stretch",
                                "items": [
                                    # {
                                    #     "type": "TextBlock",
                                    #     "text": "{<>}",
                                    #     "wrap": True,
                                    #     "weight": "Bolder",
                                    #     "horizontalAlignment": "Center",
                                    #     "spacing": "None"
                                    # },
                                    # {
                                    #     "type": "TextBlock",
                                    #     "text": "{<>}",
                                    #     "wrap": True,
                                    #     "weight": "Bolder",
                                    #     "horizontalAlignment": "Center",
                                    #     "spacing": "None"
                                    # }
                                ]
                            }
                        ]
                    }
                ],
                "actions": [
                    # {
                    #     "type": "Action.OpenUrl",
                    #     "title": "{}",
                    #     "url": '{<url>}'
                    # },
                    # {
                    #     "type": "Action.OpenUrl",
                    #     "title": "{}",
                    #     "url": '{<url>}'
                    # }
                ],
                "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
                "version": "1.4",
                "msteams": {
                    "width": "Full",
                    "entities": [
                        {
                            "type": "mention",
                            "text": "<at>User</at>",
                            "mentioned": {
                                "id": '{<user_email>}',
                                "name": '{<user_name>}'
                            }
                        },

                    ],

                }
            }}]
}


class TeamsAlertTemplate:
    """
    fields accepted in payload:
    1. "heading": heading of the alert
    2. "column_dict": dict of information to be displayed like a column, e.g. {"jobId": "78f90a"}
    3. "text_block": a block of informational text to be displayed below the column
    4. "url_actions_dict": click-open-action buttons (receive as dict button_name:url)
    5. "user_dict": to tag the relevant person {receive as dict "user_name": "user_email"}
    """

    def __init__(self,
                 heading="ALERT",
                 column_dict: dict = None,
                 text_block: str = None,
                 url_actions_dict: dict = None,
                 user_dict: dict = None):

        # following 5 public attributes can be changed on the fly
        self.heading = heading
        self.column_dict = column_dict
        self.text_block = text_block
        self.url_actions_dict = url_actions_dict
        self.user_dict = user_dict
        if not self.user_dict or not list(self.user_dict.keys())[0] or not list(self.user_dict.values())[0]:
            self.user_dict = {"user": "email"}

        # call the build_and_fetch_template to populate self._template when the above parameters are finalized
        self._template = None

        self.column_unit = {}
        self.url_action_unit = {}
        self.initialize_defaults()

    def initialize_defaults(self):

        self.column_unit = {
            "type": "TextBlock",
            "text": "{<>}",
            "wrap": True,
            "weight": "Bolder",
            "horizontalAlignment": "Left",
            "spacing": "None"
        }

        self.url_action_unit = {
            "type": "Action.OpenUrl",
            "title": "{}",
            "url": '{<url>}'
        }

    def build_and_fetch_template(self, use_upper_case: bool = False):
        self._template = copy.deepcopy(base_template)

        if use_upper_case:
            heading = str(self.heading).upper()
        else:
            heading = str(self.heading).capitalize()

        self._template["attachments"][0]["content"]["body"][0]["text"] = heading

        if self.text_block:
            self._template["attachments"][0]["content"]["body"][2]["text"] = str(self.text_block)

        if self.column_dict:
            for key, value in self.column_dict.items():
                deep_copied_column_unit = copy.deepcopy(self.column_unit)
                deep_copied_column_unit["text"] = f"{str(key).upper()}: {value}"
                self._template["attachments"][0]["content"]["body"][3]["columns"][0]["items"].append(
                    deep_copied_column_unit)

        if self.url_actions_dict:
            for key, value in self.url_actions_dict.items():
                deep_copied_url_action_unit = copy.deepcopy(self.url_action_unit)
                deep_copied_url_action_unit["title"] = key
                deep_copied_url_action_unit["url"] = value
                self._template["attachments"][0]["content"]["actions"].append(deep_copied_url_action_unit)

        self._template["attachments"][0]["content"]["msteams"]["entities"] = []
        trigger_text_block = f"Triggered by"
        for index, (user_name, user_email) in enumerate(self.user_dict.items()):
            # for multiple user tags
            entity = {
                "type": "mention",
                "text": f"<at>User{index + 1}</at>",
                "mentioned": {
                    "id": f"{user_email}",
                    "name": f"{user_name}"
                }
            }
            trigger_text_block += f" <at>User{index + 1}</at>"
            self._template["attachments"][0]["content"]["msteams"]["entities"].append(entity)

        self._template["attachments"][0]["content"]["body"][1]["text"] = trigger_text_block
        return self._template
