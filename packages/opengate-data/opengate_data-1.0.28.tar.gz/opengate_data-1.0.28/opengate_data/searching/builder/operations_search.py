"""  OperationsBuilder """

import requests
import json
import pandas as pd
from io import StringIO
from typing import Any
from flatten_dict import flatten
from opengate_data.searching.search import SearchBuilder
from opengate_data.utils.utils import send_request, handle_error_response, handle_exception, set_method_call, \
    validate_type
from opengate_data.searching.search_base import SearchBuilderBase
from urllib.parse import urlencode


class OperationsSearchBuilder(SearchBuilderBase, SearchBuilder):
    """ Builder search operations """

    def __init__(self, opengate_client):
        super().__init__()
        self.client = opengate_client
        self.headers = self.client.headers
        self.url: str | None = None
        self.method: str | None = None
        self.body_data: dict = {}
        self.method_calls: list = []

    @set_method_call
    def build(self):
        """
        Finalizes the construction of the operations search configuration.

        This method prepares the builder to execute the collection by ensuring all necessary configurations are set and validates the overall integrity of the build. It should be called before executing the collection to ensure that the configuration is complete and valid.

        The build process involves checking that mandatory fields such as the device identifier are set. It also ensures that method calls that are incompatible with each other (like `build` and `build_execute`) are not both used.

        Example:
            builder.build()

        Returns:
            OperationsSearchBuilder: Returns itself to allow for method chaining, enabling further actions like `execute`.

        Raises:
            ValueError: If required configurations are missing or if incompatible methods are used together.

        Note:
            This method should be used as a final step before `execute` to prepare the operations search configuration. It does not modify the state but ensures that the builder's state is ready for execution.
        """
        self._validate_builds()

        if 'build_execute' in self.method_calls:
            raise Exception("You cannot use build() together with build_execute()")

        return self

    @set_method_call
    def build_execute(self):
        """
        Executes the operations search immediately after building the configuration.

        This method is a shortcut that combines building and executing in a single step.

        Returns:
            dict: A dictionary containing the execution response which includes the status code and potentially other metadata about the execution.

        Raises:
            ValueError: If `build` has already been called on this builder instance.
        """
        if 'build' in self.method_calls:
            raise ValueError("You cannot use build_execute() together with build()")

        if 'execute' in self.method_calls:
            raise ValueError("You cannot use build_execute() together with execute()")

        self._validate_builds()
        return self.execute()

    @set_method_call
    def execute(self):
        """
        Executes the operations search based on the built configuration.

        Returns:
            dict, csv or dataframe: The response data in the specified format.

        Raises:
            Exception: If the build() method was not called before execute().
        """
        if 'build' in self.method_calls:
            if self.method_calls[-2] != 'build':
                raise Exception("The build() function must be the last method invoked before execute.")

        if 'build' not in self.method_calls and 'build_execute' not in self.method_calls:
            raise Exception(
                "You need to use a build() or build_execute() function the last method invoked before execute.")

        query_params = {
            'flattened': self.flatten,
            'utc': self.utc,
            'summary': self.summary,
            'defaultSorted': self.default_sorted,
            'caseSensitive': self.case_sensitive
        }

        url = f'{self.client.url}/north/v80/search/entities/operations/history?{urlencode(query_params)}'

        if self.format_data == 'csv':
            return self.operations__csv_request(url)

        return self._operations_dict_pandas_request(self.client.headers, url, self.body_data)

    def operations__csv_request(self, url: str) -> dict[str, Any] | str | Any:
        try:
            response = send_request(method='post', headers=self.client.headers, url=url, json_payload=self.body_data)
            print("response", response)
            if response.status_code != 200:
                return handle_error_response(response)

            if not self.transpose or self.mapping is None:
                return response.text

            data_str = StringIO(response.content.decode('utf-8'))
            data = pd.read_csv(data_str, sep=';')

            return data.to_csv(index=False)

        except Exception as e:
            return handle_exception(e)

    def _operations_dict_pandas_request(self, headers: dict, url: str, body_data: dict) -> Any:
        all_results = []
        limit = body_data.get("limit", {})
        start = limit.get("start", 1)
        size = limit.get("size", 1000)
        has_limit = "limit" in body_data

        while True:
            body_data.setdefault("limit", {}).update({"start": start, "size": size})
            try:
                response = send_request(method='post', headers=headers, url=url, json_payload=body_data)

                if response.status_code == 204:
                    if all_results:
                        break
                    return {'status_code': response.status_code}

                if response.status_code != 200 and response.status_code != 204:
                    return handle_error_response(response)

                data = response.json()

                if not data.get('operations'):
                    break

                all_results.extend(data['operations'])

                if has_limit:
                    break

                start += 1

            except Exception as e:
                return handle_exception(e)

        return self._format_results(all_results)

    def _format_results(self, all_results: list) -> Any:
        if self.format_data in ['dict', None]:
            return all_results

        if self.format_data == 'pandas':
            operations_flattened = [flatten(datapoint, reducer='underscore', enumerate_types=(list,)) for datapoint in
                                    all_results]
            return pd.DataFrame(operations_flattened)

        raise ValueError(f"Unsupported format: {self.format_data}")

    def _validate_builds(self):
        if self.format_data is not None and all(
                keyword not in self.format_data for keyword in ["csv", "pandas", "dict"]):
            raise ValueError(
                'Invalid value for the "with_format" method. Available parameters are only "dict", "csv", and "pandas".')

        if 'with_limit' in self.method_calls and self.format_data == 'csv':
            raise Exception("Limit is not allowed with csv format")

        if 'with_select' not in self.method_calls and self.format_data == 'csv':
            raise Exception("You need to use with_select() to apply a format in CSV")

        return self
