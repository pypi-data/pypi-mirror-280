class App:
    @staticmethod
    def Kill(process_name: str | int):
        """
        强制停止应用程序的运行（结束进程）

        App.Kill('chrome.exe')

        :param process_name:[必选参数]应用程序进程名或进程PID
        :return:None
        """
