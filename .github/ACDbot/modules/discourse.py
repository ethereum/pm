import os
import json
import requests
import urllib.parse

def _content_unchanged(topic_id: int, new_title: str, new_body: str) -> bool:
    """
    Check if the topic content (title and body) is unchanged.
    Returns True if content is identical, False if different or on error.
    """
    try:
        api_key = os.environ["DISCOURSE_API_KEY"]
        api_user = os.environ["DISCOURSE_API_USERNAME"]
        base_url = os.environ.get("DISCOURSE_BASE_URL", "https://ethereum-magicians.org")

        # Fetch the topic details
        resp_topic = requests.get(
            f"{base_url}/t/{topic_id}.json",
            headers={
                "Api-Key": api_key,
                "Api-Username": api_user
            }
        )
        resp_topic.raise_for_status()
        topic_json = resp_topic.json()

        # Compare title
        current_title = topic_json.get("title", "")
        if current_title.strip() != new_title.strip():
            print(f"[DEBUG] Title changed: '{current_title}' -> '{new_title}'")
            return False

        # Compare body (first post content)
        try:
            first_post = topic_json["post_stream"]["posts"][0]
            current_body = first_post.get("raw", "")
            if current_body.strip() != new_body.strip():
                print(f"[DEBUG] Body changed (length: {len(current_body)} -> {len(new_body)})")
                return False
        except (KeyError, IndexError, TypeError):
            print(f"[DEBUG] Could not extract current body, assuming changed")
            return False

        print(f"[DEBUG] Topic content identical for topic {topic_id}")
        return True

    except Exception as e:
        print(f"[DEBUG] Error checking content for topic {topic_id}, assuming changed: {e}")
        return False


class DiscourseDuplicateTitleError(Exception):
    """Custom exception for duplicate Discourse topic titles."""
    def __init__(self, title, message="Title has already been used"):
        self.title = title
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'{self.message}: "{self.title}"'

def create_or_update_topic(title: str, body: str, topic_id: int = None, category_id=63):
    """
    Creates a new topic or updates an existing one.
    If topic_id is provided, updates that topic. Otherwise creates a new one.
    Skips update if content is identical to avoid unnecessary API calls.
    """
    if topic_id:
        print(f"[DEBUG] Checking existing Discourse topic {topic_id}: {title}")
        try:
            # First, check if content has actually changed
            if _content_unchanged(topic_id, title, body):
                print(f"[DEBUG] Topic content unchanged, skipping update for topic {topic_id}")
                return {"topic_id": topic_id, "title": title, "action": "unchanged"}

            print(f"[DEBUG] Content changed, updating topic {topic_id}")
            update_topic(topic_id, title=title, body=body)
            return {"topic_id": topic_id, "title": title, "action": "updated"}
        except Exception as e:
            print(f"[ERROR] Failed to update topic {topic_id}, falling back to status quo: {e}")
            # Return existing topic info on update failure
            return {"topic_id": topic_id, "title": title, "action": "update_failed"}
    else:
        print(f"[DEBUG] Creating new Discourse topic: {title}")
        return create_topic(title, body, category_id)

def create_topic(title: str, body: str, category_id=63):
    """
    Creates a new Discourse topic.
    Expects environment variables:
      - DISCOURSE_API_KEY
      - DISCOURSE_API_USERNAME
      - DISCOURSE_BASE_URL (defaults to https://ethereum-magicians.org)
    If a topic with the same title already exists, raises DiscourseDuplicateTitleError.
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

    try:
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
            # Check if error is due to title already existing
            error_text = resp.text
            print(f"[DEBUG] Create topic failed. Response: {error_text}")

            if "Title has already been used" in error_text:
                print(f"[INFO] 'Title has already been used' error received for title: '{title}'. Raising specific error.")
                # Raise the specific error instead of searching
                raise DiscourseDuplicateTitleError(title)

            # If not a title already exists error, raise the original HTTP error
            resp.raise_for_status()

        response_data = resp.json()
        topic_id = response_data.get("topic_id")
        return {"topic_id": topic_id, "title": title, "action": "created"}

    except DiscourseDuplicateTitleError:
        # Re-raise the custom exception to be caught by the caller
        raise
    except Exception as e:
        print(f"[DEBUG] Error in create_topic: {str(e)}")
        # Catch other exceptions (like network issues, other API errors) and re-raise
        raise


def update_topic(topic_id: int, title: str = None, body: str = None, category_id: int = None):
    api_key = os.environ["DISCOURSE_API_KEY"]
    api_user = os.environ["DISCOURSE_API_USERNAME"]
    base_url = os.environ.get("DISCOURSE_BASE_URL", "https://ethereum-magicians.org")

    # 1. Fetch the topic details so we can retrieve the first post's ID.
    try:
        resp_topic = requests.get(
            f"{base_url}/t/{topic_id}.json",
            headers={
                "Api-Key": api_key,
                "Api-Username": api_user
            }
        )
        resp_topic.raise_for_status()
        topic_json = resp_topic.json()
    except requests.exceptions.RequestException as e:
        print(f"[ERROR] Failed to fetch topic details for ID {topic_id}: {e}")
        raise # Re-raise the exception

    # The first post ID is usually the first object in the `post_stream["posts"]`.
    try:
        first_post_id = topic_json["post_stream"]["posts"][0]["id"]
    except (KeyError, IndexError, TypeError) as e:
        print(f"[ERROR] Could not extract first_post_id for topic {topic_id}. JSON structure might be unexpected. Error: {e}")
        # For now, let's raise to indicate the problem clearly
        raise ValueError(f"Could not find first post ID for topic {topic_id}") from e

    # 2. If we have a new title or category, update the topic (PUT /t/<topic_id>.json).
    topic_updated = False
    if title is not None or category_id is not None:
        update_payload = {}
        if title:
            update_payload["title"] = title
        if category_id:
            update_payload["category_id"] = category_id

        try:
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
                error_text = resp_update_topic.text
                print(f"[ERROR] Failed to update topic title/category for {topic_id}. Response: {error_text}")
                # Check if this specific error is a duplicate title error during update
                if "Title has already been used" in error_text and title is not None:
                     raise DiscourseDuplicateTitleError(title, message=f"Failed to update topic {topic_id} because title already exists")
                resp_update_topic.raise_for_status() # Raise for other errors
            topic_updated = True
        except DiscourseDuplicateTitleError:
            raise # Re-raise duplicate title error
        except requests.exceptions.RequestException as e:
            print(f"[ERROR] Network/API error during topic update for {topic_id}: {e}")
            raise

    # 3. If we have new body content, update the text of the first post (PUT /posts/<post_id>.json).
    post_updated = False
    if body is not None:
        post_update_payload = {
            "post": {
                "raw": body
            }
        }
        try:
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
                print(f"[ERROR] Failed to update post body for post {first_post_id} (topic {topic_id}). Response: {resp_update_post.text}")
                resp_update_post.raise_for_status()
            post_updated = True
        except requests.exceptions.RequestException as e:
            print(f"[ERROR] Network/API error during post update for post {first_post_id} (topic {topic_id}): {e}")
            raise

    # Return status based on what was attempted/succeeded
    return {"topic_id": topic_id, "topic_updated": topic_updated, "post_updated": post_updated}


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

    try:
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
    except requests.exceptions.RequestException as e:
        print(f"[ERROR] Failed to create post in topic {topic_id}: {e}")
        raise # Re-raise


def get_posts_in_topic(topic_id: int):
    """
    Retrieves all posts in a Discourse topic.
    """
    api_key = os.environ["DISCOURSE_API_KEY"]
    api_user = os.environ["DISCOURSE_API_USERNAME"]
    base_url = os.environ.get("DISCOURSE_BASE_URL", "https://ethereum-magicians.org")

    try:
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
    except requests.exceptions.RequestException as e:
        print(f"[ERROR] Failed to get posts for topic {topic_id}: {e}")
        # Return empty list or raise? Raising seems safer.
        raise


def check_if_transcript_posted(topic_id: int, meeting_id: str):
    """
    Checks if the transcript for the given meeting_id has already been posted.
    Returns True if found, False otherwise. Returns None on error fetching posts.
    """
    try:
        posts = get_posts_in_topic(topic_id)
        marker = f"transcript-{meeting_id}.txt"
        for post in posts:
            # Check both raw and cooked content for robustness
            if marker in post.get("cooked", "") or marker in post.get("raw", ""):
                return True
        return False
    except Exception as e:
        print(f"[WARN] Could not check for transcript in topic {topic_id} due to error: {e}")
        return None # Indicate uncertainty due to error


def upload_file(file_content: str, file_name: str):
    """
    Uploads a file to Discourse and returns the file URL.
    """
    api_key = os.environ["DISCOURSE_API_KEY"]
    api_user = os.environ["DISCOURSE_API_USERNAME"]
    base_url = os.environ.get("DISCOURSE_BASE_URL", "https://ethereum-magicians.org")

    files = {'file': (file_name, file_content, 'text/plain')}

    try:
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
    except requests.exceptions.RequestException as e:
        print(f"[ERROR] Failed to upload file '{file_name}': {e}")
        raise # Re-raise
    except KeyError as e:
        print(f"[ERROR] Unexpected response format from file upload, missing key: {e}. Response: {resp.text}")
        raise ValueError("Invalid response from Discourse file upload API") from e


def search_topic_by_title(title: str):
    """
    DEPRECATED: Searches for a topic with the exact title.
    This function might fail due to API permissions and is being replaced
    by more robust logic in the calling script.
    Returns the topic object if found, None otherwise.
    """
    print("[WARN] discourse.search_topic_by_title is deprecated and should not be used.")
    # Keep the old logic for reference or potential future restricted use, but warn heavily.
    api_key = os.environ.get("DISCOURSE_API_KEY") # Use .get() to avoid KeyError if not set
    api_user = os.environ.get("DISCOURSE_API_USERNAME")
    base_url = os.environ.get("DISCOURSE_BASE_URL", "https://ethereum-magicians.org")

    if not api_key or not api_user:
        print("[ERROR] Discourse API Key or Username not configured for search.")
        return None

    # URL encode the title for the search query
    encoded_title = urllib.parse.quote(f'"{title}"')

    try:
        # Search for the exact title
        resp = requests.get(
            f"{base_url}/search.json?q={encoded_title}",
            headers={
                "Api-Key": api_key,
                "Api-Username": api_user,
            },
        )

        if not resp.ok:
            print(f"[DEBUG] Search failed: {resp.status_code} {resp.text}")
            # Don't raise_for_status here, just return None as search failed
            return None

        search_results = resp.json()
        topics = search_results.get("topics", [])

        # Look for an exact match by title
        for topic in topics:
            if topic.get("title") == title:
                print(f"[DEBUG] Found matching topic via deprecated search: {topic.get('id')} - {topic.get('title')}")
                return topic

        print(f"[DEBUG] No topic with exact title '{title}' found via deprecated search")
        return None
    except requests.exceptions.RequestException as e:
        print(f"[ERROR] Network error during deprecated search for '{title}': {e}")
        return None
