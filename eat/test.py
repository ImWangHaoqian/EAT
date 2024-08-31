# flake8: noqa
import os.path as osp

import eat.archs
import eat.data
import eat.models
from basicsr.test import test_pipeline

if __name__ == '__main__':
    root_path = osp.abspath(osp.join(__file__, osp.pardir, osp.pardir))
    test_pipeline(root_path)
