"""
UMP Compatibility Layer

Handles feature matching between devices.
"""


class CompatibilityManager:


    def compare(
        self,
        local,
        remote
    ):

        return {

            "version":
                self._version_match(
                    local.version,
                    remote.version
                ),

            "features":
                self._common(
                    local.features,
                    remote.features
                ),

            "transports":
                self._common(
                    local.transports,
                    remote.transports
                )
        }



    def _common(
        self,
        first,
        second
    ):

        return list(
            set(first)
            &
            set(second)
        )



    def _version_match(
        self,
        first,
        second
    ):

        return first == second
