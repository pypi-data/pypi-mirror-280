from mtai.base import MTAIBase


class Description(MTAIBase):
    """Description Class used across defined."""

    @classmethod
    def list(cls):
        """
        List all Descriptions.
        Returns:
            JSON Response
        """
        return cls().requests.get("descriptions/list")

    @classmethod
    def create_from_title(cls, title):
        """
        Create a new Description from title.
        Args:
            title: str
        Returns:
            JSON Response
        """
        return cls().requests.post(
            "/descriptions/create-session-desc-from-title", data={"title": title}
        )

    @classmethod
    def create_from_title_summary(cls, title, summary):
        """
        Create a new Description from title and summary.
        Args:
            title: str
            summary: str
        Returns:
            JSON Response
        """
        return cls().requests.post(
            "/descriptions/create-session-desc-from-title-summary",
            data={"title": title, "summary": summary},
        )

    @classmethod
    def get_description_by_id(cls, description_id):
        """
        Get a Description by id.
        Args:
            description_id: str
        Returns:
            JSON Response
        """
        return cls().requests.get(f"/descriptions/retrieve/{description_id}")

    @classmethod
    def delete_description_by_id(cls, description_id):
        """
        Delete a Description by id.
        Args:
            description_id: str
        Returns:
            JSON Response
        """
        return cls().requests.delete(f"/descriptions/delete/{description_id}")
