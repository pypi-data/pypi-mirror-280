# functionality for defining and working with Knowledge Base (Vector Store) objects
from typing import Optional
import requests
import json

import vectorshift
from vectorshift.consts import *

class KnowledgeBase:
    # initializes a new Knowledge Base
    # TODO: add support for alpha here (and the corresponding node method from_knowledge_base_obj)
    def __init__(
        self,
        name: str,
        description: str = '',
        chunk_size: int = DEFAULT_CHUNK_SIZE,
        chunk_overlap: int = DEFAULT_CHUNK_OVERLAP,
        is_hybrid: bool = False,
        id: str = None
    ):
        self.name = name
        self.description = description
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
        self.is_hybrid = is_hybrid
        self.id = id

    # converts Knowledge Base object to JSON representation
    def to_json_rep(self) -> dict:
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'chunkSize': self.chunk_size,
            'chunkOverlap': self.chunk_overlap,
            'isHybrid': self.is_hybrid,
        }
    
    def to_json(self) -> str:
        return json.dumps(self.to_json_rep())
    
    @staticmethod
    def from_json_rep(json_data: dict[str, any]) -> 'KnowledgeBase':
        return KnowledgeBase(
            name=json_data.get('name'),
            description=json_data.get('description'),
            chunk_size=json_data.get('chunkSize', DEFAULT_CHUNK_SIZE),
            chunk_overlap=json_data.get('chunkOverlap', DEFAULT_CHUNK_OVERLAP),
            is_hybrid=json_data.get('isHybrid', False),
            id=json_data.get('id'),
        )
    
    @staticmethod
    def from_json(json_str: str) -> 'KnowledgeBase':
        json_data = json.loads(json_str)
        return KnowledgeBase.from_json_rep(json_data)

    def __repr__(self):
        return f'KnowledgeBase({", ".join(f"{k}={v}" for k, v in self.to_json_rep().items())})'

    # TODO: Add validation for base_id and pipeline_id (in pipeline.py)
    # to prevent 5XX errors
    @staticmethod
    def fetch(
        base_id: str = None,
        base_name: str = None,
        username: str = None,
        org_name: str = None,
        api_key: str = None,
        public_key: str = None,
        private_key: str = None
    ) -> 'KnowledgeBase':
        if base_id is None and base_name is None:
            raise ValueError('Must specify either base_id or base_name.')
        if base_name is not None and username is None and org_name is not None:
            raise ValueError('Must specify username if org_name is specified.')

        response = requests.get(
            API_VECTORSTORE_FETCH_ENDPOINT,
            data={
                'vectorstore_id': base_id,
                'vectorstore_name': base_name,
                'username': username,
                'org_name': org_name,
            },
            headers={
                'Api-Key': api_key or vectorshift.api_key,
                'Public-Key': public_key or vectorshift.public_key,
                'Private-Key': private_key or vectorshift.private_key,
            }
        )
        if response.status_code != 200:
            raise Exception(f'Error fetching Knowledge Base object: {response.text}')
        response = response.json()

        return KnowledgeBase.from_json_rep(response)

    def save(
        self,
        update_existing: bool = False,
        api_key: str = None,
        public_key: str = None,
        private_key: str = None,
    ) -> dict:
        if update_existing and not self.id:
            raise ValueError("Error updating: KnowledgeBase object does not have an existing ID. It must be saved as a new Knowledge Base.")
        # if update_existing is false, save as a new knowledge base
        if not update_existing:
            self.id = None

        # API_VECTORSTORE_SAVE_ENDPOINT handles saving and updating knowledge bases 
        # depending on whether or not the JSON has an id (logic in api repo)
        response = requests.post(
            API_VECTORSTORE_SAVE_ENDPOINT,
            data=({'vectorstore': self.to_json()}),
            headers={
                'Api-Key': api_key or vectorshift.api_key,
                'Public-Key': public_key or vectorshift.public_key,
                'Private-Key': private_key or vectorshift.private_key,
            }
        )

        if response.status_code != 200:
            raise Exception(f'Error saving Knowledge Base object: {response.text}')
        response = response.json()
        self.id = response.get('id').get('id')

        return response
    
    def update_metadata(
        self,
        list_of_item_ids: list[str],
        list_of_metadata: list[str],
        keep_prev: bool,
        api_key: str = None,
        public_key: str = None,
        private_key: str = None,
    ) -> None:
        if not self.id:
            raise ValueError("Error updating: Knowledge Base object does not have an existing ID. It must be saved first.")
        
        data = {
            'vectorstore_id': self.id,
            'list_of_item_ids': list_of_item_ids,
            'list_of_metadata': [json.dumps(metadata) for metadata in list_of_metadata],
            'keep_prev': keep_prev,            
        }

        response = requests.post(
            API_VECTORSTORE_UPDATE_METADATA_ENDPOINT,
            data=data,
            headers={
                'Api-Key': api_key or vectorshift.api_key,
                'Public-Key': public_key or vectorshift.public_key,
                'Private-Key': private_key or vectorshift.private_key,
            }
        )

        if response.status_code != 200:
            raise Exception(f'Error updating document(s) metadata: {response.text}')
        return


    def update_selected_files(
        self,
        integration_id: str,
        keep_prev: bool,
        selected_items: Optional[list[str]] = None,
        select_all_items_flag: Optional[bool] = True,
        api_key: str = None,
        public_key: str = None,
        private_key: str = None,
    ) -> None:
        if not self.id:
            raise ValueError("Error updating: Knowledge Base object does not have an existing ID. It must be saved first.")
        
        data = {
            'vectorstore_id': self.id,
            'integration_id': integration_id,
            'selected_items': selected_items,
            'keep_prev': keep_prev,
            'select_all_items_flag': select_all_items_flag,
        }

        response = requests.post(
            API_VECTORSTORE_UPDATE_SELECTED_ITEMS_ENDPOINT,
            data=data,
            headers={
                'Api-Key': api_key or vectorshift.api_key,
                'Public-Key': public_key or vectorshift.public_key,
                'Private-Key': private_key or vectorshift.private_key,
            }
        )

        if response.status_code != 200:
            raise Exception(f'Error updating items selected: {response.text}')
        return
    
    # TODO: endpoint does not exist
    '''
    def sync(
        self,
        api_key: str = None,
        public_key: str = None,
        private_key: str = None,
    ) -> None:
        if not self.id:
            raise ValueError('Error loading documents: Knowledge Base object does not have an existing ID. It must be saved as a new Knowledge Base.')
        
        response = requests.post(
            API_VECTORSTORE_SYNC_ENDPOINT,
            data={
                'vectorstore_id': self.id,
            },
            headers={
                'Api-Key': api_key or vectorshift.api_key,
                'Public-Key': public_key or vectorshift.public_key,
                'Private-Key': private_key or vectorshift.private_key,
            }
        )

        if response.status_code != 200:
            raise Exception(response.text)
        
        response = response.json()
        return
    '''

    def load_documents(
        self,
        document,
        document_name: str = None,
        document_type: str = 'File',
        chunk_size: int = None,
        chunk_overlap: int = None,
        selected_items: list = None,
        select_all_items_flags: list = None,
        metadata: dict = None,
        metadata_by_item: dict = None,
        api_key: str = None,
        public_key: str = None,
        private_key: str = None,
    ) -> dict:
        if not self.id:
            raise ValueError('Error loading documents: Knowledge Base object does not have an existing ID. It must be saved as a new Knowledge Base.')

        if document_type not in ['File', 'Integration', 'URL', 'Recursive URL', 'Wikipedia', 'YouTube', 'Arxiv', 'Git']:
            raise ValueError('Invalid document type.')
        
        chunk_size = chunk_size or self.chunk_size
        chunk_overlap = chunk_overlap or self.chunk_overlap

        data = {
            'vectorstore_id': self.id,
            'vectorstore_name': self.name,
            'document_name': document_name,
            'document_type': document_type,
            'chunk_size': chunk_size,
            'chunk_overlap': chunk_overlap,
            'selected_items': json.dumps(selected_items),
            'select_all_items_flags': json.dumps(select_all_items_flags),
            'metadata': json.dumps(metadata),
            'metadata_by_item': json.dumps(metadata_by_item),
        }

        headers={
            'Api-Key': api_key or vectorshift.api_key,
            'Public-Key': public_key or vectorshift.public_key,
            'Private-Key': private_key or vectorshift.private_key,
        }

        if document_type == 'File':
            if isinstance(document, str):
                with open(document, 'rb') as f:
                    files = {'document': f}
                    response = requests.post(
                        API_VECTORSTORE_LOAD_ENDPOINT,
                        data=data,
                        headers=headers,
                        files=files,
                    )
            else:
                files = {'document': document}
                response = requests.post(
                    API_VECTORSTORE_LOAD_ENDPOINT,
                    data=data,
                    headers=headers,
                    files=files,
                )
        elif document_type == 'Integration':
            data['document'] = document
            response = requests.post(
                    API_VECTORSTORE_LOAD_ENDPOINT,
                    data=data,
                    headers=headers,
                )
        else:
            data['document'] = document
            response = requests.post(
                API_VECTORSTORE_LOAD_ENDPOINT,
                data=data,
                headers=headers,
            )

        if response.status_code != 200:
            raise Exception(f'KnowledgeBase object encountered an error loading documents: {response.text}')
        response = response.json()

        return response

    def query(
        self,
        query: str,
        max_docs: int = 5,
        filter: dict = None,
        rerank: bool = False,
        api_key: str = None,
        public_key: str = None,
        private_key: str = None,
    ) -> dict:
        filter = filter or {}
        response = requests.post(
            API_VECTORSTORE_QUERY_ENDPOINT,
            data={
                'vectorstore_id': self.id,
                'query': query,
                'max_docs': max_docs,
                'filter': filter,
                'rerank': rerank,
            },
            headers={
                'Api-Key': api_key or vectorshift.api_key,
                'Public-Key': public_key or vectorshift.public_key,
                'Private-Key': private_key or vectorshift.private_key,
            }
        )
        if response.status_code != 200:
            raise Exception(response.text)
        response = response.json()

        return response

    def list_documents(self, max_documents: int = None) -> dict:
        if not self.id:
            raise ValueError('Error listing documents: Knowledge Base object does not have an existing ID. It must be saved as a new Knowledge Base.')
        response = requests.post(
            API_VECTORSTORE_LIST_DOCUMENTS_ENDPOINT,
            data={
                'vectorstore_id': self.id,
                'max_documents': max_documents,
            },
            headers={
                'Api-Key': vectorshift.api_key,
                'Public-Key': vectorshift.public_key,
                'Private-Key': vectorshift.private_key,
            }
        )
        if response.status_code != 200:
            raise Exception(f'Error listing documents: {response.text}')
        response = response.json()

        return response

    def delete_documents(self, document_ids: list, filter: dict = None) -> dict:
        # TODO: Add the ability to delete multiple documents at once or by filter
        if not self.id:
            raise ValueError('Error deleting documents: Knowledge Base object does not have an existing ID. It must be saved as a new Knowledge Base.')
        
        if not isinstance(document_ids, list):
            document_ids = [document_ids]
        if len(document_ids) == 0:
            raise ValueError('Error deleting documents: document_ids must be a non-empty list of document IDs.')
        elif len(document_ids) > 1:
            raise NotImplementedError('Error deleting documents: deleting multiple documents at once is not yet supported.')
        response = requests.delete(
            API_VECTORSTORE_DELETE_DOCUMENTS_ENDPOINT,
            data={
                'vectorstore_id': self.id,
                'document_ids': document_ids,
            },
            headers={
                'Api-Key': vectorshift.api_key,
                'Public-Key': vectorshift.public_key,
                'Private-Key': vectorshift.private_key,
            }
        )
        if response.status_code != 200:
            raise Exception(f'Error deleting documents: {response.text}')
        response = response.json()

        return response

    def share(self, shared_users:list[str]) -> dict:
        if not self.id:
            raise ValueError('Error sharing: Knowledge Base does not have an existing ID. It must be saved in order to be shared.')
        
        shared_users_dicts = []
        for user in shared_users:
            shared_users_dicts.append({
                'email': user,
                'permissions': 'View',
            })
        response = requests.post(
            API_VECTORSTORE_SHARE_ENDPOINT,
            data={
                'vectorstore_id': self.id,
                'shared_users': json.dumps(shared_users_dicts),
            },
            headers={
                'Api-Key': vectorshift.api_key,
                'Public-Key': vectorshift.public_key,
                'Private-Key': vectorshift.private_key,
            }
        )
        if response.status_code != 200:
            raise Exception(f'Error sharing Knowledge Base: {response.text}')
        response = response.json()

        return response
    
    def fetch_shared(self) -> dict:
        if not self.id:
            raise ValueError('Error listing documents: Knowledge Base does not have an existing ID. It must be saved.')
        
        response = requests.get(
            API_VECTORSTORE_FETCH_SHARED_ENDPOINT,
            headers={
                'Api-Key': vectorshift.api_key,
                'Public-Key': vectorshift.public_key,
                'Private-Key': vectorshift.private_key,
            }
        )
        if response.status_code != 200:
            raise Exception(f'Error fetching shared Knowledge Base documents: {response.text}')
        response = response.json()

        return response
    
    def remove_share(self, users_to_remove:list[str]) -> dict:
        if not self.id:
            raise ValueError('Error listing documents: Knowledge Base object does not have an existing ID. It must be saved in order to be shared.')
        
        response = requests.delete(
            API_VECTORSTORE_REMOVE_SHARE_ENDPOINT,
            data={
                'vectorstore_id': self.id,
                'users_to_remove': users_to_remove,
            },
            headers={
                'Api-Key': vectorshift.api_key,
                'Public-Key': vectorshift.public_key,
                'Private-Key': vectorshift.private_key,
            }
        )
        if response.status_code != 200:
            raise Exception(f'Error removing shared Knowledge Base: {response.text}')
        response = response.json()

        return response

VectorStore = KnowledgeBase