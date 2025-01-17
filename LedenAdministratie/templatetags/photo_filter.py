from django import template
from django.forms import BoundField
from django.core.files.uploadedfile import UploadedFile
import base64
import imghdr

register = template.Library()

onbekend_persoon = """
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
gg==
"""


@register.filter(name="img2base64", is_safe=True)
def img2base64(field):
    if isinstance(field, BoundField):
        foto = field.value()
    else:
        foto = field

    if foto is None or foto == "":
        return "data:image/png;base64,{0}".format(onbekend_persoon)

    if isinstance(foto, UploadedFile):
        foto = foto.file.read()

    image_type = imghdr.what(None, foto)
    base64img = base64.encodebytes(foto).decode("ascii")
    return "data:image/{0};base64,{1}".format(image_type, base64img)
