"""
Backend for posting pastes to http://paste.ee
"""

from typing import List, Union

import httpx

from .base import BaseBackend, BasePasteFile, BasePasteResult, as_chunks

__author__ = "nexy7574 <https://github.com/nexy7574>"


class PasteEEFile(BasePasteFile):
    # noinspection PyShadowingBuiltins
    def __init__(self, content: str, filename: str = None, syntax: str = "autodetect", *, id: int = None):
        super().__init__(content)
        self.filename = filename
        self.syntax = syntax
        self.id = id

    def __hash__(self):
        return hash((self.content, self.filename))

    def as_json(self):
        return {"content": self.content, "filename": self.filename, "syntax": self.syntax}


class PasteEEBackend(BaseBackend):
    name = "paste.ee"
    base_url = "https://api.paste.ee/v1/pastes"
    post_url = "https://api.paste.ee/v1/pastes"
    html_url = "https://hst.sh/{key}"

    def __init__(self, session: httpx.Client = None, *, token: str):
        """
        :param session: An optional httpx session to use for requests
        :param token: The API token to use for authentication
        """
        self.token = token
        self._session = session

    def create_paste(
        self, *files: PasteEEFile, paste_description: str = None, encrypted: bool = False
    ) -> Union[BasePasteResult, List[BasePasteResult]]:
        """
        Creates a paste on paste.ee

        .. warning::
            Paste.ee only supports 5 files per paste, and up to 6MB
            See [their wiki/acceptable use policy](https://paste.ee/wiki/AUP) for more information.

        :param files: A list of files to post
        :param paste_description: A description of the overall paste. Can be omitted.
        :param encrypted: Whether this paste is already encrypted. Defaults to False.
        :return: A single `BasePasteResult` if less than 5 files were posted, or a list of `BasePasteResult`s if more.
        :raises ValueError: If any of the files are not text files.
        """
        if len(files) > 5:
            self._logger.warning(
                "Posting %d files to paste.ee; paste.ee only supports 5 files per-paste, so this will have to be split"
                " up into multiple pastes. Please consider reducing the number of files you need.",
                len(files),
            )
            results = []
            for chunk in as_chunks(files, 5):
                self._logger.debug("Posting files to paste.ee: %r", chunk)
                results.append(self.create_paste(*chunk))
            return results

        with self.with_session(self._session) as session:
            for file in files:
                if isinstance(file.content, bytes):
                    try:
                        file.content = file.content.decode("utf-8")
                    except UnicodeDecodeError:
                        raise ValueError("paste.ee only supports text files.")

            payload = {"sections": [x.as_json() for x in files]}
            if paste_description:
                payload["description"] = paste_description
            if encrypted:
                payload["encrypted"] = True
            response: httpx.Response = session.post(
                self.post_url,
                json={
                    "encrypted": False,
                    "description": "SuperPaste",
                },
                headers={"Accept": "application/json, text/javascript, */*; q=0.01"},
                auth=(self.token, ""),
            )
            response.raise_for_status()

            data = response.json()
            return BasePasteResult(data["link"], data["id"])

    def get_paste(self, key: str) -> List[PasteEEFile]:
        """
        Gets a paste from paste.ee

        :param key: The key of the paste to get
        :return: A list of files that were in the paste
        """
        r = []
        with self.with_session(self._session) as session:
            response: httpx.Response = session.get(
                self.post_url + "/" + key
            )
            response.raise_for_status()
            data = response.json()
            for section in data["paste"]["sections"]:
                r.append(PasteEEFile(section["content"], section["name"], section["syntax"], id=section["id"]))
        return r
