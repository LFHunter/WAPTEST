# WAPTEST Twitch 

## Overview
This document outlines WAP testing Twitch site with selenium .


## Installation Guide

### Prerequisites

- Python 3.12.2 or higher
- pip (Python package installer)

### Installation Steps

1. Clone this repository:

   ```bash
   git clone [https://github.com/LFHunter/RestAPITEST.git](https://github.com/LFHunter/WAPTEST.git)
   ```

2. Navigate to the project directory:

   ```bash
   cd WAPTEST
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the application using the following command:

```bash
export PYTHONPATH=/path/to/your_project
pytest --html=MarketstackAPITest_Proj/report.html  MarketstackAPITest_Proj/Testcases/test_historical_api.py
```
**Log**: Twitch_Proj/**%Y-%m-%d_%H%M_%S**_twitch.log  
  
ex: Twitch_Proj/2025-02-10_1804_10_twitch.log

**Html Report** : Twitch_Proj/report.html



