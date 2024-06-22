# -*- coding: utf-8 -*-
"""Altissimo Firestore class file."""

from google.cloud import firestore

from altissimo.tools import list_to_dict


class Firestore:
    """Altissimo Firestore class."""

    def __init__(self, project=None, credentials=None, database=None):
        """Initialize Firestore class."""
        self.db = firestore.Client(
            project=project,
            credentials=credentials,
            database=database,
        )
        self.firestore = firestore

    def get_collection(self, collection, include_id=True):
        """Return a list of dicts from a collection."""
        ref = self.db.collection(collection)
        items = []
        for doc in ref.stream():
            item = doc.to_dict()
            if include_id:
                item["id"] = doc.id
            items.append(item)
        return items

    def get_collection_dict(self, collection, include_id=True):
        """Return a list of dicts from a collection."""
        ref = self.db.collection(collection)
        items = {}
        for doc in ref.stream():
            item = doc.to_dict()
            if include_id:
                item["id"] = doc.id
            items[doc.id] = item
        return items

    def get_collection_group(self, collection, include_id=True):
        """Return a dict of dicts from a collection group."""
        ref = self.db.collection_group(collection)
        items = []
        for doc in ref.stream():
            item = doc.to_dict()
            if include_id:
                item["id"] = doc.id
            items.append(item)
        return items

    def get_collection_group_dict(self, collection, include_id=True):
        """Return a dict of dicts from a collection group."""
        ref = self.db.collection_group(collection)
        items = {}
        for doc in ref.stream():
            item = doc.to_dict()
            if include_id:
                item["id"] = doc.id
            items[doc.id] = item
        return items

    def get_docs(self, collection):
        """Return a list of docs in a collection."""
        ref = self.db.collection(collection)
        return list(ref.get())

    def get_docs_dict(self, collection):
        """Return a dict of docs in a collection."""
        docs = {}
        for doc in self.get_docs(collection):
            docs[doc.id] = doc
        return docs
