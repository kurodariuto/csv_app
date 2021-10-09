class MinMaxChecker:
    @property
    def check(self):
        """
        Returns
        ----------
        max_or_min : str
        """
        return self.__max_or_min

    @check.setter
    def check(self, max_or_min:str):
        """
        Parameters
        ----------
        max_or_min : str
            MAXか、MIN(小文字だとエラーを返す)
        """
        if type(max_or_min) is not str:
            raise TypeError("max_or_min must be str")

        # 大文字でない場合、Falseを返す
        check_isuppe = max_or_min.isupper()
        check_max_or_min = max_or_min
        if (check_isuppe == False):
            raise TypeError("max_or_min must capital letter")
        elif not (check_max_or_min == "MAX" or check_max_or_min == "MIN"):
            raise TypeError("MAX or MIN Specify either")
        self.__max_or_min = max_or_min

if __name__ == "__main__":
    MinMaxChecker()
