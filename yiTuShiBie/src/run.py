# !/usr/bin/env python
import sys

sys.path.append('../')

from src.config import CONFIG
from src.views import app

app.static('/statics', CONFIG.BASE_DIR + '/statics')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8001)
