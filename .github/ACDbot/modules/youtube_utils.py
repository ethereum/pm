from googleapiclient.discovery import build
import os

YOUTUBE_API_KEY = os.environ.get("YOUTUBE_API_KEY")

def get_channel_id_by_custom_url(custom_url):
    youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)

    response = youtube.channels().list(
        part='id',
        forUsername=custom_url
    ).execute()

    items = response.get('items', [])
    if items:
        return items[0]['id']
    else:
        # Try retrieving by channel custom URL path
        response = youtube.search().list(
            part='snippet',
            q=custom_url,
            type='channel',
            maxResults=1
        ).execute()
        items = response.get('items', [])
        if items:
            return items[0]['snippet']['channelId']
        else:
            raise Exception("Channel not found")

def get_channel_videos(channel_id):
    youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)

    videos = []
    next_page_token = None

    while True:
        res = youtube.search().list(
            part='snippet',
            channelId=channel_id,
            maxResults=50,
            pageToken=next_page_token,
            order='date',
            type='video'
        ).execute()

        videos.extend(res['items'])
        next_page_token = res.get('nextPageToken')

        if not next_page_token:
            break

    return videos

def get_live_streams(channel_id):
    youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)

    live_streams = []
    next_page_token = None

    while True:
        res = youtube.search().list(
            part='snippet',
            channelId=channel_id,
            eventType='live',
            type='video',
            order='date',
            maxResults=50,
            pageToken=next_page_token
        ).execute()

        live_streams.extend(res['items'])
        next_page_token = res.get('nextPageToken')

        if not next_page_token:
            break

    return live_streams

if __name__ == "__main__":
    custom_url = "EthereumProtocol"
    channel_id = get_channel_id_by_custom_url(custom_url)
    print(f"Channel ID: {channel_id}")

    videos = get_channel_videos(channel_id)
    print("Videos:")
    for video in videos:
        video_id = video['id']['videoId']
        title = video['snippet']['title']
        print(f"{title}: https://www.youtube.com/watch?v={video_id}")

    live_streams = get_live_streams(channel_id)
    print("\nLive Streams:")
    for stream in live_streams:
        stream_id = stream['id']['videoId']
        title = stream['snippet']['title']
        print(f"{title}: https://www.youtube.com/watch?v={stream_id}") 