from enum import Enum
from typing import Dict, List, Optional

from kognic.base_clients.models import BaseSerializer


class AddFeedbackItemPin(BaseSerializer):
    x: float
    y: float
    z: Optional[float]


class AddFeedbackItemSuggestedProperty(BaseSerializer):
    property_name: str
    suggested_property_value: str


class AddFeedbackItem(BaseSerializer):
    sensor_id: Optional[str]
    frame_id: Optional[str]
    object_id: Optional[str]
    pin: Optional[AddFeedbackItemPin]
    description: Optional[str]
    suggested_property: Optional[AddFeedbackItemSuggestedProperty]
    error_type_id: str
    metadata: Optional[Dict[str, str]]


class ReviewWorkflowEnum(str, Enum):
    CORRECT = "correct"


class ReviewRequest(BaseSerializer):
    feedback_items: List[AddFeedbackItem]
    workflow: ReviewWorkflowEnum
    accepted: bool


class ReviewResponse(BaseSerializer):
    created_review_id: str


class ReviewMember(BaseSerializer):
    sensor_id: Optional[str]
    frame_id: Optional[str]
    object_id: Optional[str]
    comments: Optional[List[str]]
    pin: Optional[AddFeedbackItemPin]
    description: Optional[str]
    suggested_properties: Optional[List[AddFeedbackItemSuggestedProperty]]
    error_type_id: str
    error_type_name: str
    invalid: bool
    metadata: Optional[Dict[str, str]]


class Review(BaseSerializer):
    id: str
    members: List[ReviewMember]
    input_uuid: str
    phase_id: Optional[str]


class ReviewErrorType(BaseSerializer):
    error_type_id: str
    name: str
    pin_allowed: bool
    object_allowed: bool
