from random import *  # import random python class

# written by Mehmet Ozan Guven - 22020136

class MonteCarloTech:
    # Assume that all probability result is false
    _probabilityOfAResult = False
    _probabilityOfBResult = False
    _probabilityOfCResult = False
    _probabilityOfDResult = False
    _probabilityOfEResult = False

    def _probabilityOfA(self):
        """
        Calculation of probability of A
        Generate random number between 1, 100
        :return: True, if random number is slower or equal to 20,
                 False, otherwise
        """
        x = randint(1, 100)
        if x <= 20:
            self._probabilityOfAResult = True
        else:
            self._probabilityOfAResult = False

    def _probabilityOfB(self):
        """
        Calculation of probability of B
        Generate random number between 1, 100
        :return: True, if probability result of A is True and random number is slower or equal to 80,
                 True, if probability result of A is False and random number is slower or equal to 20,
                 False, otherwise
        """
        x = randint(1, 100)
        if self._probabilityOfAResult and x <= 80:
            self._probabilityOfBResult = True
        elif not self._probabilityOfAResult and x <= 20:
            self._probabilityOfBResult = True
        else:
            self._probabilityOfBResult = False

    def _probabilityOfC(self):
        """
        Calculation of probability of C
        Generate random number between 1, 100
        :return: True, if probability result of A is True and random number is slower or equal to 20,
                 True, if probability result of A is False and random number is slower or equal to 5,
                 False, otherwise
        """
        x = randint(1, 100)
        if self._probabilityOfAResult and x <= 20:
            self._probabilityOfCResult = True
        elif not self._probabilityOfAResult and x <= 5:
            self._probabilityOfCResult = True
        else:
            self._probabilityOfCResult = False

    def _probabilityOfD(self):
        """
        Calculation of probability of D
        Generate random number between 1, 100
        :return: True, if probability result of B=T && C=T and random number is slower or equal to 80,
                 True, if probability result of B=T && C!=T and random number is slower or equal to 80,
                 True, if probability result of B!=T && C=T and random number is slower or equal to 80,
                 True, if probability result of B!=T && C!=T and random number is slower or equal to 5,
                 False, otherwise
        """
        x = randint(1, 100)
        if self._probabilityOfBResult and self._probabilityOfCResult and x <= 80:
            self._probabilityOfDResult = True
        elif self._probabilityOfBResult and not self._probabilityOfCResult and x <= 80:
            self._probabilityOfDResult = True
        elif not self._probabilityOfBResult and self._probabilityOfCResult and x <= 80:
            self._probabilityOfDResult = True
        elif not self._probabilityOfBResult and not self._probabilityOfCResult and x <= 5:
            self._probabilityOfDResult = True
        else:
            self._probabilityOfDResult = False

    def _probabilityOfE(self):
        """
        Calculation of probability of D
        Generate random number between 1, 100
        :return: True, if probability result of C=T and random number is slower or equal to 80,
                 True, if probability result of C!=T and random number is slower or equal to 60,
                 False, otherwise
        """
        x = randint(1, 100)
        if self._probabilityOfCResult and x <= 80:
            self._probabilityOfEResult = True
        elif not self._probabilityOfCResult and x <= 60:
            self._probabilityOfEResult = True
        else:
            self._probabilityOfEResult = False

    def _calculateProbabilities(self):
        """
        Calculate all probabilities
        :return:
        """
        self._probabilityOfA()
        self._probabilityOfB()
        self._probabilityOfC()
        self._probabilityOfD()
        self._probabilityOfE()

    def calculateDPlus(self, trialNumber):
        """
        Calculation of P(+D)
        Loop 1 to trialNumber
            1. Calculate all probabilities
            2. Then if probability result of D is True, increment the counter
        After loop print the probability
        :param trialNumber: is the trial number for probability accurate
        :return:
        """
        count = 0
        for i in range(1, trialNumber):
            self._calculateProbabilities()
            if self._probabilityOfDResult:
                count = count + 1

        print("Probability of P(+D): " + str(count / trialNumber))

    def calculateDPlus_and_AMinus(self, trialNumber):
        """
        Calculation of P(+D,-A)
        Loop 1 to trialNumber
            1. Calculate all probabilities
            2. Then if probability result of D is True and result of A is False, increment the counter
        After loop print the probability
        :param trialNumber: is the trial number for probability accurate
        :return:
        """
        count = 0
        for i in range(1, trialNumber):
            self._calculateProbabilities()
            if self._probabilityOfDResult and not self._probabilityOfAResult:
                count = count + 1
        print("Probability of P(+D,-A): " + str(count / trialNumber))

    def calculateEPlus_when_BMinus_known(self, trialNumber):
        """
        Calculation of P(+E|-B)
        Define 2 counters for (-B) and (+E,-B)
        Loop 1 to trialNumber
            1. Calculate all probabilities
            2. if result of B is False, then increment (-B)
                    if result of E is True, then increment (+E,-B)
        After loop print the probability
        :param trialNumber: is the trial number for probability accurate
        :return:
        """
        countForBMinus = 0
        countForEPlus_and_BMinus = 0
        for i in range(1, trialNumber):
            self._calculateProbabilities()
            if not self._probabilityOfBResult:
                countForBMinus = countForBMinus + 1
                if self._probabilityOfEResult:
                    countForEPlus_and_BMinus = countForEPlus_and_BMinus + 1

        print("Probability of P(+E|-B): " + str(countForEPlus_and_BMinus / countForBMinus))

    def calculateAPlus_when_DPlus_and_EMinus_known(self, trialNumber):
        """
        Calculation of P(+A|-D,-E)
        Define 2 counters for (+A,-D,-E) and (-A,+D,-E)
        Loop 1 to trialNumber
            1. Calculate all probabilities
            2. if result of A and D are True and result of E is False, increment (+A,-D,-E)
            3. if result of A is False and D is True and result of E is False, increment (-A,+D,-E)
        After loop print the probability
        :param trialNumber: is the trial number for probability accurate
        :return:
        """
        countForAPlus_DPlus_EMinus = 0
        countForAMinus_DPlus_EMinus = 0

        for i in range(1, trialNumber):
            self._calculateProbabilities()

            if self._probabilityOfAResult and self._probabilityOfDResult and not self._probabilityOfEResult:
                countForAPlus_DPlus_EMinus = countForAPlus_DPlus_EMinus + 1

            if not self._probabilityOfAResult and self._probabilityOfDResult and not self._probabilityOfEResult:
                countForAMinus_DPlus_EMinus = countForAMinus_DPlus_EMinus + 1

        print("Probability of P(+A|-D,-E): "+ str(countForAPlus_DPlus_EMinus / (countForAMinus_DPlus_EMinus + countForAPlus_DPlus_EMinus)))

    def calculateBPlus_and_EMinus_when_APlus_known(self, trialNumber):
        """
        Calculation of P(+B,-E|+A)
        Define 4 counters for (+B,-E,+A), (+B,+E,+A), (-B,+E,+A) and (-B,-E,+A)
        and increment the correspond counter according probability results
        :param trialNumber: is the trial number for probability accurate
        :return:
        """
        countForBPlus_EMinus_APlus = 0
        countForBPlus_EPlus_APlus = 0
        countForBMinus_EPlus_APlus = 0
        countForBMinus_EMinus_APlus = 0

        for i in range(1, trialNumber):
            self._calculateProbabilities()

            if self._probabilityOfAResult:
                if self._probabilityOfBResult:
                    if self._probabilityOfEResult:
                        countForBPlus_EPlus_APlus = countForBPlus_EPlus_APlus + 1
                    else:
                        countForBPlus_EMinus_APlus = countForBPlus_EMinus_APlus + 1
                else:
                    if self._probabilityOfEResult:
                        countForBMinus_EPlus_APlus = countForBMinus_EPlus_APlus + 1
                    else:
                        countForBMinus_EMinus_APlus = countForBMinus_EMinus_APlus + 1

        result = (countForBPlus_EMinus_APlus) / (countForBPlus_EMinus_APlus +
                                                 countForBPlus_EPlus_APlus +
                                                 countForBMinus_EPlus_APlus +
                                                 countForBMinus_EMinus_APlus)
        print("Probability of P(+B,-E|+A): "+str(result))


if __name__ == '__main__':
    monteCarloTech = MonteCarloTech()
    trialNumber = 100000

    monteCarloTech.calculateDPlus(trialNumber)  # P(+D)
    monteCarloTech.calculateDPlus_and_AMinus(trialNumber)  # P(+D,-A)
    monteCarloTech.calculateEPlus_when_BMinus_known(trialNumber)  # P(+E|-B)
    monteCarloTech.calculateAPlus_when_DPlus_and_EMinus_known(trialNumber)  # P(+A|+D,-E)
    monteCarloTech.calculateBPlus_and_EMinus_when_APlus_known(trialNumber)  # P(+B,-E|+A )
