from mongoengine import *
# The vertical collection stores information about verticals for the partner provided.


class VerticalConfig(DynamicDocument):

    partner = LongField(required=True, db_field="partner")

    # industry vertical of the partner
    vertical = StringField(required=True, db_field="vertical")

    # if vertical also goes by a different display name
    display_vertical = StringField(required=False, db_field="displayVertical", default="")

    # additional verticals if needed
    additional = DictField(required=False, db_field="additional", default={})

    meta = {
        "collection": "verticalConfig",
        "strict": False,
        'indexes':
            [
                {'fields': ('partner', 'vertical'),
                 'unique': True}
            ]
    }