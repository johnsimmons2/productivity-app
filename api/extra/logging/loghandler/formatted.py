from extra.logging.log import Log, LogLevel
from extra.logging.loghandler.loghandler import LogHandler


class FormattedLogHandler(LogHandler):
    class Colors:
        # NON RESERVED
        BLUE = '\033[94m'
        CYAN = '\033[96m'
        GREEN = '\033[92m'
        # RESERVED
        WARNING = '\033[93m'
        ERROR = '\033[91m'
        ENDC = '\033[0m'
        # MISC
        HEADER = '\033[95m'
        BOLD = '\033[1m'
        UNDERLINE = '\033[4m'

    _color_dates = False
    _color_logs = True
    _default_timestamp_color = Colors.BOLD

    def handle(self, log:Log):
        log_col = ''
        ts_col = FormattedLogHandler._default_timestamp_color if FormattedLogHandler._color_dates else ''
        if FormattedLogHandler._color_logs:
            match log._lvl:
                case LogLevel.DEBUG:
                    log_col = FormattedLogHandler.Colors.BLUE
                case LogLevel.WARN:
                    log_col = FormattedLogHandler.Colors.WARNING
                    ts_col = FormattedLogHandler.Colors.WARNING
                case LogLevel.ERROR:
                    log_col = FormattedLogHandler.Colors.ERROR \
                        + FormattedLogHandler.Colors.UNDERLINE
                    ts_col = FormattedLogHandler.Colors.ERROR  \
                        + FormattedLogHandler.Colors.UNDERLINE
                case LogLevel.SUCCESS:
                    log_col = FormattedLogHandler.Colors.GREEN
                    ts_col = FormattedLogHandler.Colors.GREEN
        message = FormattedLogHandler._apply_color(log._get_timeless_log(), log_col)
        timestamp = FormattedLogHandler._apply_color(log._get_timestamp_format(), ts_col)
        print(timestamp + message)

    def config_set_color_dates(self, val):
        FormattedLogHandler._color_dates = val

    def config_set_color_logs(self, val):
        FormattedLogHandler._color_logs = val

    def _apply_color(text, color):
        return str(color) + str(text) + FormattedLogHandler.Colors.ENDC
    

