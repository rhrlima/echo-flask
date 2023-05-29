# Echo-Flask

Simple Flask app that echoes JSON requests

## Usage

Option 1: Run the App directly
```
python app.py
```

Option 2: Using Docker
```
docker build -t echo-flask .
docker run -p 5000:5000 echo-flask:latest
```

Run Sample Request
```
curl -X POST -H "Content-Type: application/json" -d '{"key1":"value1", "key2":"value2"}' http://localhost:5000
```