import requests

class WriteToNotion:
    def __init__(self, NOTION_API_KEY, database_id):
        self.url = "https://api.notion.com"
        self.NOTION_API_KEY = NOTION_API_KEY
        self.database_id = database_id
    
    def createPage(self, pageData):
        urlPage = f"{self.url}/v1/pages"
        headers = {
            "Authorization": f"Bearer {self.NOTION_API_KEY}",
            "Content-Type": "application/json",
            "Notion-Version": "2022-06-28",
        }

        response = requests.post(urlPage, headers=headers, json=pageData)

        if response.status_code == 200:
            print("Page created successfully!")
        else:
            print("Failed to create page:", response.status_code, response.text)
        



if __name__ == "__main__":
    pageData = {
	"parent": { "page_id": "" },
  "icon": {
  	"emoji": "🥬"
  },
	"cover": {
		"external": {
			"url": "https://upload.wikimedia.org/wikipedia/commons/6/62/Tuscankale.jpg"
		}
	},
	"properties": {
		"Name": {
			"title": [
				{
					"text": {
						"content": "Tuscan Kale"
					}
				}
			]
		},
	},
	"children": [
		{
			"object": "block",
			"type": "heading_2",
			"heading_2": {
				"rich_text": [{ "type": "text", "text": { "content": "Lacinato kale" } }]
			}
		},
		{
			"object": "block",
			"type": "paragraph",
			"paragraph": {
				"rich_text": [
					{
						"type": "text",
						"text": {
							"content": "Lacinato kale is a variety of kale with a long tradition in Italian cuisine, especially that of Tuscany. It is also known as Tuscan kale, Italian kale, dinosaur kale, kale, flat back kale, palm tree kale, or black Tuscan palm.",
							"link": { "url": "https://en.wikipedia.org/wiki/Lacinato_kale" }
						}
					}
				]
			}
		}
	]
}
    wtn= WriteToNotion(NOTION_API_KEY="", database_id="")
    wtn.createPage(pageData=pageData)