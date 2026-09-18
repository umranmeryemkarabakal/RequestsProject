# RequestsProject

<p>
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/Requests-2B5B84?style=for-the-badge" alt="Requests" />
  <img src="https://img.shields.io/badge/aiohttp-2C5BB4?style=for-the-badge" alt="aiohttp" />
  <img src="https://img.shields.io/badge/BeautifulSoup-3C873A?style=for-the-badge" alt="BeautifulSoup" />
</p>

## Overview

Notes and examples on HTTP in Python: GET/POST/PUT/PATCH/DELETE with Requests against JSONPlaceholder, synchronous vs. threaded vs. asyncio/aiohttp requests, and a small link crawler.

**Quick start:** `python 01-requests_example.py`

## Proje hakkında

Python'da HTTP isteklerini anlatan not ve örnekler.

## İçerik

- `01`: HTTP, API, JSON kavramları ve temel `requests` kullanımı
- `02`: senkron istekler ile `threading` karşılaştırması
- `03`: `asyncio` + `aiohttp` ile eşzamansız istekler
- `04`, `05`: JSONPlaceholder üzerinde POST, PUT, PATCH, DELETE
- `06`: BeautifulSoup ile bağlantı toplayan küçük bir tarayıcı

## Kurulum ve çalıştırma

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Dosya yapısı

```text
RequestsProject/
├── 01-requests_example.py
├── 02-threading_example.py
├── 03-asyncio_example.py
├── 04-post.py
├── 05-put_patch_delete.py
└── 06-web_site_crawler.py
```
