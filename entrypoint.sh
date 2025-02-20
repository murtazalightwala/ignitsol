#!/bin/bash

poetry run uvicorn main:fastapi_app --host 0.0.0.0 --port 8000
