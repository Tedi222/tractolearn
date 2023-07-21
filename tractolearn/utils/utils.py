# -*- coding: utf-8 -*-

import datetime
import os
from os.path import join as pjoin
from pathlib import Path
from uuid import uuid4


def make_run_dir(out_path=None, add_uuid=True):
    """Create a directory for this training run"""
    if out_path is None:
        root_output_path = Path(os.environ.get("OUTPUT_PATH", "."))
    else:
        root_output_path = out_path

    if add_uuid:
        run_name = generate_uuid()
        run_dir = Path(pjoin(root_output_path, run_name))
    else:
        run_dir = Path(root_output_path)
    run_dir.mkdir()
    return run_dir


def generate_uuid():

    eventid = datetime.datetime.now().strftime("%Y%m%d-%H%M%S-%f-") + str(
        uuid4()
    )
    return eventid
