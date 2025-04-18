"""Validate the dataset with the template."""

from typing import Sequence

from absl import app
from absl import flags

from util import dataset_validation_util
from vertex_vision_model_garden_peft.train.vmg import utils
from util import constants


_DATASET_NAME = flags.DEFINE_string(
    'dataset_name',
    None,
    'The dataset name in huggingface.',
    required=True,
)

_TRAIN_SPLIT = flags.DEFINE_string(
    'train_split',
    'train',
    'The train split name.',
)

_TRAIN_COLUMN = flags.DEFINE_string(
    'train_column',
    constants.DEFAULT_TRAIN_COLUMN,
    'The instruct column in dataset.',
)

_TEMPLATE = flags.DEFINE_string(
    'template',
    None,
    'Template for formatting language model training data. Must be a filename'
    ' under `templates` folder, without `.json` extension, e.g. `alpaca`, or a'
    ' Cloud Storage URI to a JSON file.',
    required=True,
)

_MAX_SEQ_LENGTH = flags.DEFINE_integer(
    'max_seq_length',
    None,
    'The maximum sequence length.',
)

_VALIDATE_PERCENTAGE_OF_DATASET = flags.DEFINE_integer(
    'validate_percentage_of_dataset',
    None,
    'The percentage of the dataset to validate with the template. If set to'
    ' -1, it loads the full dataset.',
)

_VALIDATE_K_ROWS_OF_DATASET = flags.DEFINE_integer(
    'validate_k_rows_of_dataset',
    None,
    'The top k rows of the dataset to validate with the template. If set to -1,'
    ' it loads the full dataset.',
)

_USE_MULTIPROCESSING = flags.DEFINE_boolean(
    'use_multiprocessing',
    False,
    'Whether to use multiprocessing for loading the dataset.',
)


def main(unused_argv: Sequence[str]) -> None:
  utils.print_library_versions()

  dataset_validation_util.validate_dataset_with_template(
      dataset_name=_DATASET_NAME.value,
      split=_TRAIN_SPLIT.value,
      input_column=_TRAIN_COLUMN.value,
      template=_TEMPLATE.value,
      max_seq_length=_MAX_SEQ_LENGTH.value,
      use_multiprocessing=_USE_MULTIPROCESSING.value,
      validate_percentage_of_dataset=_VALIDATE_PERCENTAGE_OF_DATASET.value,
      validate_k_rows_of_dataset=_VALIDATE_K_ROWS_OF_DATASET.value,
  )


if __name__ == '__main__':
  app.run(main)
