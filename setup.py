import os

def create_structure(base_path="app"):
    folders = [
        "core",
        "models",
        "schemas",
        "crud",
        "api/v1",
        "utils"
    ]

    # app 폴더 생성
    os.makedirs(base_path, exist_ok=True)

    # 하위 폴더들 생성
    for folder in folders:
        path = os.path.join(base_path, folder)
        os.makedirs(path, exist_ok=True)
        print(f"📁 Created: {path}")

    # main.py 생성 (app 안에)
    main_file = os.path.join(base_path, "main.py")
    with open(main_file, "w", encoding="utf-8") as f:
        f.write("""\
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "SeeIn FastAPI 서버가 실행 중입니다."}
""")

    # run.py 생성 (루트에)
    run_file = "run.py"
    with open(run_file, "w", encoding="utf-8") as f:
        f.write("""\
import uvicorn

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="127.0.0.1", port=8010, reload=True)
""")

    print("\\n✅ 프로젝트 구조 생성 완료!")

if __name__ == "__main__":
    create_structure()
