"""
UMP Capability Negotiation
"""


from dataclasses import dataclass, field


@dataclass
class Capabilities:


    version: str = "1.0"

    features: list = field(
        default_factory=list
    )

    transports: list = field(
        default_factory=list
    )

    max_file_size: int = 0



    def supports(
        self,
        feature
    ):

        return feature in self.features



    def add_feature(
        self,
        feature
    ):

        if feature not in self.features:
            self.features.append(feature)



    def to_dict(self):

        return {
            "version": self.version,
            "features": self.features,
            "transports": self.transports,
            "max_file_size": self.max_file_size
        }
