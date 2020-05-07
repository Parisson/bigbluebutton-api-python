from .base import BaseResponse
from ..core.meeting import Meeting

class GetMeetingsResponse(BaseResponse):
    def get_meetings(self):
        meetings = []

        try:
            if self.get_message_key() == "noMeetings":
                return []
        except KeyError:
            pass

        all_meetings = self.get_field("meetings")["meeting"]
        if isinstance(all_meetings, dict):
            # If there is only one meeting, it'll not return a list...
            all_meetings = [ all_meetings ]
        
        for meetingXml in all_meetings:
            meetings.append(Meeting(meetingXml))
        return meetings
