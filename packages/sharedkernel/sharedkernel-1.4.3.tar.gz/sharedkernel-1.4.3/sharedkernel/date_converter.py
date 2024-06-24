import jdatetime
from datetime import datetime

from sharedkernel.enum import ErrorCode


class DateConverter:
    @staticmethod
    def to_jalali(
        input_datetime: datetime | jdatetime.datetime, format_string: str = "%Y/%m/%d"
    ):
        if isinstance(input_datetime, jdatetime.datetime):
            return input_datetime.strftime(format_string)

        if isinstance(input_datetime, datetime):
            jalali_date = jdatetime.datetime.fromgregorian(date=input_datetime)
            return jalali_date.strftime(format_string)

        raise ValueError(ErrorCode.Unsupported_Date_Type)

    @staticmethod
    def to_georgian(
        input_datetime: datetime | jdatetime.datetime, format_string: str = "%Y/%m/%d"
    ):
        if isinstance(input_datetime, jdatetime.datetime):
            georgian_date = jdatetime.datetime.togregorian(input_datetime)
            return georgian_date.strftime(format_string)

        if isinstance(input_datetime, datetime):
            return input_datetime.strftime(format_string)

        raise ValueError(ErrorCode.Unsupported_Date_Type)
