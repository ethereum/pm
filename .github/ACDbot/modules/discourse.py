import os
import json
import requests


def create_topic(title: str, body: str, category_id=63):
    """
    Creates a new Discourse topic.
    Expects environment variables:
      - DISCOURSE_API_KEY
      - DISCOURSE_API_USERNAME
      - DISCOURSE_BASE_URL (defaults to https://ethereum-magicians.org)
    """
    api_key = os.environ["DISCOURSE_API_KEY"]
    api_user = os.environ["DISCOURSE_API_USERNAME"]
    base_url = os.environ.get("DISCOURSE_BASE_URL", "https://ethereum-magicians.org")

    payload = {
        "title": title,
        "raw": body,
        "category": category_id,
        "archetype": "regular"
    }

    resp = requests.post(
        f"{base_url}/posts.json",
        headers={
            "Api-Key": api_key,
            "Api-Username": api_user,
            "Content-Type": "application/json",
        },
        data=json.dumps(payload),
    )
    if not resp.ok:
        print(resp.text)  # Log the response content for debugging
        resp.raise_for_status()

    return resp.json()


def update_topic(topic_id: int, title: str = None, body: str = None, category_id: int = None):
    api_key = os.environ["DISCOURSE_API_KEY"]
    api_user = os.environ["DISCOURSE_API_USERNAME"]
    base_url = os.environ.get("DISCOURSE_BASE_URL", "https://ethereum-magicians.org")

    # 1. Fetch the topic details so we can retrieve the first post's ID.
    resp_topic = requests.get(
        f"{base_url}/t/{topic_id}.json",
        headers={
            "Api-Key": api_key,
            "Api-Username": api_user
        }
    )
    resp_topic.raise_for_status()
    topic_json = resp_topic.json()

    # The first post ID is usually the first object in the `post_stream["posts"]`.
    first_post_id = topic_json["post_stream"]["posts"][0]["id"]

    # 2. If we have a new title or category, update the topic (PUT /t/<topic_id>.json).
    if title is not None or category_id is not None:
        update_payload = {}
        if title:
            update_payload["title"] = title
        if category_id:
            update_payload["category_id"] = category_id
        resp_update_topic = requests.put(
            f"{base_url}/t/{topic_id}.json",
            headers={
                "Api-Key": api_key,
                "Api-Username": api_user,
                "Content-Type": "application/json"
            },
            data=json.dumps(update_payload)
        )
        if not resp_update_topic.ok:
            print(resp_update_topic.text)
            resp_update_topic.raise_for_status()

    # 3. If we have new body content, update the text of the first post (PUT /posts/<post_id>.json).
    if body is not None:
        post_update_payload = {
            "post": {
                "raw": body
            }
        }
        resp_update_post = requests.put(
            f"{base_url}/posts/{first_post_id}.json",
            headers={
                "Api-Key": api_key,
                "Api-Username": api_user,
                "Content-Type": "application/json"
            },
            data=json.dumps(post_update_payload)
        )
        if not resp_update_post.ok:
            print(resp_update_post.text)
            resp_update_post.raise_for_status()

    return {"topic_id": topic_id, "updated_title": title, "updated_body": body}


def create_post(topic_id: int, body: str):
    """
    Creates a new post (reply) in the specified Discourse topic.
    """
    api_key = os.environ["DISCOURSE_API_KEY"]
    api_user = os.environ["DISCOURSE_API_USERNAME"]
    base_url = os.environ.get("DISCOURSE_BASE_URL", "https://ethereum-magicians.org")

    payload = {
        "topic_id": topic_id,
        "raw": body
    }

    resp = requests.post(
        f"{base_url}/posts.json",
        headers={
            "Api-Key": api_key,
            "Api-Username": api_user,
            "Content-Type": "application/json",
        },
        data=json.dumps(payload),
    )
    if not resp.ok:
        print(resp.text)  # Log the response content for debugging
        resp.raise_for_status()

    return resp.json()


def get_posts_in_topic(topic_id: int):
    """
    Retrieves all posts in a Discourse topic.
    """
    api_key = os.environ["DISCOURSE_API_KEY"]
    api_user = os.environ["DISCOURSE_API_USERNAME"]
    base_url = os.environ.get("DISCOURSE_BASE_URL", "https://ethereum-magicians.org")

    resp = requests.get(
        f"{base_url}/t/{topic_id}/posts.json",
        headers={
            "Api-Key": api_key,
            "Api-Username": api_user,
        },
    )
    if not resp.ok:
        print(resp.text)
        resp.raise_for_status()

    return resp.json().get("post_stream", {}).get("posts", [])


def check_if_transcript_posted(topic_id: int, meeting_id: str):
    """
    Checks if the transcript for the given meeting_id has already been posted.
    """
    posts = get_posts_in_topic(topic_id)
    marker = f"transcript-{meeting_id}.txt"
    for post in posts:
        if marker in post.get("cooked", "") or marker in post.get("raw", ""):
            return True
    return False


def upload_file(file_content: str, file_name: str):
    """
    Uploads a file to Discourse and returns the file URL.
    """
    api_key = os.environ["DISCOURSE_API_KEY"]
    api_user = os.environ["DISCOURSE_API_USERNAME"]
    base_url = os.environ.get("DISCOURSE_BASE_URL", "https://ethereum-magicians.org")

    files = {'file': (file_name, file_content, 'text/plain')}
    
    resp = requests.post(
        f"{base_url}/uploads.json",
        headers={
            "Api-Key": api_key,
            "Api-Username": api_user,
        },
        files=files
    )
    
    if not resp.ok:
        print(resp.text)
        resp.raise_for_status()
    
    return resp.json()["url"]
