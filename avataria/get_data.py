import requests

urls = ['https://cdn-sp.tortugasocial.com/avataria-ru/app/pnz-city.swf',
        'https://cdn-sp.tortugasocial.com/avataria-vk/app/appconfig.xml']

class GetData:
    def start(self):
        for url in urls:
            self.add_file(url)

    def add_file(self, url):
        req = requests.get(url)
        name = url.split("/")[-1]
        if 'appconfig' in name:
            with open(f"data/{name}", "w") as f:
                f.write(req.text)
            return f.close()
        with open(f"data/{name}", "wb") as f:
            f.write(req.content)
        return f.close()

if __name__ == "__main__":
    GetData().start()
