#!/usr/bin/env python3
"""
Calendar EID Converter

Utility script to convert between Google Calendar event IDs and encoded eids.
"""

import sys
import os
import argparse
import base64

# Add the modules directory to the path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'modules'))

def decode_eid(encoded_eid):
    """Decode a Google Calendar eid to get event ID and calendar ID."""
    try:
        # Add padding if needed
        missing_padding = len(encoded_eid) % 4
        if missing_padding:
            encoded_eid += '=' * (4 - missing_padding)

        decoded = base64.b64decode(encoded_eid).decode('utf-8')
        parts = decoded.split(' ', 1)

        if len(parts) == 2:
            event_id = parts[0]
            calendar_id = parts[1]

            # Convert shortened calendar ID back to full format
            if calendar_id.endswith('@g'):
                calendar_id = calendar_id.replace('@g', '@group.calendar.google.com')

            return event_id, calendar_id
        else:
            return decoded, None

    except Exception as e:
        print(f"Error decoding eid: {e}")
        return None, None

def encode_eid(event_id, calendar_id=None):
    """Encode event ID and calendar ID into Google Calendar eid format."""
    try:
        # Use default calendar ID if not provided
        if not calendar_id:
            calendar_id = os.getenv("GCAL_ID", "c_upaofong8mgrmrkegn7ic7hk5s@group.calendar.google.com")

        # Import the encode function from gcal module
        from modules import gcal
        return gcal.encode_calendar_eid(event_id, calendar_id)

    except Exception as e:
        print(f"Error encoding eid: {e}")
        return None

def main():
    parser = argparse.ArgumentParser(
        description='Convert between Google Calendar event IDs and encoded eids',
        epilog='''Examples:
  # Decode an eid to get event ID
  python calendar_eid_converter.py --decode NG1hN3M4NnNrYTRmZnRlaGM5ajZvdWtrNTcgY191cGFvZm9uZzhtZ3JtcmtlZ243aWM3aGs1c0Bn

  # Encode an event ID to get eid
  python calendar_eid_converter.py --encode 4ma7s86ska4fftehc9j6oukk57

  # Encode with custom calendar ID
  python calendar_eid_converter.py --encode 4ma7s86ska4fftehc9j6oukk57 --calendar-id custom@calendar.com''',
        formatter_class=argparse.RawDescriptionHelpFormatter
    )

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--decode', metavar='EID', help='Decode a Google Calendar eid')
    group.add_argument('--encode', metavar='EVENT_ID', help='Encode an event ID to eid format')

    parser.add_argument('--calendar-id', help='Calendar ID for encoding (uses default if not provided)')

    args = parser.parse_args()

    if args.decode:
        print(f"🔍 Decoding eid: {args.decode}")
        print()

        event_id, calendar_id = decode_eid(args.decode)

        if event_id:
            print(f"✅ **Event ID**: {event_id}")
            if calendar_id:
                print(f"✅ **Calendar ID**: {calendar_id}")
            print()
            print(f"💾 For mapping file: \"calendar_event_id\": \"{event_id}\"")
        else:
            print("❌ Failed to decode eid")
            return 1

    elif args.encode:
        print(f"🔧 Encoding event ID: {args.encode}")
        if args.calendar_id:
            print(f"📅 Using calendar ID: {args.calendar_id}")
        print()

        encoded_eid = encode_eid(args.encode, args.calendar_id)

        if encoded_eid:
            print(f"✅ **Encoded eid**: {encoded_eid}")
            print()
            print(f"🔗 **Direct calendar link**:")
            print(f"   https://www.google.com/calendar/event?eid={encoded_eid}")
        else:
            print("❌ Failed to encode event ID")
            return 1

    return 0

if __name__ == "__main__":
    sys.exit(main())
