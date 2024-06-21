import dataclasses
import logging
import typing
import torch.utils.data
import PIL.Image
import irisml.core

logger = logging.getLogger(__name__)


class Task(irisml.core.TaskBase):
    """Convert an object detection dataset into a classification dataset."""
    VERSION = '0.2.0'

    @dataclasses.dataclass
    class Inputs:
        dataset: torch.utils.data.Dataset

    @dataclasses.dataclass
    class Config:
        padding: float = 0.2

    @dataclasses.dataclass
    class Outputs:
        dataset: torch.utils.data.Dataset
        index_mappings: typing.Optional[typing.List[typing.Tuple[int, int]]] = None  # map cropped image index in IC to a tuple (original image index in OD dataset, box index in that image)

    def execute(self, inputs):
        if (len(inputs.dataset) == 0 or inputs.dataset[0][1].dim() <= 1):
            # Return input dataset if it is already a multiclass or multilabel classification dataset.
            logger.debug("Dataset is already classification. Skip the task.")
            return self.Outputs(inputs.dataset)
        else:
            od_as_ic_dataset = ClassificationFromDetectionDataset(inputs.dataset, padding=self.config.padding)
            return self.Outputs(od_as_ic_dataset, od_as_ic_dataset.index_mappings)

    def dry_run(self, inputs):
        return self.execute(inputs)


class ClassificationFromDetectionDataset(torch.utils.data.Dataset):
    def __init__(self, dataset, padding=0):
        self._dataset = dataset
        self.padding = padding
        valid_boxes = [self._get_valid_boxes(i) for i in range(len(dataset))]
        self._index_mappings = [(i, j) for i, n in enumerate(valid_boxes) for j in n]

        logger.info(f"Created a classificaiton dataset with {len(self._index_mappings)} samples. The source dataset has {len(self._dataset)} samples.")

    def __len__(self):
        return len(self._index_mappings)

    def __getitem__(self, index):
        image_index, box_index = self._index_mappings[index]
        image, targets = self._dataset[image_index]
        assert isinstance(image, PIL.Image.Image)
        w, h = image.size
        box = targets[box_index]
        padded_box = self._pad_box(box, w, h, self.padding)
        cropped = image.crop((int(w * padded_box[1]), int(h * padded_box[2]), int(w * box[3]), int(h * box[4])))
        return cropped, box[0].int()

    def get_targets(self, index):
        image_index, box_index = self._index_mappings[index]
        targets = self._get_targets_from_original(image_index)
        box = targets[box_index]
        return box[0].int()

    def _get_targets_from_original(self, index):
        return self._dataset.get_targets(index) if hasattr(self._dataset, 'get_targets') else self._dataset[index][1]

    def _get_valid_boxes(self, index):
        image, targets = self._dataset[index]
        w, h = image.size
        box_areas = [(int(w * box[3]) - int(w * box[1])) * (int(h * box[4]) - int(h * box[2])) for box in targets]
        return [i for i, a in enumerate(box_areas) if a > 0]

    @property
    def index_mappings(self):
        return self._index_mappings

    def _pad_box(self, box, w, h, padding):
        if padding == 0:
            return box

        w_pad = int(w * padding)
        h_pad = int(h * padding)

        _, x1, y1, x2, y2 = box
        x1 = max(0, x1 - w_pad)
        y1 = max(0, y1 - h_pad)
        x2 = min(w, x2 + w_pad)
        y2 = min(h, y2 + h_pad)
        return (box[0], x1 / w, y1 / h, x2 / w, y2 / h)
