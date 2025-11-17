from logs import Logger 
class LogChecker:
    def __init__(self):
        self.logger = Logger()
      
    def auth(self):
        try:
            username = "bilalhameed@gmail.com"
            password = ""
            # Authentication code
            message = f'Authenticated into SharePoint as: {web.properties["Title"]}'
            self.logger.log_info(message)
            print(message)
        except Exception as e:
            message = f"Exception auth: {e}"
            self.logger.log_error(message)
            print(message)
