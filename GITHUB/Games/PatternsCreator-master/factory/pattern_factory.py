from model.starfish import StarfishType
from model.pattern import Pattern

from PyQt5.Qt import QPointF


class PatternFactory(object):
    _type_conversion_table = {
        StarfishType.Orange: "starfish-orange",
        StarfishType.Yellow: "starfish-yellow",
    }

    def make(self):
        pattern = Pattern()
        return pattern

    @staticmethod
    def starfish_type_from_string(starfish_type_str):
        for key, value in PatternFactory._type_conversion_table.items():
            if value == starfish_type_str:
                return key
        raise Exception("Not a valid starfish type: {}".format(starfish_type_str))

    @classmethod
    def starfish_string_from_type(cls, starfish_type):
        return cls._type_conversion_table[starfish_type]

    def from_json(self, json_properties):
        pattern = self.make()
        pattern.set_name(json_properties["name"])
        width = json_properties["properties"]["size"][0]
        height = json_properties["properties"]["size"][1]
        for pattern_object in json_properties["properties"]["objects"]:
            x = pattern_object["offset"][0] * width
            y = -pattern_object["offset"][1] * height
            starfish_type = self.starfish_type_from_string(pattern_object["name"])
            pattern.add_starfish_at_position(QPointF(x, y), starfish_type)
        return pattern

    def to_json(self, pattern):
        objects = list()
        for starfish in pattern.starfishes():
            objects.append({
                "name": self.starfish_string_from_type(starfish.type()),
                "offset": [starfish.position().x(), -starfish.position().y()],
            })
        return {
            "name": pattern.name(),
            "properties":
                {
                    "size": [1, 1],
                    "objects": objects,
                },
        }
