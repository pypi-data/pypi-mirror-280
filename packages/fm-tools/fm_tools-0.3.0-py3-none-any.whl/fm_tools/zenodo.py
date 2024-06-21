# This file is part of fm-actor, a library for interacting with fm-data files:
# https://gitlab.com/sosy-lab/software/fm-actor
#
# SPDX-FileCopyrightText: 2024 Dirk Beyer <https://www.sosy-lab.org>
#
# SPDX-License-Identifier: MIT

import json
import logging
from functools import lru_cache

from fm_tools.download import DownloadDelegate
from fm_tools.exceptions import UnsupportedDOIException

ZENODO_API_URL_BASE = "https://zenodo.org/api/records/"


@lru_cache(maxsize=128)
def get_metadata_from_zenodo_doi(doi, download_delegate=None):
    if download_delegate is None:
        download_delegate = DownloadDelegate()

    zenodo_record_id = doi.rsplit(".")[-1]
    response = download_delegate.get(
        ZENODO_API_URL_BASE + zenodo_record_id,
        headers={"Accept": "application/json"},
    )

    if response.status_code != 200:
        raise UnsupportedDOIException(
            f"Failed to get the Zenodo record. "
            f"Status code: {response.status_code}, "
            f"URL: {response.url}"
        )

    return json.loads(response.content)


def get_archive_url_from_zenodo_doi(doi, download_delegate=None):
    if download_delegate is None:
        download_delegate = DownloadDelegate()

    data = get_metadata_from_zenodo_doi(doi, download_delegate)

    if len(data["files"]) > 1:
        logging.warning(
            "There are more than one file in the Zenodo record. "
            "The first file will be used."
        )

    # the archive URL is the first file's self link
    return data["files"][0]["links"]["self"]
