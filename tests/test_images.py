from . import WikiBaseTestCase
from google.cloud import vision


class TestImages (WikiBaseTestCase):
    # Test that Cloud Vision API is returning results.
    def test_cloud_vision(self):
        # Instantiates a client
        client = vision.ImageAnnotatorClient()

        request = {
            'image': {
                'source': {
                    'image_uri': 'https://www.cats.org.uk/uploads/images/featurebox_sidebar_kids/grief-and-loss.jpg'},
            },
            "features": [
                {
                    "type": "LABEL_DETECTION",
                }
            ],
        }

        result = client.annotate_image(request)
        labels = result.label_annotations

        assert labels