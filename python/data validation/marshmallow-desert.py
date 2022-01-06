"""
Example of usage of Marshmallow and Desert dictionary validation obtained from api.
"""
from dataclasses import dataclass
import dataclasses
import json

from marshmallow import EXCLUDE, fields, pre_dump, Schema, validate
import requests
import desert

@dataclass
class Activity:
    activity: str
    participants: int = dataclasses.field(metadata=desert.metadata(
        fields.Int(
            required=True,
            validate=validate.Range(min=1, max=50, error="Participants must be between 1 and 50 people"))
    ))
    price: int = dataclasses.field(metadata=desert.metadata(
        fields.Float(
            required=True,
            validate=validate.Range(min=0, max=.5, error="Price must be between 0 (0$) and .5 ($50)"))
    ))

    def __post_init__(self):
        """
        The 'price' field from the API is always a number between 0 and 1 (.60 is 60)
        so we convert the price to be more intuitive and readable.
        """
        self.price = self.price * 100

def get_activity():
  resp = requests.get("https://www.boredapi.com/api/activity").json()
  schema = desert.schema(Activity, meta={"unknown": EXCLUDE})
  return schema.load(resp)


print(get_activity())
# Output will look something like:
# Activity(activity='Learn how to make an Alexa skill', participants=1, price=10.0)
