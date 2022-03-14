import json
import typing
import urllib.error
import urllib.parse
import urllib.request
from email.message import Message


search_result = []

class Response(typing.NamedTuple):
    body: str
    headers: Message
    status: int
    error_count: int = 0

    def json(self) -> typing.Any:
        try:
            output = json.loads(self.body)
        except json.JSONDecodeError:
            output = ""
        return output


def request(
    url: str,
    data: dict = None,
    params: dict = None,
    headers: dict = None,
    method: str = "GET",
    data_as_json: bool = True,
    error_count: int = 0,
) -> Response:
    if not url.casefold().startswith("http"):
        raise urllib.error.URLError("Incorrect and possibly insecure protocol in url")
    method = method.upper()
    request_data = None
    headers = headers or {}
    data = data or {}
    params = params or {}
    headers = {"Accept": "application/json", **headers}

    if method == "GET":
        params = {**params, **data}
        data = None

    if params:
        url += "?" + urllib.parse.urlencode(params, doseq=True, safe="/")

    if data:
        if data_as_json:
            request_data = json.dumps(data).encode()
            headers["Content-Type"] = "application/json; charset=UTF-8"
        else:
            request_data = urllib.parse.urlencode(data).encode()

    httprequest = urllib.request.Request(
        url, data=request_data, headers=headers, method=method
    )

    try:
        with urllib.request.urlopen(httprequest) as httpresponse:
            response = Response(
                headers=httpresponse.headers,
                status=httpresponse.status,
                body=httpresponse.read().decode(
                    httpresponse.headers.get_content_charset("utf-8")
                ),
            )
    except urllib.error.HTTPError as e:
        response = Response(
            body=str(e.reason),
            headers=e.headers,
            status=e.code,
            error_count=error_count + 1,
        )

    return response

from bs4 import BeautifulSoup

def handle_url(url):
    html_text = request(str(url)).body
    soup = BeautifulSoup(html_text, 'lxml')
    output = soup.get_text().encode("utf-8")

    print(str(output).replace('\\n', '\n').replace('\\t', '\t'))

def search_term(url):
    url = url.replace(' ', '%20')
    html_text = request(str(url)).body
    soup = BeautifulSoup(html_text, 'html.parser')
    for span in soup.find_all("span", class_="ad-domain fz-14 lh-20 s-url fc-obsidian d-ib pb-4"):
        search_result.append(span.get_text())

    for span in soup.find_all("span", class_="d-ib p-abs t-0 l-0 fz-14 lh-20 fc-obsidian wr-bw ls-n pb-4"):
        search_result.append(span.get_text())

    url2 = url + "&pz=7&b=7"

    html_text = request(str(url2)).body
    soup = BeautifulSoup(html_text, 'html.parser')

    for span in soup.find_all("span", class_="ad-domain fz-14 lh-20 s-url fc-obsidian d-ib pb-4"):
        search_result.append(span.get_text())

    for span in soup.find_all("span", class_="d-ib p-abs t-0 l-0 fz-14 lh-20 fc-obsidian wr-bw ls-n pb-4"):
        search_result.append(span.get_text())

    print(search_result[:10])

def save_page(url):
    html_text = request(str(url)).body
    save_webpage = open('saved_site.html', 'w+')
    save_webpage.write(html_text)
    save_webpage.close()


# if __name__ == '__main__':

    # url = "https://www.arduino.cc/reference/en/language/functions/communication/serial/print/"
    # url2 = "https://search.yahoo.com/search?p=putin&pz=7&b=7"
#     #
#     # print(request(url))
#     #
#     # html_text = request(url).body
#     soup = BeautifulSoup(html_text, 'html.parser')
#     #
    # print(soup.get_text())
#
    # handle_url(url)
#     search_term(url)
#     print(search_result[:10])
#     save_page(url)