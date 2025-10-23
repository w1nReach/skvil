# Telegram Auto-Approve Bot (aiogram 3.x)

Бот автоматически одобряет заявки на вступление в канал/группу (chat join requests).

## Содержимое
- `main.py` — основной код (polling)
- `requirements.txt` — зависимости
- `.gitignore` — исключает `.env`, кэш и т.д.
- `bot.service` — unit-файл для systemd (автозапуск)
- `.env` — **создать вручную**, в репозиторий не коммитить

## 1) Подготовка репозитория (локально)
```bash
git init
git add main.py requirements.txt .gitignore bot.service README.md
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/<your_user>/<your_repo>.git
git push -u origin main
