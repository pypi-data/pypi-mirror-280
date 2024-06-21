# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=logging-fstring-interpolation
# pylint: disable=line-too-long

def create_custom_notice(severity, subject, message):
    return {
        "severity_code": severity.value,
        "severity_name": severity.name,
        "subject": subject,
        "message": message
    }


def create_exception_notice(severity, exception_code,exception_message, exception_traceback=None, subject=None, message=None):
    return {
        "severity_code": severity.value,
        "severity_name": severity.name,
        "subject": subject,
        "message": message,
        "exception_code": exception_code,
        "exception_message": exception_message,
        "exception_traceback": exception_traceback
    }