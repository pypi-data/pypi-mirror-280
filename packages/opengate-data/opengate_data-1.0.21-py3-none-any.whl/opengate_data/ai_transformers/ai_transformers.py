"""  AITransformersBuilder """
import json
import os
import configparser
import mimetypes
from typing import Any, Dict, List, Tuple, Optional, Union
from dotenv import load_dotenv, dotenv_values, set_key
import requests
from requests import Response
from opengate_data.utils.utils import validate_type, send_request, set_method_call, handle_basic_response


class AITransformersBuilder:
    """ Class transformer builder """

    def __init__(self, opengate_client):
        self.client: str = opengate_client
        self.base_url: str = f'{self.client.url}/north/ai'
        self.organization_name: str | None = None
        self.identifier: str | None = None
        self.config_file: str | None = None
        self.data_env: str | None = None
        self.section: str | None = None
        self.config_key: str | None = None
        self.data_evaluate: Dict = {}
        self.url: str | None = None
        self.requires: Dict = {}
        self.method: str | None = None
        self.name: str | None = None
        self.find_name: str | None = None
        self.output_file_path: str | None = None
        self.file_name: str | None = None
        self.files: List[Tuple[str, str]] = []
        self.builder: bool = False

    def with_organization_name(self, organization_name: str) -> 'AITransformersBuilder':
        """
        Specify the organization name.

        Args:
            organization_name (str): The name of the organization.

        Returns:
            AITransformersBuilder: Returns self for chaining.
        """
        self.organization_name = organization_name
        return self

    def with_identifier(self, identifier: str) -> 'AITransformersBuilder':
        """
         Specify the identifier for the pipeline.

         Args:
             identifier (str): The identifier for the pipeline.

         Returns:
             AITransformersBuilder: Returns self for chaining.
         """
        self.identifier = identifier
        return self

    def with_env(self, data_env: str) -> 'AITransformersBuilder':
        """
        Specify the environment variable.

        Args:
            data_env (str): The environment variable.

        Returns:
            AITransformersBuilder: Returns self for chaining.
        """
        self.data_env = data_env
        return self

    @set_method_call
    def with_config_file(self, config_file: str, section: str, config_key: str) -> 'AITransformersBuilder':
        """
        Sets up the configuration file (.ini).

        This method allows specifying a configuration file, a section within that file, and a key to retrieve a specific value from the section.

        Args:
            config_file (str): The path to the.ini configuration file.
            section (str): The section name within the.ini file where the desired configuration is located.
            config_key (str): The key within the specified section whose value will be retrieved.

        Raises:
            TypeError: If the provided config_file is not a string.
            TypeError: If the provided section is not a string.
            TypeError: If the provided config_key is not a string.

        Example:
            Given a configuration file named `model_config.ini` with the following example content:

            [id]
            model_id = afe07216-14ec-4134-97ae-c483b11d965a

            builder.with_config_file('model_config.ini', 'id', 'model_id')

        Returns:
            AIMod
        """
        validate_type(config_file, str, "Config file")
        validate_type(section, str, "Section")
        validate_type(config_key, str, "Config Key")

        self.config_file = config_file
        self.section = section
        self.config_key = config_key

        config = configparser.ConfigParser()
        config.read(config_file)
        self.identifier = config.get(section, config_key)
        return self

    @set_method_call
    def add_file(self, file_path: str, filetype: str = None):
        """
        Adds a file to the transformer resource.

        This method allows specifying one or more files to be included in the transformer resource being created. The content type for each file can be specified if needed.

        Args:
            file_path (str): Full path to the file to add.
            filetype (str, optional): Content type of the file. Defaults to None, meaning the content type will be automatically inferred.

        Returns:
            AITransformersBuilder: Returns the current instance to allow method chaining.

        Example:
            ai_transformer_create = client.ai_transformers_builder().with_organization('ManuCorp')\
              .add_file('exittransformer.py', 'text/python')\
              .add_file('pkl_encoder.pkl')
        """
        validate_type(file_path, str, "File path")
        validate_type(filetype, (str, None), "File type")

        if not os.path.isabs(file_path):
            file_path = os.path.join(os.getcwd(), file_path)

        if filetype is None:
            filetype = _get_file_type(file_path)

        self.files.append((file_path, filetype))
        return self

    @set_method_call
    def with_find_by_name(self, find_name: str) -> 'AITransformersBuilder':
        """
        Specify the name to find.

        Args:
            find_name (str): The name of the transformer.

        Returns:
            AITransformersBuilder: Returns self for chaining.
        """
        validate_type(find_name, str, "Find name")
        self.find_name = find_name
        return self

    def with_evaluate(self, data_evaluate: dict) -> 'AITransformersBuilder':
        """
         Evaluate with transformer

         Args:
             data_evaluate (dict): Prediction

         Raises:
             TypeError: If the prediction is not a dict.

         Example:
            evaluate_data = {
              "data": {
                "PPLast12H": 0,
                "PPLast24H": 0,
                "PPLast72H": 1,
                "currentTemp": -2,
                "changeTemp": -2,
                "minTempLast24H": -3,
                "maxTempLast24H": 2,
                "WNDSpeed": 3,
                "WNDDir": "NW",
                "TotalSND": 342,
                "newSNLast24H": 0,
                "PPNext12H": 0,
                "PPNext24H": 0,
                "PPNext48H": 0,
                "minPPNext24H": 0,
                "maxPPNext24H": 0,
                "WNDSpeedNext24H": 4,
                "WNDDirNext24H": "NW",
                "tempNext24H": -4
              },
              "date": "2022-06-13T13:59:34.779+02:00"
            }
             builder.with_evaluate(evaluate_data)

         Returns:
             AITransformersBuilder: Returns itself to allow for method chaining.
         """
        validate_type(data_evaluate, dict, "Evaluate")
        self.data_evaluate = data_evaluate
        return self

    def with_output_file_path(self, output_file_path: str) -> 'AITransformersBuilder':
        """
        Sets the output file path for the transformer.

        This method allows you to specify the path where the output file will be saved.
        It is particularly useful for operations that involve downloading or saving files.

        Args:
            output_file_path (str): The path where the output file will be saved.

        Example:
            builder.with_output_file_path("rute/prueba.onnx")

        Returns:
            AITransformersBuilder: The instance of the AIModelsBuilder class.
        """
        validate_type(output_file_path, dict, "Output file path")
        self.output_file_path = output_file_path
        return self

    def with_file_name(self, file_name: str) -> 'AITransformersBuilder':
        """
        Specifies the name of the file to be processed.

        This method allows you to specify the name of the file that will be used in operations such as download or evaluation. It is particularly useful when working with specific files that require unique identifiers or names for processing.

        Args:
            file_name (str): The name of the file to be processed.

        Returns:
            AITransformersBuilder: Returns self for chaining.

        Example:
            builder.with_file_name('pkl_encoder.pkl')
        """
        validate_type(file_name, dict, "File name")
        self.file_name = file_name
        return self

    def create(self) -> 'AITransformersBuilder':
        """
        Prepares the creation of the transformer resource.

        Returns:
            AITransformersBuilder: Returns the current instance to allow method chaining.

        Example:
            builder.with_organization('Organization').add_file('exittransformer.py', 'text/python').add_file('pkl_encoder.pkl').create()\
        """
        self.url = f'{self.base_url}/{self.organization_name}/transformers'
        self.method = 'create'
        return self

    def find_all(self) -> 'AITransformersBuilder':
        """
        Searches for all available transformer resources.

        Returns:
            AITransformersBuilder: Returns the current instance to allow method chaining.

        Example:
            builder.with_organization_name('my_organization').find_all()
        """
        self.url = f'{self.base_url}/{self.organization_name}/transformers'
        self.method = 'find'
        return self

    def find_one(self) -> 'AITransformersBuilder':
        """
        Searches for a single transformer resource by its identifier.

        This method prepares the request to find a specific transformer based on its identifier. The identifier is obtained automatically if not explicitly defined or can be obtained from a configuration file or environment variables.

        Returns:
            AITransformersBuilder: Returns the current instance to allow method chaining.

        Example:
            builder.with_organization_name('my_organization').with_identifier('identifier').find_one()
        """
        identifier = self._get_identifier()
        self.url = f'{self.base_url}/{self.organization_name}/transformers/{identifier}'
        self.method = 'find'
        return self

    def update(self) -> 'AITransformersBuilder':
        """
        Updates an existing transformer resource.

        This method prepares the URL and HTTP method necessary to send a PUT request to the API to update an existing transformer. It is necessary to configure the relevant attributes of the `AITransformersBuilder` instance, including the `identifier` of the transformer to update, before calling this method.

        Returns:
            AITransformersBuilder: Returns the current instance to allow method chaining.

        Example:
            builder.with_organization_name('my_organization').with_identifier('12345').update()
        """
        identifier = self._get_identifier()
        self.url = f'{self.base_url}/{self.organization_name}/transformers/{identifier}'
        self.method = 'update'
        return self

    def delete(self) -> 'AITransformersBuilder':
        """
        Deletes an existing transformer resource.

        This method prepares the URL and HTTP method necessary to send a DELETE request to the API to delete an existing transformer. It is necessary to configure the `identifier` attribute of the `AITransformersBuilder` instance before calling this method.

        Returns:
            AITransformersBuilder: Returns the current instance to allow method chaining.

        Example:
            builder.with_organization_name('my_organization').with_identifier('12345').delete()
        """
        identifier = self._get_identifier()
        self.url = f'{self.base_url}/{self.organization_name}/transformers/{identifier}'
        self.method = 'delete'
        return self

    def download(self) -> 'AITransformersBuilder':
        """
        Download the model file.

        This method sets up the AIModelsBuilder instance to download the file of a specific model associated with the specified organization and identifier. It configures the URL endpoint for the download operation and sets the operation type to 'download'.

        Example:
            builder.with_organization_name("MyOrganization").with_identifier("model_identifier").with_output_file_path("model.onnx").download().build().execute()
            builder.with_organization_name("MyOrganization").with_find_by_name("model_name.onnx").with_output_file_path("model.onnx").download().build().execute()
            builder.with_organization_name("MyOrganization").with_config_file('model_config.ini', 'id', 'model').with_output_file_path("model.onnx").download().build().execute()

        Returns:
            AITransformersBuilder: The instance of the AIModelsBuilder class itself, allowing for method chaining.
        """
        identifier = self._get_identifier()
        self.url = f'{self.client.url}/north/ai/{self.organization_name}/transformers/{identifier}/{self.file_name}'
        self.method = 'download'
        return self

    def evaluate(self) -> 'AITransformersBuilder':
        """
        Prepares the evaluation of the transformer with provided data.

        This method sets up the URL and method for evaluating the transformer using the provided data. The evaluation data should be set using the `with_evaluate` method before calling this method.

        Returns:
            AITransformersBuilder: Returns the current instance to allow method chaining.

        Example:
            builder.with_organization_name('my_organization').with_identifier('12345').with_evaluate(evaluate_data).evaluate()
        """
        identifier = self._get_identifier()
        self.url = f'{self.base_url}/{self.organization_name}/transformers/{identifier}/transform'
        self.method = 'evaluate'
        return self

    def save(self) -> 'AITransformersBuilder':
        """
        Saves the transformer configuration.

        This method prepares the URL and method for saving the transformer configuration. It checks if the identifier is set from the environment or configuration file and then either updates or creates the transformer accordingly.

        Returns:
            AITransformersBuilder: Returns the current instance to allow method chaining.

        Example:
            builder.with_organization_name('my_organization').with_env('TRANSFORMER_ID').save()
        """
        self.method = 'save'
        return self

    def set_config_file_identifier(self) -> 'AITransformersBuilder':
        """
        Sets the transformer identifier in the configuration file.

        This method sets the transformer identifier in the specified configuration file. It reads the configuration file, updates the identifier, and writes the changes back to the file.

        Returns:
            AITransformersBuilder: Returns the current instance to allow method chaining.

        Example:
            builder.with_config_file('config.ini', 'section', 'key').set_config_file_identifier()
        """
        self.method = 'set_config_identifier'
        return self

    def set_env_identifier(self) -> 'AITransformersBuilder':
        """
        Sets the transformer identifier in the environment variables.

        This method sets the transformer identifier in the specified environment variable. It reads the environment variable, updates the identifier, and writes the changes back to the environment file.

        Returns:
            AITransformersBuilder: Returns the current instance to allow method chaining.

        Example:
            builder.with_env('TRANSFORMER_ID').set_env_identifier()
        """
        self.method = 'set_env_identifier'
        return self

    @set_method_call
    def build(self) -> 'AITransformersBuilder':
        """
        Finalizes the construction of the transformer configuration.

        This method validates the configuration and prepares the builder to execute the request. It should be called before `execute` to ensure that the configuration is complete and valid.

        Returns:
            AITransformersBuilder: Returns the current instance to allow method chaining.

        Raises:
            Exception: If incompatible methods are used together.

        Example:
            builder.build()
        """
        self.builder = True
        self._validate_builds()

        if self.method_calls.count('build_execute') > 0:
            raise Exception("You cannot use build() together with build_execute()")

        return self

    @set_method_call
    def build_execute(self):
        """
        Executes the data sets search immediately after building the configuration.

        This method is a shortcut that combines building and executing in a single step.

        Returns:
            dict: A dictionary containing the execution response which includes the status code and potentially other metadata about the execution.

        Raises:
            ValueError: If `build` has already been called on this builder instance.
        """
        if self.method_calls.count('build') > 0:
            raise ValueError("You cannot use build_execute() together with build()")

        self._validate_builds()
        return self.execute()

    def execute(self) -> requests.Response:
        methods = {
            'create': self._execute_create,
            'find': self._execute_find_all,
            'update': self._execute_update,
            'delete': self._execute_delete,
            'download': self._execute_download,
            'evaluate': self._execute_evaluate,
            'save': self._execute_save,
            'set_config_identifier': self._execute_set_identifier,
            'set_env_identifier': self._execute_env_identifier,
        }

        function = methods.get(self.method)
        if function is None:
            raise ValueError(f'Unsupported method: {self.method}')
        return function()

    def _execute_create(self) -> dict[str, str | int]:
        file_config: Optional[configparser.ConfigParser] = self._read_config_file()
        files_to_upload = _prepare_files(self.files)
        response: requests.Response = requests.post(self.url, headers=self.client.headers, data={},
                                                    files=files_to_upload, verify=False, timeout=3000)
        if response.status_code == 201:
            all_identifiers = self.find_all().build().execute().json()
            python_files = [filename for filename, filetype in self.files if filetype == 'text/python']
            python_file = python_files[0]
            filename = os.path.basename(python_file)
            result = next((item for item in all_identifiers if item['name'] == filename), None)
            if result is not None:
                if file_config:
                    try:
                        self._read_config_file().get(self.section, self.config_key)
                        file_config.set(self.section, self.config_key, result['identifier'])
                        with open(self.config_file, 'w', encoding='utf-8') as configfile:
                            file_config.write(configfile)
                    except configparser.NoOptionError as error:
                        raise ValueError(
                            'The "transformer_id" parameter was not found in the configuration file.') from error
            elif self.data_env is not None:
                try:
                    env_vars = dotenv_values('.env')
                    if self.data_env not in env_vars:
                        raise KeyError('The environment variable was not found in the .env file.')

                    set_key('.env', self.data_env, result['identifier'])

                except KeyError as error:
                    raise ValueError('The environment variable was not found in the .env file.') from error

        else:
            return {'status_code': response.status_code, 'error': response.text}

    def _execute_find(self) -> requests.Response | dict[str, Any]:
        response = send_request('get', self.client.headers, self.url)
        if response.status_code == 200:
            return response
        else:
            return {'status_code': response.status_code, 'error': response.text}

    def _execute_update(self) -> dict[str, Any]:
        files_to_upload = _prepare_files(self.files)
        payload = {}
        response = send_request('put', self.client.headers, self.url, payload, files_to_upload)
        return handle_basic_response(response)

    def _execute_delete(self) -> dict[str, Any]:
        response = send_request('delete', self.client.headers, self.url)
        return handle_basic_response(response)

    def _execute_download(self) -> dict[str, str | int]:
        response = send_request('get', self.client.headers, self.url)

        if response.status_code == 200:
            with open(self.output_file_path, 'wb') as file:
                for chunk in response.iter_content(chunk_size=8192):
                    file.write(chunk)
        else:
            return {'status_code': response.status_code, 'error': response.text}

    def _execute_evaluate(self) -> Union[int, Dict]:
        self.client.headers['Content-Type'] = 'application/json'
        response = send_request('post', self.client.headers, self.url, json.dumps(self.data_evaluate))
        return handle_basic_response(response)

    def _execute_save(self) -> Response | ValueError:
        if self.data_env is not None or self.config_file is not None:
            if self.data_env is not None:
                identifier = dotenv_values('.env')[self.data_env]
                self.identifier = identifier

            elif self.config_file is not None:
                config = configparser.ConfigParser()
                config.read(self.config_file)
                transformer_id = config.get(self.section, self.config_key, fallback=None)
                self.identifier = transformer_id

            response = self.find_one().build().execute()
            if response.status_code == 200:
                #Update
                return self.update().build().execute()
            # Create
            return self.create().build().execute()

        return ValueError('The "config file" or env parameter was not found')

    def _execute_set_identifier(self) -> Optional[Union[None, ValueError]]:
        try:
            file_config: Optional[configparser.ConfigParser] = self._read_config_file()
            self._read_config_file().get('id', 'transformer_id')
            file_config.set('id', 'transformer_id', self.identifier)
            with open(self.config_file, 'w', encoding='utf-8') as configfile:
                file_config.write(configfile)
            return None
        except configparser.NoOptionError:
            return ValueError('The "transformer_id" parameter was not found in the configuration file.')

    def _execute_env_identifier(self) -> None:
        try:
            env_vars = dotenv_values('.env')
            if self.data_env not in env_vars:
                raise KeyError('The environment variable was not found in the .env file.')

            set_key('.env', self.data_env, self.identifier)

        except KeyError as error:
            raise ValueError('The environment variable was not found in the .env file.') from error

    def _read_config_file(self) -> Optional[configparser.ConfigParser]:
        if self.config_file is not None:
            if os.path.exists(self.config_file):
                config: configparser.ConfigParser = configparser.ConfigParser()
                config.read(self.config_file)
                return config
            raise ValueError('The configuration file does not exist.')
        return None

    def _get_identifier(self) -> str:
        if self.identifier is not None:
            return self.identifier

        if self.data_env is not None:
            config = dotenv_values()
            identifier = config.get(self.data_env)
            if identifier is None:
                raise ValueError('The parameter was not found in the configuration env')
            return identifier

        if self.config_file is not None and self.section is not None and self.config_key is not None:
            config = self._read_config_file()
            try:
                return config.get(self.section, self.config_key)
            except configparser.NoOptionError:
                raise ValueError('The "transformer_id" parameter was not found in the configuration file.')

        if self.find_name is not None:
            response = self.find_all().build().execute()
            all_identifiers = parse_json(response)
            name_identifier = [item['identifier'] for item in all_identifiers if item['name'] == self.find_name]

            if not name_identifier:
                raise Exception(f'File name "{self.find_name}" does not exist')

            return name_identifier[0]

        raise ValueError(
            'A configuration file with identifier, a transformer identifier, or a find by name is required.')

    def _validate_builds(self):
        if not self.device_identifier:
            raise ValueError("Device identifier must be set.")

        if self.method_calls.count('with_device_identifier') > 1:
            raise ValueError("It cannot have more than one device identifier.")

        if self.method_calls.count('from_dict') == 0 and not self.payload['datastreams']:
            raise ValueError(
                "The from_dict() or add_datastream_datapoints or add_datastream_datapoints_with_from() from_add method must be called or at least one datastream must be configured.")

    @staticmethod
    def _get_file_type(file_path: str) -> str:
        filename = os.path.basename(file_path)
        type_guess = mimetypes.guess_type(filename)[0]

        if filename.endswith('.py'):
            return 'text/python'

        return type_guess if type_guess else 'application/octet-stream'

    @staticmethod
    def _prepare_files(files: List[Tuple]) -> List[Tuple[str, Tuple[str, bytes, str]]]:
        files_to_upload: List[Tuple[str, Tuple[str, bytes, str]]] = []
        for file_obj in files:
            file_path, file_type = file_obj
            with open(file_path, 'rb') as file:
                file_data = file.read()
            file_entry: Tuple[str, Tuple[str, bytes, str]] = (
                'files', (os.path.basename(file_path), file_data, file_type))
            files_to_upload.append(file_entry)
        return files_to_upload
