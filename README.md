# Pythonista Blog


### Create & active virtual Python environment
```bash
python -m venv venv
```
On `Linux` / `MacOS`
```bash
source venv/bin/activate
```
On `Windows`
```bash
venv\Scripts\activate
```
Install lib
```bash
pip install -r requirements.txt
```

### Create environment file
Copy content of `.env.example` to `.env`
```bash
cp .env.example .env
```
And change database environment variable to whatever you want

### Build docker container
```bash
docker compose build
```

### Run Project
```bash
docker compose up
```

