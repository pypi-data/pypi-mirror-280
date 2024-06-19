from aoa.api.iterator_base_api import BaseApi


class UserAttributesApi(BaseApi):

    path = "/api/userAttributes/"
    type = "USER_ATTRIBUTES"

    def _get_header_params(self):
        header_vars = [
            "AOA-Project-ID",
            "VMO-Project-ID",
            "Accept",
        ]  # AOA-Project-ID kept for backwards compatibility
        header_vals = [
            self.aoa_client.project_id,
            self.aoa_client.project_id,
            self.aoa_client.select_header_accept(
                ["application/json", "text/plain", "*/*"]
            ),
        ]

        return self.generate_params(header_vars, header_vals)

    def get_default_connection(self):

        return self.aoa_client.get_request(
            path=self.path + "search/findByName",
            header_params=self._get_header_params(),
            query_params=self.generate_params(["name"], ["DEFAULT_CONNECTION"]),
        )
