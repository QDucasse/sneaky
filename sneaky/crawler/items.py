# -*- coding: utf-8 -*-

# sneaky
# author - Quentin Ducasse
# https://github.com/QDucasse
# quentin.ducasse@ensta-bretagne.org

from scrapy import Item,Field

class BaseItem(Item):
    link = Field()
    name = Field()
    price = Field()

class KithItem(BaseItem):
    pass

class DTLRItem(BaseItem):
    pass

class FootshopItem(BaseItem):
    pass
