import warnings
from datetime import datetime
from typing import Optional

import dateutil.parser
import requests

from marble_client.exceptions import ServiceNotAvailableError
from marble_client.services import MarbleService

__all__ = ["MarbleNode"]


class MarbleNode:
    def __init__(self, nodeid: str, jsondata: dict[str]) -> None:
        self._nodedata = jsondata
        self._id = nodeid
        self._name = jsondata["name"]

        self._links_service = None
        self._links_collection = None
        self._links_version = None

        for item in jsondata["links"]:
            if item.get("rel") in ("service", "collection", "version"):
                setattr(self, "_links_" + item["rel"], item["href"])

        self._services: dict[str, MarbleService] = {}

        for service in jsondata.get("services", []):
            s = MarbleService(service, self)
            if not getattr(self, s.name, False):
                setattr(self, s.name, s)
            self._services[s.name] = s

    def is_online(self) -> bool:
        try:
            registry = requests.get(self.url)
            registry.raise_for_status()
            return True
        except (requests.exceptions.RequestException, requests.exceptions.ConnectionError):
            return False

    @property
    def id(self) -> str:
        return self._id

    @property
    def name(self) -> str:
        return self._name

    @property
    def description(self) -> str:
        return self._nodedata["description"]

    @property
    def url(self) -> Optional[str]:
        return self._links_service

    @property
    def collection_url(self) -> Optional[str]:
        warnings.warn("collection_url has been renamed to services_url", DeprecationWarning, 2)
        return self._links_collection

    @property
    def services_url(self) -> Optional[str]:
        return self._links_collection

    @property
    def version_url(self) -> Optional[str]:
        return self._links_version

    @property
    def date_added(self) -> datetime:
        return dateutil.parser.isoparse(self._nodedata["date_added"])

    @property
    def affiliation(self) -> str:
        return self._nodedata["affiliation"]

    @property
    def location(self) -> dict[str, float]:
        return self._nodedata["location"]

    @property
    def contact(self) -> str:
        return self._nodedata["contact"]

    @property
    def last_updated(self) -> datetime:
        return dateutil.parser.isoparse(self._nodedata["last_updated"])

    @property
    def marble_version(self) -> str:
        warnings.warn("marble_version has been renamed to version", DeprecationWarning, 2)
        return self._nodedata["version"]

    @property
    def version(self) -> str:
        return self._nodedata["version"]

    @property
    def services(self) -> list[str]:
        return list(self._services)

    @property
    def links(self) -> list[dict[str, str]]:
        return self._nodedata["links"]

    def __getitem__(self, service: str) -> MarbleService:
        """Get a service at a node by specifying its name.

        :param service: Name of the Marble service
        :type service: str
        :raises ServiceNotAvailable: This exception is raised if the service is not available at the node
        :return: _description_
        :rtype: MarbleService
        """
        try:
            return self._services[service]
        except KeyError as e:
            raise ServiceNotAvailableError(f"A service named '{service}' is not available on this node.") from e

    def __contains__(self, service: str) -> bool:
        """Check if a service is available at a node

        :param service: Name of the Marble service
        :type service: str
        :return: True if the service is available, False otherwise
        :rtype: bool
        """
        return service in self._services

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__}(id: '{self.id}', name: '{self.name}')>"
