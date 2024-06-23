"""Base script used across defined."""

import requests
import mtai as api


class Borg:
    """Borg class making class attributes global"""

    _shared_state = {}

    def __init__(self):
        self.__dict__ = self._shared_state


class MTAIBase(Borg):
    """Base Class used across defined."""

    def __init__(self, *args, **kwargs):
        """Initialize mtai with secret key."""
        Borg.__init__(self)
        headers = {}
        secret_key = kwargs.get("secret_key", api.SECRET_KEY)
        if secret_key is not None:
            headers["SECRET-KEY"] = secret_key

        arguments = dict(api_url=api.API_URL, headers=headers)
        if not hasattr(self, "requests"):
            req = MTAIApiRequests(**arguments)
            self._shared_state.update(requests=req)


class MTAIApiRequests(object):
    def __init__(self, api_url=api.API_URL, headers=None):
        """Initialize MTAI API Request object for browsing resource.
        Args:
                api_url: str
                headers: dict
        """
        self.API_BASE_URL = f"{api_url}"
        self.headers = headers

    def _request(self, method, resource_uri, **kwargs):
        """Perform a method on a resource.
        Args:
                method: requests.`method`
                resource_uri: resource endpoint
        Raises:
                HTTPError
        Returns:
                JSON Response
        """
        data = kwargs.get("data")
        params = kwargs.get("params")
        headers = kwargs.get("headers")
        files = kwargs.get("files")
        if headers is not None:
            headers.update(self.headers)
        else:
            headers = self.headers
        if files:
            response = method(
                self.API_BASE_URL + resource_uri,
                data=data,
                headers=headers,
                params=params,
                files=files,
            )
        else:
            response = method(
                self.API_BASE_URL + resource_uri,
                json=data,
                headers=headers,
                params=params,
            )
        return response.json()

    def get(self, endpoint, **kwargs):
        """Get a resource.
        Args:
                endpoint: resource endpoint.
        """
        return self._request(requests.get, endpoint, **kwargs)

    def post(self, endpoint, **kwargs):
        """Create a resource.
        Args:
                endpoint: resource endpoint.
        """
        return self._request(requests.post, endpoint, **kwargs)

    def put(self, endpoint, **kwargs):
        """Update a resource.
        Args:
                endpoint: resource endpoint.
        """
        return self._request(requests.put, endpoint, **kwargs)

    def delete(self, endpoint, **kwargs):
        """Delete a resource.
        Args:
                endpoint: resource endpoint.
        """
        return self._request(requests.delete, endpoint, **kwargs)
