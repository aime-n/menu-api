menu-mvp-api
_________________

[![PyPI version](https://badge.fury.io/py/menu-mvp-api.svg)](http://badge.fury.io/py/menu-mvp-api)
[![Test Status](https://github.com/aime-n/menu-mvp-api/workflows/Test/badge.svg?branch=develop)](https://github.com/aime-n/menu-mvp-api/actions?query=workflow%3ATest)
[![Lint Status](https://github.com/aime-n/menu-mvp-api/workflows/Lint/badge.svg?branch=develop)](https://github.com/aime-n/menu-mvp-api/actions?query=workflow%3ALint)
[![codecov](https://codecov.io/gh/aime-n/menu-mvp-api/branch/main/graph/badge.svg)](https://codecov.io/gh/aime-n/menu-mvp-api)
[![Join the chat at https://gitter.im/aime-n/menu-mvp-api](https://badges.gitter.im/aime-n/menu-mvp-api.svg)](https://gitter.im/aime-n/menu-mvp-api?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)
[![License](https://img.shields.io/github/license/mashape/apistatus.svg)](https://pypi.python.org/pypi/menu-mvp-api/)
[![Downloads](https://pepy.tech/badge/menu-mvp-api)](https://pepy.tech/project/menu-mvp-api)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://timothycrosley.github.io/isort/)
_________________

[Read Latest Documentation](https://aime-n.github.io/menu-mvp-api/) - [Browse GitHub Code Repository](https://github.com/aime-n/menu-mvp-api/)
_________________

# 🧠 Menu AI

Menu AI is an intelligent assistant that helps you eat better by transforming your nutrition plan or fridge contents into recipes, meal plans, grocery lists, and calorie/cost estimations.

This is the **MVP version**, focused on PDF parsing, recipe generation, and grocery planning — built using **LangGraph**, **FastAPI**, and **Streamlit**.

---

## 🚀 MVP Features

- 📄 Upload a nutritionist PDF and extract meals
- 🍲 Generate recipes from meals or ingredients
- 🗓 Select recipes for the week
- 🛒 Generate a grocery list
- 🔢 Estimate calories and price per recipe

---

## 🧰 Tech Stack

| Layer        | Tech               |
|--------------|--------------------|
| Backend API  | FastAPI            |
| AI Orchestration | LangGraph        |
| Frontend     | Streamlit (MVP)    |
| Language     | Python 3.10+       |

---

## 📦 Setup Instructions

```bash
# 1. Create virtual environment
python -m venv venv
source venv/bin/activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run Streamlit app
cd src/app
streamlit run app.py

# 4. Run FastAPI backend (in a separate terminal)
cd src/api
uvicorn main:app --reload
```


⸻

📝 TODO (Initial Milestone)
-	Integrate LangGraph with FastAPI
-	Parse and normalize uploaded PDFs
-	Generate recipes from meals
-	Build weekly planner and grocery list

⸻

🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

⸻

📄 License

This project is licensed under the MIT License.

---

Let me know if you want a Portuguese version too, or to include badges (build passing, license, etc).