from root import create_app

app = create_app('config_uat.py')

if __name__ == "__main__":
    app.run(host="0.0.0.0")