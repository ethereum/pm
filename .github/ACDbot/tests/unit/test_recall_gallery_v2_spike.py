from scripts.recall_gallery_v2_spike import build_create_bot_payload, find_video_mixed_download_url


def test_build_create_bot_payload_uses_gallery_view_v2_mp4():
    payload = build_create_bot_payload(
        meeting_url="https://zoom.us/j/123",
        bot_name="Recorder",
        screenshare_mode="beside",
    )

    assert payload["meeting_url"] == "https://zoom.us/j/123"
    assert payload["bot_name"] == "Recorder"
    assert payload["recording_config"] == {
        "video_mixed_mp4": {},
        "video_mixed_layout": "gallery_view_v2",
        "video_mixed_participant_video_when_screenshare": "beside",
    }


def test_build_create_bot_payload_adds_rtmp_endpoint_when_requested():
    payload = build_create_bot_payload(
        meeting_url="https://zoom.us/j/123",
        bot_name="Recorder",
        screenshare_mode="overlap",
        rtmp_url="rtmp://example.test/live/key",
    )

    recording_config = payload["recording_config"]
    assert recording_config["video_mixed_flv"] == {}
    assert recording_config["realtime_endpoints"] == [
        {
            "type": "rtmp",
            "url": "rtmp://example.test/live/key",
            "events": ["video_mixed_flv.data"],
        }
    ]


def test_find_video_mixed_download_url_returns_done_mp4_url():
    bot = {
        "recordings": [
            {
                "media_shortcuts": {
                    "video_mixed": {
                        "status": {"code": "processing"},
                        "data": {"download_url": "https://example.test/not-ready.mp4"},
                    }
                }
            },
            {
                "media_shortcuts": {
                    "video_mixed": {
                        "status": {"code": "done"},
                        "data": {"download_url": "https://example.test/ready.mp4"},
                    }
                }
            },
        ]
    }

    assert find_video_mixed_download_url(bot) == "https://example.test/ready.mp4"


def test_find_video_mixed_download_url_returns_none_when_not_ready():
    assert find_video_mixed_download_url({"recordings": [{"media_shortcuts": {}}]}) is None
