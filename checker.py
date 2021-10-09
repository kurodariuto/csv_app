class MinMaxChecker:
    @property
    def check(self):
        """
        Returns
        ----------
        min_or_max : str
        """
        return self.__min_or_max

    @check.setter
    def check(self, min_or_max:str):
        """
        Parameters
        ----------
        min_or_max : str
            MAXか、MIN(小文字だとエラーを返す)
        """
        if type(min_or_max) is not str:
            raise TypeError("min_or_max must be str")

        # 大文字でない場合、Falseを返す
        check_isuppe = min_or_max.isupper()
        check_min_or_max = min_or_max
        if (check_isuppe == False):
            raise TypeError("min_or_max must capital letter")
        elif not (check_min_or_max == "MAX" or check_min_or_max == "MIN"):
            raise TypeError("MAX or MIN Specify either")
        self.__min_or_max = min_or_max

if __name__ == "__main__":
    MinMaxChecker()
