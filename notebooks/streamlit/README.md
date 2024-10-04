# Stramlit

## 使用

### 命令行

```shell
streamlit run your_script.py [-- script args]
python -m streamlit run your_script.py
streamlit run https://raw.githubusercontent.com/streamlit/demo-uber-nyc-pickups/master/streamlit_app.py
```

### write

```python
import streamlit as st

st.write("Here's our first attempt at using data to create a table:")
```

### df

```python
dataframe: Dataframe = pd.DataFrame(...)
st.dataframe(dataframe.style.highlight_max(axis=0))
st.table(dataframe)
st.line_chart(chart_data)
```

## widgets

```python
x = st.slider('x')
st.write(x, 'squared is', x * x)

st.text_input("Your name", key="name")
```

# Fastapi

## Installation

```shell
pip install fastapi uvicorn
uvicorn main:app --reload
```

## User Guide

### 请求

```python
@app.post()
@app.put()
@app.delete()


@app.options()
@app.head()
@app.patch()
@app.trace()
```
    
### 请求路径

```python
@app.get("/items/{item_id}")
```

### 文档

Swagger UI： http://127.0.0.1:8000/docs
ReDoc： http://127.0.0.1:8000/redoc
json: http://127.0.0.1:8000/openapi.json


## Practice

[FastApi下载文件](https://zhuanlan.zhihu.com/p/432561474)

## 参考

- [FastApi 简单入门，附生产级脚手架代码](https://pylixm.top/posts/2021-01-05-start.html)
- [FastApi 官方教程](https://fastapi.tiangolo.com/tutorial/)

## 参考

- [Streamlit Documentation](https://docs.streamlit.io/library/get-started/create-an-app)
