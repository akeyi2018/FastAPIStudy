import uvicorn
from fastapi import Depends, FastAPI
from fastapi.security import OAuth2PasswordBearer
from fastapi.responses import HTMLResponse

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def generate_html_response():
    html_content = """
<html>
  <head>
    <title>Some HTML in here</title>
  </head>
  <body>
    <h1>Look ma! HTML!</h1>
    <h2>test</h2>
 
    <a href="https://www.yahoo.co.jp">リンク先にジャンプ</a>	
    
  </body>
</html>
    """
    return HTMLResponse(content=html_content, status_code=200)


@app.get("/", response_class=HTMLResponse)
async def root():
    res = """
    <head>	 
<title>文書番号002</title>	 
<link rel="index" href="https://www.yahoo.co.jp">	
<link rel="contents" href="mokuji.htm">	
<link rel="search" href="kensaku.html">	
<link rel="help" href="help.html">	
<link rel="prev" href="001.htm">	
<link rel="next" href="003.htm">	
</head>
    """
    # return {"message": "Hello World"}
    return generate_html_response()

@app.get("/items/")
async def read_items(token: str = Depends(oauth2_scheme)):
    return {"token": token}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)