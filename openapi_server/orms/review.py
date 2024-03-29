import os
from typing import Optional
from pynamodb.models import Model
from pynamodb.attributes import (
    UnicodeAttribute,
    NumberAttribute,
    BooleanAttribute,
)


class DbReview(Model):
    class Meta:
        table_name: str = "Review"
        host: Optional[str] = os.environ.get("AWS_DYNAMODB_HOST")

    id: UnicodeAttribute = UnicodeAttribute(hash_key=True, default="")
    created_at: UnicodeAttribute = UnicodeAttribute(default="")
    updated_at: UnicodeAttribute = UnicodeAttribute(default="")
    username: UnicodeAttribute = UnicodeAttribute(default="")
    restaurantId: UnicodeAttribute = UnicodeAttribute(default="")
    rating: NumberAttribute = NumberAttribute(default=0)
    favorite_food: UnicodeAttribute = UnicodeAttribute(default="")
    starred: BooleanAttribute = BooleanAttribute(default=False)
    content: UnicodeAttribute = UnicodeAttribute(null=True)
    photo_url: UnicodeAttribute = UnicodeAttribute(null=True)
