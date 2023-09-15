import requests
from  notion_client import Client
NOTION_TOKEN = "secret_GgdXobPc670NsqgzJwuKkzFTPg6RlMtjBd0kgpckvAF"
DATABASE_ID = "e9dee07ab9b646f58828ca87cfd3f692"

headers = {
    "Authorization": "Bearer " + NOTION_TOKEN,
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28",
}


def update_page(page_id: str, data: dict):
    url = f"https://api.notion.com/v1/pages/{page_id}"

    payload = {"properties": data}

    res = requests.patch(url, json=payload, headers=headers)
    return res

def create_page(data: dict):
    create_url = "https://api.notion.com/v1/pages"

    payload = {"parent": {"database_id": DATABASE_ID}, "properties": data}

    res = requests.post(create_url, headers=headers, json=payload)
    # print(res.status_code)
    return res
def get_latest_page():
    notion = Client(auth=NOTION_TOKEN)

    database_id = DATABASE_ID
    results = notion.databases.query(
            **{
                "database_id": database_id,
                "sorts": [
                    {
                        "property": "date_added",
                        "direction": "ascending"
                    }
                ]
            }
        )

    print(results)
    #read json into dict
    latest_page = results['results'][-1]
    latest_page_id = latest_page['id']
    title = latest_page['properties']['Name']['title'][0]['text']['content']
    return latest_page_id, title
def update_latest_page(data: str,col=None):
    latest_page_id, title = get_latest_page()
    res = update_page(latest_page_id, data) if col is None else update_page_col(latest_page_id, data,col)
def update_page(latest_page_id, data: str):
    notion = Client(auth=NOTION_TOKEN)

    pg_id = latest_page_id
    results = notion.pages.update(
        **{
            "page_id": pg_id,
            "properties": {
                "pdf":{
                    "rich_text": [
                        {
                            "text": {
                                "content": data
                            }
                        }
                    ]
                    
                }
            }
        }
    )
    return results

def update_page_col(latest_page_id, data: str,col):
    notion = Client(auth=NOTION_TOKEN)

    pg_id = latest_page_id
    results = notion.pages.update(
        **{
            "page_id": pg_id,
            "properties": {
                col:{
                    "rich_text": [
                        {
                            "text": {
                                "content": data
                            }
                        }
                    ]
                    
                }
            }
        }
    )
    return results
if __name__ == '__main__':
    # res = create_page({"Name": {"title": [{"text": {"content": "test"}}]}})
    # print(res.json())
    # res = update_page("e9dee07ab9b646f58828ca87cfd3f692", {"Name": {"title": [{"text": {"content": "test"}}]}})
    # print(res.json())
    notion = Client(auth=NOTION_TOKEN)

    database_id = DATABASE_ID
    results = notion.databases.query(
        **{
            "database_id": database_id,
            "sorts": [
                {
                    "property": "date_added",
                    "direction": "ascending"
                }
            ]
        }
    )

    print(results)
    #read json into dict
    latest_page = results['results'][-1]
    latest_page_id = latest_page['id']
    title = latest_page['properties']['Name']['title'][0]['text']['content']
    update_latest_page("test")
    # print(results)
