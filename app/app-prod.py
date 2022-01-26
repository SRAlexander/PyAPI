from root import create_app

app = create_app('config_prod.py')

if __name__ == "__main__":
    app.run(host="0.0.0.0")