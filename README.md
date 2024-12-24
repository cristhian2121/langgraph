Steps

1. conda create -n NAME python=3.11
2. conda activate NAME
3. conda install -c conda-forge poetry
4. conda env export --from-history > environment.yml
5. poetry add langgraph
6. poetry add langchain-openai
7. ∂poetry add python-dotenv
8. poetry add "fastapi[standard]"
9. fastapi dev ./app/api.py

Run langgraph studio: `langgraph dev`
