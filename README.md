# Hmong Fashion Backend API

Hệ thống Backend RESTful API tinh gọn (minimal setup) xây dựng trên nền tảng **FastAPI** và **Python 3.12+**, sẵn sàng kết nối với Frontend Next.js (`hmong-fashion`).

---

## 🛠️ Tech Stack

- **Framework:** [FastAPI](https://fastapi.tiangolo.com/) (High performance, async, auto OpenAPI docs)
- **ASGI Server:** [Uvicorn](https://www.uvicorn.org/)
- **Configuration & Validation:** [Pydantic v2](https://docs.pydantic.dev/) & [pydantic-settings](https://docs.pydantic.dev/latest/concepts/pydantic_settings/)
- **Database & ORM:** [SQLAlchemy 2.0](https://www.sqlalchemy.org/) + [Alembic](https://alembic.sqlalchemy.org/) (hỗ trợ SQLite cho dev, PostgreSQL cho production)
- **Package & Environment Manager:** [uv](https://docs.astral.sh/uv/) (hoặc `pip` / `venv`)
- **Testing:** [Pytest](https://pytest.org/) + [HTTPX](https://www.python-httpx.org/)

---

## 📁 Cấu trúc thư mục

```text
hmong-fashion-backend/
├── app/
│   ├── __init__.py
│   ├── main.py                  # Khởi tạo FastAPI app, CORS middleware, Lifespan
│   ├── core/
│   │   ├── __init__.py
│   │   └── config.py            # Cấu hình Settings (đọc từ .env)
│   ├── db/
│   │   ├── __init__.py
│   │   ├── base.py              # DeclarativeBase SQLAlchemy
│   │   └── session.py           # Database engine & session generator (get_db)
│   ├── schemas/
│   │   ├── __init__.py
│   │   └── health.py            # Pydantic schemas (Health check)
│   └── api/
│       ├── __init__.py
│       └── v1/
│           ├── __init__.py
│           ├── router.py        # Central Router gom các endpoint v1
│           └── endpoints/
│               ├── __init__.py
│               └── health.py    # Health check endpoint
├── tests/
│   ├── __init__.py
│   ├── conftest.py              # Pytest fixtures & TestClient
│   └── test_health.py           # Unit tests
├── .env.example                 # Mẫu cấu hình môi trường
├── .env                         # File cấu hình local (được gitignore)
├── .gitignore                   # Quy tắc bỏ qua file rác / venv
├── pyproject.toml               # Định nghĩa dependencies (uv / pip)
├── requirements.txt             # Danh sách dependencies dạng pip
└── README.md
```

---

## 🚀 Hướng dẫn khởi chạy

### Cách 1: Sử dụng `uv` (Khuyên dùng - Cực nhanh)

1. Cài đặt dependencies và tạo môi trường ảo tự động:
   ```bash
   uv sync
   ```

2. Chạy server phát triển (Development Server):
   ```bash
   uv run uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
   ```

3. Chạy kiểm thử (Tests):
   ```bash
   uv run pytest
   ```

---

### Cách 2: Sử dụng `venv` và `pip` tiêu chuẩn

1. Tạo và kích hoạt môi trường ảo:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

2. Cài đặt dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Khởi chạy server:
   ```bash
   uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
   ```

4. Chạy kiểm thử:
   ```bash
   pytest
   ```

---

## 🌐 Các Endpoint có sẵn

- **Trang chủ API:** [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
- **Health Check:** [http://127.0.0.1:8000/api/v1/health](http://127.0.0.1:8000/api/v1/health)
- **Swagger UI (Interactive Docs):** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **ReDoc:** [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## 📌 Khuyến nghị cho Initial Commit

Để hoàn tất commit đầu tiên lên Git:

```bash
git add .
git commit -m "feat: initial commit minimal fastapi backend setup"
git push origin main
```
