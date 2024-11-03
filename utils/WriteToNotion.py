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
	"parent": { "page_id": "130a663f4aea808bb93bca83dd27826d" },
  "icon": {
  	"emoji": "🥬"
  },
	"cover": {
		"external": {
			"url": "https://upload.wikimedia.org/wikipedia/commons/6/62/Tuscankale.jpg"
		}
	},
	"properties": {
        "title": [
            {
                "text": {
                    "content": "🆗 Working"
                }
            }
        ]
    },
    "children": [
        {
            "object": "block",
            "type": "heading_2",
            "heading_2": {
                "rich_text": [
                    {
                        "text": {
                            "content": "Idea"
                        }
                    }
                ]
            }
        },
        {
            "object": "block",
            "type": "heading_2",
            "heading_2": {
                "rich_text": [
                    {
                        "text": {
                            "content": "Abstract"
                        }
                    }
                ]
            }
        },
        {
            "object": "block",
            "type": "heading_2",
            "heading_2": {
                "rich_text": [
                    {
                        "text": {
                            "content": "Objectives"
                        }
                    }
                ]
            }
        },
        {
            "object": "block",
            "type": "heading_2",
            "heading_2": {
                "rich_text": [
                    {
                        "text": {
                            "content": "Research Questions"
                        }
                    }
                ]
            }
        },
        {
            "object": "block",
            "type": "heading_2",
            "heading_2": {
                "rich_text": [
                    {
                        "text": {
                            "content": "Hypothesis"
                        }
                    }
                ]
            }
        },
        {
            "object": "block",
            "type": "heading_2",
            "heading_2": {
                "rich_text": [
                    {
                        "text": {
                            "content": "Planning"
                        }
                    }
                ]
            }
        },
        {
            "object": "block",
            "type": "heading_2",
            "heading_2": {
                "rich_text": [
                    {
                        "text": {
                            "content": "Methodology"
                        }
                    }
                ]
            }
        },
        {
            "object": "block",
            "type": "bulleted_list_item",
            "bulleted_list_item": {
                "rich_text": [
                    {
                        "text": {
                            "content": "Method 1"
                        }
                    }
                ]
            }
        },
        {
            "object": "block",
            "type": "bulleted_list_item",
            "bulleted_list_item": {
                "rich_text": [
                    {
                        "text": {
                            "content": "Method 2"
                        }
                    }
                ]
            }
        },
        {
            "object": "block",
            "type": "heading_2",
            "heading_2": {
                "rich_text": [
                    {
                        "text": {
                            "content": "Planning"
                        }
                    }
                ]
            }
        },
        # {
        #     "object": "block",
        #     "type": "link_preview",
        #     "link_preview": {
        #         "url": "https://www.notion.so/130a663f4aea80188ec6fff7999537f1?pvs=21"
        #     }
        # },
        {
            "object": "block",
            "type": "heading_2",
            "heading_2": {
                "rich_text": [
                    {
                        "text": {
                            "content": "LAB"
                        }
                    }
                ]
            }
        },
        {
            "object": "block",
            "type": "heading_2",
            "heading_2": {
                "rich_text": [
                    {
                        "text": {
                            "content": "Literature Review"
                        }
                    }
                ]
            }
        },
        {
            "object": "block",
            "type": "heading_2",
            "heading_2": {
                "rich_text": [
                    {
                        "text": {
                            "content": "Experimental Setup"
                        }
                    }
                ]
            }
        },
        {
            "object": "block",
            "type": "paragraph",
            "paragraph": {
                "rich_text": [
                    {
                        "text": {
                            "content": "Experimental Setup Goes here."
                        }
                    }
                ]
            }
        },
        {
            "object": "block",
            "type": "heading_2",
            "heading_2": {
                "rich_text": [
                    {
                        "text": {
                            "content": "Results"
                        }
                    }
                ]
            }
        },
        {
            "object": "block",
            "type": "heading_2",
            "heading_2": {
                "rich_text": [
                    {
                        "text": {
                            "content": "Discussion"
                        }
                    }
                ]
            }
        },
        {
            "object": "block",
            "type": "heading_2",
            "heading_2": {
                "rich_text": [
                    {
                        "text": {
                            "content": "Conclusion"
                        }
                    }
                ]
            }
        },
        {
            "object": "block",
            "type": "heading_2",
            "heading_2": {
                "rich_text": [
                    {
                        "text": {
                            "content": "Future Study"
                        }
                    }
                ]
            }
        },
        {
            "object": "block",
            "type": "heading_2",
            "heading_2": {
                "rich_text": [
                    {
                        "text": {
                            "content": "Final Verdicts"
                        }
                    }
                ]
            }
        },
        {
            "object": "block",
            "type": "heading_2",
            "heading_2": {
                "rich_text": [
                    {
                        "text": {
                            "content": "Citation"
                        }
                    }
                ]
            }
        },
        {
            "object": "block",
            "type": "numbered_list_item",
            "numbered_list_item": {
                "rich_text": [
                    {
                        "text": {
                            "content": "1."
                        }
                    }
                ]
            }
        }
    ]
}
    wtn= WriteToNotion(NOTION_API_KEY="", database_id="")
    wtn.createPage(pageData=pageData)