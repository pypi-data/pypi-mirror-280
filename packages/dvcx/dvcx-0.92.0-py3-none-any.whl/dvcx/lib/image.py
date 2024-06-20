import inspect
from io import BytesIO
from typing import Any, Callable, Optional

try:
    import torch
    from PIL import Image
except ImportError as exc:
    raise ImportError(
        "Missing dependencies for computer vision:\n"
        "To install run:\n\n"
        "  pip install 'dvcx[cv]'\n"
    ) from exc

from dvcx.lib.file import BinaryFile
from dvcx.lib.reader import FeatureReader


def convert_image(
    img: Image.Image,
    mode: str = "RGB",
    size: Optional[tuple[int, int]] = None,
    transform: Optional[Callable] = None,
    open_clip_model: Optional[Any] = None,
):
    """
    Resize, transform, and otherwise convert an image.

    Args:
        img (Image): PIL.Image object.
        mode (str): PIL.Image mode.
        size (tuple[int, int]): Size in (width, height) pixels for resizing.
        transform (Callable): Torchvision v1 or other transform to apply.
        open_clip_model (Any): Encode image using model from open_clip library.
    """
    if mode:
        img = img.convert(mode)
    if size:
        img = img.resize(size)
    if transform:
        img = transform(img)
        if open_clip_model:
            img = img.unsqueeze(0)  # type: ignore[attr-defined]
    if open_clip_model:
        method_name = "encode_image"
        if not (
            hasattr(open_clip_model, method_name)
            and inspect.ismethod(getattr(open_clip_model, method_name))
        ):
            raise ValueError(
                f"Unable to render Image: 'open_clip_model' doesn't support"
                f" '{method_name}()'"
            )
        img = open_clip_model.encode_image(img)
    return img


class ImageFile(BinaryFile):
    def get_value(self):
        value = super().get_value()
        return Image.open(BytesIO(value))


class ImageReader(FeatureReader):
    def __init__(
        self,
        mode: str = "RGB",
        size: Optional[tuple[int, int]] = None,
        transform: Optional[Callable] = None,
        open_clip_model: Any = None,
    ):
        """
        Read and optionally transform an image.

        All kwargs are passed to `convert_image()`.
        """
        self.mode = mode
        self.size = size
        self.transform = transform
        self.open_clip_model = open_clip_model
        super().__init__(ImageFile)

    def __call__(self, img: Image.Image):
        return convert_image(
            img,
            mode=self.mode,
            size=self.size,
            transform=self.transform,
            open_clip_model=self.open_clip_model,
        )


def similarity_scores(
    model: Any,
    preprocess: Callable,
    tokenizer: Callable,
    image: Image.Image,
    text: str,
    prob: bool = False,
) -> list[float]:
    """
    Calculate CLIP similarity scores for one or more texts given an image.

    Args:
        model: Model from clip or open_clip packages.
        preprocess: Image preprocessing transforms.
        tokenizer: Text tokenizer.
        image: Image.
        text: Text.
        prob: Compute softmax probabilities across texts.
    """

    with torch.no_grad():
        image = preprocess(image).unsqueeze(0)
        text = tokenizer(text)

        image_features = model.encode_image(image)
        text_features = model.encode_text(text)

        image_features /= image_features.norm(dim=-1, keepdim=True)
        text_features /= text_features.norm(dim=-1, keepdim=True)

        logits_per_text = 100.0 * image_features @ text_features.T

        if prob:
            scores = logits_per_text.softmax(dim=1)
        else:
            scores = logits_per_text

        return scores[0].tolist()
