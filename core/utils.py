# -*- coding: utf-8 -*-
# core/utils.py

import logging

logger = logging.getLogger(__name__)


def log_exception(source, error):
    logger.error(f"[{source}] Exception occurred: {error}")
