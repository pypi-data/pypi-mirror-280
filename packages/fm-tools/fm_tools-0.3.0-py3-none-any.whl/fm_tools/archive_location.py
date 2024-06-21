# This file is part of fm-tools, a library for interacting with fm-data files:
# https://gitlab.com/sosy-lab/software/fm-actor
#
# SPDX-FileCopyrightText: 2024 Dirk Beyer <https://www.sosy-lab.org>
#
# SPDX-License-Identifier: MIT

import logging
from dataclasses import dataclass
from typing import Optional

import httpx

from fm_tools.download import DownloadDelegate
from fm_tools.zenodo import get_archive_url_from_zenodo_doi, get_metadata_from_zenodo_doi


@dataclass(frozen=True)
class ArchiveLocation:
    raw: str
    resolved: Optional[str] = None

    def resolve(self, download_delegate=None) -> "ArchiveLocation":
        if self.resolved is not None:
            return self

        delegate = download_delegate or DownloadDelegate()

        resolved = get_archive_url_from_zenodo_doi(self.raw, delegate)
        return ArchiveLocation(self.raw, resolved)

    def is_zenodo_based(self) -> bool:
        return (self.resolved is None) or (self.raw != self.resolved)

    def checksum(self, download_delegate=None) -> Optional[str]:
        """
        Obtain the checksum for the archive. If the archive is zenodo
        based, the zenodo API is queried for the checksum.
        In the other cases this functions tries to obtain the etag of the
        zip file.
        
        :returns: the checksum as a string or None if it could not be obtained
        """
        delegate = download_delegate or DownloadDelegate()

        if not self.is_zenodo_based():
            return httpx.head(self.resolved, timeout=10).headers.get("etag", None)

        data = get_metadata_from_zenodo_doi(self.raw, delegate)

        if len(data["files"]) > 1:
            logging.warning(
                "There are more than one file in the Zenodo record. "
                "The first files checksum will be used."
            )

        return data["files"][0].get("checksum", None)
