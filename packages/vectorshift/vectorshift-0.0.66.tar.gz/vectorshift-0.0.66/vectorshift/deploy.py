# functionality to deploy and run pipelines
import inspect
import json
import mimetypes
import requests
from types import GenericAlias

import vectorshift
from vectorshift.pipeline import Pipeline
from vectorshift.consts import *


class Config:
    # For now, the config is just a wrapper for the API key
    def __init__(self, api_key=None, public_key=None, private_key=None):
        self.api_key = api_key or vectorshift.api_key
        self.public_key = public_key or vectorshift.public_key
        self.private_key = private_key or vectorshift.private_key

    def fetch_user_details(self) -> dict:
        response = requests.get(
            API_USER_DETAILS_ENDPOINT,
            headers={
                'Api-Key': self.api_key,
                'Public-Key': self.public_key,
                'Private-Key': self.private_key,
            },
        )
        if response.status_code != 200:
            raise Exception(response.text)
        return response.json()

    def fetch_all_pipelines(self) -> list[dict]:
        response = requests.get(
            API_PIPELINE_FETCH_ALL_ENDPOINT,
            headers={
                'Api-Key': self.api_key,
                'Public-Key': self.public_key,
                'Private-Key': self.private_key,
            },
        )
        if response.status_code != 200:
            raise Exception(response.text)
        return response.json()

    def fetch_all_pipeline_ids(self) -> list[str]:
        ps = self.fetch_all_pipelines()
        ids = [p.get('id') for p in ps]
        return [id for id in ids if id is not None]

    # Save the pipeline as a new pipeline to the VS platform.
    def save_new_pipeline(self, pipeline: Pipeline) -> dict:
        # already implemented in the Pipeline class
        # save method will itself raise an exception if 200 isn't returned
        response = pipeline.save(
            api_key=self.api_key,
            public_key=self.public_key,
            private_key=self.private_key,
            update_existing=False,
        )
        return response.json()

    def fetch_shared_pipelines(self) -> dict:
        response = requests.get(
            API_PIPELINE_SHARED_ENDPOINT,
            headers={
                'Api-Key': self.api_key,
                'Public-Key': self.public_key,
                'Private-Key': self.private_key,
            },
        )
        if response.status_code != 200:
            raise Exception(response.text)
        return response.json()

    # Update the pipeline, assuming it already exists in the VS platform.
    # Raises if the pipeline ID doesn't exist, or isn't in the VS platform.
    def update_pipeline(self, pipeline: Pipeline) -> dict:
        response = pipeline.save(
            api_key=self.api_key,
            public_key=self.public_key,
            private_key=self.private_key,
            update_existing=True,
        )

        if response.status_code != 200:
            raise Exception(response.text)
        return response.json()

    def delete_pipelines(self, pipeline_ids: list[str]):
        if pipeline_ids == []:
            return
        response = requests.delete(
            API_PIPELINE_DELETE_ENDPOINT,
            data={'pipeline_ids': pipeline_ids},
            headers={
                'Api-Key': self.api_key,
                'Public-Key': self.public_key,
                'Private-Key': self.private_key,
            },
        )
        if response.status_code != 200:
            raise Exception(response.text)
        return response.json()

    def fetch_all_files(self) -> list[dict]:
        response = requests.get(
            API_FILE_FETCH_ALL_ENDPOINT,
            headers={
                'Api-Key': self.api_key,
                'Public-Key': self.public_key,
                'Private-Key': self.private_key,
            },
        )
        if response.status_code != 200:
            raise Exception(response.text)
        return response.json()

    def upload_file(
        self, file: str, folder_id: str = None, filetype: str = None
    ) -> dict:
        try:
            headers = {
                'Api-Key': self.api_key,
                'Public-Key': self.public_key,
                'Private-Key': self.private_key,
            }
            # infer the file type
            if filetype is None:
                filetype = mimetypes.guess_type(file)[0]
            if filetype is None:
                raise ValueError(
                    f'Could not determine file type of {file}. Please ensure the file name has an appropriate suffix.'
                )

            with open(file, 'rb') as f:
                files = {'file': (file, f, filetype)}
                response = requests.post(
                    API_FILE_UPLOAD_ENDPOINT,
                    data={'folderId': folder_id},
                    headers=headers,
                    files=files,
                )
        except Exception as e:
            raise ValueError(f'Problem uploading file: {e}')
        print('Successfully uploaded file.')
        return response.json()

    def delete_files_by_id(self, file_ids: list[str]) -> dict:
        headers = {
            'Api-Key': self.api_key,
            'Public-Key': self.public_key,
            'Private-Key': self.private_key,
        }
        response = requests.delete(
            API_FILE_DELETE_ENDPOINT,
            data={'file_ids': file_ids},
            headers=headers,
        )
        if response.status_code != 200:
            raise Exception(response.text)
        print('Successfully deleted file(s).')
        return response.json()

    def delete_files_by_name(self, file_names: list[str]) -> dict:
        headers = {
            'Api-Key': self.api_key,
            'Public-Key': self.public_key,
            'Private-Key': self.private_key,
        }
        response = requests.delete(
            API_FILE_DELETE_BY_NAMES_ENDPOINT,
            data={'file_names': file_names},
            headers=headers,
        )
        if response.status_code != 200:
            raise Exception(response.text)
        print('Successfully deleted file(s).')
        return response.json()

    def fetch_all_knowledge_bases(self) -> list[dict]:
        response = requests.get(
            API_VECTORSTORE_FETCH_ALL_ENDPOINT,
            headers={
                'Api-Key': self.api_key,
                'Public-Key': self.public_key,
                'Private-Key': self.private_key,
            },
        )
        if response.status_code != 200:
            raise Exception(response.text)
        return response.json()

    fetch_all_vectorstores = fetch_all_knowledge_bases

    # TODO add methods to delete vectorstores & share objs

    def fetch_all_transformations(self) -> list[dict]:
        response = requests.get(
            API_TRANSFORMATION_FETCH_ALL_ENDPOINT,
            headers={
                'Api-Key': self.api_key,
                'Public-Key': self.public_key,
                'Private-Key': self.private_key,
            },
        )
        if response.status_code != 200:
            raise Exception(response.text)
        return response.json()

    def fetch_transformation(
        self, transformation_id: str = None, transformation_name: str = None
    ):
        if transformation_id is None and transformation_name is None:
            raise ValueError(
                'At least one of the transformation ID or name must be specified.'
            )
        response = requests.get(
            API_TRANSFORMATION_FETCH_ENDPOINT,
            data={
                'transformation_id': transformation_id,
                'transformation_name': transformation_name,
            },
            headers={
                'Api-Key': self.api_key,
                'Public-Key': self.public_key,
                'Private-Key': self.private_key,
            },
        )
        if response.status_code != 200:
            raise Exception(response.text)
        return response.json()

    def save_transformation(
        self,
        transformation_func,
        outputs: dict[str, str],
        name: str = '',
        description: str = '',
        inputs: dict[str, str] = {},
        update_id: str = None,
    ) -> dict:
        def get_transformation_type_from_anno_type(t):
            if type(t) == type:
                return TRANSFORMATION_TYPE_NAMES.get(t.__name__, 'Any')
            elif isinstance(t, GenericAlias):
                return TRANSFORMATION_TYPE_NAMES.get(t.__origin__.__name__, 'Any')
            return 'Any'

        # validate inputs
        if not callable(transformation_func):
            raise ValueError('Cannot save a non-function object as a transformation')
        f_code = transformation_func.__code__
        n_args = f_code.co_argcount
        if inputs != {} and len(inputs.keys()) != n_args:
            raise ValueError(
                f'Incorrect number of inputs given for function (expected {n_args})'
            )
        f_argnames = f_code.co_varnames[:n_args]
        if inputs != {} and sorted(inputs.keys()) != sorted(f_argnames):
            raise ValueError(
                f'Incorrect input names given for function (expected {f_argnames})'
            )
        supported_transformation_types = TRANSFORMATION_TYPE_NAMES.values()
        for t in inputs.values():
            if t not in supported_transformation_types:
                raise ValueError(f'Invalid transformation input type {t}')
        for t in outputs.values():
            if t not in supported_transformation_types:
                raise ValueError(f'Invalid transformation output type {t}')
        # infer types from annotations if applicable
        _f_members = inspect.getmembers(transformation_func)
        f_members = {m[0]: m[1] for m in _f_members}
        f_type_annos = f_members.get('__annotations__', {})
        for argname in f_argnames:
            if argname in f_type_annos:
                arg_t = get_transformation_type_from_anno_type(f_type_annos[argname])
                if argname in inputs:
                    input_t = inputs[argname]
                    if input_t != 'Any' and input_t != arg_t:
                        raise ValueError(
                            f'Provided transformation type {input_t}is incompatible with inferred type {arg_t} from type annotations'
                        )
                else:
                    inputs[argname] = arg_t
            else:
                if argname not in inputs:
                    inputs[argname] = 'Any'
        if name == '':
            name = transformation_func.__name__
        # TODO is there some way to check outputs?
        transformation_rep = {
            'id': update_id,
            'name': name,
            'description': description,
            'functionName': transformation_func.__name__,
            'inputs': inputs,
            'outputs': outputs,
            'function': inspect.getsource(transformation_func),
        }
        print(transformation_rep)
        transformation_json = json.dumps(transformation_rep, indent=4)
        response = requests.post(
            API_TRANSFORMATION_SAVE_ENDPOINT,
            data={'transformation': transformation_json},
            headers={
                'Api-Key': self.api_key,
                'Public-Key': self.public_key,
                'Private-Key': self.private_key,
            },
        )
        if response.status_code != 200:
            raise Exception(f'Server error creating transformation: {response.text}')
        return response.json()

    def delete_transformation(self, transformation_ids: list[str]):
        headers = {
            'Api-Key': self.api_key,
            'Public-Key': self.public_key,
            'Private-Key': self.private_key,
        }
        response = requests.delete(
            API_TRANSFORMATION_DELETE_ENDPOINT,
            data={'transformation_ids': transformation_ids},
            headers=headers,
        )
        if response.status_code != 200:
            raise Exception(response.text)
        print('Successfully deleted transformation(s).')
        return response.json()


VectorShift = Config
