# ACD Video Sandwich Test

This workflow tests whether PM can build a recorded ACD video from:

```text
first half of ev.mp4 + Zoom MP4 + last half of ev.mp4
```

## Viability

- `ffmpeg` is the right tool for this test. It can trim the bumper, normalize frame size/rate/audio, concatenate the three segments, and write a YouTube-friendly MP4 with `+faststart`.
- The workflow should not commit `ev.mp4` directly to the repository. The local file is about 89 MB, which is near GitHub's ordinary repository file limit and would bloat clone history. Store it as a release asset, Git LFS object, or external object-storage URL, then expose that URL as `ACD_BUMPER_URL`.
- GitHub-hosted runners are viable for a proof of concept, but standard runners have limited disk. A full job needs room for the downloaded Zoom file, bumper, intermediate decode/encode work, and final MP4.
- GitHub Actions artifacts work for a short-lived downloadable proof artifact. Keep retention low because private-repo artifact quotas are small.
- YouTube upload by API is viable for normal uploads and scheduled publishing. A true Premiere may still require YouTube Studio or a non-Data-API integration because the public Data API exposes `publishAt` scheduling but not a documented `set as Premiere` upload flag.

## Required Configuration

The workflow expects these values to be available to PRs from branches in the repository:

- `ACD_BUMPER_URL`: repository variable or secret pointing to a downloadable `ev.mp4`
- `ZOOM_CLIENT_ID`
- `ZOOM_CLIENT_SECRET`
- `ZOOM_REFRESH_TOKEN`

The workflow is skipped for forked PRs because GitHub does not expose repository secrets to untrusted pull requests.
