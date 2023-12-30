# coding: utf-8

"""
    CVPartner

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictBool, StrictStr
from scienta.cvpartner_api.models.user_image import UserImage
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class User(BaseModel):
    """
    User
    """ # noqa: E501
    user_id: StrictStr
    id: StrictStr
    email: Optional[StrictStr] = None
    external_unique_id: Optional[StrictStr] = None
    upn: Optional[StrictStr] = None
    name: Optional[StrictStr] = None
    telephone: Optional[StrictStr] = None
    default_cv_id: Optional[StrictStr] = None
    deactivated: Optional[StrictBool] = None
    deactivated_at: Optional[StrictBool] = None
    created_at: Optional[StrictStr] = None
    updated_at: Optional[StrictStr] = None
    role: Optional[StrictStr] = None
    extra_roles: Optional[List[StrictStr]] = None
    office_id: Optional[StrictStr] = None
    office_name: Optional[StrictStr] = None
    country_id: Optional[StrictStr] = None
    country_code: Optional[StrictStr] = None
    language_code: Optional[StrictStr] = None
    image: Optional[UserImage] = None
    __properties: ClassVar[List[str]] = ["user_id", "id", "email", "external_unique_id", "upn", "name", "telephone", "default_cv_id", "deactivated", "deactivated_at", "created_at", "updated_at", "role", "extra_roles", "office_id", "office_name", "country_id", "country_code", "language_code", "image"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of User from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
            },
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of image
        if self.image:
            _dict['image'] = self.image.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of User from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "user_id": obj.get("user_id"),
            "id": obj.get("id"),
            "email": obj.get("email"),
            "external_unique_id": obj.get("external_unique_id"),
            "upn": obj.get("upn"),
            "name": obj.get("name"),
            "telephone": obj.get("telephone"),
            "default_cv_id": obj.get("default_cv_id"),
            "deactivated": obj.get("deactivated"),
            "deactivated_at": obj.get("deactivated_at"),
            "created_at": obj.get("created_at"),
            "updated_at": obj.get("updated_at"),
            "role": obj.get("role"),
            "extra_roles": obj.get("extra_roles"),
            "office_id": obj.get("office_id"),
            "office_name": obj.get("office_name"),
            "country_id": obj.get("country_id"),
            "country_code": obj.get("country_code"),
            "language_code": obj.get("language_code"),
            "image": UserImage.from_dict(obj.get("image")) if obj.get("image") is not None else None
        })
        return _obj


