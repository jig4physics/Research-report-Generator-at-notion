from utils import GenAI, WriteToNotion, ReadText
import os
from dotenv import load_dotenv
import json

load_dotenv()

if __name__ == "__main__":

    reader = ReadText()
    result = reader.read()
    print("---IDEA---")
    print(result)
    print("---Genreating report---")
    gen = GenAI(api_key=os.getenv("OPEN_AI"))
    response = gen.generate(prompt=result)
    print("---Creating notion page---")
    if isinstance(response, str):
        try:
            response = json.loads(response) 
            pageData = {
                "parent": { 
                    "page_id": os.getenv("PAGE_ID") 
                },
                "icon": {
                    "emoji": response["emoji"]
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
                                "content": response["title"]
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
            "type": "divider",
            "divider": {}
        },
                    {
                        "object": "block",
                        "type": "paragraph",
                        "paragraph": {
                            "rich_text": [
                                {
                                    "text": {
                                        "content": response["Idea"]
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
            "type": "divider",
            "divider": {}
        },
                    {
                        "object": "block",
                        "type": "paragraph",
                        "paragraph": {
                            "rich_text": [
                                {
                                    "text": {
                                        "content": response["Abstract"]
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
            "type": "divider",
            "divider": {}
        },
                    {
                        "object": "block",
                        "type": "paragraph",
                        "paragraph": {
                            "rich_text": [
                                {
                                    "text": {
                                        "content": response["Objectives"]
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
            "type": "divider",
            "divider": {}
        },
                    {
                        "object": "block",
                        "type": "paragraph",
                        "paragraph": {
                            "rich_text": [
                                {
                                    "text": {
                                        "content": "_NA_"
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
            "type": "divider",
            "divider": {}
        },
                    {
                        "object": "block",
                        "type": "paragraph",
                        "paragraph": {
                            "rich_text": [
                                {
                                    "text": {
                                        "content": response["Hypothesis"]
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
            "type": "divider",
            "divider": {}
        },
                    {
                        "object": "block",
                        "type": "paragraph",
                        "paragraph": {
                            "rich_text": [
                                {
                                    "text": {
                                        "content": response["Methodology"]
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
            "type": "divider",
            "divider": {}
        },
                    {
                        "object": "block",
                        "type": "paragraph",
                        "paragraph": {
                            "rich_text": [
                                {
                                    "text": {
                                        "content": "_NA_"
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
            "type": "divider",
            "divider": {}
        },
                    {
                        "object": "block",
                        "type": "paragraph",
                        "paragraph": {
                            "rich_text": [
                                {
                                    "text": {
                                        "content": response["Experimental_setup"]
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
            "type": "divider",
            "divider": {}
        },
                    {
                        "object": "block",
                        "type": "paragraph",
                        "paragraph": {
                            "rich_text": [
                                {
                                    "text": {
                                        "content": "_NA_"
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
            "type": "divider",
            "divider": {}
        },
                    {
                        "object": "block",
                        "type": "paragraph",
                        "paragraph": {
                            "rich_text": [
                                {
                                    "text": {
                                        "content": "_NA_"
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
            "type": "divider",
            "divider": {}
        },
                    {
                        "object": "block",
                        "type": "paragraph",
                        "paragraph": {
                            "rich_text": [
                                {
                                    "text": {
                                        "content": response["Conclusion"]
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
            "type": "divider",
            "divider": {}
        },
                    {
                        "object": "block",
                        "type": "paragraph",
                        "paragraph": {
                            "rich_text": [
                                {
                                    "text": {
                                        "content": response["Future_Study"]
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
            "type": "divider",
            "divider": {}
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
            "type": "divider",
            "divider": {}
        },
                    {
                        "object": "block",
                        "type": "numbered_list_item",
                        "numbered_list_item": {
                            "rich_text": [
                                {
                                    "text": {
                                        "content": "_NA_"
                                    }
                                }
                            ]
                        }
                    }
                ]
            }

            wtn= WriteToNotion(NOTION_API_KEY=os.getenv("NOTION_API_KEY"))
            wtn.createPage(pageData=pageData)

        except json.JSONDecodeError:
            print("Error: Failed to decode the response string into JSON")
    else:
        print("Response is already in dictionary format.")

   
    